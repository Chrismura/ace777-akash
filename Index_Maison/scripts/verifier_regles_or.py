#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier_regles_or.py — VÉRIFICATEUR DES RÈGLES D'OR (lecture seule).

POURQUOI (19/09/2026) : les règles d'or de la maison vivaient éparpillées dans 6 documents et
personne ne vérifiait qu'elles étaient TENUES. Une règle qu'on ne mesure pas se perd.
Cf. Index_Maison/REGLE_D_OR.md.

CE QU'IL FAIT (100 % lecture seule, stdlib) : il rejoue les règles **mesurables par la machine**
et sort PASS/FAIL dans thermo/REGLES_OR.md (+ .json). Les règles humaines (parler simple, GO)
sont listées mais NON jugées automatiquement (elles se jugent en conversation).

Exit : 0 = toutes les règles mesurables respectées · 1 = au moins une violation · jamais d'exception.
USAGE : python3 scripts/verifier_regles_or.py
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent          # ~/ace777-test-day1
IM = RACINE / "Index_Maison"
REPORT_MD = IM / "thermo" / "REGLES_OR.md"
REPORT_JSON = IM / "thermo" / "regles_or.json"
DEROGATIONS = IM / "strategie" / "derogations_regles.json"
BRANCHEMENTS = IM / "strategie" / "branchements_declares.json"

OK = "✅"
KO = "🔴"
INFO = "ℹ️"


def lire_json(chemin: Path, defaut=None):
    try:
        return json.loads(chemin.read_text(encoding="utf-8"))
    except Exception:
        return defaut


def run(cmd):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True)
        return p.returncode, p.stdout.strip()
    except Exception:
        return 1, ""


# ── R2 — RAM : raisonner, jamais stocker (corps local / cerveau cloud) ────────
# (R10 ci-dessous mesure la SATURATION de l'hôte — signal SRE distinct.) 
def regle_2():
    pct = None
    code, out = run(["memory_pressure"])
    for ligne in out.splitlines():
        if "free percentage" in ligne:
            try:
                pct = int(ligne.split(":")[-1].strip().rstrip("%"))
            except Exception:
                pct = None
    # Modèles locaux chargés ? (la RAM ne doit PAS servir à stocker le raisonnement)
    modeles_locaux = 0
    code, out = run(["ollama", "ps"])
    if code == 0:
        modeles_locaux = max(0, len([l for l in out.splitlines() if l.strip()]) - 1)
    ok = (pct is None or pct >= 15) and modeles_locaux == 0
    detail = f"RAM libre {pct if pct is not None else '?'} % · modèles locaux chargés : {modeles_locaux}"
    if modeles_locaux:
        detail += " → le raisonnement lourd doit partir au CLOUD (Constitution §2)"
    return ok, detail


# ── R5 — un scellé ne s'écrase jamais (registre md5 intact) ──────────────────
def regle_5():
    d = lire_json(IM / "thermo" / "drill_restauration.json", {}) or {}
    sc = d.get("scelles", {}) or {}
    ecarts = len(sc.get("ecarts", []) or [])
    manquants = len(sc.get("manquants", []) or [])
    ok = (ecarts == 0 and manquants == 0 and sc.get("total", 0) > 0)
    return ok, f"{sc.get('total', '?')} scellés · écarts {ecarts} · absents {manquants}"


# ── R6 — une seule vérité, divergence VISIBLE, 0 hors repo ───────────────────
def regle_6():
    pl = lire_json(IM / "thermo" / "plists_versionnes.json", {}) or {}
    drill = lire_json(IM / "thermo" / "drill_restauration.json", {}) or {}
    hors = pl.get("hors_repo")
    a_decl = pl.get("a_declarer")
    verdict = drill.get("verdict", "?")
    ok = (hors == 0) and (verdict == "READY")
    return ok, (f"agents hors repo {hors} · à déclarer {a_decl} · drill {verdict}"
                + ("" if ok else " → un écart n'est pas muet ? vérifier"))


