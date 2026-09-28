#!/usr/bin/env python3
"""
FUSIBLES PAR PAIRE (10/09/2026, GO Christophe) — la protection épouse la nature de chaque actif.

Principe (mesuré, pas inventé) : la plus folle des 20 paires bouge 7,8× plus que
la plus sage (EDEL 10 %/jour vs MNSRY 1,3 %). Une règle unique est donc
mathématiquement fausse. Chaque paire reçoit un BUDGET DE PERTE JOURNALIER :

    budget$(pair) = k × sigma_jour(pair) × mise_std   [k=1.5, mesure data/volatilite_paires.json]

ÉTAGE 1 — GEL SUR DONNÉES : budget consommé (perte réalisée du jour ≥ budget)
→ ENTRÉES interdites pour CETTE paire seule (sorties toujours libres — règle
maison : on ne bloque jamais une sortie). Le flottille continue.
DEGEL : sur DONNÉES, jamais sur horloge (demande explicite Christophe) — la
paire redémonte son gel quand elle PROUVE le rebond : prix > MM24h ET
dd6 > −3 % (mesures rafraîchies par com.ace777.fusibles-mesure, 5 min).
Paire dégélée : ré-autorisée à ×0.5 (elle a brûlé son budget une fois
aujourd'hui ; le reset UTC 00:00 remet tout à neuf, cf. disjoncteur global).

ÉTAGE 2 — DÉTARAGE PROGRESSIF (on freine avant le mur) : entre 0 et 100 % du
budget consommé, la mise est rabotée linéairement : mult = 1 − perte/budget.
À −50 % de budget → mises ×0.5. Aucun palier arbitraire, une seule règle.

SOURCES (fail-open indépendantes) :
  · budgets : Index_Maison/data/volatilite_paires.json (outil ré-rançable) ;
    si le fichier disparaît → sigma embarquées en fallback (mesure du 10/09).
  · pertes du jour : CSV du run live via le pointeur canonique
    .hulk_resume_pointer, events SELL*, pivot 00:00 UTC (même convention que
    le disjoncteur global et le nourrisseur).
CONFIG : Index_Maison/strategie/fusibles_config.json relu chaque 60 s.
  {"on": false} coupe TOUT (volontairement fail-open pour permettre la coupure).
  Absent/illisible → protection ACTIVE avec défauts internes : c'est un
  garde-fou, il ne doit pas mourir avec son fichier de config (inverse des
  features, philosophie disjoncteur).
C3 : on réduit ou refuse, on ne crée jamais d'ordre. Ce module ne commande rien.
"""
from __future__ import annotations

import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path

# ── Chemins (même topologie que paper_diprip.py : ROOT = hulk-mexc/) ─────────
_ROOT = Path(__file__).resolve().parents[1]
_RUNS = _ROOT / "runs"
_HUB = _ROOT.parent / "Index_Maison"
_MESURES_PATH = _HUB / "data" / "volatilite_paires.json"
_CFG_PATH = _HUB / "strategie" / "fusibles_config.json"

# ── Défauts internes (la protection survit à la perte de ses fichiers) ───────
_DFL_ON = True
_DFL_K = 1.5
_DFL_MISE_STD = 20.0
_DFL_TTL_CFG = 60.0
_DFL_TTL_MES = 60.0
_DFL_TTL_PNL = 60.0
_MES_FRAICHE_MAX = 900.0  # mesures de dégel > 15 min = périmées → dégel impossible (fail-closed)

# Fallback : sigmas journalières mesurées le 10/09 (45 j daily MEXC).
# Sert UNIQUEMENT si volatilite_paires.json est absent/illisible.
_SIGMA_FALLBACK: dict[str, float] = {
    "EDELUSDT": 10.00, "RIZEUSDT": 9.51, "CHIPUSDT": 7.60, "RWAINCUSDT": 5.80,
    "TELUSDT": 5.12, "KITEUSDT": 4.78, "ZBCNUSDT": 4.70, "BIOUSDT": 4.59,
    "REDUSDT": 4.41, "CCUSDT": 4.40, "FLUIDUSDT": 4.32, "XRPUSDT": 4.07,
    "PYTHUSDT": 3.96, "ETHUSDT": 3.33, "WUSDT": 3.28, "RWAUSDT": 2.53,
    "HBARUSDT": 2.44, "QNTUSDT": 2.40, "BTCUSDT": 2.16, "MNSRYUSDT": 1.29,
}

