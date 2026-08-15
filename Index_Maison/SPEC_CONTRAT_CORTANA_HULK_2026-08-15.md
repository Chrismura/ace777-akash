# SPEC — Contrat JSON Cortana ↔ moteur Hulk (v1 ADVISORY) — 15/08/2026

**Cible** : `hulk-mexc/scripts/cortana_contract.py` (NOUVEAU) + `hulk-mexc/strategie/cortana_pilot.json` (NOUVEAU) + `hulk-mexc/scripts/paper_diprip.py` + `hulk-mexc/config/defaults.env` + `hulk-mexc/scripts/cortana_propose_params.py` (NOUVEAU, côté écriture Cortana)
**Nature** : HORS genesis. Réversible (fichiers neufs supprimables, diff inverse pour paper_diprip.py).
**Verdict famille** (gemini 85% / nvidia 72%) : GO-AVEC-RÉSERVE — contrat + **ADVISORY strict** ; **NO auto-application tant que justesse < 60%** (Cortana = 44% aujourd'hui).

## Principe
Cortana (lecture seule, F5) écrit des propositions de paramètres dans `strategie/cortana_pilot.json`. Le moteur lit/valide/log (traçabilité + données shadow pour la boucle d'apprentissage A/B), et **n'applique RIEN en mode ADVISORY**. Le chemin AUTO (clampé, bornes dures) est implémenté mais **gated** : il ne se déclenche que si `enforced_mode=AUTO` ET `cortana_accuracy_score ≥ 0.60`.

---

## 1. NOUVEAU : `hulk-mexc/scripts/cortana_contract.py`
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrat JSON Cortana ↔ moteur Hulk (v1, ADVISORY).

Famille 15/08 (gemini 85%, nvidia 72%) : GO-AVEC-RÉSERVE.
  - ADVISORY : propositions validées + LOGGÉES, JAMAIS appliquées si justesse < 60%.
  - AUTO (futur, justesse ≥ 60% durable) : appliquées CLAMPÉES dans les bornes dures.
  - Fail-safe : fichier absent/corrompu → paramètres actuels GELÉS (aucun défaut silencieux).
"""
from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MIN_SCORE_AUTO = 0.60
BOUNDS = {
    "DIP_FLOOR_MULT": (0.85, 1.15),
    "RIP_FLOOR_MULT": (0.85, 1.15),
    "STOP_FLOOR_MULT": (0.90, 1.10),
    "NOTIONAL_MULT": (0.90, 1.10),
}
CONFIDENCES = ("faible", "moyenne", "haute")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _safe_load(path: Path) -> dict[str, Any]:
    try:
        if not path.exists():
            return {}
        d = json.loads(path.read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def load_proposals(path: Path) -> tuple[dict[str, Any], list[str]]:
    """Fail-safe : absent/corrompu → ({}, [warn])."""
    data = _safe_load(path)
    warns: list[str] = []
    if not data:
        warns.append("cortana_pilot absent/vide → paramètres actuels GELÉS (fail-safe)")
    elif not isinstance(data.get("proposals"), list):
        warns.append("cortana_pilot sans 'proposals'[] → rien à traiter")
        data = {}
    return data, warns


def validate_proposals(
    data: dict[str, Any], *, score: float = 0.0, mode: str = "ADVISORY"
) -> tuple[list[dict[str, Any]], list[str]]:
    """Valide chaque proposition (whitelist, bornes, expiry, confiance). Retourne (valides, rejets)."""
    valid: list[dict[str, Any]] = []
    rejects: list[str] = []
    for p in data.get("proposals") or []:
        param = str(p.get("param") or "")
        if param not in BOUNDS:
            rejects.append(f"{param}: hors liste blanche")
            continue
        if str(p.get("param_class") or "") != "threshold_multiplier":
            rejects.append(f"{param}: param_class != threshold_multiplier")
            continue
        try:
            value = float(p.get("value"))
        except Exception:
            rejects.append(f"{param}: valeur non numérique")
            continue
        lo, hi = BOUNDS[param]
        if not (lo <= value <= hi):
            rejects.append(f"{param}: {value} hors bornes [{lo},{hi}]")
            continue
        expiry = str(p.get("expiry") or "")
        if not expiry:
            rejects.append(f"{param}: expiry manquante")
            continue
        try:
            exp_ts = datetime.fromisoformat(expiry.replace("Z", "+00:00")).timestamp()
        except Exception:
            rejects.append(f"{param}: expiry invalide")
            continue
        if exp_ts <= time.time():
            rejects.append(f"{param}: expiry dépassée")
            continue
        conf = str(p.get("confidence") or "moyenne").lower()
        if conf not in CONFIDENCES:
            rejects.append(f"{param}: confiance '{conf}' invalide")
            continue
        if conf == "haute" and score < MIN_SCORE_AUTO:
            rejects.append(f"{param}: confiance 'haute' ignorée (score {score:.0%} < 60%)")
            continue
        valid.append(p)
    return valid, rejects


def apply_overrides(data: dict[str, Any], *, score: float = 0.0) -> dict[str, float]:
    """Mode AUTO uniquement : valeurs CLAMPÉES. Appelé SEULEMENT si mode=AUTO et score≥0.60."""
    if score < MIN_SCORE_AUTO:
        return {}
    overrides: dict[str, float] = {}
    for p in data.get("proposals") or []:
        param = str(p.get("param") or "")
        if param not in BOUNDS:
            continue
        try:
            value = float(p.get("value"))
        except Exception:
            continue
        lo, hi = BOUNDS[param]
        overrides[param] = round(max(lo, min(hi, value)), 4)
    return overrides


def process_pilot(
    path: Path, *, default_mode: str = "ADVISORY"
) -> tuple[list[dict[str, Any]], dict[str, float], list[str]]:
    """Point d'entrée du moteur : (pending, applied_overrides, warns).
    pending = propositions valides (ADVISORY : loggées, pas appliquées)."""
    data, warns = load_proposals(path)
    if not data:
        return [], {}, warns
    score = float(data.get("cortana_accuracy_score") or 0)
    mode = str(data.get("enforced_mode") or default_mode).strip().upper()
    pending, rejects = validate_proposals(data, score=score, mode=mode)
    applied: dict[str, float] = {}
    if mode == "AUTO" and score >= MIN_SCORE_AUTO:
        applied = apply_overrides(data, score=score)
    return pending, applied, warns + rejects
```

## 2. NOUVEAU : `hulk-mexc/strategie/cortana_pilot.json` (état initial vide, valide)
```json
{
  "ts": "2026-08-15T00:00:00Z",
  "source": "cortana",
  "session_id": "init",
  "cortana_accuracy_score": 0.44,
  "enforced_mode": "ADVISORY",
  "proposals": []
}
```

## 3. `paper_diprip.py` — hooks moteur
### 3a. Import
OLD :
```
from veille_gates import entry_gate_check, record_stop, veille_stale  # noqa: E402
```
NEW :
```
from veille_gates import entry_gate_check, record_stop, veille_stale  # noqa: E402
from cortana_contract import process_pilot  # noqa: E402
```

### 3b. Config (après `self.veille_stale_h = ...`)
OLD :
```
        self.veille_stale_h = float(cfg.get("VEILLE_STALE_HOURS", "6"))
```
NEW :
```
        self.veille_stale_h = float(cfg.get("VEILLE_STALE_HOURS", "6"))
        self.cortana_mode = (cfg.get("CORTANA_MODE", "ADVISORY") or "ADVISORY").strip().upper()
        self.cortana_pilot = ROOT / (cfg.get("CORTANA_PILOT_FILE") or "strategie/cortana_pilot.json")
        self.cortana_pending: list = []
        self.cortana_applied: dict = {}
```

### 3c. Nouvelle méthode (insérer juste avant `def run(self) -> int:`)
OLD :
```
    def run(self) -> int:
```
NEW :
```
    def refresh_cortana_pilot(self):
        """Contrat Cortana : lire/valider/logguer (ADVISORY = pas appliqué < 60%)."""
        try:
            pending, applied, warns = process_pilot(self.cortana_pilot, default_mode=self.cortana_mode)
        except Exception as e:
            say("warn", f"[{utc_now()}] cortana_pilot ERR: {e}")
            return
        self.cortana_pending = pending
        self.cortana_applied = applied
        for w in warns:
            say("warn", f"[{utc_now()}] cortana: {w}")
        if applied:
            say("heart", f"[{utc_now()}] cortana PILOT AUTO → {applied}")
        elif pending:
            say("heart", f"[{utc_now()}] cortana PILOT ADVISORY → {len(pending)} proposition(s)")

    def run(self) -> int:
```

### 3d. Boot (après `self.refresh_scores()` et `self.seed_inventory()`)
OLD :
```
        self.refresh_scores()
        self.seed_inventory()
        n = 0
```
NEW :
```
        self.refresh_scores()
        self.refresh_cortana_pilot()
        self.seed_inventory()
        n = 0
```

### 3e. Cycle (avec refresh_scores)
OLD :
```
            if n > 0 and n % self.score_every == 0:
                self.refresh_scores()
```
NEW :
```
            if n > 0 and n % self.score_every == 0:
                self.refresh_scores()
                self.refresh_cortana_pilot()
```

### 3f. Heartbeat (ajouter le compteur pilote)
OLD :
```
                    f"pnl={self.pnl_total:+.4f}$ | {regimes}{standby}",
```
NEW :
```
                    f"pnl={self.pnl_total:+.4f}$ | {regimes}{standby} "
                    f"cortana={len(self.cortana_pending)}",
```

## 4. `defaults.env` — config
OLD :
```
# Kill-switch global : veille muette (DIGEST_LATEST.md) > X heures → STANDBY (plus de nouvel achat)
VEILLE_STALE_HOURS=6
```
NEW :
```
# Kill-switch global : veille muette (DIGEST_LATEST.md) > X heures → STANDBY (plus de nouvel achat)
VEILLE_STALE_HOURS=6
# Contrat Cortana ↔ moteur : ADVISORY = propositions loggées, JAMAIS appliquées tant que justesse < 60%
CORTANA_MODE=ADVISORY
CORTANA_PILOT_FILE=strategie/cortana_pilot.json
```

## 5. NOUVEAU : `hulk-mexc/scripts/cortana_propose_params.py` (côté écriture Cortana)
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cortana propose des ajustements de paramètres Hulk → écrit strategie/cortana_pilot.json.

Lecture seule (Cortana ne passe aucun ordre). Utilisation :
  python3 cortana_propose_params.py [--speak]
"""
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HULK = Path(__file__).resolve().parents[1]
WS = Path(os.path.expanduser("~/ace777-test-day1/Index_Maison"))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
PILOT = HULK / "strategie" / "cortana_pilot.json"
STATE = max(
    (HULK / "runs").glob("PAPER_V1_*_state.json"),
    key=lambda p: p.stat().st_mtime,
    default=None,
)
JUSTESSE = WS / "scripts" / "justesse_cockpit.json"
IDENT = WS / "identity" / "prompts" / "cortana.md"
CONTRACT = (HULK / "scripts" / "cortana_contract.py")
sys.path.insert(0, str(HULK / "scripts"))
from cortana_contract import BOUNDS, validate_proposals  # noqa: E402


def main() -> int:
    score = 0.0
    try:
        score = float(json.load(open(JUSTESSE)).get("pct") or 0) / 100.0
    except Exception:
        pass
    state_txt = "indisponible"
    if STATE:
        try:
            st = json.load(open(STATE))
            state_txt = (
                f"PnL={st.get('pnl_total')} $ · positions={len(st.get('positions') or {})} "
                f"· bags={len(st.get('bags') or {})}"
            )
        except Exception:
            pass
    ident = open(IDENT, encoding="utf-8").read() if IDENT.exists() else ""
    user = (
        "Tu es le pilote de paramètres de Hulk (paper MEXC, dip&rip + bags). État : "
        f"{state_txt}. Ton score de justesse : {score:.0%}. Ta discipline F1 : si score < 60%, "
        "tu es prudemte (confiance faible/moyenne, jamais 'haute').\n"
        "Propose au plus 3 ajustements de paramètres DANS le contrat, uniquement parmi : "
        f"{list(BOUNDS.keys())} (bornes : {BOUNDS}). Format EXACT JSON (rien d'autre) :\n"
        '{"proposals": [{"param": "DIP_FLOOR_MULT", "param_class": "threshold_multiplier", '
        '"value": 0.9, "confidence": "faible|moyenne|haute", "reason": "…", '
        '"expiry": "2026-08-17T00:00:00Z"}]}\n'
        "Règle : ne propose que si TU as une raison fondée ; sinon proposals vides."
    )
    payload = {
        "task": "cortana.analyse",
        "messages": [{"role": "system", "content": ident}, {"role": "user", "content": user}],
        "temperature": 0.3,
        "max_tokens": 700,
    }
    req = urllib.request.Request(HUB, data=json.dumps(payload).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=None) as r:
        d = json.loads(r.read().decode())
    raw = d["choices"][0]["message"]["content"].strip()
    # extraire le bloc JSON
    start, end = raw.find("{"), raw.rfind("}")
    if start == -1 or end == -1:
        print("cortana: pas de JSON exploitable", file=sys.stderr)
        return 1
    try:
        data = json.loads(raw[start:end + 1])
        data.setdefault("proposals", [])
    except Exception as e:
        print(f"cortana: JSON invalide : {e}", file=sys.stderr)
        return 1
    valid, rejects = validate_proposals(data, score=score, mode="ADVISORY")
    out = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "cortana",
        "session_id": datetime.now(timezone.utc).strftime("%Y%m%d%H%M"),
        "cortana_accuracy_score": round(score, 3),
        "enforced_mode": "ADVISORY",
        "proposals": valid,
    }
    PILOT.parent.mkdir(parents=True, exist_ok=True)
    tmp = PILOT.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(PILOT)
    print(f"cortana: {len(valid)} proposition(s) → {PILOT}")
    for r in rejects:
        print(f"cortana REJET: {r}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## VÉRIFICATIONS ATTENDUES
1. `python3 -m py_compile cortana_contract.py paper_diprip.py cortana_propose_params.py` → OK.
2. Test `cortana_contract` : pilot vide → ([], {}, warn GELÉ) · proposition valide → pending=1 · valeur hors bornes → rejet · confidence haute + score 0.44 → rejet · mode AUTO + score 0.44 → applied={}.
3. `cortana_propose_params.py` (avec réseau) écrit un pilot valide.
4. Aucun impact sur les ventes/stops/bags (ADVISORY = rien n'est appliqué).

## CONTRAINTES
- En ADVISORY (valeur par défaut), le moteur n'applique JAMAIS. L'application AUTO est gated par `score ≥ 0.60` (ne se déclenche pas aujourd'hui).
- Ne rien changer d'autre.
