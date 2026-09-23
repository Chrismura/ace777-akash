#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIF SEUIL MOTEUR — LE GARDE-FOU CONTRE UNE CLASSE D'ERREUR ENTIÈRE
===================================================================
POURQUOI CE SCRIPT EXISTE (23/09/2026)
  J'ai écrit, puis publié, puis répété pendant trois jours un chiffre FAUX :
  « le repli exigé par le moteur vaut max(dip 4,2 % ; 5 % ; 0,30 × m6), soit 5 à 12,75 %
  sur RIZE ». Le vrai seuil était **21,70 %**. Il manquait LE terme dominant :
      dip = max(dip_pct du profil ; DIP_CADENCE_MULT × cadence)
  (paper_diprip.score_pair, l.566). La cadence de RIZE — que LE MOTEUR écrit lui-même dans
  son journal (colonne 9) — vaut ~49 %, donc 0,50 × 49 = 24,55 % de repli exigé.
  L'erreur n'était pas un chiffre : c'était **une méthode** — reconstruire un seuil en
  recopiant une formule de mémoire au lieu de la confronter à ce que le moteur ÉCRIT.

CE QUE CE SCRIPT FAIT (lecture seule, 0 ordre, 0 €)
  1. INVARIANT SUR DONNÉES RÉELLES : il lit le journal du run, prend chaque ligne où le
     moteur a écrit SES propres chiffres (`ATTENTE:IMPULSE_WAIT dd6=… seuil=… m6=…` +
     sa cadence colonne 9), **recalcule le seuil depuis `config/defaults.env` et le profil
     de la paire**, et compare. Si les deux divergent → **il crie** (sortie rc=3).
     C'est ce contrôle qui aurait attrapé mon erreur en 1 seconde, tous les jours.
  2. DÉTERMINANCE (R15) : il nomme **le terme qui décide** par paire (cadence / plancher
     profil / m6 / plancher global). Un seuil qu'on ne sait pas expliquer ne se discute pas.
  3. DÉTECTEUR D'INSTRUMENTS : il balaie les scripts de la maison et signale tout fichier
     qui **recalcule un seuil d'entrée sans le terme cadence** (motif exact de l'erreur).
  4. AUTOTEST : il vérifie qu'il SAIT détecter (un chiffre faux injecté doit faire sortir
     rc=3). Un gardien qui ne peut pas échouer n'est pas un gardien.

Usage :
  python3 verif_seuil_moteur.py                 # invariant + déterminance + détecteur
  python3 verif_seuil_moteur.py --autotest      # prouve qu'il détecte (rc=3 attendu)
  python3 verif_seuil_moteur.py --json runs/SEUIL_MOTEUR.json
