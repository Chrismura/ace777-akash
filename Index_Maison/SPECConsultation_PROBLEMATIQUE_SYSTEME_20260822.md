# SPEC — Consultation Famille : Sortir de la boucle

## CONTEXTE VIVANT (22/08/2026)

Christophe est dans une situation critique. Le système ACE777 est devenu ingérable :

### Ce qui casse en continu
1. **Le hub** : providers qui timeout, blacklists, budget explosé (3599 appels/jour vs 624 budget), retry loops infinies
2. **Les indices santé** : dégradations silencieuses non détectées
3. **Le bot** : ghost fills supposés (finalement faux), positions orphelines, PnL brut positif mais NET incertain
4. **Les audits** : 484 documents mais aucune action concrète qui tient

### Ce qu'on a découvert aujourd'hui
- Le PnL brut est positif (+22 USDT sur 15 jours, 5408 trades, 40% win rate)
- Le testnet te PAYE des rebates de commission (+141 USDT) — le NET réel est incertain
- 25-39% des trades ALPHA sont des FLAT (entrée=sortie, zéro gain)
- Le revenge représente 91% des trades ALPHA (le TTL est neutralisé par le heartbeat)
- Les ghost fills N'EXISTENT PAS sur Binance — c'était une fausse piste de Buffy
- Le mode hedge n'existe plus sur le testnet

### Le pattern diabolique (MEMOIRE_SUFFRANCE_EN_FORCE)
> « Les idées de Christophe n'ont JAMAIS été le problème. Les erreurs sont toujours dans la couche d'exécution. »
> « Arrêter d'ajouter de l'intelligence et commencer à soustraire de la fragilité. »
> « La bonne séquence : résilience → stabilité → mesure fiable → PnL. »

### La réalité
- Christophe n'a pas le niveau pour tout superviser seul
- Buffy (l'IA) saute aux conclusions sans vérifier
- Chaque session ajoute de la complexité sans rien résoudre
- Le système est devenu un organisme où chaque brique ajoutée augmente la surface de dégradation silencieuse

## QUESTION À LA FAMILLE

**Comment sortir de cette boucle ?**

Contraintes :
- Pas de nouveau code complexe (on a déjà trop)
- Pas de dépendance à une IA conversationnelle (Buffy oublie tout entre les sessions)
- Le système doit fonctionner sans supervision humaine constante
- Christophe ne peut pas tout vérifier lui-même

Ce qu'on veut : une SOLUTION CONCRÈTE, pas un diagnostic. Quelque chose qu'on peut mettre en place cette semaine qui casse la boucle.

## CLAUSE PERMANENTE (Christophe)
« Prouve la meilleure logique et applique-la dans la correction et l'amélioration si possible. » Pas de rustine : PROUVE.

## FORMAT DE SORTIE OBLIGATOIRE
1. VERDICT en une phrase
2. La solution concrète (3-5 étapes max)
3. Ce qu'on ARRÊTE de faire
4. Ce qu'on COMMENCE à faire
5. Risques et réserves