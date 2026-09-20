#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PLANCHER CONFIRMÉ — SIMULATEUR SHADOW (papier)
==============================================
GO direct Christophe 11/09/2026 (« appliquons la, on est en test, je veux la
voir sous les yeux »). Ce n'est PAS le moteur : aucun ordre, aucune écriture
dans hulk-mexc. Le moteur continue de décider exactement comme avant.

L'idée (recadrage du plan « -39% en paliers » de Christophe) :
  Sur une manipulée_fragile, il n'y a pas de plancher à attraper pendant la
  chute (MUR-CASSE 84%/s, -66%/6h). Il y a un FOND à attendre. On achète les
  paliers SEULEMENT après la triple confirmation :
    C1 — les murs ont cessé de casser : drop_*_pct_per_s = 0 (aspiration_live)
    C2 — le spread est revenu : <= 2x spread_bps_med du profil (univers)
    C3 — premier rebond : prix >= bas_roulant * 1.03
  Puis achat papier en 3 paliers (confirmation, -3%, -6% sous confirmation).

Paires (15/09 GO Christophe « regarde le plancher pour tout le monde ») : les 11
paires couvertes par la sonde L2 (aspiration_live.json) — avant : RIZE+ZBCN
seulement. Les paires sans profil spread (QNT/FLUID/RWA/MNSRY) passent C2
avec le spread LIVE seul (garde 100 bps) au lieu d'être aveugles.

Entrées (lecture seule) :
  hulk-mexc/runs/DIGEST_*.json (le plus frais)   -> prix last / high_24h / low_24h
  hulk-mexc/runs/aspiration_live.json            -> drop_*_pct_per_s, spread_bps live
  hulk-mexc/strategie/universe_profils.json      -> spread_bps_med (profil)

Sorties :
  Index_Maison/data/plancher_confirme_hist.jsonl     (1 ligne/paire/cycle)
  Index_Maison/data/plancher_confirme_etat.json      (état du shadow)
  Index_Maison/cockpit/plancher_live.js              (feed cockpit, regénéré)
