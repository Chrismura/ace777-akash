#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sante_mesures.py — l'organe qui REFUSE une mesure périmée (03/11/2026).

POURQUOI IL EXISTE (deux fautes déclarées le 03/11, « elles ne doivent plus se répéter »)
-----------------------------------------------------------------------------------------
① **La mesure du filet des souches était ARRÊTÉE sans le dire.** `runs/KLINES_1H`
   s'arrêtait au 2026-10-28 21:43 : on a mesuré, chiffré et décidé sur des données
   vieilles de 6 jours, dont la jambe du crash était absente. Personne ne le savait
   parce qu'AUCUN contrôle ne regardait l'âge de la mesure.
② **Le cycle GBAG (qui gère les souches) était MUET depuis le 29/10** : 4 296
   `GBAG_ERR`, et sur exception `tick_pair` rendait la main → les souches figées,
   cockpit vert. Un organe muet n'est pas un organe qui va bien (E29).

CE QU'IL FAIT : il lit des traces de vie **et il sait dire NON**.
  · `runs/KLINES_SANTE.json` → âge de la dernière barre vs 3 cadences de barre.
  · `runs/GBAG_SANTE.json`   → âge du dernier passage GBAG réussi vs 6 intervalles
    mesurés (`GBAG_CHECK_SEC` lu dans la config — aucun seuil fixe en dur).
  · codes : **0** tout frais · **2** au moins une mesure périmée/absente (refus).

Aucune décision de trading, 0 ordre, lecture seule (+ son état). Idempotent.
Usage : python3 sante_mesures.py [--silencieux] [--json] [--autotest]
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
CFG = ROOT / "config" / "defaults.env"
ETAT = RUNS / "SANTE_MESURES.json"
CADENCE_BARRE_S = 3600.0      # cadence des bougies lues (1 h)
FACTEUR_BARRE = 3.0           # 3 cadences manquées = la mesure n'est plus d'actualité
FACTEUR_GBAG = 6.0            # 6 intervalles GBAG sans passage réussi = organe muet


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


def _age(ts) -> float | None:
    try:
        return max(0.0, time.time() - float(ts))
    except (TypeError, ValueError):
        return None


def controle(home: Path, cfg: dict) -> list[dict]:
    """Rend la liste des contrôles, chacun avec son verdict et SA raison."""
    out = []

    # ── ① fraîcheur des klines (la mesure qui était arrêtée)
    ks = home / "KLINES_SANTE.json"
    seuil_barre = FACTEUR_BARRE * CADENCE_BARRE_S
    try:
        d = json.loads(ks.read_text())
    except Exception:
        d = None
    # `age_derniere_barre_s` est une DURÉE (pas un horodatage) : on l'additionne à l'âge
    # du rapport, sinon on soustrait une durée de l'heure courante et on obtient un faux
    # « très vieux » — le premier autotest l'a attrapé (3/4), corrigé avant câblage.
    age_barre = None
    if isinstance(d, dict):
        try:
            age_barre = max(0.0, float(d.get("age_derniere_barre_s")))
        except (TypeError, ValueError):
            age_barre = None
        age_rapport = _age(d.get("ts"))
        if age_barre is not None and age_rapport is not None:
            age_barre += age_rapport
    out.append({
        "controle": "klines-fraicheur",
        "ok": bool(age_barre is not None and age_barre <= seuil_barre),
        "mesure_s": round(age_barre, 1) if age_barre is not None else None,
        "seuil_s": seuil_barre,
        "raison": ("dernière barre fraîche" if age_barre is not None and age_barre <= seuil_barre
                   else ("aucun état KLINES_SANTE.json lisible" if age_barre is None
                         else f"dernière barre vieille de {age_barre/3600:.1f} h "
                              f"> {seuil_barre/3600:.1f} h — la mesure klines est PÉRIMÉE")),
    })

    # ── ② vie du cycle GBAG (l'organe muet)
    gbag_sec = 300.0
    try:
        gbag_sec = float(cfg.get("GBAG_CHECK_SEC", "300") or 300)
    except (TypeError, ValueError):
        pass
    seuil_gbag = FACTEUR_GBAG * gbag_sec
    gs = home / "GBAG_SANTE.json"
    try:
        g = json.loads(gs.read_text())
    except Exception:
        g = None
    age_gbag = _age(g.get("ts", 0)) if isinstance(g, dict) else None
    out.append({
        "controle": "gbag-vivant",
        "ok": bool(age_gbag is not None and age_gbag <= seuil_gbag),
        "mesure_s": round(age_gbag, 1) if age_gbag is not None else None,
        "seuil_s": seuil_gbag,
        "raison": ("cycle GBAG vivant" if age_gbag is not None and age_gbag <= seuil_gbag
                   else ("aucune trace GBAG_SANTE.json" if age_gbag is None
                         else f"dernier passage GBAG il y a {age_gbag/60:.0f} min "
                              f"> {seuil_gbag/60:.0f} min — l'organe est MUET")),
    })
    return out


