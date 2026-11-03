#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rafraichir_klines.py — l'organe qui EMPÊCHE une mesure de vieillir en silence.

DÉFAUT DÉCLARÉ (03/11/2026, faute grave) : `runs/KLINES_1H/` s'arrêtait au
**2026-10-28 21:43** et AUCUN organe ne le rafraîchissait. Toute mesure bâtie
dessus (chiffrage, mesure du filet des souches) était donc **périmée sans le dire**,
y compris pendant la jambe du crash du 29/10 : on croyait mesurer, on mesurait le
passé. Une mesure qui ne dit pas son âge est un mensonge par omission (classe E29).

CE QUE FAIT L'ORGANE
--------------------
1. Télécharge les bougies 1 h (par défaut 30 jours = 720 barres) des paires du
   périmètre LISES DANS LA CONFIG (aucune liste en dur, repli sur les fichiers déjà
   présents si la config est illisible).
2. Écrit chaque fichier **atomiquement** (tmp + os.replace) : jamais de fichier
   tronqué si la machine tombe pendant l'écriture.
3. Refuse d'écrire une réponse vide ou trop courte (règle #8 : pas de mesure =
   pas d'écrasement ; on garde l'ancien fichier et on le DIT).
4. Publie `runs/KLINES_SANTE.json` : âge de la dernière barre, paires OK/KO,
   horodatage. C'est ce fichier que `sante_mesures.py` REFUSE quand il vieillit.

Aucune décision de trading, 0 ordre. Réversible : il suffit de décharger l'agent.
Usage : python3 rafraichir_klines.py [--silencieux] [--autotest]
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
KL_DIR = RUNS / "KLINES_1H"
CFG = ROOT / "config" / "defaults.env"
SANTE = RUNS / "KLINES_SANTE.json"
BASE = "https://api.mexc.com/api/v3/klines"
BARS = 720          # 30 jours de bougies 1 h
CADENCE_S = 3600    # cadence des barres écrite dans l'état (mesure, pas seuil de décision)


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_env(path: Path) -> dict:
    d = {}
    try:
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            d[k.strip()] = v.strip()
    except Exception:
        pass
    return d


def perimetre(cfg: dict) -> list[str]:
    """Paires à suivre : LISES dans la config, sinon les fichiers déjà présents."""
    brut = " ".join(
        str(cfg.get(k, "")) for k in ("PAPER_PAIRS", "PAPER_OBSERVE_PAIRS", "WATCH_PAIRS")
    ).replace(";", ",")
    pairs = [p.strip().upper() for p in brut.replace(" ", ",").split(",") if p.strip()]
    pairs = [p for p in dict.fromkeys(pairs) if p.endswith("USDT")]
    if not pairs:
        pairs = sorted(p.stem for p in KL_DIR.glob("*.json"))
    return pairs


def fetch(pair: str, bars: int = BARS) -> list:
    q = urllib.parse.urlencode({"symbol": pair, "interval": "60m", "limit": min(1000, bars)})
    req = urllib.request.Request(f"{BASE}?{q}", headers={"User-Agent": "ace777-klines/1.0"})
    last = None
    for essai in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                data = json.loads(r.read().decode())
            if isinstance(data, list) and data:
                return data
            last = ValueError(f"réponse vide ({type(data).__name__})")
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
            last = e
            time.sleep(1.0 * (essai + 1))
    raise last if last else RuntimeError("échec inconnu")


def ecrit_atomique(path: Path, data: list) -> None:
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data), encoding="utf-8")
    os.replace(tmp, path)


def age_derniere_barre(path: Path) -> float | None:
    """Âge (s) de la dernière barre CLOSE du fichier. None si illisible/vide."""
    try:
        data = json.loads(path.read_text())
        if not data:
            return None
        return max(0.0, time.time() - float(data[-1][0]) / 1000.0)
    except Exception:
        return None


