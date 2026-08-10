#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""qwen_btc.py — Qwen analyse BTC (début d'apprentissage).

Même mécanique que cortana_analyse.py mais:
  * analyse GLOBALE de BTC (tous les indices mis en relation, pas un seul)
  * fournisseur Qwen local (task qwen.btc -> qwen-local prioritaire)
  * journalise dans analyses/YYYY-MM-DD.jsonl au MÊME format
    -> le professeur (score_justesse.py) note Qwen automatiquement (HIT/MISS).

Usage :
  python3 qwen_btc.py            # analyse BTC par Qwen + journalisation
  python3 qwen_btc.py --json     # sortie brute JSON

Ne passe JAMAIS d'ordre — lecture et opinion uniquement.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone

SCRIPTS = os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts")
THERMO_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/thermo")
LIVE_JSON = os.path.join(THERMO_DIR, "live.json")
HISTORY = os.path.join(THERMO_DIR, "history.jsonl")
ANALYSES_DIR = os.path.join(THERMO_DIR, "analyses")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
TASK = "qwen.btc"

LEXIQUE = {
    "mark": ("Prix mark BTC", "USD"),
    "chg24": ("Variation prix 24h", "%"),
    "chg1h": ("Variation prix 1h", "%"),
    "chg4h": ("Variation prix 4h", "%"),
    "funding": ("Taux de financement", "taux par période de 8h"),
    "fundingAvg30": ("Funding moyenne 30j", "taux"),
    "oi": ("Open interest", "BTC (contrats)"),
    "longShort": ("Ratio long/short", "ratio"),
    "takerRatio": ("Ratio taker", "ratio"),
    "topTraderLS": ("Ratio L/S top traders", "ratio"),
    "fearGreed": ("Fear & Greed", "/100"),
    "marketCapUsd": ("Capitalisation totale", "USD"),
    "btcDominance": ("Dominance BTC", "%"),
    "altSeason": ("Saison altcoins", "label"),
    "altSeasonScore": ("Score saison altcoins", "/100"),
    "panierDownPct": ("Panier en baisse", "%"),
    "whaleUsd": ("Flux baleines", "USD"),
    "whaleN": ("Baleines (≥50M$)", "compte"),
    "volQuote": ("Volume 24h", "USD"),
    "score": ("Score composite", "/100"),
    "climate": ("Climat", "label"),
    "liq24Usd": ("Liquidations 24h", "USD"),
    "liqLongUsd": ("Liquidations longues 24h", "USD"),
    "liqShortUsd": ("Liquidations courtes 24h", "USD"),
    "etfBtcM": ("ETF BTC net inflow", "M$"),
    "gexPutCall": ("GEX proxy put/call OI", "ratio"),
    "volumeCachedTaker": ("Taker buy ratio 24h", "ratio"),
    "volumeCachedPerpSpot": ("Ratio volume perp/spot", "ratio"),
}

CONTEXT_KEYS = list(LEXIQUE.keys())


def load_live():
    if not os.path.exists(LIVE_JSON):
        return {}
    try:
        return json.load(open(LIVE_JSON))
    except Exception:
        return {}


def load_history():
    if not os.path.exists(HISTORY):
        return []
    out = []
    try:
        with open(HISTORY) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except Exception:
                    continue
    except Exception:
        return []
    return out


def fmt_val(v):
    if v is None:
        return "INDISPONIBLE (null)"
    if isinstance(v, float):
        if abs(v) < 1e-4 and v != 0:
            return f"{v:.2e}"
        return f"{v:,.4f}" if abs(v) < 10 else f"{v:,.2f}"
    return str(v)


def trend_pct(history, key, hours):
    if not history or key not in history[-1]:
        return None
    now = history[-1][key]
    if not isinstance(now, (int, float)) or now == 0:
        return None
    target_ts = history[-1].get("tsUnix", 0) - hours * 3600
    past = None
    for row in history:
        if row.get("tsUnix", 0) <= target_ts and row.get(key) is not None:
            past = row[key]
    if past is None or not isinstance(past, (int, float)) or past == 0:
        return None
    return (now - past) / abs(past) * 100.0