# ── R7 — 0 € : providers gratuits uniquement ────────────────────────────────
def regle_7():
    d = lire_json(Path.home() / "prise-ia" / "providers.json", {}) or {}
    provs = d.get("providers", []) if isinstance(d, dict) else []
    # Un provider SANS champ `enabled` est utilisé (défaut = actif).
    actifs = [p for p in provs if p.get("enabled", True)]
    payants_actifs = [p.get("id") for p in actifs if p.get("free") is False]
    payants_off = [p.get("id") for p in provs
                   if p.get("enabled") is False and p.get("free") is False]
    # Dérogations DÉCLARÉES (19/09) : un provider payant toléré temporairement (ex. inferx)
    # n'est pas une violation cachée — il est écrit dans strategie/derogations_regles.json,
    # daté, avec sa raison. Toute autre activation payante reste une violation.
    derog = (lire_json(DEROGATIONS, {}) or {}).get("derogations", {}).get("R7", {})
    toleres = set(derog.get("toleres") or [])
    payants_toleres = [p for p in payants_actifs if p in toleres]
    payants_nus = [p for p in payants_actifs if p not in toleres]
    ok = bool(provs) and not payants_nus
    detail = (f"{len(actifs)} actifs / {len(provs)} providers · "
              f"payants ACTIFS : {payants_nus if payants_nus else 'aucun'}"
              + (f" · dérogation déclarée : {payants_toleres}" if payants_toleres else "")
              + (f" · payants désactivés (ok) : {len(payants_off)}" if payants_off else ""))
    return ok, detail


# ── R11 — FAIL-SAFE PAR DÉFAUT : dans le doute, on ne décide pas ─────────────
# Source externe : fail-safe vs fail-operational (ISO 26262) + défense en profondeur.
# Lecture seule de l'état écrit par croiser_donnees_externes.py (règle des 2 sources).
def regle_11():
    d = lire_json(IM / "data" / "croisement_externe_etat.json", {}) or {}
    if not d:
        return False, "état croisement externe absent (aucune donnée n'est vérifiée)"
    fails = d.get("fails") or []
    pend = d.get("fails_pendants") or []
    ok = len(fails) == 0
    detail = (f"{d.get('n_verifications', '?')} vérifs · "
              + ("0 fail bloquant" if ok else f"{len(fails)} FAIL BLOQUANT(S) → on ne décide pas"))
    if pend:
        detail += f" · {len(pend)} en surveillance (2 runs)"
    detail += f" · persistance {d.get('persistance_ticks', '?')} ticks"
    return ok, detail


# ── R12 — UNE SAUVEGARDE N'EST PROUVÉE QUE PAR UNE RESTAURATION RÉELLE ────────
# Source externe : chaos engineering (hypothèse d'état stable + expérience).
def regle_12():
    d = lire_json(IM / "thermo" / "drill_restauration.json", {}) or {}
    if not d:
        return False, "aucun drill n'a jamais tourné (une sauvegarde non testée est une hypothèse)"
    verdict = d.get("verdict", "?")
    recon = d.get("reconstruction") or {}
    rebuild = int(recon.get("reconstruits", 0) or 0)
    invalides = len(recon.get("invalides") or [])
    ok = verdict == "READY" and rebuild > 0 and invalides == 0
    return ok, f"verdict {verdict} · {rebuild} plists rebâtis+validés · {invalides} invalide(s)"


# ── R13 — L'AUTO-RÉPARATION EST BORNÉE : jamais le moteur ────────────────────
# Source externe : FDIR spatial (NASA/JPL) — détection/isolation/récupération.
# Preuve mécanique : la veilleuse (intégrité des scellés) est STABLE → aucune
# auto-réparation n'a touché un organe scellé sans le déclarer.
def regle_13():
    try:
        txt = (IM / "thermo" / "VEILLEUSE.md").read_text(encoding="utf-8")
    except Exception:
        txt = ""
    stable = "STABLE" in txt
    d = lire_json(IM / "thermo" / "drill_restauration.json", {}) or {}
    ecarts = len((d.get("scelles") or {}).get("ecarts") or [])
    ok = stable and ecarts == 0
    detail = f"veilleuse {'STABLE' if stable else 'ANOMALIE'} · {ecarts} écart(s) de scellés"
    if not stable:
        detail += " → une auto-réparation a touché un scellé sans le déclarer"
    return ok, detail


