#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-consultation FAMILLE — brief FUSIONNÉ (heartbeat/TTL + revenge + infra) — 15/08/2026.

Protocole §C #9 Multi-Perspective + #5 Confidence-Weighted + AMÉLIORATIONS.
Code EXACT injecté (§B #6 Context Injection) pour éviter l'hallucination.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_HEARTBEAT_TTL_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — CONSULTATION FUSIONNÉE MOTEUR (2ᵉ passe, avec la pièce manquante)

=== LE SYSTÈME ===
ACE777 = duo scalper Binance testnet : BETA (scout, ouvre) + ALPHA (hunter, amplifie x13).
« Revenge » : quand BETA ferme une PERTE (stop_loss / shock_inversion_stop / shock_exit_10bps /
fluid_exit_inversion / fluid_exit_brake / beta_sentinel_cut), ALPHA ré-entre en mode « revenge »
à ~1.5x pour récupérer. Il est censé être LIMITÉ par un TTL de 20s (DUO_EVENT_TTL_SEC=20) :
si l'événement scout date de >20s, le revenge doit être désarmé (stale_state).

=== LE BUG SUSPECTÉ (code EXACT du genesis, vérifié) ===
L297  : DUO_EVENT_TTL_SEC="${DUO_EVENT_TTL_SEC:-20}"
L875-891 (fonction) :
  # P2 : rafraîchit ts_ms du duo_state sans changer le reste (évite stale_state entre trades SCOUT)
  duo_touch_heartbeat() { duo_is_scout || return 0; duo_touch_heartbeat_force; }
  duo_touch_heartbeat_force() { ... j["ts_ms"]=(Time.now.to_f*1000).to_i; ... }
L1026-1031 (décision revenge) :
  age=((Time.now.to_f*1000).to_i - j["ts_ms"])
  if age > ttl*1000
    puts "allow=false mode=none ... reason=stale_state ..."   # <- désarme le revenge si >20s
    exit 0
  end
L1545 (boucle principale, à CHAQUE cycle SCOUT non-pausé) :
  duo_touch_heartbeat    # <- rafraîchit ts_ms à chaque cycle
=> CONTRADICTION : L1545 rafraîchit ts_ms en continu, donc L1027 `age > 20s` n'est JAMAIS vrai
=> `stale_state` ne se déclenche jamais => le revenge reste armé EN PERMANENCE (TTL 20s inopérant).

=== CHIFFRES (CSV scellés ALPHA, 12-15/08) ===
%revenge ALPHA : 71% (12) / 58% (13) / 68% (14) / 89% (15) — MONTE alors que le marché se calme.
%shock_inversion_stop (exits) : 68-84% tous les jours.
PnL revenge : -1.30 (12) / -3.60 (13) / +51.14 (14) / +0.93 (15) — ultra-volatil.
BETA : 0% revenge, 3-4x plus de trades qu'ALPHA mais PnL 0.40-2.51$ (vs 8.61-28.26$ ALPHA).
Flat ALPHA (entrée=sortie) : 25-39%, dominés par shock_inversion_stop.

=== INFRA (run du 15/08 12:45-14:47) ===
E-STALE : 0 (jours précédents) → 1032 aujourd'hui (`tension_stale age>800ms (NUAGE)` = feed de
tension qui lag 8-12s) → le bot SKIP / décide sur prix fantômes.
E-PROC : 4 → 75 (workers qui meurent).

=== VOTRE MISSION (format EXACT exigé) ===
Analysez sous 3 angles :
  • Technique : confirmez-vous que le couple L1545 (heartbeat) + L1027 (TTL 20s) neutralise le
    stale_state et rend le revenge quasi-permanent ? Est-ce le bug dominant ou un symptôme ?
  • Risque/Impact : quel est le fix le plus SÛR et le plus MINIMAL (ex. ne plus toucher ts_ms
    quand l'état est une perte SCOUT fermée, OU ne rafraîchir le heartbeat que si pnl>=0) ?
    Un fix du TTL casse-t-il un autre mécanisme (cooldown_revenge L1091, boost L1094) ?
  • Priorité : ordre infra (E-STALE/E-PROC) vs fix TTL/heartbeat vs gel du revenge ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur « ouvrir un chantier correctif TTL/heartbeat », réserve précisée)
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