_cache: dict = {"cfg": None, "cfg_ts": 0.0, "mes": None, "mes_ts": 0.0,
                "pnl": None, "pnl_ts": 0.0}


def _lire_cfg() -> dict:
    """Config fusibles, cache 60 s. Absent/illisible → défauts (protection active)."""
    now = time.time()
    if _cache["cfg"] is not None and now - _cache["cfg_ts"] < _DFL_TTL_CFG:
        return _cache["cfg"]
    cfg = {"on": _DFL_ON, "k": _DFL_K, "mise_std": _DFL_MISE_STD}
    try:
        raw = json.loads(_CFG_PATH.read_text(encoding="utf-8"))
        if isinstance(raw, dict):
            cfg["on"] = bool(raw.get("on", _DFL_ON))
            cfg["k"] = float(raw.get("k", _DFL_K))
            cfg["mise_std"] = float(raw.get("mise_std", _DFL_MISE_STD))
    except Exception as e:
        note_erreur(f"cfg fusibles illisible ({e}) → défauts (protection active)")
    cfg["k"] = max(0.1, min(10.0, cfg["k"]))          # bornes anti-faute de frappe
    cfg["mise_std"] = max(1.0, min(1000.0, cfg["mise_std"]))
    _cache.update(cfg=cfg, cfg_ts=now)
    return cfg


def _lire_mesures() -> dict[str, dict]:
    """Mesures de volatilité + conditions de dégel, cache 60 s. Fallback embarqué."""
    now = time.time()
    if _cache["mes"] is not None and now - _cache["mes_ts"] < _DFL_TTL_MES:
        return _cache["mes"]
    mes: dict[str, dict] = {}
    try:
        d = json.loads(_MESURES_PATH.read_text(encoding="utf-8"))
        ts = float(d.get("ts") or 0)
        if now - ts <= _MES_FRAICHE_MAX:  # périmé → fallback (jamais de dégel sur vieilles données)
            for p in d.get("paires", []):
                sym = str(p.get("pair") or "")
                if sym:
                    mes[sym] = {
                        "sigma": float(p.get("sigma_jour_pct") or 0.0),
                        "degel_eligible": bool(p.get("degel_eligible")),
                        "prix": float(p.get("prix") or 0.0),
                        "dd6": float(p.get("dd6_pct") or 0.0),
                    }
        else:
            note_erreur(f"mesures volatilite périmées ({(now-ts)/60:.0f} min) → dégel neutralisé")
    except Exception as e:
        mes = {}
        note_erreur(f"mesures volatilite illisibles ({e}) → fallback embarqué")
    if not mes:  # fallback embarqué : budgets vivent, dégel inconnu (jamais inventé)
        mes = {s: {"sigma": v, "degel_eligible": False, "prix": 0.0, "dd6": 0.0}
               for s, v in _SIGMA_FALLBACK.items()}
    _cache.update(mes=mes, mes_ts=now)
    return mes


def _pnl_jour() -> dict[str, float]:
    """Perte réalisée du jour PAR PAIRE, depuis le CSV du pointeur canonique (ts ISO UTC).
    ⚠️ PIÈGE DOCUMENTÉ (10/09, vérifié sur le terrain) : le resume de HULK COPIE le
    journal complet dans le nouveau CSV (paper_diprip.py:1593 shutil.copy2) — le SELL
    d'avant-redémarrage existe donc DANS PLUSIEURS CSV. Scanner tous les CSV du jour
    = DOUBLE COMPTE. Le CSV du pointeur seul suffit : chaque reprise copie le journal
    du précédent, la chaîne est continue, le pointeur contient TOUT. Pivot 00:00 UTC
    (convention disjoncteur/nourrisseur). Fail-open : échec → {}."""
    now = time.time()
    if _cache["pnl"] is not None and now - _cache["pnl_ts"] < _DFL_TTL_PNL:
        return _cache["pnl"]
    out: dict[str, float] = {}
    jour = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        ptr = (_RUNS / ".hulk_resume_pointer").read_text(encoding="utf-8").strip()
        state = _RUNS / ptr                      # PAPER_V1_{ts}_state.json
        csvp = state.with_name(state.name.replace("_state.json", ".csv"))
        if csvp.exists():
            with csvp.open(newline="") as f:
                for row in csv.DictReader(f):
                    ev = row.get("event") or ""
                    if ev.startswith("SELL") and (row.get("ts") or "").startswith(jour):
                        try:
                            p = row.get("pair") or ""
                            out[p] = out.get(p, 0.0) + float(row.get("pnl_usdt") or 0.0)
                        except (ValueError, TypeError):
                            pass
    except Exception as e:
        out = {}
        note_erreur(f"scan PnL CSV échoué ({e}) → fusibles neutres ce cycle")
    _cache.update(pnl=out, pnl_ts=now)
    return out