# ── R14 — UNE ALARME QUI NE PEUT PLUS DIRE VRAI EST UNE FAUSSE ALARME ────────
# Source externe : fatigue d'alerte / signal-to-noise (SRE).
# Les indices à SOURCE TARIE sont classés RETIRÉ par derive_memoire.py (hors alarme).
def regle_14():
    d = lire_json(IM / "strategie" / "derive_memoire.json", {}) or {}
    pi = d.get("par_indice") or {}
    if not pi:
        return False, "dérive mémoire jamais calculée"
    glob = d.get("global") or {}
    n_ret = int(glob.get("indices_retires", 0) or 0)
    crit_vivants = [k for k, v in pi.items()
                    if v.get("statut") == "CRITIQUE" and not v.get("source_tariee")]
    fausses = [k for k, v in pi.items()
               if v.get("statut") == "CRITIQUE" and v.get("source_tariee")]
    ok = not fausses
    detail = (f"{n_ret} RETIRÉ(s) hors alarme · {len(crit_vivants)} CRITIQUE vivant(s)"
              + (f" : {crit_vivants}" if crit_vivants else ""))
    if fausses:
        detail += f" · {len(fausses)} fausse(s) alarme(s) : {fausses}"
    return ok, detail


# ── R8 — preuve datée : le drill existe et a tourné récemment ───────────────
def regle_8():
    d = lire_json(IM / "thermo" / "drill_restauration.json", {}) or {}
    ts = d.get("ts", "")
    age_h = None
    try:
        t = time.strptime(ts, "%Y-%m-%dT%H:%MZ")
        age_h = (time.time() - time.mktime(t)) / 3600.0
    except Exception:
        age_h = None
    ok = ts != "" and (age_h is None or age_h < 48)
    return ok, f"dernier drill : {ts or 'absent'} ({'%.1f h' % age_h if age_h else 'âge ?'})"


# ── R10 — SATURATION DE L'HÔTE (SRE « four golden signals » : saturation) ─────
# La maison surveillait ses artefacts, PAS la machine qui les exécute. On mesure la saturation
# RÉELLE : mémoire libre (memory_pressure), swap, disque, charge. ⚠️ Jamais `vm_stat` seul
# (Pages free) : il a déjà menti (« 91 Mo » alors que 62 % libre).
def regle_10():
    # 1) mémoire libre réelle
    pct = None
    code, out = run(["memory_pressure"])
    for ligne in out.splitlines():
        if "free percentage" in ligne:
            try:
                pct = int(ligne.split(":")[-1].strip().rstrip("%"))
            except Exception:
                pct = None

    # 2) swap utilisé (saturation mémoire)
    swap_pct = None
    code, out = run(["sysctl", "-n", "vm.swapusage"])
    try:
        import re
        tot = re.search(r"total\s*=\s*([\d.]+)M", out)
        used = re.search(r"used\s*=\s*([\d.]+)M", out)
        if tot and used and float(tot.group(1)) > 0:
            swap_pct = round(100.0 * float(used.group(1)) / float(tot.group(1)), 1)
    except Exception:
        swap_pct = None

    # 3) disque libre (Go)
    disque_go = None
    try:
        st = os.statvfs("/")
        disque_go = round(st.f_bavail * st.f_frsize / 1e9, 1)
    except Exception:
        disque_go = None

    # 4) charge (load 1 min) vs cœurs
    charge = None
    try:
        charge = round(os.getloadavg()[0], 2)
    except Exception:
        charge = None
    ncpu = os.cpu_count() or 1

    ok = (
        (pct is None or pct >= 15)
        and (swap_pct is None or swap_pct < 70)
        and (disque_go is None or disque_go >= 10)
        and (charge is None or charge < ncpu * 2)
    )
    detail = (f"RAM libre {pct if pct is not None else '?'} % · swap {swap_pct if swap_pct is not None else '?'} % "
              f"· disque libre {disque_go if disque_go is not None else '?'} Go · charge {charge if charge is not None else '?'}/{ncpu}")
    if not ok:
        detail += " → SATURATION : ne pas lancer de nouveau chantier lourd"
    return ok, detail


