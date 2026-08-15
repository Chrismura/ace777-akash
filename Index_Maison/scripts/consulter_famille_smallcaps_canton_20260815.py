#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE (flotille) — small caps ACE777 : thèse Christophe + Canton Network (CC)."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_SMALLCAPS_CANTON_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — STRATÉGIE SMALL CAPS ACE777 (Hulk)

=== LA THÈSE DE CHRISTOPHE (règle d'exception) ===
Hulk (paper MEXC spot) surveille 15 small-caps. Christophe précise une RÈGLE D'EXCEPTION :
ces small-caps ne sont PAS « du fun ». Ce sont des projets à GROS potentiel d'adoption, suivis
depuis longtemps, souvent adossés à de l'INSTITUTIONNEL, et délibérément tenus SOUS LE RADAR du
mainstream (peu de hype médiatique). Donc :
  - le manque de liquidité / les spreads larges / les dumps NE SONT PAS des signaux de fuite,
    mais des OCCASIONS d'accumuler des BAGS (acheter bas, tenir, revendre au rebond).
  - le but Hulk = AUGMENTER LES BAGS, pas scalper.
  - « après tout dump elle remonte car projet avec institutionnel derrière, qui fait tout pour
    que le mainstream ne s'y intéresse pas ».
  - La prudence « norme marché » (filtre liquidité/spread strict) ne s'applique PAS de la même
    façon ici. XRP et HBAR sortent de cette logique (plus mainstream).

=== LE TEST : CC (Canton Network / Canton Coin) — tiré au hasard, hors XRP/HBAR ===
Vérification factuelle (web, sources officielles + presse) :
  • Canton Network = « the public blockchain chosen by Wall Street ». Bâti par Digital Asset
    (langage Daml). Objectif : « Bringing Trillions Onchain » (tokenisation d'actifs réels).
  • PARTICIPANTS institutionnels vérifiés : Goldman Sachs, BNY Mellon, CBOE, Microsoft, Moody's,
    S&P Global, Deloitte, Deutsche Börse Group, BNP Paribas, Deutsche Bank, ASX, SBI Digital
    Asset, Paxos, EquiLend… (lancement avec 30+ participants ; tests Goldman/BNY/CBOE concluants
    en mars 2024). 700+ firmes connectées, $6T+ d'actifs réels tokenisés, $300B+/jour de repo US
    Treasury.
  • Canton Coin (CC) = token d'UTILITÉ (frais du Global Synchronizer + récompenses d'usage).
  • TOKENOMICS anti-spéculation : « no pre-mine, no VC allocations » — chaque coin en circulation
    est GAGNÉ par de l'utilité réelle ; modèle burn-and-mint (frais brûlés, coins mintés selon
    l'usage). Approvisionnement sur courbe prédéfinie.
  • Positionnement assumé « under the radar » : « Canton isn't chasing headlines, it's rewiring… »
    → pas de marketing memecoin, utilité > spéculation.

=== LES QUESTIONS (format EXACT exigé) ===
1. Cette thèse « small caps institutionnelles sous le radar = accumuler les dumps en bags » est-elle
   FONDÉE en général, et le cas Canton Network la CONFIRME-t-il ? (institutionnel + utilité +
   pas de VC unlock + sous-radar)
2. Quels sont les RISQUES de cette exception (ex. un projet « institutionnel » peut quand même
   mourir ; l'illiquidité peut geler un bag ; le « sous-radar » peut durer des années) ?
3. CONCRÈTEMENT, comment adapter Hulk pour CES small caps : assouplir/quels filtres (liquidité,
   spread, volume DEAD/DRY), mais renforcer quoi en contrepartie (taille par position, stop,
   horizon des bags, diversification, kill-switch) ? Faut-il 2 « classes » de paires (core
   liquides vs small caps bag) avec des règles différentes ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur « adopter une règle d'exception small caps pour Hulk », préciser)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) qui ferai(en)t basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)

SYNTHÈSE (5 lignes max) : thèse validée/infirmée + règles Hulk recommandées.

Factuel, concis, français. Si une info manque : « information insuffisante ». Vous DONNEZ UN AVIS,
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