Sortie : rc=0 conforme · rc=3 DÉSACCORD (à traiter) · rc=2 pas assez de données
"""
import argparse
import glob
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
HULK = os.path.dirname(ICI)
RACINE = os.path.dirname(HULK)
RUNS = os.path.join(HULK, "runs")
ENGINE = os.path.join(ICI, "paper_diprip.py")     # la FORMULE de référence, lue à la source
ENV = os.path.join(HULK, "config", "defaults.env")
PROFILS = os.path.join(HULK, "strategie", "universe_profils.json")
# ÉTAT lu par le cockpit (même convention que thermo/drill_restauration.json,
# thermo/regles_or.json… : un verdict qui n'est affiché nulle part n'existe pas).
STATE = os.path.join(RACINE, "Index_Maison", "thermo", "seuil_moteur.json")
SOURCES_AUDIT = [ICI, os.path.join(RACINE, "Index_Maison", "scripts")]

# motif exact de l'erreur : on calcule un seuil d'entrée (repli) …
MOTIF_SEUIL = re.compile(r"IMPULSE_PULLBACK|impulse_entry|impulse_pullback")
# … sans le terme qui le domine.
MOTIF_CADENCE = re.compile(r"DIP_CADENCE_MULT")
# … ET seulement si c'est un CALCUL. Sinon on signalerait à tort les scripts qui se
# contentent de LISTER les clés lues par le moteur (ex. `"impulse_pullback_min_pct",`
# dans la liste des 11 clés `calib` de serrure_preflight.py) — un faux positif, et un
# gardien qui crie à tort finit ignoré (c'est le même défaut que le faux vert).
MOTIF_CALCUL = re.compile(r"max\(|impulse_entry\s*=|seuil|>=|<=|,\s*PULLBACK")
# fichiers exclus de l'audit : ils TRAITENT le motif (ce gardien, le moteur lui-même,
# et les instruments déjà corrigés/validés qui lisent la cadence par un autre chemin).
EXCLUS = {"verif_seuil_moteur.py", "paper_diprip.py"}


def env():
    cfg = {}
    if os.path.exists(ENV):
        for l in open(ENV, encoding="utf-8"):
            l = l.strip()
            if l and not l.startswith("#") and "=" in l:
                k, v = l.split("=", 1)
                cfg[k.strip()] = v.strip()
    return cfg


def profil(paire):
    try:
        return (json.load(open(PROFILS, encoding="utf-8")).get(paire) or {})
    except Exception:
        return {}


def csv_actuel():
    cands = [c for c in glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv"))
             if os.path.getsize(c) > 1000]
    return max(cands, key=os.path.getmtime) if cands else None


def seuil_attendu(cal, cfg, cadence, m6):
    """LA FORMULE RÉELLE, recopiée de score_pair() — et rien d'autre.
    On renvoie aussi le terme DOMINANT (déterminance R15) et chaque terme."""
    if cal.get("dip_pct") is not None:
        dip_floor = float(cal["dip_pct"])
        src_floor = "profil"%()
    else:
        dip_floor = float(cfg.get("DIP_FLOOR_PCT", "2.5"))
        src_floor = "DIP_FLOOR_PCT"
    mult = float(cfg.get("DIP_CADENCE_MULT", "0.45"))
    t_cad = cadence * mult
    dip = max(dip_floor, t_cad)
    # FAUTE E23 (23/09/2026, ce gardien s'accusait LUI-MÊME) : j'avais omis le terme
    # `impulse_pullback_min_pct` du PROFIL PAR PAIRE (paper_diprip.score_pair l.649 :
    # `_cal.get("impulse_pullback_min_pct", cfg.get("IMPULSE_PULLBACK_MIN_PCT", "5"))`).
    # Résultat : sur BTC (profil 1,5 < global 5,0) le gardien annonçait « écrit 1,70 ·
    # recalculé 4,25 — DÉSACCORD » alors que LE MOTEUR AVAIT RAISON. Un gardien qui
    # accuse à tort le moteur est pire qu'aucun gardien (R14 : fausse alarme).
    if cal.get("impulse_pullback_min_pct") is not None:
        pull_min = float(cal["impulse_pullback_min_pct"])
        src_pull = "profil.impulse_pullback_min_pct"
    else:
        pull_min = float(cfg.get("IMPULSE_PULLBACK_MIN_PCT", "5"))
        src_pull = "IMPULSE_PULLBACK_MIN_PCT"
    pull_frac = float(cfg.get("IMPULSE_PULLBACK_FRAC", "0.30"))
    t_m6 = m6 * pull_frac
    terms = {"profil/plancher": (dip_floor, src_floor), "cadence": (t_cad, "0.50 × cadence"),
             "plancher_pullback": (pull_min, src_pull),
             "m6": (t_m6, "0.30 × m6")}
    need = max(dip, pull_min, t_m6)
    dom = max(terms.items(), key=lambda kv: kv[1][0])[0]
    return need, dom, terms


def lignes_refus(csv_path, limite=4000):
    """Lignes où le moteur a écrit SES chiffres de refus (forme introduite le 23/09)."""
    out = []
    rx = re.compile(r"ATTENTE:IMPULSE_WAIT dd6=([\d.]+) seuil=([\d.]+) manque=([\d.]+)pt m6=([\d.]+)")
    with open(csv_path, encoding="utf-8", errors="ignore") as f:
        for l in f:
            if "ATTENTE:IMPULSE_WAIT dd6=" not in l:
                continue
            c = l.rstrip("\n").split(",")
            if len(c) < 11:
                continue
            m = rx.search(c[10])
            if not m or not c[9].strip():
                continue
            out.append({"utc": c[0], "paire": c[1], "cadence": float(c[9]),
                        "dd6": float(m.group(1)), "seuil": float(m.group(2)),
                        "m6": float(m.group(4))})
    return out[-limite:]


def invariant(rows, cfg, tol=0.05):
    """LE CŒUR : le seuil écrit par le moteur == le seuil recalculé depuis la config."""
    ok, ko, par_paire = 0, [], {}
    for r in rows:
        # `cal` injecté (AUTOTEST seulement) : permet de prouver le gardien sur un profil
        # SYNTHÉTIQUE (ex. BTC réel, pull_min profil 1,5 < global 5,0). En production
        # `lignes_refus` ne pose jamais `cal` → comportement inchangé.
        cal = r.get("cal") or (profil(r["paire"]) or {}).get("calib") or {}
        need, dom, terms = seuil_attendu(cal, cfg, r["cadence"], r["m6"])
        attendu = need * 0.85                      # seuil de BASCULE de régime
        ecart = r["seuil"] - attendu
        d = par_paire.setdefault(r["paire"], {"n": 0, "dom": {}, "cad": r["cadence"]})
        d["n"] += 1
        d["dom"][dom] = d["dom"].get(dom, 0) + 1
        d["cad"] = r["cadence"]
        if abs(ecart) <= tol:
            ok += 1
        elif len(ko) < 8:
            ko.append({**r, "attendu": round(attendu, 2), "ecart": round(ecart, 2)})
    return ok, ko, par_paire


def detecter_instruments():
    """Signale tout instrument qui RECALCULE un seuil d'entrée SANS le terme cadence :
    c'est le motif exact de mon erreur, cherché par le texte, pas par intuition."""
    flags = []
    for dossier in SOURCES_AUDIT:
        if not os.path.isdir(dossier):
            continue
        for p in sorted(glob.glob(os.path.join(dossier, "*.py"))):
            nom = os.path.basename(p)
            # FAUX POSITIF CORRIGÉ (23/09, tour 5) : les outils de DÉCLARATION (`declarer_*`)
            # citent la formule EN PROSE dans leurs textes — le motif les attrapait. Or un
            # gardien qui crie à tort finit ignoré (R14) : on les exclut NOMMÉMENT (audit de
            # CALCUL, pas de documentation). Vérifié : le même soir, ce détecteur accusait
            # `declarer_rescel_20260923b.py` alors qu'il ne recalcule aucun seuil.
            if nom in EXCLUS or nom.endswith(".bak") or nom.startswith("declarer_"):
                continue
            try:
                txt = open(p, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            touche_calcul = any(MOTIF_SEUIL.search(l) and MOTIF_CALCUL.search(l)
                                for l in txt.splitlines())
            if touche_calcul and not MOTIF_CADENCE.search(txt):
                flags.append(os.path.relpath(p, RACINE))
    return flags


def detecter_termes_profil():
    """DÉTECTEUR DE TERMES DU PROFIL — rendre la faute E23 IMPOSSIBLE au lieu de la corriger.

    Exigence de la famille (tour 5, 23/09, 3 voix convergentes) : « exiger un test qui
    injecte un profil SYNTHÉTIQUE COMPLET et vérifie que TOUS les termes du profil sont
    lus ; un gardien qui accuse le moteur sans ça est DÉSACTIVÉ ».

    Réalisation MÉCANIQUE (pas une promesse) : on LIT la formule du moteur dans son propre
    source (`impulse_entry = max(...)` de score_pair), on en extrait CHAQUE clé de profil
    (`_cal.get("X"` / `_cal["X"]`), et on exige que CE gardien lise la même clé. Si une clé
    est ajoutée à la formule du moteur et non lue ici, le gardien se SIGNALE (donc se
    désactive) au lieu d'accuser le moteur. La faute devient impossible, pas seulement
    évitée : c'est la différence entre corriger et empêcher.
    """
    try:
        src = open(ENGINE, encoding="utf-8", errors="ignore").read()
    except Exception:
        return None, []
    m = re.search(r"impulse_entry\s*=\s*max\((.*?)\)\s*\n", src, re.S)
    if not m:
        return None, []
    expr = m.group(1)
    cles = set(re.findall(r"_cal(?:\.get\(\s*|\[)\s*['\"]([a-z_]+)['\"]", expr))
    # `dip` est un terme de la formule : sa clé de profil vit dans `dip_floor = float(_cal.get(
    # "dip_pct"...))`, une ligne au-dessus. On récupère donc aussi la clé qui construit `dip`.
    m2 = re.search(r"dip_floor\s*=\s*float\(_cal\.get\(\s*['\"]([a-z_]+)['\"]", src)
    if m2:
        cles.add(m2.group(1))
    try:
        moi = open(__file__, encoding="utf-8", errors="ignore").read()
    except Exception:
        return None, []
    manquants = sorted(k for k in cles
                       if not re.search(r"cal(?:\.get\(\s*|\[)\s*['\"]" + re.escape(k), moi))
    return cles, manquants


def autotest(cfg):
    """Preuve que le gardien SAIT échouer — et MESURE son taux de détection.

    Objection de la famille (nemotron-120b, 23/09) : « aucune preuve de son taux de faux
    négatifs ». Réponse : on n'injecte pas UNE erreur, on injecte TOUTES les façons de
    tronquer la formule — dont celle que j'ai réellement commise. Un gardien qui ne
    détecte que le cas déjà connu ne protège que du passé.
    """
    # DEUX POINTS D'ESSAI, PARCE QU'UN SEUL NE SUFFIT PAS (leçon attrapée le 23/09 par ce
    # gardien lui-même) : sur une paire à cadence 49 %, le terme cadence ÉCRASE le plancher
    # et le terme m6 — donc injecter « sans le plancher » ne change RIEN et n'est pas une
    # erreur DÉTECTABLE là. Un autotest qui compte ces cas comme des échecs crie à tort ; un
    # autotest qui les ignore ne prouve rien. On teste donc les deux régimes : celui où la
    # cadence domine (RIZE) et celui où le plancher / m6 dominent (paire docile).
    points = [("RIZE (cadence domine)", {"dip_pct": 4.2}, 49.1, 12.5),
              ("paire docile (plancher domine)", {"dip_pct": 2.5}, 2.6, 12.5),
              ("rafale verticale (m6 domine)", {"dip_pct": 2.5}, 2.6, 60.0),
              # CAS BTC RÉEL (23/09) : profil pull_min 1,5 < global 5,0 — c'est LE point où
              # l'omission du terme profil faisait accuser le moteur à tort (classe E23).
              ("profil pull_min bas (BTC réel)", {"dip_pct": 2.0,
                                              "impulse_pullback_min_pct": 1.5}, 3.03, 1.7)]
    frac = float(cfg.get("IMPULSE_PULLBACK_FRAC", "0.30"))
    mult = float(cfg.get("DIP_CADENCE_MULT", "0.50"))
    minp = float(cfg.get("IMPULSE_PULLBACK_MIN_PCT", "5"))
    total_dis, total_det = 0, 0
    for label, cal, cad, m6 in points:
        need, _dom, _t = seuil_attendu(cal, cfg, cad, m6)
        vrai = round(need * 0.85, 2)
        plancher = float(cal.get("dip_pct") or cfg.get("DIP_FLOOR_PCT", "2.5"))
        faux = {
            "sans le terme cadence (MON erreur réelle)":
                max(plancher, minp, m6 * frac) * 0.85,
            "cadence avec un mauvais multiplicateur (0,30 au lieu de 0,50)":
                max(plancher, cad * 0.30, minp, m6 * frac) * 0.85,
            "sans le plancher IMPULSE_PULLBACK_MIN_PCT":
                max(plancher, cad * mult, m6 * frac) * 0.85,
            # MON erreur réelle E23 : recalculer avec le plancher GLOBAL au lieu du terme
            # `impulse_pullback_min_pct` DU PROFIL (le gardien accusait le moteur).
            "sans le terme impulse_pullback_min_pct DU PROFIL (mon E23)":
                max(plancher, cad * mult, minp, m6 * frac) * 0.85,
            "sans le terme 0,30 × m6":
                max(plancher, cad * mult, minp) * 0.85,
            "sans le facteur 0,85 de la porte de régime": need,
        }
        r = {"utc": "AUTOTEST", "paire": "TEST", "cadence": cad, "dd6": 0.0,
             "seuil": vrai, "m6": m6, "cal": cal}
        ok_vrai, _ko, _ = invariant([r], cfg)
        print(f"  AUTOTEST {label} — vrai {vrai} % (terme dominant : {_dom}) ·"
              f" conforme : {ok_vrai == 1}")
        for nom, val in faux.items():
            val = round(val, 2)
            if abs(val - vrai) < 0.05:
                print(f"    (non discriminant à ce point) {nom}")
                continue
            total_dis += 1
            _ok, ko_f, _ = invariant([{**r, "seuil": val}], cfg)
            vu = len(ko_f) == 1
            total_det += 1 if vu else 0
            print(f"    {'DÉTECTÉ ' if vu else 'RATÉ     '} {nom}  ({val} %, écart {val - vrai:+.2f} pt)")
    taux = (100.0 * total_det / total_dis) if total_dis else 0.0
    print(f"  → TAUX DE DÉTECTION : {total_det}/{total_dis} erreurs DISCRIMINANTES"
          f" ({taux:.0f} %) — le reste n'était pas une erreur au point testé")
    return total_dis >= 6 and total_det == total_dis


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=STATE,
                    help="où écrire l'état lu par le cockpit (défaut :"
                         " Index_Maison/thermo/seuil_moteur.json)")
    ap.add_argument("--autotest", action="store_true")
    a = ap.parse_args()
    cfg = env()
    if a.autotest:
        bon = autotest(cfg)
        print("  → GARDIEN FIABLE" if bon else "  → GARDIEN CASSÉ (il ne détecte pas)")
        return 0 if bon else 3

    csv_path = csv_actuel()
    if not csv_path:
        print("[ERR] aucun journal de run exploitable")
        return 2
    rows = lignes_refus(csv_path)
    print("SOURCE : journal du run (les chiffres écrits PAR LE MOTEUR lui-même)")
    print(f"  {os.path.basename(csv_path)} · {len(rows)} refus chiffrés lus")
    if len(rows) < 5:
        print("  ⚠️ pas assez de refus chiffrés pour conclure (le refus parlant date du"
              " 23/09 — il faut ~1 h de recul)")
        return 2
    ok, ko, par_paire = invariant(rows, cfg)
    print(f"\n== 1. INVARIANT (seuil écrit == seuil recalculé) — tolérance 0,05 pt ==")
    print(f"  conformes : {ok}/{len(rows)}")
    for k in ko:
        print(f"  ❌ {k['utc']} {k['paire']} : écrit {k['seuil']:.2f} % · recalculé"
              f" {k['attendu']:.2f} % · écart {k['ecart']:+.2f} pt")
    print("\n== 2. DÉTERMINANCE (R15) — quel terme fixe le seuil, par paire ==")
    print(f"  {'paire':12}{'cadence':>9}{'seuil exigé':>13}   terme dominant")
    for p, d in sorted(par_paire.items()):
        need, dom, _ = seuil_attendu((profil(p) or {}).get("calib") or {}, cfg, d["cad"], 0.0)
        print(f"  {p.replace('USDT', ''):12}{d['cad']:>8.1f}%{need * 0.85:>12.2f}%"
              f"   {max(d['dom'].items(), key=lambda kv: kv[1])[0]} ({d['n']} refus)")
    flags = detecter_instruments()
    print("\n== 3. DÉTECTEUR D'INSTRUMENTS (recalcule un seuil SANS le terme cadence) ==")
    if flags:
        print(f"  ❌ {len(flags)} fichier(s) à corriger :")
        for f in flags:
            print(f"     {f}")
    else:
        print("  ✔ aucun instrument ne recalcule un seuil d'entrée sans la cadence")
    cles, manquants = detecter_termes_profil()
    print("\n== 4. DÉTECTEUR DE TERMES DU PROFIL (rend E23 impossible) ==")
    if cles is None:
        print("  ⚠️ formule `impulse_entry` introuvable dans le moteur → gardien NON PROUVÉ")
        manquants = ["formule_introuvable"]
    elif manquants:
        print(f"  ❌ le moteur lit {sorted(cles)} mais CE gardien ne lit PAS : {manquants}")
        print("     → gardien DÉSACTIVÉ (il accuserait le moteur sur un terme oublié = classe E23)")
    else:
        print(f"  ✔ termes du profil lus par le moteur ET par le gardien : {sorted(cles)}")
    conforme = (not ko) and (not flags) and (not manquants)
    # DÉRIVE DE CONFIG (objection de la famille du 23/09 : « le gardien suppose une
    # configuration STATIQUE ; si quelqu'un change DIP_CADENCE_MULT ou un profil entre deux
    # passages, il compare à de nouvelles valeurs et peut tout déclarer conforme »).
    # Réponse : le gardien ÉCRIT les empreintes de la config et des profils, et SIGNALE un
    # changement depuis son dernier passage — car si la config a bougé sans redémarrage du
    # moteur, c'est le moteur qui tourne sur d'ANCIENS paramètres (et mes recalculs, sur les
    # nouveaux → un désaccord peut être légitime et doit être expliqué, pas subi).
    import hashlib

    def _md5(p):
        try:
            h = hashlib.md5()
            with open(p, "rb") as f:
                for b in iter(lambda: f.read(1 << 16), b""):
                    h.update(b)
            return h.hexdigest()
        except Exception:
            return None

    h_cfg, h_prof = _md5(ENV), _md5(PROFILS)
    prec = {}
    try:
        prec = json.load(open(a.json, encoding="utf-8")) if a.json else {}
    except Exception:
        prec = {}
    change = []
    for nom, h, cle in (("config/defaults.env", h_cfg, "config_md5"),
                        ("strategie/universe_profils.json", h_prof, "profils_md5")):
        if prec.get(cle) and prec.get(cle) != h:
            change.append(nom)
    if change:
        print(f"\n  ⚠️ DÉRIVE DE CONFIG depuis le dernier passage : {', '.join(change)}")
        print("     → si le moteur N'A PAS été relancé depuis, ses décisions reposent sur les"
              " ANCIENS paramètres : un désaccord ci-dessus serait alors LÉGITIME. Vérifier"
              " l'heure de démarrage du moteur (launchd) avant de conclure à une faute.")
    if a.json:
        import time as _t
        from datetime import datetime as _dt, timezone as _tz
        try:
            os.makedirs(os.path.dirname(a.json) or ".", exist_ok=True)
            json.dump({"ts": _dt.now(_tz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "ts_epoch": _t.time(),
                       "config_md5": h_cfg, "profils_md5": h_prof,
                       "config_change": change,
                       "conforme": conforme, "refus_lus": len(rows), "conformes": ok,
                       "desaccords": ko,
                       "par_paire": {p: {"cadence": d["cad"], "n": d["n"]}
                                     for p, d in par_paire.items()},
                       "instruments_a_corriger": flags,
                       "termes_profil": sorted(cles) if cles else [],
                       "termes_profil_manquants": manquants},
                      open(a.json, "w"), ensure_ascii=False, indent=2)
            print(f"  (état écrit : {a.json})")
        except Exception as e:
            print(f"  ⚠️ état NON écrit ({e}) — le verdict ne sera pas visible au cockpit")
    print("\n" + ("✔ CONFORME — le seuil recalculé est exactement celui du moteur"
                  if conforme else "❌ DÉSACCORD — NE PAS publier de chiffre avant d'avoir"
                  " expliqué l'écart ci-dessus"))
    return 0 if conforme else 3


if __name__ == "__main__":
    raise SystemExit(main())
