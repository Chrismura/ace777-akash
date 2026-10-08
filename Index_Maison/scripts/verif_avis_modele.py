#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIF AVIS MODELE — garde mécanique de la classe E16 (câblée le 08/10/2026)
==========================================================================
CLASSE D'ERREUR (E16, mesurée le 23/09) : « publier un avis sous le nom du modèle DEMANDÉ,
pas de celui qui a RÉPONDU ». Le hub peut SUBSTITUER un modèle (`substitue: true`) ; si je ne
lis que `provider`, je compte **Gemini deux fois** comme **deux voix indépendantes** → un jury
de 4 devient un jury de 3 (R19/R20.3 : un tour sous quorum n'est qu'un avis consultatif).

C'EST QUOI CETTE GARDE : une vérification **déterministe** des AVIS publiés dans les sessions
famille. Elle lit chaque `AVIS/*.md` et exige :
  1. un en-tête traçable : `demandé « X » — RÉPONDU PAR « Y »` ;
  2. que le NOM DU FICHIER corresponde au modèle **DEMANDÉ** (`T0n_<modele>.md`, `/` et `:`
     remplacés par `_`) — un fichier nommé pour un autre modèle est une faute d'étiquette ;
  3. un bandeau `SUBSTITUTION` dès que Y ≠ X (l'avis ne compte alors PAS comme voix
     indépendante).
Elle publie aussi, par tour, le nombre de **voix indépendantes** (modèles servis distincts,
`substitue` faux) — le chiffre dont R19/R20.3 dépendent.

POURQUOI ELLE EXISTE : `couverture_erreurs.py` a déclaré E16 « promesse » (aucune garde
mécanique). La proposition vient du HUB (`--ia`) ; c'est la première proposition IA câblée
après mesure, pas appliquée aveuglément.

LECTURE SEULE · 0 ordre · 0 € · stdlib. Écrit seulement `thermo/avis_modele.json` (+ --json).
Branché par `git_push_auto.sh` (tour des 3 h). Autotest : `--autotest` (prouve qu'elle SAIT
dire NON : nom de fichier menteur, substitution non déclarée, en-tête absente).

Usage :
  python3 verif_avis_modele.py                 # rapport humain, exit 0/1
  python3 verif_avis_modele.py --json CHEMIN   # sortie machine
  python3 verif_avis_modele.py --autotest      # prouve la détection (ne touche à rien)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent          # ace777-test-day1
IM = RACINE / "Index_Maison"
SESSIONS = IM / "scripts" / "SESSIONS_FAMILLE"
OUT_JSON = IM / "thermo" / "avis_modele.json"

# `# Tour 2 — demandé « X » — RÉPONDU PAR « Y » (…)`
RE_ENTETE = re.compile(r"demand[ée]\s*[«\"]([^»\"]+)[»\"].*?R[ÉE]PONDU\s+PAR\s*[«\"]([^»\"]+)[»\"]",
                       re.I | re.S)
RE_FICHIER = re.compile(r"^T\d+_(.+)\.md$")
RE_TOUR = re.compile(r"^T(\d+)_")


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def normaliser(modele: str) -> str:
    """Le nom de fichier est le modèle demandé, `/` et `:` remplacés par `_`."""
    return modele.strip().replace("/", "_").replace(":", "_")


def analyser_dossier(session: Path) -> dict:
    """Vérifie tous les AVIS d'UNE session. Rend {avis, anomalies, voix_par_tour}."""
    anomalies: list[str] = []
    avis_dir = session / "AVIS"
    n_avis = 0
    if avis_dir.is_dir():
        for f in sorted(avis_dir.glob("*.md")):
            n_avis += 1
            txt = f.read_text(encoding="utf-8", errors="replace")
            tete = txt[:600]
            m = RE_ENTETE.search(tete)
            if not m:
                anomalies.append(f"{f.name} : en-tête SANS « demandé … RÉPONDU PAR … » "
                                 f"(un avis non traçable n'existe pas — E16)")
                continue
            demande, servi = m.group(1).strip(), m.group(2).strip()
            mf = RE_FICHIER.match(f.name)
            if mf:
                attendu = normaliser(demande)
                if mf.group(1) != attendu:
                    anomalies.append(f"{f.name} : le NOM DU FICHIER ne correspond pas au modèle "
                                     f"DEMANDÉ « {demande} » (attendu T0n_{attendu}.md)")
            if servi != demande and "SUBSTITUTION" not in txt.upper():
                anomalies.append(f"{f.name} : demandé « {demande} » mais RÉPONDU PAR « {servi} » "
                                 f"SANS bandeau SUBSTITUTION (cet avis serait compté à tort comme "
                                 f"voix indépendante — E16/R20.3)")
    # voix indépendantes par tour (le chiffre dont R19 dépend) — lu au transcript
    voix_par_tour: dict[str, list] = {}
    tr = session / "transcript.jsonl"
    if tr.exists():
        for ligne in tr.read_text(encoding="utf-8", errors="replace").splitlines():
            if not ligne.strip():
                continue
            try:
                e = json.loads(ligne)
            except Exception:
                continue
            if e.get("role") == "famille" and e.get("tour") is not None and not e.get("substitue"):
                modele = e.get("model_servi")
                if modele:
                    v = voix_par_tour.setdefault(str(e["tour"]), [])
                    if modele not in v:
                        v.append(modele)
    return {"avis": n_avis, "anomalies": anomalies, "voix_par_tour": voix_par_tour}