def build_facts():
    live = load_live()
    history = load_history()
    facts = {
        "instrument": "BTC-USDT",
        "indices": {},
        "tendances": {
            "mark_24h_pct": trend_pct(history, "mark", 24),
            "mark_semaine_pct": trend_pct(history, "mark", 24 * 7),
            "funding_24h_pct": trend_pct(history, "funding", 24),
        },
        "serie_prix_recente": [],
        "historique_funding_recent": [],
    }
    for k in CONTEXT_KEYS:
        if k in live:
            facts["indices"][k] = fmt_val(live.get(k))
    for row in history[-12:]:
        if "mark" in row:
            facts["serie_prix_recente"].append({
                "ts": row.get("ts", "?"), "mark": row.get("mark")})
        if "funding" in row:
            facts["historique_funding_recent"].append({
                "ts": row.get("ts", "?"), "funding": fmt_val(row.get("funding"))})

    raw = {k: live.get(k) for k in CONTEXT_KEYS if k in live}
    raw["ts"] = live.get("ts")
    raw["tendances"] = facts["tendances"]
    return facts, raw


def _dernier_avis_qwen():
    """Dernière entrée indice=='btc' (celle de Qwen) dans les journaux d'analyses.
    Retourne (ts, avis, horizon) ou (None, None, None). Filtre STRICT sur btc :
    le champ 'derniere' du professeur est GLOBAL (souvent Gemini) et trompeur."""
    try:
        files = sorted(f for f in os.listdir(ANALYSES_DIR) if f.endswith(".jsonl"))
    except OSError:
        return None, None, None
    for fn in reversed(files):
        try:
            with open(os.path.join(ANALYSES_DIR, fn)) as f:
                for line in reversed(f.readlines()):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        e = json.loads(line)
                    except Exception:
                        continue
                    if e.get("indice") == "btc":
                        txt = e.get("analyse", "") or ""
                        m_av = re.search(r"AVIS\s*STRICT\s*:\s*(\w+)", txt, re.IGNORECASE)
                        m_h = re.search(r"HORIZON\s*:\s*([0-9]+h|1\s*semaine|semaine|48h|24h|1h|4h)", txt, re.IGNORECASE)
                        return (e.get("ts", "?")[:16],
                                m_av.group(1).upper() if m_av else None,
                                m_h.group(1).strip().lower() if m_h else None)
        except OSError:
            continue
    return None, None, None


def bilan_eleve():
    """Bilan de justesse de Qwen (indice btc) : compteur du professeur + dernier
    avis btc (filtré Qwen, jamais global). Boucle de feedback exigée par l'audit
    tiers (07/08) : sans retour sur ses erreurs, Qwen répète ses biais."""
    hit = n = 0
    try:
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
            tmp = tf.name
        try:
            subprocess.run(
                [sys.executable, os.path.join(SCRIPTS, "score_justesse.py"), "--json", tmp],
                capture_output=True, timeout=60, check=False)
            d = json.load(open(tmp))
            btc = (d.get("par_indice") or {}).get("btc", {})
            n = int(btc.get("n", 0) or 0)
            hit = int(btc.get("hit", 0) or 0)
        finally:
            try:
                os.unlink(tmp)
            except OSError:
                pass
    except Exception as e:
        return f"(bilan indisponible : {e})"

    ts, avis, horizon = _dernier_avis_qwen()
    if n == 0 and avis is None:
        return "Aucun bilan encore : c'est ton tout premier avis, sois rigoureuse."
    lignes = [f"[TON BILAN RÉCENT — professeur] : {hit}/{n} correct(s)"]
    if avis:
        lignes.append(f"Ton dernier avis btc ({ts}): {avis} / {horizon or '-'}")
    if n >= 3 and hit / max(n, 1) < 0.4:
        lignes.append("⚠️ Tes avis sont souvent FAUX : sois humble, privilégie NEUTRE et confiance faible.")
    return " ".join(lignes)