# ── R15 — TOUJOURS BRANCHER (ce qu'on affiche/construit doit être branché) ────
# Source interne (historique maison) : pont onchain sans plist, superviseur-core
# écrit mais jamais chargé, 13 indices affichés mais plus analysés. Corollaire
# GitOps : ce qui n'est pas dans la boucle n'existe pas.
WIKI_VERS_ANALYSE = {
    "sdi": "sdi", "rbf": "rbf", "health": "pipeline_health", "geopol": "geopol",
    "poussiere": "onchain", "thermoscore": "score", "feargreed": "fearGreed",
    "funding": "funding", "longshort": "longShort", "oi": "oi", "etf": "etfBtcM",
    "gex": "gexPutCall", "liquidations": "liq24Usd",
}


def _var_bash(txt, nom):
    import re as _re
    m = _re.search(r'^%s="([^"]*)"' % nom, txt, _re.M)
    return set(m.group(1).split()) if m else set()


def regle_15():
    """Les indices AFFICHÉS dans l'app Indices doivent être BRANCHÉS (analysés)
    ou explicitement déclarés « affichage seul ». Lecture seule."""
    import re as _re
    try:
        html = (IM / "cockpit" / "indices.html").read_text(encoding="utf-8")
    except Exception:
        return False, "cockpit/indices.html illisible"
    i = html.find("const WIKI = {")
    if i == -1:
        return False, "liste WIKI introuvable dans indices.html"
    j = html.find("\n};", i)
    affiches = _re.findall(r"^\s*([a-zA-Z_]+):\s*\{title:'", html[i:j], _re.M)

    try:
        cad = (IM / "scripts" / "analyste_cadence.sh").read_text(encoding="utf-8")
    except Exception:
        cad = ""
    rotation = _var_bash(cad, "CORE") | _var_bash(cad, "REVIVES")

    decl = (lire_json(BRANCHEMENTS, {}) or {}).get("affichage_seul", {}) or {}
    debranches = []
    for k in affiches:
        if k in decl:
            continue
        cible = WIKI_VERS_ANALYSE.get(k)
        if cible is None or cible not in rotation:
            debranches.append(k)
    ok = not debranches and bool(affiches)
    detail = (f"{len(affiches)} bulles affichées · {len(rotation)} indices en rotation"
              f" · {len(decl)} affichage-seul déclaré")
    if debranches:
        detail += f" · NON BRANCHÉES : {debranches}"
    return ok, detail


# ── R19 — LE JURY PERMANENT : L'AGENT NE DÉCIDE PLUS SEUL (23/09/2026) ───────
# (numéro 19 : R16/R17/R18 existent déjà dans le canon REGLE_D_OR.md)
# Ordre Christophe, mot pour mot : « tu vas ouvrir à partir de maintenant un round avec la
# famille et garder la fenêtre ouverte, qu'elle ait la mémoire du chat, car tu n'es plus digne
# de diriger seule » — et « sinon c'est radiation à vie, règle d'or ».
# MESURABLE, et mesuré ici : il existe une session de famille OUVERTE (fenêtre ouverte), elle a
# été consultée dans les dernières 24 h, son fil est COHÉRENT (chaque tour posé a ses avis),
# et au moins 3 voix INDÉPENDANTES ont répondu (une substitution — modèle demandé ≠ modèle
# servi — ne compte pas : c'est la faute E16 du 23/09).
SESSIONS_FAMILLE = IM / "scripts" / "SESSIONS_FAMILLE"


