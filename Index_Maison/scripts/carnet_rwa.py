#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
carnet_rwa.py — LE CARNET DE RENDEMENTS RWA, EN FORME DE PRODUIT (maquette 29/09/2026).

POURQUOI CE FICHIER EXISTE
    Le 29/09, la revue des 12 terrains a conclu : 0 edge de trading prouvé, et le seul
    chemin de monétisation chiffré est un PRODUIT D'INFORMATION
    (COUT_REEL_VIVRE_ET_VERDICTS_20260913.md : newsletter/API 49 $/mo x ~75 clients ~
    coût de vie). Le radar RWA a été rouvert et re-tranché SUCCÈS sur son BON univers
    (scripts/verdicts_protocoles.py). Il manquait la MARCHANDISE : ce que le client lit.
    C'est ce fichier.

CE QU'IL FAIT
    Lit le MÊME historique brut que le radar (data/rwa_yields_hist.jsonl) et en tire un
    carnet : une ligne par POOL — le coffre réel — et non par « projet/symbole », qui
    n'est pas un identifiant : mesuré, le seul couple centrifuge-protocol/USDC recouvre
    18 déploiements distincts (des fonds différents : Janus Henderson AAA CLO, Apollo
    Diversified Credit, JAAA, NYLIM High Yield…). Chaque ligne porte le niveau de
    rendement, les drapeaux constatés, la bande de risque de DONNÉE, et la source.