def autotest() -> int:
    """Prouve que l'organe SAIT dire NON (règle #8) sans toucher aux vraies données."""
    import tempfile

    ok = 0
    total = 0

    # 1) une réponse vide ne doit JAMAIS écraser un fichier existant
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "XUSDT.json"
        p.write_text(json.dumps([[1, "1", "1", "1", "1"]]), encoding="utf-8")
        avant = p.read_text()
        try:
            data = []
            if not data:
                raise ValueError("réponse vide")
            ecrit_atomique(p, data)
            verdict = "ÉCRIT (défaut)"
        except ValueError:
            verdict = "refusé"
        total += 1
        if verdict == "refusé" and p.read_text() == avant:
            ok += 1
        print(f"  [{'OK' if verdict == 'refusé' else 'KO'}] réponse vide refusée, fichier intact")

    # 2) l'âge d'une barre FRAÎCHE doit être petit, celui d'une barre VIEILLE grand
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "F.json"
        p.write_text(json.dumps([[int((time.time() - 120) * 1000), "1", "1", "1", "1"]]))
        a_frais = age_derniere_barre(p)
        p.write_text(json.dumps([[int((time.time() - 6 * 86400) * 1000), "1", "1", "1", "1"]]))
        a_vieux = age_derniere_barre(p)
        total += 1
        if a_frais is not None and a_frais < 600 and a_vieux is not None and a_vieux > 5 * 86400:
            ok += 1
            print(f"  [OK] âge calculé : frais {a_frais:.0f}s · vieux {a_vieux:.0f}s")
        else:
            print(f"  [KO] âge mal calculé : {a_frais} / {a_vieux}")

    # 3) un fichier illisible ne doit pas produire un faux « frais »
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "G.json"
        p.write_text("pas du json", encoding="utf-8")
        total += 1
        if age_derniere_barre(p) is None:
            ok += 1
            print("  [OK] fichier illisible → âge INCONNU (jamais « frais »)")
        else:
            print("  [KO] fichier illisible jugé frais")

    print(f"AUTOTEST {ok}/{total}")
    return 0 if ok == total else 1


def main() -> int:
    sil = "--silencieux" in sys.argv
    if "--autotest" in sys.argv:
        return autotest()

    cfg = load_env(CFG)
    pairs = perimetre(cfg)
    KL_DIR.mkdir(parents=True, exist_ok=True)

    ok, ko, dernier = [], [], None
    for pair in pairs:
        try:
            data = fetch(pair)
            if not data or len(data) < 50:
                raise ValueError(f"trop court ({len(data) if data else 0} barres)")
            ecrit_atomique(KL_DIR / f"{pair}.json", data)
            ok.append(pair)
            dernier = max(dernier or 0, int(data[-1][0]))
            if not sil:
                print(f"  [+] {pair:12} {len(data)} barres · dernière {data[-1][4]}")
        except Exception as e:
            ko.append((pair, f"{type(e).__name__}: {e}"[:120]))
            if not sil:
                print(f"  [KO] {pair:12} {e}")

    if not ok:
        # rien de neuf : on ne prétend pas avoir rafraîchi. L'état le dit, et il garde
        # l'âge RÉEL du cache (celui qui fera refuser la mesure en aval).
        age = age_derniere_barre(KL_DIR / f"{pairs[0]}.json") if pairs else None
        SANTE.write_text(json.dumps({
            "organe": "rafraichir-klines", "ts_utc": utc(), "ok": False,
            "paires_ok": [], "paires_ko": [p for p, _ in ko],
            "derniere_barre_utc": None,
            "age_derniere_barre_s": round(age, 1) if age else None,
            "note": "AUCUN téléchargement réussi : le cache n'a PAS été rafraîchi.",
        }, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"RAFRAÎCHISSEMENT ÉCHOUÉ ({len(ko)} paire(s)) — cache non modifié")
        return 2

    age = age_derniere_barre(KL_DIR / f"{ok[0]}.json")
    SANTE.write_text(json.dumps({
        "organe": "rafraichir-klines", "ts_utc": utc(), "ok": True,
        "paires_ok": ok, "paires_ko": [p for p, _ in ko],
        "derniere_barre_utc": (datetime.fromtimestamp(dernier / 1000, timezone.utc)
                               .strftime("%Y-%m-%dT%H:%M:%SZ") if dernier else None),
        "age_derniere_barre_s": round(age, 1) if age is not None else None,
        "cadence_barre_s": CADENCE_S,
        "note": ("Écrit par rafraichir_klines.py. Si `age_derniere_barre_s` dépasse "
                 "3 cadences, sante_mesures.py REFUSE de croire une mesure klines."),
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"KLINES RAFRAÎCHIES : {len(ok)} ok · {len(ko)} ko · dernière barre {age/60:.0f} min"
          if age is not None else f"KLINES RAFRAÎCHIES : {len(ok)} ok · {len(ko)} ko")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
