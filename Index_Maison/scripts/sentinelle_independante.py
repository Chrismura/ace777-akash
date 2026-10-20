#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sentinelle_independante.py — Organe de VÉRITÉ du moteur Hulk (GO Christophe 15/09).
Rôle : recalculer depuis les LOGS BRUTS ce que le moteur DÉCLARE, sans jamais lui faire confiance.
Unanime de la flotille (Gemini + DeepSeek + Grok) : « tu pilotes un paquebot avec un compteur cassé ».

SPEC FIGÉE AVANT LE PREMIER RUN (anti data-snooping) :
  C1 RÉCONCILIATION PnL : realized_pnl(CSV brut) vs state.pnl_total déclaré.
     Divergence > 1.00 $ → CRITIQUE.
  C2 RÉCONCILIATION POSITIONS : qty de CHAQUE position déclarée vs replay BUY/SELL du CSV.
     Toute divergence sur une paire → CRITIQUE.
     AMENDEMENT 20/09/2026 (Buffy, GO Christophe « trancher la sentinelle ») — C2 jugeait
     à une résolution que la DÉCLARATION elle-même n'a pas. Preuve mesurée ce jour
     (CCUSDT) : le CSV, écrit en repr(float), est EXACT (seed 80.69722402 − sorties =
     19.92722402), tandis que le moteur DÉCLARE 19.92 : il tronque sa propre position au
     pas du marché (ce qu'un exchange détiendrait réellement, poussière exclue). L'écart
     (0,0072 = 0,036 %) n'est donc pas un trou de position : c'est la résolution de la
     valeur déclarée. Règle : on ne juge pas le moteur plus fin que ce qu'il déclare →
     tolérance C2 = max(1e-4 × qty, pas d'écriture de la valeur DÉCLARÉE, 1e-6), le pas
     étant LU sur la chaîne déclarée (« 19.92 » → 0.01 ; « 0.08207455429497568 » →
     pleine précision, la tolérance relative prend alors le relais). Reste flagué : tout
     écart PLUS GRAND que la résolution de la déclaration — donc tout vrai trou.
     AMENDEMENT POUSSIÈRE 20/10/2026 (GO « corrige une dernière fois ») — preuve
     forensique sur 109 099 lignes : 5 paires rejouaient +0,002/+0,011 jetons au-dessus
     du déclaré, TOUTES = poussière documentée du moteur (pop ≤ 0,1 % sell_trade +
     copeaux lot-floor du stake-out, valeur totale ~0,005 $). Depuis ce jour le moteur
     LOGGUE chaque abandon (DUST_DROP, pnl 0) ; la sentinelle soustrait le loggué et
     simule la règle pour l'historique. Un DUST_DROP qui contredit la simulation =
     journal mensonger → CRITIQUE. Zéro faux positif, zéro trou masqué.
  C3 BATTEMENT DE CŒUR : state.ts plus vieux que 30 min (le moteur écrit ~toutes les 20 s,
     tolérance large pour le réseau partagé) → CRITIQUE.
  C4 GARDE ABSOLUE : pnl_total < -20.00 $ (= base_notional 20 $ intégralement perdu) → CRITIQUE.

SORTIES :
  - Index_Maison/thermo/sentinelle_independante_etat.json  (mode « produit » pour le chien)
  - strategie/alarme.json ÉCRASÉ (dialecte vigie_live.py : dict unique, type "sentinelle")
    UNIQUEMENT sur verdict CRITIQUE — zéro cri quand tout va bien.
  - "kill_switch": true dans l'état le jour où un verdict CRITIQUE tombe.
    Le moteur est PAPIER : le kill-switch physique se branchera le jour où des ordres réels existent.

Lecture seule sur le moteur. 0 € · 0 ordre.
"""
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(os.path.expanduser("~/ace777-test-day1"))
RUNS = BASE / "hulk-mexc" / "runs"
OUT_ETAT = BASE / "Index_Maison" / "thermo" / "sentinelle_independante_etat.json"
OUT_ALARME = BASE / "Index_Maison" / "strategie" / "alarme.json"

SEUIL_DIV_PNL = 1.00          # $ — divergence PnL déclaré vs recalculé
SEUIL_HEARTBEAT_MIN = 30      # minutes
SEUIL_CATASTROPHE = -20.00    # $ — pnl_total plancher absolu


def dernier_run():
    """Le couple CSV + state le plus récent par mtime du CSV."""
    csvs = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    for c in csvs:
        st = c.with_name(c.stem + "_state.json")
        if st.exists():
            return c, st
    return None, None


def pas_ecriture(valeur):
    """Pas d'écriture d'une quantité : 0.01 pour « 19.92 », 1e-08 pour « 80.69722402 ».
    Accepte une chaîne (CSV) ou un nombre (state JSON — repr(float) est exact au
    round-trip en Python 3, donc fidèle à ce qui est déclaré).
    C'est la RÉSOLUTION de l'instrument : en dessous, une différence n'est pas
    mesurable (amendement C2 du 20/09/2026)."""
    t = valeur if isinstance(valeur, str) else ("" if valeur is None else repr(valeur))
    t = t.strip()
    if not t or "e" in t.lower():
        return None
    if "." not in t:
        return 1.0
    return 10.0 ** (-len(t.split(".", 1)[1].rstrip("0")))


def replay_csv(chemin):
    """Rejoue le CSV brut : realized PnL + qty nette par paire + pas d'écriture
    observé + POUSSIÈRE documentée.
    Retourne (pnl, {paire: qty}, n_trades, {paire: pas}, {paire: dust},
              {paire: dust_usd}, [mensonges]).
    AMENDEMENT POUSSIÈRE 20/10/2026 (GO « corrige une dernière fois », preuve
    forensique sur 109 099 lignes : 19 paires à l'écart 0.000000000, 5 paires à
    +0.002/+0.011 jetons TOUTES expliquées) : le moteur abandonne sans vente
      (a) les restes ≤ 0,1 % d'une position (pop sell_trade, ligne ~2657),
      (b) les copeaux lot-floor du stake-out (pop inconditionnel stake_out_half).
    Depuis le fix, chaque abandon est LOGGUÉ (DUST_DROP, pnl 0) ; pour
    l'historique antérieur, la règle est SIMULÉE (lifecycle exact de la position :
    core_trend retire du tradable, house/conservation vident, trend_add BAG_DCA
    renforce le TRADABLE — vérifié CHIP/RWAINC à 0.000000000 près).
    dust[paire] = loggué + simulé-non-loggué. mensonges = (paire, ts) où le
    loggué contredit le simulé au-delà du bruit flottant → journal mensonger."""
    pnl = 0.0
    qty_net = {}
    pas = {}
    n = 0
    rows = list(csv.DictReader(open(chemin, newline="", encoding="utf-8")))
    # Passe 1 : keeps du stake-out (BAG_ARM house_half, même ts que la vente) +
    # lignes DUST_DROP déjà logguées.
    keep_par_ts = {}
    dust_logged = {}
    last_px = {}
    for row in rows:
        ev = (row.get("event") or "").strip()
        pair = (row.get("pair") or "").strip()
        if not ev or not pair:
            continue
        try:
            q = float(row.get("qty") or 0)
            px = float(row.get("price") or 0)
        except ValueError:
            continue
        if px > 0:
            last_px[pair] = px
        note = row.get("reason") or ""
        if ev == "BAG_ARM" and "house_half" in note:
            keep_par_ts[(row.get("ts"), pair)] = q
        elif ev == "DUST_DROP":
            dust_logged[pair] = dust_logged.get(pair, 0.0) + q
    # Passe 2 : replay naïf + lifecycle du tradable pour la poussière simulée.
    # Le DUST_DROP est loggué dans la foulée du pop (même seconde ou la suivante)
    # → l'appariement loggué/simulé se fait à ±60 s, jamais au ts exact.
    pos = {}
    sim_events = []

    def _poussiere(pair, ts, montant):
        if montant > 1e-12:
            sim_events.append((ts, pair, montant))

    for row in rows:
        ev = (row.get("event") or "").strip()
        pair = (row.get("pair") or "").strip()
        if not ev or not pair:
            continue
        try:
            q = float(row.get("qty") or 0)
            p = float(row.get("pnl_usdt") or 0)
        except ValueError:
            continue
        ts = row.get("ts")
        note = row.get("reason") or ""
        mouvement = ev in ("BUY", "BAG_DCA", "GBAG_SOUCHE", "GBAG_PYRAMIDE",
                           "SELL", "SELL_PARTIAL", "BAG_SELL", "BAG_CRASH",
                           "DUST_DROP")
        if mouvement:
            p_ecr = pas_ecriture(row.get("qty"))
            if p_ecr:
                # le pas le plus GROSSIER écrit pour la paire = la résolution limite
                pas[pair] = max(pas.get(pair, 0.0), p_ecr)
        if ev in ("BUY", "GBAG_PYRAMIDE"):
            qty_net[pair] = qty_net.get(pair, 0.0) + q
            pos[pair] = pos.get(pair, 0.0) + q
        elif ev == "BAG_DCA" and "trend_" in note:
            # trend_add / trend_rebuy renforcent le TRADABLE (p = self.pos).
            qty_net[pair] = qty_net.get(pair, 0.0) + q
            pos[pair] = pos.get(pair, 0.0) + q
        elif ev in ("BAG_DCA", "GBAG_SOUCHE"):
            qty_net[pair] = qty_net.get(pair, 0.0) + q
        elif ev in ("SELL", "SELL_PARTIAL"):
            qty_net[pair] = qty_net.get(pair, 0.0) - q
            pnl += p
            n += 1
            full = pos.get(pair, 0.0)
            if "stake_out_" in note and "sell_" in note:
                keep = keep_par_ts.get((ts, pair), 0.0)
                _poussiere(pair, ts, full - q - keep)
                pos[pair] = 0.0
            else:
                left = full - q
                if full > 0 and left <= full * 0.001:
                    _poussiere(pair, ts, left)
                    pos[pair] = 0.0
                else:
                    pos[pair] = left
        elif ev == "BAG_ARM":
            if "core_trend" in note:
                pos[pair] = pos.get(pair, 0.0) - q
            elif "house_half" in note or "conservation_half" in note:
                pos[pair] = 0.0
        elif ev in ("BAG_SELL", "BAG_CRASH"):
            qty_net[pair] = qty_net.get(pair, 0.0) - q
            pnl += p
            n += 1
        elif ev == "DUST_DROP":
            qty_net[pair] = qty_net.get(pair, 0.0) - q
    # Appariement : chaque DUST_DROP loggué doit avoir une cause simulée (même
    # paire, ±60 s). Simulé-sans-log = historique antérieur au fix (expliqué).
    # Loggué-sans-cause = le moteur abandonne par un chemin inconnu → CRITIQUE.
    def _ts(s):
        try:
            return datetime.fromisoformat(str(s).replace("Z", "+00:00")).timestamp()
        except Exception:
            return None
    log_events = []
    for row in rows:
        if (row.get("event") or "").strip() != "DUST_DROP":
            continue
        try:
            log_events.append((_ts(row.get("ts")),
                              (row.get("pair") or "").strip(),
                              float(row.get("qty") or 0), row.get("ts")))
        except ValueError:
            continue
    dust_unlogged = {}
    mensonges = []
    libres = list(sim_events)
    for lts, lpair, lq, lts_raw in log_events:
        best, best_dt = None, None
        for i, (sts, spair, sq) in enumerate(libres):
            if spair != lpair:
                continue
            dt = abs(lts - _ts(sts)) if lts and _ts(sts) else (0 if sts == sts else None)
            if dt is None:
                continue
            if best is None or dt < best_dt:
                best, best_dt = i, dt
        if best is not None and best_dt <= 60:
            _, _, sq = libres.pop(best)
            if abs(sq - lq) > max(1e-9, 1e-6 * abs(lq)):
                mensonges.append(f"{lpair}@{lts_raw}: loggué {lq:.9f} vs simulé {sq:.9f}")
        else:
            mensonges.append(f"{lpair}@{lts_raw}: DUST_DROP {lq:.9f} sans cause simulée")
    for _sts, spair, sq in libres:
        dust_unlogged[spair] = dust_unlogged.get(spair, 0.0) + sq
    dust = {}
    for pair in set(dust_logged) | set(dust_unlogged):
        dust[pair] = dust_logged.get(pair, 0.0) + dust_unlogged.get(pair, 0.0)
    dust_usd = {pair: abs(d) * last_px.get(pair, 0.0) for pair, d in dust.items()}
    return pnl, qty_net, n, pas, dust, dust_usd, mensonges


def main():
    verdict = "OK"
    motifs = []
    now = datetime.now(timezone.utc)

    csv_path, state_path = dernier_run()
    if not csv_path:
        verdict, motifs = "CRITIQUE", ["aucun run PAPER_V1 avec state trouvé"]
    else:
        state = json.loads(state_path.read_text())
        # C3 battement de cœur
        ts_state = datetime.fromisoformat(state["ts"].replace("Z", "+00:00"))
        age_min = (now - ts_state).total_seconds() / 60
        if age_min > SEUIL_HEARTBEAT_MIN:
            verdict = "CRITIQUE"
            motifs.append(f"C3 heartbeat: state vieux de {age_min:.0f} min (> {SEUIL_HEARTBEAT_MIN})")
        # C1 PnL
        pnl_csv, qty_csv, n_trades, pas_csv, dust, dust_usd, mensonges = replay_csv(csv_path)
        if mensonges:
            verdict = "CRITIQUE"
            motifs.append("C2 journal mensonger: " + " ; ".join(mensonges)[:280])
        pnl_declare = float(state.get("pnl_total") or 0)
        div = abs(pnl_declare - pnl_csv)
        if div > SEUIL_DIV_PNL:
            verdict = "CRITIQUE"
            motifs.append(f"C1 PnL: déclaré {pnl_declare:.2f} $ vs recalculé {pnl_csv:.2f} $ (div {div:.2f} > {SEUIL_DIV_PNL})")
        # C2 positions — tolérance = la RÉSOLUTION DE LA MESURE (amendement 20/09/2026) :
        # on ne peut pas juger plus fin que le pas d'écriture du journal.
        poches = {}
        for _k in ("positions", "bags", "conservation", "bag_dca"):
            for _pair, _v in (state.get(_k) or {}).items():
                poches.setdefault(_pair, []).append(_v)
        c2_resolution = {}
        for pair in sorted(set(poches) | set(qty_csv) | set(dust)):
            q_declare = sum(float(_v.get("qty") or 0) if isinstance(_v, dict) else 0.0
                            for _v in poches.get(pair, []))
            # Le replay brut compte la poussière abandonnée (jamais vendue, plus
            # déclarée) : on la soustrait — logguée (DUST_DROP) ou simulée
            # (historique, règle 0,1 % / stake-out). Amendement 20/10/2026.
            q_recalc = qty_csv.get(pair, 0.0) - dust.get(pair, 0.0)
            pas_declare = sum(pas_ecriture(_v.get("qty")) or 0.0
                              if isinstance(_v, dict) else 0.0
                              for _v in poches.get(pair, []))
            tol = max(1e-6, 1e-4 * abs(q_declare), pas_declare)
            ecart = abs(q_declare - q_recalc)
            if ecart > tol:
                verdict = "CRITIQUE"
                motifs.append(f"C2 position {pair}: déclaré {q_declare:.6f} vs replay {q_recalc:.6f} "
                              f"(écart {ecart:.6f} > tolérance {tol:.6g})")
            elif ecart > 1e-6:
                # Sous la tolérance mais non nul : c'est la RÉSOLUTION de la déclaration
                # (position tronquée au pas du marché). On l'ÉCRIT — traçabilité, jamais
                # une alarme : une explication vaut mieux qu'un faux positif.
                c2_resolution[pair] = {"ecart": round(ecart, 6), "pas_declare": pas_declare,
                                      "pas_csv": pas_csv.get(pair),
                                      "poussiere_qty": round(dust.get(pair, 0.0), 9),
                                      "poussiere_usd": round(dust_usd.get(pair, 0.0), 6)}
        # C4 catastrophe
        if pnl_declare < SEUIL_CATASTROPHE:
            verdict = "CRITIQUE"
            motifs.append(f"C4 catastrophe: pnl_total {pnl_declare:.2f} < {SEUIL_CATASTROPHE}")

        etat = {
            "ts": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "verdict": verdict,
            "run_csv": str(csv_path.relative_to(BASE)),
            "state_ts": state["ts"],
            "age_state_min": round(age_min, 1),
            "pnl_declare": round(pnl_declare, 4),
            "pnl_recalcule_csv": round(pnl_csv, 4),
            "divergence_usd": round(div, 4),
            "n_sorties_replay": n_trades,
            "n_positions_declarees": len(poches),
            "poussiere_usd_total": round(sum(dust_usd.values()), 6),
            "poussieres": {p: {"qty": round(dust.get(p, 0.0), 9),
                                "usd": round(dust_usd.get(p, 0.0), 6)}
                            for p in sorted(dust) if abs(dust.get(p, 0.0)) > 1e-12},
            "motifs": motifs,
            "c2_resolution": c2_resolution,
            "kill_switch": verdict == "CRITIQUE",
            "spec": ("figée en docstring avant premier run (C1>1$ C2 qty C3 30min C4<-20$). "
                     "C2 AMENDÉE 20/09/2026 : tolérance = max(1e-4×qty, pas de la valeur DÉCLARÉE, "
                     "1e-6) — on ne juge pas le moteur plus fin que ce qu'il déclare (CCUSDT : "
                     "déclaré 19.92, tronqué au pas du marché, vs replay exact 19.92722402 → "
                     "0,0072 de résolution, pas un trou de position)."),
        }

    OUT_ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1))

    if verdict == "CRITIQUE":
        # dialecte alarme.json = dict unique écrasé (vérifié chez vigie_live.py)
        alerte = {
            "ts": etat["ts"],
            "type": "sentinelle",
            "symbole": None,
            "ancienne": etat.get("pnl_declare"),
            "nouvelle": etat.get("pnl_recalcule_csv"),
            "variation_pct": None,
            "raison": " ; ".join(motifs)[:300],
            "titre_news": None,
            "source_news": "sentinelle_independante",
            "lien_news": None,
        }
        OUT_ALARME.write_text(json.dumps(alerte, ensure_ascii=False, indent=2))
        print(f"🚨 SENTINELLE CRITIQUE : {' ; '.join(motifs)}")
        return 1

    print(f"SENTINELLE OK — pnl déclaré {etat['pnl_declare']:.2f} $ = recalculé {etat['pnl_recalcule_csv']:.2f} $ "
          f"(div {etat['divergence_usd']:.4f}) · {etat['n_positions_declarees']} positions · state {etat['age_state_min']:.1f} min")
    return 0


if __name__ == "__main__":
    sys.exit(main())