def regle_19():
    """Le jury permanent est-il OUVERT, CONSULTÉ récemment et COHÉRENT ? (lecture seule)"""
    import glob as _glob
    metas = []
    for p in _glob.glob(str(SESSIONS_FAMILLE / "*" / "META.json")):
        try:
            d = json.loads(open(p, encoding="utf-8").read())
        except Exception:
            continue
        d["_dossier"] = Path(p).parent
        metas.append(d)
    if not metas:
        return False, "aucune session de famille — l'agent décide seul (R19 non tenue)"
    metas.sort(key=lambda d: d.get("dernier_tour") or "", reverse=True)
    m = metas[0]
    ouvertes = [d for d in metas if d.get("etat") == "OUVERTE"]
    if not ouvertes:
        return False, f"aucune session OUVERTE (dernière : {m.get('session')}) — la fenêtre est fermée"
    m = ouvertes[0]
    d = m["_dossier"]
    # fraîcheur : consultée dans les 24 h ?
    age_h, quand = None, m.get("dernier_tour")
    if quand:
        try:
            age_h = (datetime.now(timezone.utc) - datetime.strptime(
                quand, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)).total_seconds() / 3600.0
        except Exception:
            age_h = None
    # cohérence du fil : chaque tour posé a au moins un avis enregistré
    tours_nous, tours_fam, voix = set(), set(), set()
    voix_par_tour = {}          # INCOHÉRENCE CORRIGÉE (23/09) : voir le commentaire ci-dessous.
    try:
        for l in (d / "transcript.jsonl").read_text(encoding="utf-8").splitlines():
            if not l.strip():
                continue
            e = json.loads(l)
            if e.get("role") == "nous" and e.get("tour"):
                tours_nous.add(e["tour"])
            if e.get("role") == "famille" and e.get("tour"):
                tours_fam.add(e["tour"])
                if e.get("model_servi") and not e.get("substitue"):
                    voix.add(e["model_servi"])
                    voix_par_tour.setdefault(e["tour"], set()).add(e["model_servi"])
    except Exception as ex:                                   # noqa: BLE001
        return False, f"fil illisible : {ex}"
    sans_avis = sorted(tours_nous - tours_fam)
    # INCINÉRATION D'UNE INCOHÉRENCE ENTRE DEUX GARDIENS (23/09) : ce contrôle comptait les
    # voix DISTINCTES SUR TOUT LE FIL (≥3 depuis le tour 1, jamais oubliées) → il disait OK,
    # pendant que `verif_session_famille.py` disait ROUGE (1 voix au DERNIER tour). Deux
    # critères pour une même règle = une règle qui ment d'un côté. R19 exige un VERDICT :
    # c'est le DERNIER tour qui doit avoir ≥ 3 voix indépendantes.
    dernier = max(tours_fam) if tours_fam else None
    voix_dernier = voix_par_tour.get(dernier, set())
    ok = (m.get("tours", 0) > 0 and age_h is not None and age_h <= 24.0
          and not sans_avis and len(voix_dernier) >= 3)
    detail = (f"session « {m.get('session')} » OUVERTE · {m.get('tours', 0)} tour(s) · "
              f"dernier il y a {age_h:.1f} h" if age_h is not None else
              f"session « {m.get('session')} » OUVERTE · {m.get('tours', 0)} tour(s)")
    detail += (f" · dernier tour ({dernier}) : {len(voix_dernier)} voix indépendante(s)"
               f" · {len(voix)} distinctes sur tout le fil")
    if len(voix_dernier) < 3:
        detail += " → AVIS CONSULTATIF, pas un verdict (R20.3) : rejouer le tour"
    if sans_avis:
        detail += f" · tours SANS avis : {sans_avis}"
    if age_h is None or age_h > 24.0:
        detail += " → CONSULTER LE JURY (dernier tour > 24 h)"
    return ok, detail