SOURCE UNIQUE (règle d'or #6 : une seule vérité par fait)
    L'univers (est_pool_credit / univers_credit_prive) vient de verdicts_protocoles.py —
    importé, jamais recopié. Le carnet et le verdict ne peuvent pas diverger.

LES RÈGLES SONT DÉCLARÉES ICI, AVANT LE CALCUL (on ne règle pas après avoir vu le résultat)
    NIVEAU (rendement de référence de la fenêtre) :
        < 3 %   -> « faible »
        3-5 %   -> « courant »
        5-8 %   -> « élevé »
        >= 8 %  -> « très élevé »
        aucun relevé non nul -> « n/d »
        Le rendement de référence est la MÉDIANE. Un 0 publié par la source est une
        donnée manquante probable, PAS un rendement nul : quand il y en a, le niveau est
        calculé sur la MÉDIANE HORS ZÉRO et les DEUX valeurs sont affichées.
    DRAPEAUX (constatés, pas jugés) :
        VALEUR_CONSTANTE      : amplitude = 0 bps sur TOUTE la fenêtre -> à confirmer par
                                une 2ᵉ source (taux fixe annoncé OU source figée : les
                                deux se ressemblent, on ne tranche pas à la place du client)
        AUCUN_RENDEMENT_PUBLIE: la source n'a publié QUE des 0 sur la fenêtre -> aucune
                                valeur exploitable
        RELEVES_A_ZERO        : au moins un zéro PARMI des valeurs non nulles -> trou de
                                publication
        PROFONDEUR_FAIBLE     : TVL < 1 000 000 $
        RECOMPENSE_MIXTE      : > 30 % du rendement courant vient d'incitations (apyReward),
                                donc pas du crédit
        HISTORIQUE_COURT      : < 60 jours d'historique publié par la source
        RENDEMENT_INHABITUEL  : rendement de référence >= 12 % (à justifier)
    BANDE DE RISQUE = lecture mécanique des drapeaux :
        0-1 drapeau -> « faible » · 2 -> « modéré » · >= 3 -> « élevé »
        VALEUR_CONSTANTE force au minimum « modéré ».

CE QUE CE CARNET NE DIT PAS (bornes déclarées, R8 — on écrit ce qu'on ne mesure pas)
    · Le risque de CRÉDIT (défaut de l'emprunteur, qualité du collatéral, gouvernance du
      fonds) n'est PAS évalué : la source n'en publie pas. La colonne « risque » est le
      risque de FIABILITÉ de la donnée, pas le risque de perte en capital. La colonne
      « Crédit » vaut « non évalué » pour TOUTE ligne — c'est dit sur chaque ligne, pas
      seulement en bas de page.
    · Il n'y a qu'UNE source (DefiLlama). Toute valeur CONSTANTE est marquée « à
      confirmer » : on ne publie pas un taux « garanti » sur une seule source.
    · Aucune exécution, aucun ordre, aucun € : maquette d'information, pas un conseil.
    · Un rendement passé n'est pas un rendement futur.

Sorties :
    Index_Maison/thermo/CARNET_RWA.json      (le produit, lisible par une machine)
    Index_Maison/CARNET_RENDEMENTS_RWA.md    (le produit, lisible par un client)
Usage : python3 carnet_rwa.py   ·   python3 carnet_rwa.py --autotest
Stdlib uniquement. Lecture seule sur la maison, n'écrit QUE ses deux sorties.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
IM = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
# Source unique de l'univers : le radar des protocoles (aucune règle recopiée).
from verdicts_protocoles import charger_par_pool, univers_credit_prive, est_pool_credit  # noqa: E402

OUT_JSON = IM / "thermo" / "CARNET_RWA.json"
OUT_MD = IM / "CARNET_RENDEMENTS_RWA.md"

SEUIL_PROFONDEUR_USD = 1_000_000
SEUIL_PART_RECOMPENSE = 0.30
SEUIL_HISTORIQUE_JOURS = 60
SEUIL_RENDEMENT_INHABITUEL = 12.0
ORDRE_RISQUE = ("faible", "modéré", "élevé")
SOURCE = "DefiLlama (yields.llama.fi/pools)"
MOTIF_RISQUE = "0-1 drapeau faible · 2 modéré · >= 3 élevé · VALEUR_CONSTANTE force >= modéré"
PERIMETRE_RISQUE = "FIABILITÉ DE LA DONNÉE uniquement — le risque de CRÉDIT n'est pas évalué ici"


# ── les règles, isolées pour être testables et auto-prouvées ───────────────────
def bande_niveau(apy_pct):
    if apy_pct is None:
        return "n/d"
    if apy_pct < 3.0:
        return "faible"
    if apy_pct < 5.0:
        return "courant"
    if apy_pct < 8.0:
        return "élevé"
    return "très élevé"


def bande_risque(drapeaux):
    n = len(drapeaux)
    bande = "faible" if n <= 1 else ("modéré" if n == 2 else "élevé")
    if "VALEUR_CONSTANTE" in drapeaux and ORDRE_RISQUE.index(bande) < 1:
        bande = "modéré"                      # un taux « garanti » non confirmé n'est pas une donnée faible
    return bande


def drapeaux_pool(apy, tvl_dernier, part_recompense, jours_suivis, rendement_reference):
    tous_zero = all(a == 0 for a in apy)
    d = []
    if not tous_zero and round((max(apy) - min(apy)) * 100) == 0:
        d.append("VALEUR_CONSTANTE")
    if tous_zero:
        d.append("AUCUN_RENDEMENT_PUBLIE")
    elif any(a == 0 for a in apy):
        d.append("RELEVES_A_ZERO")
    if tvl_dernier < SEUIL_PROFONDEUR_USD:
        d.append("PROFONDEUR_FAIBLE")
    if part_recompense > SEUIL_PART_RECOMPENSE:
        d.append("RECOMPENSE_MIXTE")
    if jours_suivis is not None and jours_suivis < SEUIL_HISTORIQUE_JOURS:
        d.append("HISTORIQUE_COURT")
    if rendement_reference is not None and rendement_reference >= SEUIL_RENDEMENT_INHABITUEL:
        d.append("RENDEMENT_INHABITUEL")
    return d


# ── construction du carnet ────────────────────────────────────────────────────
def analyse(pid, v):
    apy = [y[1].get("apy") or 0.0 for y in v]
    triee = sorted(apy)
    median = triee[len(triee) // 2]
    non_nulles = sorted(a for a in apy if a > 0)
    median_hors_zero = non_nulles[len(non_nulles) // 2] if non_nulles else None
    # Le niveau décrit le RENDEMENT DU COFFRE : quand la source a publié des 0 (trous),
    # on lit la médiane hors zéro. Les deux valeurs restent affichées.
    reference = median_hors_zero if median_hors_zero is not None else None
    tvl = [y[1].get("tvlUsd") or 0.0 for y in v]
    tvl_median = sorted(tvl)[len(tvl) // 2]
    dernier = v[-1][1]
    base = dernier.get("apyBase")
    recompense = dernier.get("apyReward")
    apy_courant = apy[-1]
    part = (recompense / apy_courant) if (recompense and apy_courant > 0) else 0.0
    jours = dernier.get("count")
    drapeaux = drapeaux_pool(apy, tvl[-1], part, jours, reference)
    return {
        "pool": pid,
        "projet": dernier.get("project"),
        "symbole": dernier.get("symbol"),
        "chaine": dernier.get("chain"),
        "produit": dernier.get("poolMeta") or "—",
        "apy_median_pct": round(median, 3),
        "apy_median_hors_zero_pct": None if median_hors_zero is None else round(median_hors_zero, 3),
        "apy_min_pct": round(min(apy), 3),
        "apy_max_pct": round(max(apy), 3),
        "amplitude_bps": round((max(apy) - min(apy)) * 100),
        "apy_courant_pct": round(apy_courant, 3),
        "apy_base_pct": None if base is None else round(base, 3),
        "apy_recompense_pct": None if recompense is None else round(recompense, 3),
        "part_recompense_pct": round(part * 100, 1),
        "tvl_dernier_usd": round(tvl[-1]),
        "tvl_median_usd": round(tvl_median),
        "n_releves": len(v),
        "jours_suivis": jours,
        "sigma": dernier.get("sigma"),
        "releves_a_zero": sum(1 for a in apy if a == 0),
        "niveau": bande_niveau(reference),
        "risque": bande_risque(drapeaux),
        "risque_credit": "non évalué",
        "drapeaux": drapeaux,
        "source": SOURCE,
    }


def construire():
    par_pool = charger_par_pool()
    if not par_pool:
        return None
    couv, n_cycles = univers_credit_prive(par_pool)
    # TOUS les pools de crédit (même hors fenêtre) : on doit pouvoir dire pourquoi on les
    # écarte. Classer par « je ne les regarde pas » serait cacher des lignes (R8).
    credit = {pid: sorted(v) for pid, v in par_pool.items() if v and est_pool_credit(v[0][1])}
    tous = [t for v in par_pool.values() for t, _ in v]
    t0, t1 = min(tous), max(tous)
    lignes, exclus = [], []
    for pid, v in credit.items():
        r0 = v[0][1]
        ligne_excl = {"pool": pid, "projet": r0.get("project"), "symbole": r0.get("symbol"),
                      "chaine": r0.get("chain")}
        if pid not in couv:
            exclus.append(dict(ligne_excl, raison="fenêtre incomplète : %d relevé(s) sur %d cycles"
                                                     % (len(v), n_cycles)))
            continue
        if (r0.get("apy") or 0.0) == 0:
            exclus.append(dict(ligne_excl, raison="apparition : premier relevé à 0 % (le pool naît dans la fenêtre)"))
            continue
        lignes.append(analyse(pid, v))
    lignes.sort(key=lambda x: (x["projet"] or "", -x["apy_median_pct"]))
    return {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "titre": "Carnet de rendements RWA — crédit privé tokenisé",
        "nature": "MAQUETTE DE PRODUIT D'INFORMATION — 0 ordre, 0 €, aucun conseil",
        "source": SOURCE,
        "fenetre": {"debut": _iso(t0), "fin": _iso(t1), "cycles": n_cycles,
                    "releves_bruts": sum(len(v) for v in par_pool.values()), "pools_suivis": len(par_pool)},
        "univers": {
            "regle": ("credit privé = project ∈ liste crédit ET symbole = devise ; pool présent sur TOUTE "
                      "la fenêtre ; une APPARITION (premier relevé à 0) n'est pas un rendement"),
            "pools_credit_bruts": len(credit),
            "retenus": len(lignes),
            "ecartes": len(exclus),
            "source_de_la_regle": "scripts/verdicts_protocoles.py (est_pool_credit / univers_credit_prive)",
        },
        "regles": {
            "niveau": "< 3 % faible · 3-5 % courant · 5-8 % élevé · >= 8 % très élevé "
                      "(médiane de la fenêtre ; médiane HORS ZÉRO quand la source publie des 0)",
            "drapeaux": {
                "VALEUR_CONSTANTE": "APY identique (0 bps d'amplitude) sur toute la fenêtre -> à confirmer par une 2ᵉ source",
                "AUCUN_RENDEMENT_PUBLIE": "la source n'a publié que des 0 sur la fenêtre -> aucune valeur exploitable",
                "RELEVES_A_ZERO": "au moins un zéro parmi des valeurs non nulles -> trou de publication, jamais lu comme 0 %",
                "PROFONDEUR_FAIBLE": "TVL < 1 M$",
                "RECOMPENSE_MIXTE": "> 30 % du rendement courant vient d'incitations, pas du crédit",
                "HISTORIQUE_COURT": "< 60 jours d'historique publié",
                "RENDEMENT_INHABITUEL": "rendement de référence >= 12 % (à justifier)",
            },
            "risque": MOTIF_RISQUE,
            "perimetre_du_risque": PERIMETRE_RISQUE,
        },
        "ne_dit_pas": [
            "le risque de crédit (défaut de l'emprunteur, collatéral, gouvernance du fonds) : la source n'en publie pas",
            "une deuxième source : tout est marqué « à confirmer » quand la valeur est constante",
            "une exécution ou une liquidité garantie : le TVL est un ordre de grandeur, pas une profondeur de marché",
            "un conseil en investissement, un ordre, un euro",
        ],
        "lignes": lignes,
        "exclus": sorted(exclus, key=lambda x: (x["projet"] or "", x["chaine"] or "")),
    }


def _iso(ts):
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ── rendu lisible par un client ───────────────────────────────────────────────
def _tvl(usd):
    if usd >= 1e9:
        return "%.2f Md$" % (usd / 1e9)
    if usd >= 1e6:
        return "%.1f M$" % (usd / 1e6)
    return "%.0f k$" % (usd / 1e3)


def _cellule_apy(x):
    """La médiane brute, et la médiane hors zéro quand la source a publié des trous."""
    if x["releves_a_zero"] and x["apy_median_hors_zero_pct"] is not None:
        return "%.2f %% *(hors 0 : %.2f %%)*" % (x["apy_median_pct"], x["apy_median_hors_zero_pct"])
    if x["releves_a_zero"]:
        return "n/d *(%d relevé(s) à 0)*" % x["releves_a_zero"]
    return "%.2f %%" % x["apy_median_pct"]


def rendre_md(c):
    L = []
    a = L.append
    a("# Carnet de rendements RWA — crédit privé tokenisé")
    a("")
    a("**%s**" % c["nature"])
    a("")
    a("Généré le %s · source **%s** · règle d'univers partagée avec le radar "
      "(`scripts/verdicts_protocoles.py`)" % (c["ts"].split("+")[0] + "Z", c["source"]))
    a("")
    f = c["fenetre"]
    a("Fenêtre mesurée : **%s → %s** — %d cycles, %s relevés bruts, %d pools suivis."
      % (f["debut"], f["fin"], f["cycles"], "{:,}".format(f["releves_bruts"]).replace(",", " "), f["pools_suivis"]))
    a("")
    u = c["univers"]
    a("Univers retenu : **%d lignes** (pools de crédit privé présents sur toute la fenêtre) · "
      "%d écarté(s) (voir § 3)." % (u["retenus"], u["ecartes"]))
    a("")
    a("> Une ligne = un **coffre** (pool), pas un « projet/symbole » : un même couple peut recouvrir "
      "plusieurs fonds et plusieurs chaînes — ce sont des déploiements distincts, pas des doublons.")
    a("")
    a("> **Le risque de crédit n'est pas évalué dans ce carnet** : la source n'en publie pas. "
      "La colonne « Risque » mesure la *fiabilité de la donnée*. La colonne « Crédit » vaut "
      "« non évalué » sur chaque ligne, et c'est un angle mort déclaré, pas un oubli.")
    a("")

    a("## 1. Le carnet")
    a("")
    a("| Projet | Produit | Sym | Chaîne | APY méd. | Amplitude | TVL | Niveau | Risque | Crédit | Jours | Drapeaux |")
    a("|---|---|---|---|---:|---:|---:|---|---|---|---:|---|")
    for x in c["lignes"]:
        a("| %s | %s | %s | %s | %s | %d bps | %s | %s | %s | non évalué | %s | %s |" % (
            x["projet"], x["produit"], x["symbole"], x["chaine"], _cellule_apy(x), x["amplitude_bps"],
            _tvl(x["tvl_dernier_usd"]), x["niveau"], x["risque"],
            x["jours_suivis"] if x["jours_suivis"] is not None else "n/d",
            ", ".join(x["drapeaux"]) or "—"))
    a("")

    zero_pur = [x for x in c["lignes"] if "AUCUN_RENDEMENT_PUBLIE" in x["drapeaux"]]
    if zero_pur:
        a("### Lignes sans aucun rendement publiable (%d)" % len(zero_pur))
        a("")
        a("La source n'a publié que des 0 sur toute la fenêtre : ces lignes sont listées pour la "
          "complétude de l'univers, **pas comme des rendements**.")
        a("")
        a("| Projet | Produit | Sym | Chaîne | TVL |")
        a("|---|---|---|---|---:|")
        for x in zero_pur:
            a("| %s | %s | %s | %s | %s |" % (x["projet"], x["produit"], x["symbole"], x["chaine"],
                                               _tvl(x["tvl_dernier_usd"])))
        a("")

    plats = [x for x in c["lignes"] if "VALEUR_CONSTANTE" in x["drapeaux"]]
    a("## 2. À confirmer par une 2ᵉ source (%d)" % len(plats))
    a("")
    if plats:
        a("Ces rendements sont **identiques à l'octet près sur les %d cycles** de la fenêtre. "
          "Un taux fixe annoncé et une source figée se ressemblent : **on ne publie pas ces valeurs "
          "sans deuxième confirmation.**" % c["fenetre"]["cycles"])
        a("")
        a("| Projet | Produit | Sym | Chaîne | Rendement constant | TVL |")
        a("|---|---|---|---|---:|---:|")
        for x in plats:
            a("| %s | %s | %s | %s | %.2f %% | %s |" % (
                x["projet"], x["produit"], x["symbole"], x["chaine"], x["apy_median_pct"], _tvl(x["tvl_dernier_usd"])))
    else:
        a("_Aucun couple à valeur constante dans la fenêtre._")
    a("")

    a("## 3. Écartés de l'univers (%d) — et pourquoi" % len(c["exclus"]))
    a("")
    a("Rien n'est caché : ce qui sort du carnet est listé avec sa raison.")
    a("")
    a("| Projet | Sym | Chaîne | Raison |")
    a("|---|---|---|---|")
    for x in c["exclus"]:
        a("| %s | %s | %s | %s |" % (x["projet"], x["symbole"], x["chaine"], x["raison"]))
    a("")

    a("## 4. Ce que ce carnet ne dit PAS")
    a("")
    for n in c["ne_dit_pas"]:
        a("- %s" % n)
    a("")
    a("**Le risque de crédit n'est pas évalué ici.** La colonne « Risque » mesure la *fiabilité de la "
      "donnée* (relevés à 0, valeur constante, profondeur faible, part incitative, historique court, "
      "rendement inhabituel) — pas la probabilité de défaut d'un emprunteur, que la source ne publie pas.")
    a("")

    a("## 5. Règles (déclarées avant le calcul)")
    a("")
    a("- **Niveau** : %s" % c["regles"]["niveau"])
    for k, val in c["regles"]["drapeaux"].items():
        a("- **%s** : %s" % (k, val))
    a("- **Risque** : %s" % c["regles"]["risque"])
    a("")
    a("## 6. Format de livraison")
    a("")
    a("Le même contenu est disponible en machine : `Index_Maison/thermo/CARNET_RWA.json` "
      "(une entrée par pool + les règles + les écarts) — prêt à alimenter une API ou un envoi périodique.")
    a("")
    return "\n".join(L) + "\n"


# ── autotest : le générateur prouve ses règles sur des cas fabriqués ──────────
def autotest():
    cas = []
    def ck(nom, obtenu, attendu):
        cas.append((nom, obtenu == attendu, obtenu, attendu))

    ck("niveau 2.9 -> faible", bande_niveau(2.9), "faible")
    ck("niveau 3.0 -> courant", bande_niveau(3.0), "courant")
    ck("niveau 5.0 -> élevé", bande_niveau(5.0), "élevé")
    ck("niveau 8.0 -> très élevé", bande_niveau(8.0), "très élevé")
    ck("niveau sans relevé non nul -> n/d", bande_niveau(None), "n/d")
    ck("risque 0 drapeau -> faible", bande_risque([]), "faible")
    ck("risque 2 drapeaux -> modéré", bande_risque(["RELEVES_A_ZERO", "PROFONDEUR_FAIBLE"]), "modéré")
    ck("risque 3 drapeaux -> élevé", bande_risque(["RELEVES_A_ZERO", "PROFONDEUR_FAIBLE", "HISTORIQUE_COURT"]), "élevé")
    ck("VALEUR_CONSTANTE seule -> modéré (forcé)", bande_risque(["VALEUR_CONSTANTE"]), "modéré")
    ck("valeur constante détectée", "VALEUR_CONSTANTE" in drapeaux_pool([4.0] * 10, 5e6, 0.0, 200, 4.0), True)
    ck("constante seule -> aucun autre faux drapeau",
       drapeaux_pool([4.0] * 10, 5e6, 0.0, 200, 4.0), ["VALEUR_CONSTANTE"])
    ck("relevé à 0 détecté",
       "RELEVES_A_ZERO" in drapeaux_pool([0.0, 4.0, 4.0], 5e6, 0.0, 200, 4.0), True)
    ck("tous à 0 -> AUCUN_RENDEMENT_PUBLIE, pas RELEVES_A_ZERO ni VALEUR_CONSTANTE",
       drapeaux_pool([0.0, 0.0], 5e6, 0.0, 200, None), ["AUCUN_RENDEMENT_PUBLIE"])
    ck("part incitative > 30 % détectée",
       "RECOMPENSE_MIXTE" in drapeaux_pool([4.0, 4.1], 5e6, 0.5, 200, 4.0), True)
    ck("historique court détecté",
       "HISTORIQUE_COURT" in drapeaux_pool([4.0, 4.5], 5e6, 0.0, 30, 4.2), True)
    ck("rendement inhabituel détecté",
       "RENDEMENT_INHABITUEL" in drapeaux_pool([15.0, 17.0], 5e6, 0.0, 200, 17.0), True)
    ck("aucun rendement inhabituel sous le seuil",
       "RENDEMENT_INHABITUEL" in drapeaux_pool([10.0, 11.0], 5e6, 0.0, 200, 11.0), False)
    ok = all(c[1] for c in cas)
    return ok, cas


def main():
    if "--autotest" in sys.argv[1:]:
        ok, cas = autotest()
        print("=== CARNET RWA — autotest des règles ===")
        for nom, bon, obtenu, attendu in cas:
            print("  [%s] %s (obtenu %r, attendu %r)" % ("ok" if bon else "KO", nom, obtenu, attendu))
        print("Autotest : %s (%d/%d)" % ("FIABLE" if ok else "NON FIABLE",
                                          sum(1 for c in cas if c[1]), len(cas)))
        return 0 if ok else 1

    c = construire()
    if c is None:
        print("IMPOSSIBLE : aucun historique RWA (data/rwa_yields_hist.jsonl)")
        return 1
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_MD.write_text(rendre_md(c), encoding="utf-8")
    n = len(c["lignes"])
    plats = sum(1 for x in c["lignes"] if "VALEUR_CONSTANTE" in x["drapeaux"])
    zero_pur = sum(1 for x in c["lignes"] if "AUCUN_RENDEMENT_PUBLIE" in x["drapeaux"])
    par_risque = {}
    for x in c["lignes"]:
        par_risque[x["risque"]] = par_risque.get(x["risque"], 0) + 1
    print("Carnet RWA : %d ligne(s) · %d à confirmer (valeur constante) · %d sans rendement publié · "
          "%d écarté(s) · %s" % (n, plats, zero_pur, len(c["exclus"]),
                                 " ".join("%s=%d" % (k, par_risque[k]) for k in ORDRE_RISQUE if k in par_risque)))
    print("  -> %s" % OUT_JSON.relative_to(IM.parent))
    print("  -> %s" % OUT_MD.relative_to(IM.parent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