def analyser(base: Path = SESSIONS) -> dict:
    sessions, anomalies = {}, []
    if base.is_dir():
        for s in sorted(p for p in base.iterdir() if p.is_dir()):
            r = analyser_dossier(s)
            if r["avis"] or r["anomalies"]:
                sessions[s.name] = r
                anomalies += [f"[{s.name}] {a}" for a in r["anomalies"]]
    return {"ts": utc(), "base": str(base), "sessions": sessions,
            "n_sessions": len(sessions), "n_anomalies": len(anomalies),
            "anomalies": anomalies, "conforme": not anomalies, "lecture_seule": True, "ordres": 0}


def rapport(res: dict) -> str:
    L = [f"# Gardien des avis — classe E16 — {res['ts']}",
         "",
         f"**Verdict : {'✅ CONFORME' if res['conforme'] else '🔴 NON CONFORME'}** · "
         f"{res['n_sessions']} session(s) · {res['n_anomalies']} anomalie(s).",
         "", "| Session | Avis | Voix indépendantes par tour |", "|---|---|---|"]
    for nom, s in res["sessions"].items():
        v = ", ".join(f"T{k}:{len(x)}" for k, x in sorted(s["voix_par_tour"].items()) if x)
        L.append(f"| {nom} | {s['avis']} | {v or '—'} |")
    L.append("")
    if res["anomalies"]:
        L.append("## Anomalies (un avis publié sous un nom menteur, ou substitution tue)")
        for a in res["anomalies"]:
            L.append(f"- 🔴 {a}")
    else:
        L.append("- ✅ Chaque avis est traçable, nommé pour le modèle DEMANDÉ, et une "
                 "substitution porte son bandeau.")
    L += ["", "---",
          "*Généré par `scripts/verif_avis_modele.py` (lecture seule). Classe E16 ; "
          "déclaré dans `strategie/gardes_erreurs.json` ; appelé par `git_push_auto.sh`.*", ""]
    return "\n".join(L)


def autotest() -> int:
    """Prouve la détection par des CAS FACTICES (aucune session réelle touchée)."""
    cas = []
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)

        def mk_session(nom: str, avis: dict, transcript: list | None = None):
            d = base / nom
            (d / "AVIS").mkdir(parents=True)
            for fn, contenu in avis.items():
                (d / "AVIS" / fn).write_text(contenu, encoding="utf-8")
            if transcript is not None:
                (d / "transcript.jsonl").write_text(
                    "\n".join(json.dumps(e) for e in transcript) + "\n", encoding="utf-8")

        H = "# Tour 1 — demandé « {d} » — RÉPONDU PAR « {s} » ({f}, 1.0s)\n\ncorps\n"
        # 1) demande == servi, nom cohérent → OK
        mk_session("S1", {"T01_m_a.md": H.format(d="m/a", s="m/a", f="prov")})
        # 2) servi != demande SANS bandeau → DOIT crier
        mk_session("S2", {"T01_m_a.md": H.format(d="m/a", s="gemini", f="prov")})
        # 3) servi != demande AVEC bandeau → OK
        mk_session("S3", {"T01_m_a.md": H.format(d="m/a", s="gemini", f="prov")
                          + "> ⚠ SUBSTITUTION : pas une voix indépendante.\n"})
        # 4) nom de fichier menteur (fichier nommé m/b, en-tête demandé m/a) → DOIT crier
        mk_session("S4", {"T01_m_b.md": H.format(d="m/a", s="m/a", f="prov")})
        # 5) en-tête absente → DOIT crier
        mk_session("S5", {"T01_m_a.md": "# Tour 1 — avis de m/a\n\ncorps\n"})
        # 6) transcript : 2 servis dont 1 substitué → 1 seule voix indépendante
        mk_session("S6", {"T01_m_a.md": H.format(d="m/a", s="m/a", f="prov")}, [
            {"role": "famille", "tour": 1, "model_servi": "m/a", "substitue": False},
            {"role": "famille", "tour": 1, "model_servi": "gemini", "substitue": True}])

        r = analyser(base)
        par_session = {n: set(s["anomalies"]) for n, s in r["sessions"].items()}
        cas.append(("demandé == servi, nom cohérent → aucune anomalie",
                    not par_session.get("S1")))
        cas.append(("substitution SANS bandeau → détectée", bool(par_session.get("S2"))))
        cas.append(("substitution AVEC bandeau → aucune anomalie", not par_session.get("S3")))
        cas.append(("nom de fichier menteur → détecté", bool(par_session.get("S4"))))
        cas.append(("en-tête absente → détectée", bool(par_session.get("S5"))))
        voix = r["sessions"].get("S6", {}).get("voix_par_tour", {}).get("1", [])
        cas.append(("voix indépendantes = 1 (substitution exclue)", voix == ["m/a"]))

    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  -> {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'} "
          f"({sum(1 for _, o in cas if o)}/{len(cas)})")
    return 0 if bon else 3


def main() -> int:
    ap = argparse.ArgumentParser(description="Garde E16 — avis publiés sous le bon modèle")
    ap.add_argument("--json", default=None)
    ap.add_argument("--autotest", action="store_true")
    a = ap.parse_args()
    if a.autotest:
        return autotest()
    res = analyser()
    Path(OUT_JSON).parent.mkdir(parents=True, exist_ok=True)
    Path(OUT_JSON).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(rapport(res))
    if a.json:
        Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0 if res["conforme"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
