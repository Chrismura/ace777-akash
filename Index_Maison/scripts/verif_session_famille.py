#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GARDIEN DE LA FENÊTRE FAMILLE (R19) — 23/09/2026
=================================================
Ordre de Christophe : « tu vas ouvrir un round avec la famille et GARDER LA FENÊTRE OUVERTE,
qu'elle ait la mémoire du chat, car tu n'es plus digne de diriger seule. »

Une promesse ne garde rien. Ce gardien regarde les SESSIONS_FAMILLE et crie si la fenêtre se
referme, si un tour reste sans avis, si une voix substituée est comptée comme indépendante, ou
si la mémoire du fil ne suit plus. Il est appelé toutes les 3 h par `git_push_auto.sh` et affiché
au cockpit. Il N'ÉCRIT JAMAIS dans une session (lecture seule) : il juge, il ne répare pas.

RÈGLES
  R1  au moins une session existe et son état est OUVERTE (une fermeture doit être DATÉE et MOTIVÉE)
  R2  chaque tour écrit par nous a au moins un avis de la famille
  R3  les voix du dernier tour sont INDÉPENDANTES (une substitution ne compte pas) — seuil 3
  R4  la mémoire du fil (MEMOIRE.md) parle du dernier tour → « la famille a la mémoire du chat »
  R5  le fil ne dort pas : un tour avec avis non suivi d'un nouveau tour depuis > MAX_DORMANT h
  R6  toute substitution vue dans le fil est ÉTIQUETÉE (E16 : jamais un avis sous un faux nom)

