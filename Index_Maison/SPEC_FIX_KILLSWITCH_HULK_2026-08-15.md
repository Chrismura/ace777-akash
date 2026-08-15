# SPEC — Kill-switch déterministe global Hulk (STANDBY si veille muette) — 15/08/2026

**Cible** : `hulk-mexc/scripts/veille_gates.py` + `hulk-mexc/scripts/paper_diprip.py` + `hulk-mexc/config/defaults.env`
**Nature** : HORS genesis (outil paper). Réversible via backup. Ne touche PAS au moteur ACE.
**Motif** : la veille (digest_watch.py) peut mourir (réseau WiFi/alpage). Si elle est muette trop longtemps, Hulk est AVEUGLE et ne doit plus ouvrir de NOUVELLE position. On veut un STANDBY déterministe : plus d'achat, mais l'existant (ventes/stops/bags/DCA) continue d'être géré (protecteur). Validé famille (nvidia, chantier Hulk n°2).

## Signal de fraîcheur
`DIGEST_LATEST.md` est réécrit à CHAQUE cycle de la veille (`run_once` → `latest.write_text(md)`, inconditionnel, même si signal IDLE). Donc son mtime = « dernière fois que la veille a vu ». C'est le signal canonique.

## DIFF EXACT (appliquer au caractère près)

### 1. `veille_gates.py` — ajouter la fonction `veille_stale` entre `veille_blocks` et `entry_gate_check`
OLD :
```
    reason = str(info.get("reason") or "RED")
    return True, reason


def entry_gate_check(
```
NEW :
```
    reason = str(info.get("reason") or "RED")
    return True, reason


def veille_stale(
    runs: Path,
    *,
    max_age_hours: float = 6.0,
) -> tuple[bool, str]:
    """Kill-switch global : la veille n'a pas produit de digest frais depuis max_age_hours.

    Signal = mtime de DIGEST_LATEST.md (réécrit à CHAQUE cycle du digest_watch.py).
    Fail-open : fichier absent/corrompu → (False, "") = on ne bloque pas (le skip RED
    existant protège déjà ; ne bloque pas un test paper sans veille).
    """
    latest = runs / "DIGEST_LATEST.md"
    if not latest.exists():
        return False, ""
    try:
        age_h = (datetime.now(timezone.utc).timestamp() - latest.stat().st_mtime) / 3600.0
    except Exception:
        return False, ""
    if age_h > float(max_age_hours):
        return True, f"veille_stale_{age_h:.1f}h>{max_age_hours:.0f}h"
    return False, ""


def entry_gate_check(
```

### 2. `paper_diprip.py` — import
OLD :
```
from veille_gates import entry_gate_check, record_stop  # noqa: E402
```
NEW :
```
from veille_gates import entry_gate_check, record_stop, veille_stale  # noqa: E402
```

### 3. `paper_diprip.py` — config (après veille_refresh_sec)
OLD :
```
        self.veille_refresh_sec = float(cfg.get("VEILLE_STATUS_REFRESH_SEC", "60"))
```
NEW :
```
        self.veille_refresh_sec = float(cfg.get("VEILLE_STATUS_REFRESH_SEC", "60"))
        self.veille_stale_h = float(cfg.get("VEILLE_STALE_HOURS", "6"))
```

### 4. `paper_diprip.py` — gate globale dans `buy()` (avant le entry_gate_check)
OLD :
```
        regime = sc.get("regime", "")
        # v1.5 : cooldown post-stop + skip RED veille (soft, fail-open)
        allowed, code, detail = entry_gate_check(
```
NEW :
```
        regime = sc.get("regime", "")
        # Kill-switch global : veille muette → pas de nouvel achat (l'existant est géré)
        stale, sreason = veille_stale(RUNS, max_age_hours=self.veille_stale_h)
        if stale:
            say("warn", f"[{utc_now()}] STANDBY | {pair} | {sreason} (pas de nouvel achat)")
            self.log(
                pair, "SKIP", regime, price, price, 0.0, 0.0,
                sc.get("cadence_pct"), f"STANDBY:{sreason}",
            )
            return
        # v1.5 : cooldown post-stop + skip RED veille (soft, fail-open)
        allowed, code, detail = entry_gate_check(
```

### 5. `paper_diprip.py` — indicateur STANDBY dans le heartbeat
OLD :
```
                notion = self.current_notional()
                regimes = ",".join(
                    f"{p[0]}:{self.scores.get(p,{}).get('regime','?')[:3]}"
                    for p in self.pairs[:5]
                )
                say(
                    "heart",
                    f"[{utc_now()}] heartbeat open={open_n} bags={bags_n} "
                    f"dca={len(self.bag_dca)} cash_pairs={cash_n}({cash_sum:.1f}$) "
                    f"mise={notion:.2f}$ trades={self.trades} "
                    f"pnl={self.pnl_total:+.4f}$ | {regimes}",
                )
```
NEW :
```
                notion = self.current_notional()
                regimes = ",".join(
                    f"{p[0]}:{self.scores.get(p,{}).get('regime','?')[:3]}"
                    for p in self.pairs[:5]
                )
                _stale, _sreason = veille_stale(RUNS, max_age_hours=self.veille_stale_h)
                standby = f" | STANDBY({_sreason})" if _stale else ""
                say(
                    "heart",
                    f"[{utc_now()}] heartbeat open={open_n} bags={bags_n} "
                    f"dca={len(self.bag_dca)} cash_pairs={cash_n}({cash_sum:.1f}$) "
                    f"mise={notion:.2f}$ trades={self.trades} "
                    f"pnl={self.pnl_total:+.4f}$ | {regimes}{standby}",
                )
```

### 6. `defaults.env` — ajouter le seuil
OLD :
```
# Veille robuste au réseau (WiFi/alpage) — deadline max d'un scan complet (fix 15/08)
# (timeout HTTP 12s + back-off + circuit-breaker 3 échecs/60s sont codés en dur dans digest_watch.py)
SCAN_DEADLINE_SEC=90
```
NEW :
```
# Veille robuste au réseau (WiFi/alpage) — deadline max d'un scan complet (fix 15/08)
# (timeout HTTP 12s + back-off + circuit-breaker 3 échecs/60s sont codés en dur dans digest_watch.py)
SCAN_DEADLINE_SEC=90
# Kill-switch global : veille muette (DIGEST_LATEST.md) > X heures → STANDBY (plus de nouvel achat)
VEILLE_STALE_HOURS=6
```

## VÉRIFICATIONS ATTENDUES
1. `python3 -m py_compile veille_gates.py paper_diprip.py` → OK.
2. Test isolé : `veille_stale(RUNS, max_age_hours=...)` → (False,"") si DIGEST_LATEST.md frais ; (True, "veille_stale_...") si on force un mtime vieux (`os.utime`).
3. Aucun impact sur `sell_trade`/`stake_out_half`/`bag`/`DCA` (l'existant continue d'être géré).
4. `digest_watch.py` et le moteur ACE non touchés.

## CONTRAINTES
- Ne rien changer d'autre. Le kill-switch ne bloque QUE les nouveaux achats (`buy`), jamais les ventes.
