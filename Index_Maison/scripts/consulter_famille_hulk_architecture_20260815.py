#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — architecture Hulk « portefeuille intelligent » (15/08/2026).

Protocole §C #9 Multi-Perspective + #5 Confidence-Weighted + AMÉLIORATIONS.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_HULK_ARCHITECTURE_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — ARCHITECTURE HULK : portefeuille intelligent autonome

=== L'OBJECTIF DE CHRISTOPHE (formulé, validé avec lui) ===
Un « guetteur de portefeuille au max de ses capacités » sur ses 15 small-caps MEXC (watchlist
CoinMarketCap « The Hulk Crypto Portfolio Picks », qu'il connaît par cycle/projet). Il doit :
  1. acheter les dips, revendre les rips ;
  2. faire des « bags » : mise → 2× → vendre 50% (récupère la mise), le reste = bag maison (plus-value),
     racheter plus bas (DCA) ;
  3. AGIR SEUL (Christophe ne peut pas veiller 24/24) ;
  4. avec CORTANA comme cerveau (ajuste, recommande, alerte à la voix).

=== CE QUI EXISTE DÉJÀ (Hulk = dossier séparé, hulk-mexc/) ===
Architecture vérifiée dans le code (pas de mémoire) :

PISTE A — exécution (DÉTERMINISTE, déjà autonome) : scripts/paper_diprip.py
  • régimes 15j/impulse, dip/rip/stop, STAKE_DOUBLE_MULT=2.0, STAKE_SELL_FRAC=0.50 (bag),
    BAG_DCA_ON, BAG_CRASH_SELL_FRAC=0.90, CASH_REDEPLOY, COMPOUND_ON, REENTRY, sense MEXC book.
  • PAPER_PAIRS = 15 small-caps (XRP, HBAR, QAIT, RIZE, ZBCN, W, RED, CC, PYTH, BIO, KITE, TEL,
    CHIP, RWAINC, EDEL). MODE=paper, NOTIONAL_USDT=20.
  • = environ 80% de l'objectif déjà implémenté.

PISTE B — veille (les « yeux ») : scripts/digest_watch.py
  • scan MEXC + DefiLlama en boucle, écrit VEILLE_ALERT.md / DIGEST_LATEST.md.
  • documenté « pas branché en websocket ; Qwen = superviseur MANUEL » (docs/VEILLE_QWEN.md).

ACTEURS POSÉS (fondations ACE777) : Ada (horizon/voilure), Cortana (cerveau + dashboard F3,
lit déjà Hulk), Qwen (apprentissage, pas encore branchée).

=== LES 2 TROUS DIAGNOSTIQUÉS (lecture seule, confirmé) ===
1. LA VEILLE SE PEND SUR LE RÉSEAU : digest_watch.py expire sans rien écrire (test one-shot
   timeout 120s). Dernier digest = 2,5 jours d'âge. Conséquence : plus de signal → tout reste
   en régime WATCH → 3 positions « seed » gelées depuis 2 jours, PnL = −4,54 USDT.
   CAUSE RACINE : la contrainte WiFi/téléphone/alpage (RÉELLE, PROUVÉE, PERMANENTE chez
   Christophe) — le scan MEXC/DefiLlama n'a pas de timeout/back-off propre → il se pend.
2. CORTANA NON BRANCHÉE À HULK : elle lit Hulk (dashboard F3) mais ne pilote AUCUN paramètre
   (régimes, risque, actifs surveillés). Le lien cerveau↔moteur n'existe pas.

=== MA PROPOSITION D'ARCHITECTURE (à juger) ===
Deux étages SÉPARÉS (doctrine maison C2/C3 : jamais de LLM dans la boucle d'ordre) :
  • Étage EXÉCUTION = moteur déterministe (paper_diprip.py, déjà autonome, garde-fous C7)
    → agit SEUL sur les ordres, sans LLM.
  • Étage CERVEAU = Cortana → ajuste les PARAMÈTRES (régimes, risque, quels actifs, seuils),
    recommande, alerte à la voix — mais NE PASSE PAS les ordres.
Le chantier = boucher les 2 trous : (a) veille robuste au réseau (timeout + back-off +
circuit-breaker + fallback STANDBY), (b) brancher Cortana en pilote de stratégie.

=== LA QUESTION OUVERTE (à trancher) ===
Christophe pensait avoir demandé « le moteur champion (ACE) pour Hulk ». Le code livré dit
l'inverse : « jamais le genesis, copie d'IDÉES seulement » (README/PLAN). Faut-il :
  • TRANSPOSER le moteur champion (genesis bash, Binance FUTURES, scalper BTC x5→x13, duo
    scout/hunter + revenge 1,5×) vers Hulk (MEXC SPOT, 15 small-caps, dip&rip heures/jours) ?
  • OU garder la PHILOSOPHIE du champion (radar/sense/prudence) déjà empruntée, et finir Hulk
    tel quel (moteur déterministe dédié spot) ?
Mon avis provisoire : la transposition littérale est un non-sens technique (scalper futures à
levier ≠ spot small-cap à position longue ; le revenge 6s n'a pas de sens sur un bag de heures).
Mais je soumets aux 4 modèles.

=== VOTRE MISSION (format EXACT exigé) ===
Analysez sous 3 angles :
  • Architecture : l'architecture à 2 étages (moteur déterministe + cerveau Cortana hors boucle
    d'ordre) est-elle la bonne pour « portefeuille intelligent autonome » ? Y a-t-il un étage
    manquant (ex. Ada/horizon, kill-switch déterministe, mode dégradé hors-ligne) ?
  • Transposition ACE : transposer le moteur champion tel quel, ou garder Hulk dédié spot en
    reprenant la philosophie ? Pourquoi ?
  • Priorité : quel est l'ordre réel des chantiers (veille robuste ? brancher Cortana ? autre) ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur « ouvrir le chantier architecture Hulk », préciser)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3 hypothèses
  CE QUI CHANGERAIT L'AVIS : le(s) fait(s) qui ferait/faisaient basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)

SYNTHÈSE (5 lignes max) : architecture retenue + ordre des actions.

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