AUTOTEST (--autotest) : construit des sessions en mémoire et vérifie que CHAQUE règle attrape bien
son cas (une garde qui ne sait pas échouer n'est pas une garde).

Usage : python3 verif_session_famille.py [--autotest] [--json FICHIER]
Sortie : 0 = conforme · 1 = alerte. Lecture seule · 0 ordre · 0 €.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

IM = Path(__file__).resolve().parent.parent            # Index_Maison
SESSIONS = IM / "scripts" / "SESSIONS_FAMILLE"
VOIX_MIN = 3
MAX_DORMANT_H = 6.0


def now() -> datetime:
    return datetime.now(timezone.utc)


def lire_fil(d: Path) -> list[dict]:
    p = d / "transcript.jsonl"
    if not p.exists():
        return []
    out = []
    for l in p.read_text(encoding="utf-8").splitlines():
        if l.strip():
            try:
                out.append(json.loads(l))
            except Exception:
                pass
    return out


def iso_dt(s):
    try:
        return datetime.strptime(str(s), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except Exception:
        return None


def juger(d: Path, ref: datetime | None = None) -> list[str]:
    """Retourne la liste des ALERTES de cette session (vide = conforme)."""
    ref = ref or now()
    alertes: list[str] = []
    meta = {}
    if (d / "META.json").exists():
        try:
            meta = json.loads((d / "META.json").read_text(encoding="utf-8"))
        except Exception:
            alertes.append("R1 META.json illisible")
    fil = lire_fil(d)
    tours_nous = {e.get("tour") for e in fil if e.get("role") == "nous" and e.get("tour")}
    tours_fam = {e.get("tour") for e in fil if e.get("role") == "famille" and e.get("tour")}

    # R1 — la fenêtre est-elle ouverte ?
    if meta.get("etat") != "OUVERTE":
        if not (meta.get("fermee_le") and meta.get("motif_fermeture")):
            alertes.append(f"R1 session {d.name} en état « {meta.get('etat')} » SANS fermeture datée "
                           f"et motivée — la fenêtre ne doit pas se refermer en silence")
    # R2 — chaque tour a des avis
    manquants = sorted(t for t in tours_nous if t not in tours_fam)
    if manquants:
        alertes.append(f"R2 tours sans avis : {manquants}")
    # R3 — voix indépendantes du dernier tour
    if tours_fam:
        dernier = max(tours_fam)
        voix = {e.get("model_servi") for e in fil
                if e.get("tour") == dernier and e.get("role") == "famille" and e.get("model_servi")}
        if len(voix) < VOIX_MIN:
            alertes.append(f"R3 dernier tour ({dernier}) : {len(voix)} voix indépendante(s) < {VOIX_MIN}")
        # R5 — le fil dort-il ?
        ts = [iso_dt(e.get("ts")) for e in fil
              if e.get("role") == "nous" and e.get("tour") == dernier]
        ts = [t for t in ts if t]
        if ts and (ref - max(ts)).total_seconds() / 3600.0 > MAX_DORMANT_H:
            h = (ref - max(ts)).total_seconds() / 3600.0
            alertes.append(f"R5 fil DORMANT : dernier tour il y a {h:.1f} h (> {MAX_DORMANT_H} h) "
                           f"— un jury sans nouveau tour ne juge plus")
    # R4 — la mémoire du fil suit-elle ?
    memo = (d / "MEMOIRE.md")
    if not memo.exists():
        alertes.append("R4 MEMOIRE.md absente — la famille n'a PAS la mémoire du chat")
    elif tours_fam and f"## Tour {max(tours_fam)}" not in memo.read_text(encoding="utf-8"):
        alertes.append(f"R4 MEMOIRE.md ne couvre pas le tour {max(tours_fam)}")
    # R6 — les substitutions sont-elles étiquetées ?
    for e in fil:
        if e.get("role") == "famille" and e.get("model_servi") and e.get("model_demande"):
            if e["model_servi"] != e["model_demande"] and e.get("substitue") is not True:
                alertes.append(f"R6 avis du tour {e.get('tour')} servi par {e['model_servi']} "
                               f"demandé {e['model_demande']} SANS étiquette de substitution (E16)")
    return alertes


def autotest() -> int:
    import tempfile
    ok = 0
    total = 0

    def cas(nom, meta, fil, memo, doit_attraper, ref=None):
        nonlocal ok, total
        total += 1
        with tempfile.TemporaryDirectory() as t:
            d = Path(t)
            (d / "META.json").write_text(json.dumps(meta), encoding="utf-8")
            (d / "transcript.jsonl").write_text(
                "\n".join(json.dumps(x) for x in fil) + "\n", encoding="utf-8")
            if memo is not None:
                (d / "MEMOIRE.md").write_text(memo, encoding="utf-8")
            al = juger(d, ref=ref)
            if doit_attraper is None:                    # contrôle POSITIF : doit être propre
                attrape = not al
            else:
                attrape = any(a.startswith(doit_attraper) for a in al)
            print(f"  [{'OK ' if attrape else 'RATÉ'}] {nom} → {al if al else 'conforme'}")
            ok += 1 if attrape else 0

    t0 = now()
    bon = {"etat": "OUVERTE"}
    fil_bon = ([{"ts": t0.strftime("%Y-%m-%dT%H:%M:%SZ"), "role": "nous", "tour": 1, "texte": "q"}] +
               [{"ts": t0.strftime("%Y-%m-%dT%H:%M:%SZ"), "role": "famille", "tour": 1,
                 "model_demande": f"m{i}", "model_servi": f"m{i}", "substitue": False, "texte": "a"}
                for i in range(3)])
    cas("session saine (doit PASSER, 0 alerte)", bon, fil_bon, "## Tour 1 — x", None)
    cas("session fermée sans motif", {"etat": "FERMÉE"}, fil_bon, "## Tour 1 — x", "R1")
    cas("tour sans avis", bon, [{"ts": t0.strftime("%Y-%m-%dT%H:%M:%SZ"), "role": "nous",
                                 "tour": 1, "texte": "q"}], "## Tour 1", "R2")
    cas("voix substituée comptée", bon,
        [e for e in fil_bon[:2]] + [{"ts": t0.strftime("%Y-%m-%dT%H:%M:%SZ"), "role": "famille",
                                     "tour": 1, "model_demande": "a", "model_servi": "b",
                                     "substitue": True, "texte": "a"}], "## Tour 1", "R3")
    cas("mémoire absente", bon, fil_bon, None, "R4")
    cas("mémoire qui ne suit pas", bon, fil_bon, "## Tour 99 — x", "R4")
    cas("fil dormant", bon, fil_bon, "## Tour 1 — x", "R5",
        ref=t0 + timedelta(hours=MAX_DORMANT_H + 1))
    cas("substitution non étiquetée", bon,
        fil_bon[:1] + [{"ts": t0.strftime("%Y-%m-%dT%H:%M:%SZ"), "role": "famille", "tour": 1,
                        "model_demande": "a", "model_servi": "b", "texte": "a"},
                       {"ts": t0.strftime("%Y-%m-%dT%H:%M:%SZ"), "role": "famille", "tour": 1,
                        "model_demande": "c", "model_servi": "c", "substitue": False, "texte": "a"},
                       {"ts": t0.strftime("%Y-%m-%dT%H:%M:%SZ"), "role": "famille", "tour": 1,
                        "model_demande": "d", "model_servi": "d", "substitue": False, "texte": "a"}],
        "## Tour 1", "R6")
    print(f"  AUTOTEST {ok}/{total}")
    return 0 if ok == total else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--autotest", action="store_true")
    ap.add_argument("--json", metavar="FICHIER")
    a = ap.parse_args()
    if a.autotest:
        return autotest()
    sessions = sorted(p for p in SESSIONS.iterdir() if p.is_dir()) if SESSIONS.exists() else []
    if not sessions:
        print("SESSION FAMILLE : aucune session — la fenêtre n'est PAS ouverte (R19, ordre Christophe)")
        return 1
    lignes, tout = [], True
    for s in sessions:
        al = juger(s)
        fil = lire_fil(s)
        tours_fam = {e.get("tour") for e in fil if e.get("role") == "famille" and e.get("tour")}
        n_tours = len({e.get("tour") for e in fil if e.get("role") == "nous" and e.get("tour")})
        voix, dernier = 0, 0
        if tours_fam:
            dernier = max(tours_fam)
            voix = len({e.get("model_servi") for e in fil
                        if e.get("tour") == dernier and e.get("role") == "famille"
                        and e.get("model_servi")})
        etat = "OUVERTE, conforme" if not al else "ALERTE"
        print(f"  Session famille « {s.name} » — {etat} · {n_tours} tour(s) · "
              f"{voix} voix indépendante(s) au dernier tour ({dernier})"
              + ("" if not al else " : " + " · ".join(al)))
        tout = tout and not al
        lignes.append({"session": s.name, "alertes": al, "tours": n_tours,
                       "dernier_tour": dernier, "voix_independantes": voix})
    print(f"Gardien fenêtre famille (R19) — {len(sessions)} session(s) · "
          f"{sum(len(x['alertes']) for x in lignes)} alerte(s) · "
          f"{'CONFORME' if tout else 'AU ROUGE'}")
    if a.json:
        Path(a.json).write_text(json.dumps(
            {"ts_utc": now().strftime("%Y-%m-%dT%H:%M:%SZ"), "sessions": lignes,
             "conforme": tout}, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0 if tout else 1


if __name__ == "__main__":
    sys.exit(main())