def main() -> int:
    if "--autotest" in sys.argv:
        import tempfile
        ok = total = 0
        cfg = {"GBAG_CHECK_SEC": "300"}
        with tempfile.TemporaryDirectory() as td:
            h = Path(td)
            # 1) rien du tout → doit REFUSER les deux
            r = controle(h, cfg)
            total += 1
            if not any(c["ok"] for c in r):
                ok += 1; print("  [OK] états absents → refus (0/2 verts)")
            else:
                print("  [KO] états absents jugés verts")
            # 2) tout frais → doit ACCEPTER
            now = time.time()
            (h / "KLINES_SANTE.json").write_text(json.dumps(
                {"ts": now, "age_derniere_barre_s": 600}))
            (h / "GBAG_SANTE.json").write_text(json.dumps({"ts": now}))
            r = controle(h, cfg)
            total += 1
            if all(c["ok"] for c in r):
                ok += 1; print("  [OK] états frais → accepté (2/2 verts)")
            else:
                print("  [KO] états frais refusés à tort")
            # 3) klines vieilles de 6 jours → doit REFUSER ce contrôle-là seulement
            (h / "KLINES_SANTE.json").write_text(json.dumps(
                {"ts": now, "age_derniere_barre_s": 6 * 86400}))
            r = controle(h, cfg)
            k = next(c for c in r if c["controle"] == "klines-fraicheur")
            g2 = next(c for c in r if c["controle"] == "gbag-vivant")
            total += 1
            if (not k["ok"]) and g2["ok"]:
                ok += 1; print(f"  [OK] klines 6 j → refusé ({k['raison'][:60]}…) ; GBAG intact")
            else:
                print("  [KO] klines périmées acceptées ou GBAG faussement rouge")
            # 4) GBAG muet depuis 6 intervalles → refus
            (h / "KLINES_SANTE.json").write_text(json.dumps(
                {"ts": now, "age_derniere_barre_s": 600}))
            (h / "GBAG_SANTE.json").write_text(json.dumps({"ts": now - 6 * 300 - 60}))
            r = controle(h, cfg)
            g3 = next(c for c in r if c["controle"] == "gbag-vivant")
            total += 1
            if not g3["ok"]:
                ok += 1; print(f"  [OK] GBAG muet 30 min → refusé ({g3['raison'][:50]}…)")
            else:
                print("  [KO] GBAG muet jugé vivant")
        print(f"AUTOTEST {ok}/{total}")
        return 0 if ok == total else 1

    cfg = load_env(CFG)
    res = controle(RUNS, cfg)
    mauvais = [c for c in res if not c["ok"]]
    etat = {
        "organe": "sante-mesures", "ts_utc": utc(), "ok": not mauvais,
        "controles": res,
        "note": ("Refuse de croire une mesure dont la source n'est pas fraîche. "
                 "0 = tout frais · 2 = au moins une mesure périmée/absente."),
    }
    try:
        ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass

    if "--json" in sys.argv:
        print(json.dumps(etat, ensure_ascii=False, indent=2))
    elif "--silencieux" not in sys.argv:
        for c in res:
            print(f"  [{'OK ' if c['ok'] else 'REF'}] {c['controle']:16} {c['raison']}")
        print("SANTE MESURES :", "OK" if not mauvais else f"{len(mauvais)} REFUS")
    return 0 if not mauvais else 2


if __name__ == "__main__":
    raise SystemExit(main())