Exit 0 dans tous les cas d'observation ; != 0 seulement si données vitales absentes.
"""
import json
import glob
import os
import sys
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1")
HULK = os.path.join(BASE, "hulk-mexc")
DATA = os.path.join(BASE, "Index_Maison", "data")
COCKPIT = os.path.join(BASE, "Index_Maison", "cockpit")
PROFILS = os.path.join(HULK, "strategie", "universe_profils.json")
ASPI = os.path.join(HULK, "runs", "aspiration_live.json")
HIST = os.path.join(DATA, "plancher_confirme_hist.jsonl")
ETAT = os.path.join(DATA, "plancher_confirme_etat.json")
FEED = os.path.join(COCKPIT, "plancher_live.js")

PAIRES = ["BTCUSDT", "ETHUSDT", "QNTUSDT", "FLUIDUSDT", "RWAUSDT",
          "MNSRYUSDT", "CCUSDT", "RIZEUSDT", "EDELUSDT", "REDUSDT",
          "RWAINCUSDT", "ZBCNUSDT"]
SPREAD_ABS_GARDE_BPS = 100.0  # C2 sans profil : spread live <= 100 bps
SEUIL_CHUTE_PCT = 25.0      # documenté : la chute doit avoir fait -25% depuis le pic
REBOND_CONFIRM_PCT = 3.0    # C3 : rebond de >= 3% au-dessus du bas roulant
SPREAD_TOLERANCE = 2.0      # C2 : spread <= 2x la médiane du profil
PALIERS_PCT = [0.0, -3.0, -6.0]  # achat à la confirmation, puis -3%, puis -6%
MISE_PAPIER_USD = 100.0     # notional papier par palier (pas un ordre réel)


def now_utc():
    return datetime.now(timezone.utc)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def dernier_digest():
    fs = sorted(glob.glob(os.path.join(HULK, "runs", "DIGEST_*.json")),
                key=os.path.getmtime)
    return fs[-1] if fs else None


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def charger_etat():
    d = load_json(ETAT) or {}
    d.setdefault("paires", {})
    return d


def sauver_etat(d):
    tmp = ETAT + ".tmp"
    with open(tmp, "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    os.replace(tmp, ETAT)


def roulant(st, cle, val, ts, demi_vie_h=48):
    """Extremum roulant avec oubli : si rien de neuf depuis demi_vie, on repart de la valeur actuelle."""
    prev = st.get(cle)
    ts_prev = st.get(cle + "_ts", 0)
    if prev is None or (ts - ts_prev) > demi_vie_h * 3600:
        return val, ts
    if cle.startswith("haut"):
        return (max(prev, val), ts) if val >= prev else (prev, ts_prev)
    return (min(prev, val), ts) if val <= prev else (prev, ts_prev)


def traiter_paire(pa, digest, aspi_p, profils, etat, ts_now, digest_nom):
    st = etat["paires"].setdefault(pa, {"phase": "OBSERVATION"})
    p = digest.get(pa) or {}
    last = p.get("last")
    if not last:
        st["dernier_erreur"] = "pas de prix dans DIGEST"
        return None

    high24 = p.get("high_24h") or last
    low24 = p.get("low_24h") or last
    st["haut_roulant"], st["haut_ts"] = roulant(st, "haut", high24, ts_now)
    st["bas_roulant"], st["bas_ts"] = roulant(st, "bas", low24, ts_now)

    drop_depuis_pic = (st["haut_roulant"] - last) / st["haut_roulant"] * 100.0

    a = (aspi_p or {})
    drop_bid_s = a.get("drop_bid_pct_per_s")
    drop_ask_s = a.get("drop_ask_pct_per_s")
    spread_live = a.get("spread_bps")
    murs_stables = (drop_bid_s in (0, None)) and (drop_ask_s in (0, None))

    prof = (profils.get(pa) or {})
    spread_med = prof.get("spread_bps_med")
    c2 = None
    if spread_live is not None and spread_med:
        c2 = spread_live <= spread_med * SPREAD_TOLERANCE
    elif spread_live is not None:
        # 15/09 GO « pour tout le monde » : paire sans profil (QNT/FLUID/RWA/MNSRY)
        # C2 = garde absolue sur le spread LIVE au lieu de None (aveugle)
        c2 = spread_live <= SPREAD_ABS_GARDE_BPS

    c3 = None
    if st.get("bas_roulant"):
        c3 = last >= st["bas_roulant"] * (1 + REBOND_CONFIRM_PCT / 100.0)

    chute = drop_depuis_pic >= SEUIL_CHUTE_PCT
    confirme = chute and murs_stables and bool(c2) and bool(c3)

    # --- machine à états (papier) ---
    if confirme and st["phase"] == "OBSERVATION":
        st["phase"] = "CONFIRME"
        st["confirm_prix"] = last
        st["confirm_ts"] = iso(now_utc())
        st["paliers_faits"] = []
        st["achats"] = []
        st["preuves_confirm"] = {
            "C1_murs_stables": True,
            "C2_spread": {"live": spread_live, "med_profil": spread_med,
                          "seuil": round(spread_med * SPREAD_TOLERANCE, 2) if spread_med else None},
            "C3_rebond": {"bas_roulant": st.get("bas_roulant"),
                          "rebond_pct": round((last / st["bas_roulant"] - 1) * 100, 2) if st.get("bas_roulant") else None},
        }
    elif st["phase"] in ("CONFIRME", "ACHETE") and st.get("confirm_prix"):
        cp = st["confirm_prix"]
        for i, pal in enumerate(PALIERS_PCT):
            seuil = cp * (1 + pal / 100.0)
            tag = "palier%d" % (i + 1)
            if tag not in st.get("paliers_faits", []) and last <= seuil:
                st.setdefault("achats", []).append({
                    "palier": i + 1, "prix": last, "ts": iso(now_utc()),
                    "notional_usd": MISE_PAPIER_USD})
                st["paliers_faits"].append(tag)
                st["phase"] = "ACHETE"

    achats = st.get("achats", [])
    pnl = None
    if achats:
        n = sum(x["notional_usd"] for x in achats)
        pxm = sum(x["notional_usd"] / x["prix"] for x in achats)
        valeur = pxm * last
        pnl = round((valeur / n - 1) * 100, 2)

    return {
        "paire": pa, "phase": st["phase"], "last": last,
        "drop_depuis_pic_pct": round(drop_depuis_pic, 1),
        "chute_seuil": chute,
        "C1_murs_stables": murs_stables,
        "C2_spread_ok": c2,
        "C3_rebond_ok": c3,
        "veto": bool(chute and st["phase"] == "OBSERVATION"),
        "paliers_faits": st.get("paliers_faits", []),
        "pnl_latent_pct": pnl,
        "digest": digest_nom,
    }


def construire_feed(resum):
    payload = json.dumps(resum, ensure_ascii=False)
    js_lines = [
        'window.__PLANCHER__ = ' + payload + ';',
        '(function(){',
        '  // Réparé 20/09/2026 (Buffy, GO Christophe « incassable ») : ce feed est chargé',
        '  // en TÊTE de page, AVANT la carte qui porte #plancher-body. Exécuté tout de suite,',
        '  // il ne trouvait pas l\'élément, sortait aussitôt — et la carte restait À VIE sur',
        '  // « Chargement du shadow plancher… » (bloc jamais affiché). On attend le DOM,',
        '  // quel que soit l\'ordre des balises : un organe vivant dont l\'affichage est mort',
        '  // est un faux vide (même famille que le chien qui mesure un faux âge).',
        '  function rendre(){',
        '  var b=document.getElementById(\'plancher-body\');',
        '  if(!b||!window.__PLANCHER__)return;',
        '  var d=window.__PLANCHER__,h=\'\';',
        '  h+=\'<div style="font-size:12px;color:#9ab;margin-bottom:6px">\'+d.note+\'</div>\';',
        '  d.paires.forEach(function(p){',
        '    var col=p.phase===\'ACHETE\'?\'var(--acid)\':(p.phase===\'CONFIRME\'?\'#ffd34d\':\'#888\');',
        '    h+=\'<div style="border:1px solid #233;border-radius:8px;padding:8px 10px;margin-bottom:6px">\';',
        '    h+=\'<b style="color:\'+col+\'">\'+p.paire+\' \u2014 \'+p.phase+\'</b>\';',
        '    if(p.veto){h+=\' <span style="background:#a33;color:#fff;border-radius:4px;padding:1px 6px;font-size:11px">\u26d4 VETO anti-couteau</span>\';}',
        '    h+=\' <span style="color:#9ab">prix \'+p.last+\'</span><br>\';',
        '    var c1=p.C1_murs_stables?\'\u2705\':\'\u274c\';',
        '    var c2=(p.C2_spread_ok==null)?\'\u2014\':(p.C2_spread_ok?\'\u2705\':\'\u274c\');',
        '    var c3=(p.C3_rebond_ok==null)?\'\u2014\':(p.C3_rebond_ok?\'\u2705\':\'\u274c\');',
        '    h+=\'<span style="font-size:12px;color:#9ab">chute depuis pic: \'+p.drop_depuis_pic_pct+\'% (seuil 25%) \u00b7 C1 murs: \'+c1+\' \u00b7 C2 spread: \'+c2+\' \u00b7 C3 rebond: \'+c3+\'</span><br>\';',
        '    var pf=p.paliers_faits.length?p.paliers_faits.join(\', \'):\'aucun\';',
        '    var pnl=(p.pnl_latent_pct==null)?\'\u2014\':p.pnl_latent_pct+\'%\';',
        '    h+=\'<span style="font-size:12px;color:#9ab">paliers faits: \'+pf+\' \u00b7 PnL papier: \'+pnl+\'</span>\';',
        '    h+=\'</div>\';',
        '  });',
        '  h+=\'<div style="font-size:11px;color:#667">journal: \'+d.journal+\' \u00b7 cycle \'+d.ts+\'</div>\';',
        '  b.innerHTML=h;',
        '  }',
        '  if(document.readyState===\'loading\'){document.addEventListener(\'DOMContentLoaded\',rendre);}else{rendre();}',
        '})();',
    ]
    return "\n".join(js_lines) + "\n"


def main():
    os.makedirs(DATA, exist_ok=True)
    ts_now = now_utc().timestamp()
    dp = dernier_digest()
    digest = load_json(dp) if dp else None
    aspi = load_json(ASPI) or {}
    profils = load_json(PROFILS) or {}
    if not digest:
        print("[plancher-shadow] aucun DIGEST — abandon cycle", file=sys.stderr)
        return 1
    pairs = digest.get("pairs") or {}
    dmap = {p.get("pair"): p for p in pairs if isinstance(p, dict)} if isinstance(pairs, list) else pairs
    aspi_paires = aspi.get("paires") or {}

    etat = charger_etat()
    etat["ts"] = iso(now_utc())
    resultats = []
    for pa in PAIRES:
        r = traiter_paire(pa, dmap, aspi_paires.get(pa), profils, etat, ts_now,
                          os.path.basename(dp))
        if r:
            resultats.append(r)
            with open(HIST, "a") as f:
                f.write(json.dumps({"ts": etat["ts"], **r}, ensure_ascii=False) + "\n")
    sauver_etat(etat)

    resum = {
        "ts": etat["ts"],
        "note": "SHADOW PAPIER \u2014 aucun ordre, moteur intact. GO direct Christophe 11/09 (test).",
        "regle": "C1 murs cessent de casser + C2 spread revenu + C3 rebond >=3% du bas, puis 3 paliers (0/-3/-6%).",
        "paires": resultats,
        "journal": "Index_Maison/data/plancher_confirme_hist.jsonl",
    }
    js = construire_feed(resum)
    tmp = FEED + ".tmp"
    with open(tmp, "w") as f:
        f.write(js)
    os.replace(tmp, FEED)

    print("[plancher-shadow] cycle OK —", ", ".join(
        "%s:%s" % (r["paire"], r["phase"]) for r in resultats))
    return 0


if __name__ == "__main__":
    sys.exit(main())
