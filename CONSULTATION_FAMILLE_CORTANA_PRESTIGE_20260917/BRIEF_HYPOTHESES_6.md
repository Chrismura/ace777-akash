# BRIEF — 6 hypothèses architecturales pour Cortana (17/09/2026)

## Contexte
Cortana est l'analyste IA de la maison ACE777 : elle reçoit un indice crypto à la fois (funding, OI, Fear&Greed, GEX, ETF...), écrit une analyse structurée (FAITS → OPINION STRICT), est notée par un professeur (score_justesse.py, fenêtre 8h, zone morte, seuil FLAT ±0,3%), et sa note est réinjectée dans son prompt suivant. 2 analyses/jour. Un moteur de croisements (règle des 2 sources) et un portier anti-contradictions sont actifs depuis ce matin.

## FAITS d'audit du code actuel (vérifiés ce jour à la source)
- Le prompt master déclare déjà : « structures de prix = géométries fractales autonomes, même motif à différentes échelles » + section PATTERN obligatoire + tendance 24h/7j + historique horaire remis dans le contexte.
- Le seuil est déjà adaptatif par endroits : z-score adaptatif documenté (anti-baleines, CPFP) au lieu de seuils fixes.
- La boucle de réinjection existe (justesse récente remise dans le prompt) MAIS aucune consolidation périodique n'existe : le corpus analyses/ grandit en jsonl brut, jamais synthétisé.
- Le porte-monnaie-trading (Hulk) est un monde séparé, nourri par ses propres capteurs MEXC — aucun apprentissage partagé.

## Les 6 hypothèses à évaluer (origine : l'opérateur)

**H1 — Raisonnement rétrograde** : partir de la conclusion visée (ex : « BTC tenons-nous 2 jours au-dessus de 76k ? ») et remonter les conditions nécessaires. Pour un analyste noté sur ses avis, est-ce un gain de justesse mesurable ?

**H2 — Loi des seuils invisibles / points de bascule** : trouver les seuils réels où le marché change de régime (au-delà des seuils fixes que tout le monde voit). Cortana a déjà le z-score adaptatif ; faut-il aller plus loin (détection de points de bascule formels, catastrophe theory, hysteresis) ?

**H3 — Information fractale** : le prompt l'affirme déjà, mais les données remises sont-elles vraiment multi-échelles (4h/1h/15min ?) ou une seule échelle horaire ? Y a-t-il un gain à ajouter des outils fractals formels (Hurst, multifractaux) pour un LLM qui reçoit du texte ?

**H4 — Hippocampe artificiel** : mémoire à deux voies (court terme = contexte LLM, long terme = consolidation périodique). Faut-il construire une consolidation hebdomadaire qui comprime le corpus en « leçons » stables réinjectées ? Quel risque de surfacet/fossile (leçons périmées) ?

**H5 — Entraînement aux patterns** : exposer Cortana à des patterns historiques étiquetés (ex : « funding > 0,08% + OI hausse = échauffement longs ») en few-shot. Le prompt est aujourd'hui zero-shot sur les patterns. Gain attendu vs risque de sur-apprentissage de récits ?

**H6 — Intelligence distribuée** : « c'est le réseau qui pense, pas une seule IA ». Cortana (observation) + Hulk (exécution) + moteur de croisements + professeur = déjà un système distribué ? Ou faut-il une vraie architecture multi-agents avec débat entre agents ? Coût/complexité vs gain réel pour la justesse ?

## Questions précises
1. Pour chaque hypothèse : GO / NO-GO pour un système de production noté (pas un labo), avec l'objection principale.
2. Quel est le SEUL chantier prioritaire si on n'en fait qu'un ?
3. Quel test prouverait le gain en 30 jours avec n limité (≈60 analyses) ?
