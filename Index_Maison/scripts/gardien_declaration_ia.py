#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gardien_declaration_ia.py — garde MÉCANIQUE de la règle R23 (10/10/2026).

RÈGLE R23 (REGLE_D_OR.md, ordre Christophe 10/10/2026 : « rétablir la règle de
déclarer quelle IA va œuvrer ») : avant sa première écriture de la session, toute
IA déclare son identité RÉELLE (persona + modèle + client), son périmètre et le GO
— dans `strategie/DECLARATIONS_IA.jsonl` (append-only) ET sur la ligne
MEMOIRE_COLLAB de ses actes ; tout motif de pré-déclaration porte `IA=<identité>`.

UNE RÈGLE SANS GARDE EST UNE PROMESSE (§13.1 trou B) — ce contrôleur répond,
classe par classe, « la règle est-elle encore tenue ? » :

  R1  tout motif de `strategie/PREDECLARATIONS.jsonl` postérieur à l'activation
      porte `IA=` (l'identité de qui œuvre) — sinon TROU ;
  R2  toute ligne MEMOIRE_COLLAB postérieure à l'activation porte dans sa colonne
      « qui » une identité DÉCLARÉE (nom + modèle entre parenthèses) — sinon TROU ;
  R3  `strategie/DECLARATIONS_IA.jsonl` existe, est append-only lisible, et chaque
      entrée porte {ts, ia, modele, client, perimetre, go} — sinon TROU.

LIMITES DÉCLARÉES (R8) : c'est une trace VOLONTAIRE — le contrôleur prouve qui
s'est DÉCLARÉ, pas qui a physiquement écrit ; il ne vérifie pas la véracité du
modèle nommé. Il ne crie que sur la FORME absente (faux positif R14 : il ne juge
jamais le fond d'un acte).

Lecture seule + son propre rapport `Index_Maison/thermo/declaration_ia.json`.
Usage : `python3 gardien_declaration_ia.py` (rc=0 conforme, rc=1 trous) ·
        `python3 gardien_declaration_ia.py --autotest` (5/5, il SAIT dire NON).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent   # ace777-test-day1
INDEX = RACINE / "Index_Maison"
DECL = INDEX / "strategie" / "DECLARATIONS_IA.jsonl"
PREDECL = INDEX / "strategie" / "PREDECLARATIONS.jsonl"
MEMOIRE = INDEX / "MEMOIRE_COLLAB.md"
RAPPORT = INDEX / "thermo" / "declaration_ia.json"

# Activation de la règle (première déclaration écrite — la mienne, Buffy 10/10/2026).
ACTIVATION_ISO = "2026-10-10T06:47:24Z"     # horloge PREDECLARATIONS (UTC)
ACTIVATION_MEM = "2026-10-10T0647Z"         # horloge MEMOIRE_COLLAB (libellé maison)
CLES_DECLARATION = ("ts", "ia", "modele", "client", "perimetre", "go")
RE_IDENTITE = re.compile(r"^\s*([^\s(]+)\s*\(([^)]+)\)\s*$")  # « Nom (modèle, client) »
# ORGANES LOGICIELS (pas des IA) : leurs lignes automatiques portent leur nom de
# code, c'est LEUR identité réelle — exiger « Nom (modèle) » criera à tort sur la
# snapshot du soir (R14). Liste DÉCLARÉE, fermée : les 4 écrivains connus du canon
# + le traceur de journal. Tout autre nom SANS identité déclarée = TROU.
ORGANES_LOGICIELS = {"journal_soir", "journal_auto", "memoire_log",
                     "auto_reparer", "sync_console_journal"}


def lire_declarations(chemin: Path) -> tuple[list[dict], list[str]]:
    """Lit le JSONL de déclarations. Retourne (entrées valides, trous R3)."""
    if not chemin.exists():
        return [], [f"R3 · {chemin} ABSENT — aucune déclaration d'IA n'existe"]
    entrees, trous = [], []
    for n, ligne in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
        if not ligne.strip():
            continue
        try:
            d = json.loads(ligne)
        except Exception as e:
            trous.append(f"R3 · ligne {n} illisible ({e})")
            continue
        manquantes = [k for k in CLES_DECLARATION if not str(d.get(k) or "").strip()]
        if manquantes:
            trous.append(f"R3 · ligne {n} sans {manquantes}")
            continue
        entrees.append(d)
    return entrees, trous


def controler(decl_path=DECL, predecl_path=PREDECL, memoire_path=MEMOIRE) -> list[str]:
    trous: list[str] = []
    decls, trous3 = lire_declarations(decl_path)
    trous += trous3
    noms_declares = {str(d.get("ia", "")).strip() for d in decls}

    # R1 — tout motif de pré-déclaration porte IA=
    if predecl_path.exists():
        for n, ligne in enumerate(predecl_path.read_text(encoding="utf-8").splitlines(), 1):
            if not ligne.strip():
                continue
            try:
                d = json.loads(ligne)
            except Exception:
                continue  # une ligne illisible est déjà le problème de predemodifier
            if str(d.get("ts") or "") <= ACTIVATION_ISO:
                continue
            if "IA=" not in str(d.get("motif") or ""):
                trous.append(f"R1 · pré-déclaration {d.get('ts')} ({d.get('fichier')}) "
                             f"SANS IA=<identité> dans le motif")

    # R2 — toute ligne mémoire postérieure à l'activation porte une identité déclarée
    if memoire_path.exists():
        for ligne in memoire_path.read_text(encoding="utf-8").splitlines():
            if not ligne.startswith("| 2026-"):
                continue
            cell = [c.strip() for c in ligne.split("|")]
            if len(cell) < 5:
                continue
            ts, qui = cell[1], cell[2]
            if ts <= ACTIVATION_MEM:
                continue
            m = RE_IDENTITE.match(qui)
            if not m:
                if qui in ORGANES_LOGICIELS:
                    continue  # organe logiciel déclaré : son nom de code EST son identité
                trous.append(f"R2 · ligne mémoire {ts} : colonne « qui » = {qui!r} "
                             f"sans identité déclarée « Nom (modèle, client) »")
            elif m.group(1) not in noms_declares:
                trous.append(f"R2 · ligne mémoire {ts} : {m.group(1)!r} n'a AUCUNE "
                             f"déclaration dans {decl_path.name}")
    return trous


def ecrire_rapport(trous: list[str]) -> None:
    try:
        RAPPORT.parent.mkdir(parents=True, exist_ok=True)
        RAPPORT.write_text(json.dumps({
            "ts": __import__("datetime").datetime.now(
                __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "regle": "R23 — déclaration de l'IA qui œuvre",
            "activation": ACTIVATION_ISO,
            "trous": trous,
            "statut": "CONFORME" if not trous else f"{len(trous)} TROU(S)",
            "limite_declaree": "trace volontaire : prouve qui s'est déclaré, pas qui a écrit",
        }, ensure_ascii=False, indent=1), encoding="utf-8")
    except Exception:
        pass  # le rapport est un miroir : jamais bloquant (R11)


def autotest() -> int:
    """6 cas — il SAIT dire NON et ne crie pas à tort (R14)."""
    import tempfile
    ok = 0
    total = 6

    def fichiers(tmp, decl_lines, predecl_lines, memoire_lines):
        d = Path(tmp) / "DECLARATIONS_IA.jsonl"
        p = Path(tmp) / "PREDECLARATIONS.jsonl"
        m = Path(tmp) / "MEMOIRE_COLLAB.md"
        d.write_text("\n".join(decl_lines), encoding="utf-8")
        p.write_text("\n".join(predecl_lines), encoding="utf-8")
        m.write_text("\n".join(memoire_lines), encoding="utf-8")
        return d, p, m

    bonne_decl = json.dumps({"ts": ACTIVATION_ISO, "ia": "Buffy", "modele": "MiMo 2.6 Pro",
                             "client": "Freebuff", "perimetre": "test", "go": "test"},
                            ensure_ascii=False)
    avec_ia = json.dumps({"ts": "2026-10-10T09:00:00Z", "fichier": "x.py",
                          "motif": "IA=Buffy (test) : acte", "go": "g"}, ensure_ascii=False)
    sans_ia = json.dumps({"ts": "2026-10-10T09:00:00Z", "fichier": "x.py",
                          "motif": "acte sans identité", "go": "g"}, ensure_ascii=False)
    bonne_ligne = "| 2026-10-10T0900Z | Buffy (MiMo 2.6 Pro, Freebuff) | ★ | c | r |"
    mauvaise_ligne = "| 2026-10-10T0900Z | Buffy | ★ | c | r |"

    with tempfile.TemporaryDirectory() as tmp:
        # 1. tout conforme → silence
        d, p, m = fichiers(tmp, [bonne_decl], [avec_ia], [bonne_ligne])
        if controler(d, p, m) == []:
            ok += 1
        # 2. motif sans IA= → cri R1
        d, p, m = fichiers(tmp, [bonne_decl], [sans_ia], [bonne_ligne])
        if any(t.startswith("R1") for t in controler(d, p, m)):
            ok += 1
        # 3. ligne mémoire sans identité → cri R2
        d, p, m = fichiers(tmp, [bonne_decl], [avec_ia], [mauvaise_ligne])
        if any(t.startswith("R2") for t in controler(d, p, m)):
            ok += 1
        # 4. identité non déclarée → cri R2
        d, p, m = fichiers(tmp, [bonne_decl], [avec_ia],
                           ["| 2026-10-10T0900Z | Inconnu (X-1, ailleurs) | ★ | c | r |"])
        if any("n'a AUCUNE déclaration" in t for t in controler(d, p, m)):
            ok += 1
        # 5. déclaration incomplète → cri R3
        d, p, m = fichiers(tmp, [json.dumps({"ts": "x", "ia": "Buffy"})], [avec_ia], [bonne_ligne])
        if any(t.startswith("R3") for t in controler(d, p, m)):
            ok += 1
        # 6. organe logiciel (pas une IA) → SILENCE (pas de faux positif R14)
        d, p, m = fichiers(tmp, [bonne_decl], [avec_ia],
                           ["| 2026-10-10T2053Z | journal_soir | ★ | journal | auto |"])
        if controler(d, p, m) == []:
            ok += 1
    total = 6
    print(f"AUTOTEST {ok}/{total}" + (" ✔ FIABLE" if ok == total else " ✘ CASSÉ"))
    return 0 if ok == total else 1


def main() -> int:
    if "--autotest" in sys.argv:
        return autotest()
    trous = controler()
    ecrire_rapport(trous)
    if trous:
        print(f"❌ R23 · {len(trous)} TROU(S) de déclaration d'IA :")
        for t in trous:
            print("   " + t)
        return 1
    print("✔ R23 CONFORME — toute écriture depuis l'activation porte une déclaration d'IA")
    return 0


if __name__ == "__main__":
    sys.exit(main())