def budget_usd(pair: str, cfg: dict | None = None, mes: dict[str, dict] | None = None) -> float:
    """Budget de perte journalier de la paire en $ : k × sigma × mise_std."""
    cfg = cfg or _lire_cfg()
    mes = mes or _lire_mesures()
    m = mes.get(pair)
    if not m:
        return 0.0
    return cfg["k"] * (m["sigma"] / 100.0) * cfg["mise_std"]


def mult_mise(pair: str, pnl_jour: dict[str, float] | None = None) -> tuple[float, str]:
    """Décision fusible pour la paire → (multiplicateur de mise, raison).
    1.0 = normal · 0<x<1 = détarage (étage 2) · 0.0 = gel (étage 1).
    pnl_jour : injection pour tests/harnais (None → lecture CSV live)."""
    cfg = _lire_cfg()
    if not cfg["on"]:
        return 1.0, "off"
    mes_all = _lire_mesures()
    m = mes_all.get(pair)
    if not m or m["sigma"] <= 0:
        return 1.0, "sans-mesure"          # jamais de gel sur inconnu
    pnl = pnl_jour if pnl_jour is not None else _pnl_jour()
    perte = -float(pnl.get(pair, 0.0))     # positif si la paire a perdu
    if perte <= 0:
        return 1.0, "ok"
    bud = budget_usd(pair, cfg, mes_all)
    if bud <= 0:
        return 1.0, "sans-mesure"
    frac = perte / bud
    if frac < 1.0:                          # étage 2 : détarage linéaire
        mult = max(0.0, 1.0 - frac)
        return (round(mult, 3), f"detarage:{perte:.2f}$/{bud:.2f}$")
    # étage 1 : budget consommé → gel, SAUF preuve de rebond (données, pas horloge)
    if m["degel_eligible"]:
        return 0.5, "degel-rebond(budget epuise, preuve faite)"
    return 0.0, f"gel:budget {bud:.2f}$ consomme (perte {perte:.2f}$)"


def note_scan_csv() -> None:
    """Pique le cache PnL pour forcer la relecture des CSV au prochain mult_mise().
    Appelé une fois par cycle moteur (cycle d'itération HULK ≈ 60 s > TTL 60 s) :
    garantit qu'un SELL du cycle précédent est compté AVANT la prochaine entrée —
    sans ça, le cache d'une lecture entre deux SELLs ferait juger le fusible sur
    des pertes périmées. Coût : nul (le re-scan n'a lieu que si le TTL a expiré)."""
    _cache["pnl_ts"] = 0.0


ERREURS = 0


def note_erreur(msg: str) -> None:
    """Traçabilité des échecs du module (règle maison : une erreur visible, jamais muette).
    Append jsonl fail-silent — événement rare par construction (fail-open internes)."""
    global ERREURS
    ERREURS += 1
    try:
        with (_HUB / "data" / "fusibles_erreurs.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                "msg": msg}) + "\n")
    except Exception:
        pass


def etat() -> dict:
    """Photo complète pour surveillance/debug (CLI, cockpit futur)."""
    cfg = _lire_cfg()
    mes_all = _lire_mesures()
    pnl = _pnl_jour()
    out = {"on": cfg["on"], "k": cfg["k"], "mise_std": cfg["mise_std"], "paires": {}}
    for sym in sorted(mes_all):
        mult, raison = mult_mise(sym, pnl)
        out["paires"][sym] = {
            "sigma": mes_all[sym]["sigma"],
            "budget_usd": round(budget_usd(sym, cfg, mes_all), 2),
            "pnl_jour": round(pnl.get(sym, 0.0), 4),
            "mult": mult,
            "raison": raison,
        }
    return out


if __name__ == "__main__":
    e = etat()
    print(f"FUSIBLES {'ON' if e['on'] else 'OFF'} · k={e['k']} · mise_std={e['mise_std']}$")
    print(f"{'paire':<12} {'sigma':>6} {'budget':>7} {'pnl jour':>9} {'mult':>6}  raison")
    for sym, v in e["paires"].items():
        print(f"{sym:<12} {v['sigma']:>5.2f}% {v['budget_usd']:>6.2f}$ "
              f"{v['pnl_jour']:>+9.4f}$ {v['mult']:>6.2f}  {v['raison']}")
