#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — garde-fou PRIX FIGÉ (price_stasis) — 16/08/2026.

Protocole §C #9 Multi-Perspective + #5 Confidence-Weighted + AMÉLIORATIONS.
Code EXACT injecté (§B #6 Context Injection) pour éviter l'hallucination.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_PRICE_STASIS_20260816")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 16/08/2026) — CONSULTATION FAMILLE : garde-fou PRIX FIGÉ (price_stasis)

=== LE SYSTÈME ===
ACE777 = duo scalper Binance testnet : BETA (scout, ouvre les positions) + ALPHA (hunter,
amplifie x13 après une perte scout : le « revenge », récemment borné à 120s par le fix
last_loss_ts du 16/08 au matin). Les deux partagent la même boucle principale bash : gates
radar (tension) → tactic → stase → duo → qty → llm_gate → EXÉCUTION DE L'ORDRE.

=== LE CONSTAT TERRAIN (run de test 16/08 07:19Z, 40 premières minutes) ===
10 fills BETA dont 8 à pnl = 0.00000000 (entrée = sortie au même prix, hold 7-8s).
Exemple fill #100 : tension=10.67, bid_drop=69.4% (mur bid fondu), conf=0.9993
… prix FIGÉ à 63035.10 depuis 5 minutes. Pattern déjà présent au run de nuit
(69/160 fills BETA flat = 43%).
=> Le radar entre sur des signaux de carnet (bid_drop / tension) alors que le PRIX ne bouge
pas (marché sans liquidité, testnet calme) → fausse « rupture imminente » → ordre →
sortie flat 8s plus tard → trades nuls + frais.

=== LA SPEC PROPOSÉE (extraits EXACTS) ===
Principe : ne pas entrer si le prix n'a pas bougé d'au moins X bps sur la fenêtre Y s.

1. Variables :
  PRICE_STASIS_GUARD="${PRICE_STASIS_GUARD:-TRUE}"
  PRICE_STASIS_MIN_MOVE_BPS="${PRICE_STASIS_MIN_MOVE_BPS:-1.0}"
  PRICE_STASIS_WINDOW_SEC="${PRICE_STASIS_WINDOW_SEC:-30}"

2. État glissant (avec les autres prev_*) :
  price_stasis_ref_px=""; price_stasis_ref_ts=""

3. Check inséré JUSTE AVANT l'exécution de l'ordre (après toutes les gates, p2 = prix cycle) :
  if [ "$PRICE_STASIS_GUARD" = "TRUE" ]; then
    now_ps="$(now_sec)"
    if [ -n "$price_stasis_ref_px" ]; then
      dt_ps=$((now_ps - price_stasis_ref_ts)); [ "$dt_ps" -le 0 ] && dt_ps=1
      if [ "$dt_ps" -ge "$PRICE_STASIS_WINDOW_SEC" ]; then
        move_bps="$(ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); a=1.0 if a<=0.0; printf("%.6f", ((b-a).abs/a)*10000.0)' -- "$price_stasis_ref_px" "$p2")"
        if num_lt "$move_bps" "$PRICE_STASIS_MIN_MOVE_BPS"; then
          echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,price_stasis,,reason=price_frozen move_bps=$move_bps window=${dt_ps}s" >> "$LOG_FILE"
          sleep "$SLEEP_SEC"; continue
        fi
        price_stasis_ref_px="$p2"; price_stasis_ref_ts="$now_ps"
      fi
    else
      price_stasis_ref_px="$p2"; price_stasis_ref_ts="$now_ps"
    fi
  fi

Logique : référence posée au premier cycle ; quand la fenêtre (30s) est atteinte, comparaison
prix courant vs référence → mouvement < 1 bps = prix figé = SKIP `price_stasis` (raison
visible dans le CSV + log) ; sinon entrée OK + nouvelle référence. Le check est dans la
section d'entrée COMMUNE → s'applique au SCOUT (BETA) ET au HUNTER (ALPHA).
num_lt / now_sec existent déjà (réutilisés, aucune nouvelle fonction).
Le fix last_loss_ts du matin n'est PAS touché (le check se fait après le duo).

=== LES 4 QUESTIONS À LA FAMILLE ===
1. Seuils : 1.0 bps / 30s raisonnables ? (BTC actif ≈ 0.1-1 bps/s)
2. Défaut TRUE ou FALSE (sécurité vs comportement attendu) ?
3. Le skip doit-il compter comme un skip classique (juste visible dans le CSV) ou faut-il une
   métrique dédiée (ex. compteur dans le rapport) ?
4. Risque de faux positifs sur les entrées « wall collapse » légitimes (rupture de mur SANS
   mouvement de prix encore) — faut-il une exception (ex. tension > seuil très haut) ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur « implémenter le garde-fou price_stasis »,
    réserve précisée)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3 hypothèses
  CE QUI CHANGERAIT L'AVIS : le(s) fait(s) qui ferait/faisaient basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)

SYNTHÈSE (5 lignes max) : diagnostic le plus probable + ordre des actions.

Factuel, concis, français. Si une info manque : « information insuffisante ». Vous DONNEZ UN AVIS :
ne touchez à rien, n'écrivez aucun code."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2400, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for m in MODELS:
        for attempt in (1, 2):
            try:
                content, provider, secs = ask(m)
                with open(os.path.join(OUT, f"AVIS_{m}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
                print(f"[OK] {m} ({secs}s)")
                break
            except Exception as e:
                print(f"[ERR] {m} (tentative {attempt}): {e}")
                time.sleep(3)
        time.sleep(2)


if __name__ == "__main__":
    main()
