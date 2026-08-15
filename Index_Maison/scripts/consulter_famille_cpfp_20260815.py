#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — Onchain v2 : détection camouflage UTXO/CPFP + seuils adaptatifs.
Avis seulement, rien n'est appliqué."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_CPFP_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — ONCHAIN V2 : DÉTECTION DU CAMOUFLAGE UTXO/CPFP

=== LA PÉPITE (Christophe, source directe) ===
Les baleines camouflent leurs gros mouvements :
1. UTXO indivisible → dépense du billet entier + monnaie rendue (change).
2. CAMOUFLAGE : arbre de milliers de micro-tx de POUSSIÈRE (dust) à frais zéro, invisibles
   au fond de la mempool.
3. DÉCLENCHEUR CPFP : une tx « enfant » finale avec frais astronomiques liée à la monnaie rendue.
4. EXÉCUTION : le mineur est obligé de valider tout l'arbre à frais zéro pour toucher la prime
   de l'enfant → bloc réglé d'un coup.
5. EXPULSION : ce bloc massif expulse les tx des petits porteurs.
→ Une baleine peut déplacer des milliers de BTC SANS jamais créer une tx ≥1000 BTC.
→ Notre scanner actuel (gros blocs ≥1000 BTC + fragmentation ≥500 BTC/3 blocs) NE LA VOIT PAS.

=== CONSIGNE CHRISTOPHE ===
Seuils PLUS BAS que les seuils publics (les baleines connaissent les seuils des amateurs et
s'adaptent). Nous, tout petits, devons être plus malins.

=== CARTES DU SUPERVISEUR (à juger) ===
1. SEUILS STATISTIQUES ADAPTATIFS (z-score) : au lieu de seuils fixes, mesurer l'ANORMALITÉ
   — moyenne mobile + écart-type sur 7j → déclencher à N× l'écart-type. La baleine ne peut
   pas s'adapter à une ligne qui bouge chaque jour. (Même principe que le seuil X relatif d'Ada.)
2. SIGNATURE CPFP PAR FRAIS (inaltérable) : surveiller la distribution des frais sats/vB —
   une tx à >20× la médiane avec parent à frais quasi nuls = signature d'exécution de
   camouflage. Le montant se camoufle, le frais astronomique est LE mécanisme (incontournable).
3. ANTICIPATION PAR ACCUMULATION : détecter le cluster de dust par source sur 24-72h
   glissantes → voir la baleine PRÉPARER son coup avant le déclencheur.

=== CONTEXTE SYSTÈME ===
- Module existant : surveiller_whales.py (mempool.space free, scan 5 min launchd), 4 adresses
  vérifiées (Binance hot/cold, Bitfinex cold, Genesis), écrit whales_scan_latest.json +
  whales_mouvements.jsonl.
- Pont onchain (livré ce jour) : injecte section onchain dans live.json → synthèse textuelle
  pour Cortana (44% justesse, NEUTRE forcé <60%) + modulateur voilure Ada (±10%, jamais bloqué).
- Doctrine : 100% gratuit, zéro budget, stdlib, kill-switch, réversible, famille consultée.

=== VOTRE MISSION ===
1. Les 3 cartes (z-score, signature frais CPFP, accumulation dust) : lesquelles garder ?
   Quels seuils concrets v1 (z-score à combien de σ ? >20× médiane ? fenêtre 24/48/72h ?) ?
2. FAUX POSITIFS : les CPFP légitimes existent (re-spend d'urgence). Comment distinguer
   « exécution de camouflage » d'un CPFP banal sans noyer les alertes ?
3. COÛT API mempool.space : suivre parents/enfants + dust par source = combien d'appels/scan ?
   Budget raisonnable (scan 5 min) ? Limites de robustesse ?
4. INTÉGRATION : le nouveau signal (CPFP/poussière) doit-il passer par le même pont →
   live.json → synthèse Cortana + modulateur Ada ? Pondération vs les signaux existants
   (gros blocs/fragmentation) ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur onchain v2 CPFP/dust/statistique)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) qui ferai(en)t basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)
SYNTHÈSE (5 lignes max) : cartes retenues + seuils v1 + intégration.

Factuel, concis, français. Info manquante → « information insuffisante ». Vous DONNEZ UN
AVIS, ne touchez à rien."""

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
    for model in MODELS:
        out_file = os.path.join(OUT, f"AVIS_{model}.md")
        if os.path.exists(out_file):
            print(f"[SKIP] {model} déjà répondu")
            continue
        try:
            content, provider, dur = ask(model)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(f"# AVIS {model} (provider {provider}, {dur}s)\n\n{content}\n")
            print(f"[OK] {model} ({dur}s)")
        except Exception as e:
            print(f"[ERREUR] {model}: {e}")


if __name__ == "__main__":
    main()