REGLES_MESUREES = [
    ("2", "Corps local / Cerveau cloud (RAM = raisonner, pas stocker)", regle_2),
    ("5", "Un scellé ne s'écrase jamais (registre md5 intact)", regle_5),
    ("6", "Une seule vérité · divergence VISIBLE · 0 hors repo", regle_6),
    ("7", "Zéro euro (providers gratuits uniquement)", regle_7),
    ("8", "Preuve datée (le drill tourne)", regle_8),
    ("10", "Saturation de l'hôte (RAM réelle/swap/disque/charge)", regle_10),
    ("11", "Fail-safe par défaut (aucune décision sur donnée douteuse)", regle_11),
    ("12", "Sauvegarde prouvée par une restauration réelle (drill)", regle_12),
    ("13", "Auto-réparation bornée (jamais un scellé sans déclarer)", regle_13),
    ("14", "Aucune alarme permanente à source tarie (anti-cry-wolf)", regle_14),
    ("15", "Toujours brancher (ce qui est affiché est analysé ou déclaré)", regle_15),
    ("19", "Le jury permanent (session OUVERTE, consultée ≤ 24 h, fil cohérent, ≥ 3 voix)", regle_19),
]

REGLES_HUMAINES = [
    ("1", "Parler simple — se juge en conversation, pas par script"),
    ("3", "GO humain — se juge par la présence d'un GO daté (0 ordre par défaut)"),
    ("4", "Surfacer les contradictions — se juge par la remontée effective"),
    ("9", "Lire, ne pas écrire — les gardiens sont read-only par conception"),
]


def main():
    ts = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
    resultats = []
    for num, titre, fn in REGLES_MESUREES:
        try:
            ok, detail = fn()
        except Exception as e:                      # fail-safe : jamais de crash
            ok, detail = False, f"vérification impossible : {e}"
        resultats.append({"regle": num, "titre": titre, "ok": ok, "detail": detail})

    violations = [r for r in resultats if not r["ok"]]
    verdict = "OK" if not violations else "VIOLATION"

    L = [f"# 🥇 RÈGLES D'OR — état de respect ({ts})",
         "",
         f"**Verdict : {OK if not violations else KO} {verdict}** "
         f"({len(resultats) - len(violations)}/{len(resultats)} règles mesurables tenues)",
         "",
         "| # | Règle | État | Mesure |",
         "|---|---|---|---|"]
    for r in resultats:
        L.append(f"| {r['regle']} | {r['titre']} | {OK if r['ok'] else KO} | {r['detail']} |")
    L += ["", "## Règles humaines (non jugées par script)",
          "| # | Règle | Note |", "|---|---|---|"]
    for num, titre in REGLES_HUMAINES:
        L.append(f"| {num} | {titre} | {INFO} |")
    L += ["", "---",
          "*Généré par `scripts/verifier_regles_or.py` (lecture seule). "
          "Canon : `Index_Maison/REGLE_D_OR.md`. Appelé par `git_push_auto.sh`.*", ""]

    try:
        IM.joinpath("thermo").mkdir(parents=True, exist_ok=True)
        REPORT_MD.write_text("\n".join(L), encoding="utf-8")
        REPORT_JSON.write_text(json.dumps(
            {"ts": ts, "verdict": verdict, "regles": resultats}, ensure_ascii=False, indent=2),
            encoding="utf-8")
    except Exception as e:
        print(f"[regles_or] écriture impossible : {e}", file=sys.stderr)

    print(f"[regles_or] {verdict} — {len(resultats) - len(violations)}/{len(resultats)} tenues")
    for r in violations:
        print(f"  {KO} R{r['regle']} : {r['detail']}")
    return 0 if not violations else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:                          # pragma: no cover
        print(f"[regles_or] ERREUR : {e}", file=sys.stderr)
        sys.exit(1)