def call_hub(facts, correction=None):
    bilan = bilan_eleve()
    system = (
        "Tu es QWEN, l'analyste BTC junior du système ACE777 (Mac Air 8 Go). "
        "Tu es en APPRENTISSAGE : chaque avis est noté par le professeur "
        "(score_justesse) contre le marché réel. Tu dois donc être rigoureuse, "
        "honnête, jamais inventer un chiffre. Tu PROPOSES un avis, tu ne décides rien. "
        f"{bilan}\n\n"
        "RÈGLE ANTI-SURCONFIANCE : si le marché est PLAT (|chg1h| < 0.1 % et "
        "|chg24| < 0.3 %) ou si les signaux sont contradictoires, tu DOIS choisir "
        "NEUTRE avec confiance faible — JAMAIS LONG/SHORT avec confiance haute "
        "sur un marché sans signal clair. "
        "Structure EXACTE de ta réponse :\n"
        "FAITS : 3-4 phrases chiffrées exactes.\n"
        "LECTURE PHYSIQUE : 2 phrases (momentum, liquidité, climat).\n"
        "INTERPRÉTATION : 2 phrases.\n"
        "MISE EN RELATION : 2 phrases (croiser au moins 3 indices).\n"
        "PATTERN : 1 phrase (le régime de marché).\n"
        "OPINION : 2 phrases.\n"
        "Puis TERMINER EXACTEMENT par 3 lignes :\n"
        "AVIS STRICT : LONG ou SHORT ou NEUTRE\n"
        "HORIZON : 24h ou 48h ou 1 semaine\n"
        "CONFIANCE : haute ou moyenne ou faible"
    )
    payload = {
        "task": TASK,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": (
                "Analyse le marché BTC-USDT à partir de ces données :\n\n"
                f"{json.dumps(facts, ensure_ascii=False, indent=1)}\n\n"
                "Donne ton analyse selon ta structure."
                + (correction or "")
            )},
        ],
        "temperature": 0.4,
        "max_tokens": 900,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=None) as resp:
        data = json.load(resp)
    return data["choices"][0]["message"]["content"], data.get("provider", "?")


def surconfiance_detectee(content, facts_bruts):
    """Vérifie déterministiquement la règle anti-surconfiance : marché plat
    (|chg1h| < 0.1 et |chg24| < 0.3) + avis LONG/SHORT + confiance haute.
    Retourne True si le modèle a enfreint la règle (on le FLAG, on n'invente
    pas de verdict à sa place)."""
    try:
        chg1h = abs(float(facts_bruts.get("chg1h") or 0))
        chg24 = abs(float(facts_bruts.get("chg24") or 0))
    except Exception:
        return False
    if not (chg1h < 0.1 and chg24 < 0.3):
        return False
    m_av = re.search(r"AVIS\s*STRICT\s*:\s*(LONG|SHORT)", content, re.IGNORECASE)
    m_cf = re.search(r"CONFIANCE\s*:\s*haute", content, re.IGNORECASE)
    return bool(m_av and m_cf)


def journalise(facts, facts_bruts, content, provider, avis_ok=True):
    os.makedirs(ANALYSES_DIR, exist_ok=True)
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(ANALYSES_DIR, f"{day}.jsonl")
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "indice": "btc",
        "provider": provider,
        "faits": facts,
        "faits_bruts": facts_bruts,
        "analyse": content,
        "avis_ok": avis_ok,
        "surconfiance_detectee": surconfiance_detectee(content, facts_bruts),
    }
    with open(path, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    facts, facts_bruts = build_facts()
    print("[qwen_btc] envoi au hub (qwen.btc)...", file=sys.stderr)
    try:
        content, provider = call_hub(facts)
    except Exception as e:
        print(f"✘ hub injoignable : {e}", file=sys.stderr)
        return 1

    has_avis = re.search(r"AVIS\s*STRICT\s*:\s*(LONG|SHORT|NEUTRE)",
                         content, re.IGNORECASE) is not None
    if not has_avis:
        print("[avis] AVIS STRICT absent - retry avec correction...", file=sys.stderr)
        correction = ("\n\nTa réponse n'a PAS les 3 lignes finales obligatoires. "
                      "Rends l'analyse À NOUVEAU, terminée par EXACTEMENT :\n"
                      "AVIS STRICT : LONG|SHORT|NEUTRE\n"
                      "HORIZON : 24h|48h|1 semaine\n"
                      "CONFIANCE : haute|moyenne|faible")
        try:
            content2, provider2 = call_hub(facts, correction)
            if re.search(r"AVIS\s*STRICT\s*:\s*(LONG|SHORT|NEUTRE)",
                         content2, re.IGNORECASE):
                content, provider = content2, provider2
                has_avis = True
            else:
                content = content2
        except Exception as e2:
            print(f"✘ retry échoué : {e2}", file=sys.stderr)

    journal = journalise(facts, facts_bruts, content, provider, avis_ok=has_avis)
    print(f"[provider: {provider}]", file=sys.stderr)
    print(f"[journal: {journal}]", file=sys.stderr)

    if a.json:
        import re as _re
        m = _re.search(r"AVIS\s*STRICT\s*:\s*(\w+)", content, _re.IGNORECASE)
        print(json.dumps({
            "provider": provider,
            "avis": m.group(1).upper() if m else None,
            "avis_ok": has_avis,
            "journal": journal,
        }, ensure_ascii=False))
        return 0
    print(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
