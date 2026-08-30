# SPEC — PROTOCOLE DE FONCTIONNEMENT INCASSABLE (23/08/2026)

## DEMANDE DE CHRISTOPHE (exacte)
On a déjà eu **les mêmes erreurs plusieurs fois**. Établir un protocole de bon
fonctionnement et de détection qui TIENNE LA ROUTE, **incassable**, et un
protocole d'évaluation. Le système doit pouvoir détecter sa propre panne avant
qu'elle ne fasse des dégâts, et doit être évalué honnêtement.

## CONTEXTE TECHNIQUE (à intégrer, pas à survoler)
Système ACE777 sur Mac mini M1 8 Go, macOS, Python stdlib uniquement, lancement
par plists launchd, hub IA local (~/prise-ia, endpoints OpenAI-compatibles,
clé broker sk-orca-...). Chaîne concernée :
hub IA → détecteurs mempool (pépite = blocs privatisés / tx jamais vues dans la
mempool publique = OTC de baleine ; poussière dust) → indice onchain →
analyses Cortana (IA) → évaluation.

## CATALOGUE DES ERREURS RÉCURRENTES (factuel, 15/08→23/08)
1. **Plists KeepAlive en boucle** : scripts relancés 50× plus souvent que prévu
   → saturation, écrasement des corrections appliquées (« les corrections
   disparaissent »), explosion de crédits.
2. **Bombardement API** : le détecteur creusait ~50 appels / 2 min sur
   mempool.space → rate-limit / bannissement IP → 8 h de silence.
3. **SYN black-hole réseau** : certaines IP ne répondent jamais (SYN_SENT sans
   SYN-ACK) et le timeout socket Python ne se déclenche PAS → process bloqué
   des heures (vérifié 6 min bloqué, socket toujours en SYN_SENT).
4. **Score menteur / cumul saturé** : le score « poussière » était le cumul 48 h
   → saturé à 100 même avec 0 poussière au run courant → fausses corrélations
   (r=−0,67 déclarée à tort, rétractée).
5. **Artefact « carnet vide → 100 % »** : échantillon 0 tx → taux fantôme 100 %
   au lieu de « non fiable ».
6. **Détecteur qui tourne mais n'écrit plus** : process vivant, données figées
   pendant 8 h, logs inchangés — la mort silencieuse.
7. **Détecteur aveugle** : endpoint 404 / endpoint down pendant plusieurs jours,
   données manquantes sans que personne ne le signale.
8. **Évaluation faussée** : les « indécis » (marché ni up ni down) comptés comme
   échec → justesse 46 % au lieu de 59 % réel ; et la consigne « sous 60 % →
   NEUTRE » pénalisait la réponse NEUTRE dès que le marché bougeait.
9. **Briefs en boucle** : agents qui génèrent des briefs quasi vides en boucle,
   qui ne disent rien d'utile mais consomment des crédits.
10. **Corrections non durables** : chaque correction est re-cassée par une autre
    boucle ou un autre script qui écrit le même fichier.

## CE QU'IL FAUT PRODUIRE (livrables)
A. **Protocole de BON FONCTIONNEMENT** : les règles d'or d'exécution (cadence,
   escriture, atomicité, redondance, repli, ressources), pensées pour être
   INCASSABLES : chaque brique doit avoir un garde-fou dont la RÉSILIENCE est
   elle-même vérifiée, et la panne de la mesure doit être visible AVANT qu'elle
   ne fausse les analyses.
B. **Protocole de DÉTECTION** : comment le système détecte automatiquement SES
   PROPRES dérives (morts silencieuses, données figées, scores saturés, boucles,
   bannissements, artefact) — avec seuils, fréquence, canal d'alerte. Chaque
   mode de panne du catalogue doit avoir un détecteur dédié.
C. **Protocole d'ÉVALUATION** : comment mesurer honnêtement la justesse de la
   chaîne (l'IA, la pépite, l'indice) — règles de scoring sans biais (cas
   indécis, échantillons trop petits, période de référence), minimum
   d'échantillons pour conclure, procédure de réévaluation automatique.

## CONSIGNES DE BRILLANCE (exigeant — Christophe)
Tu ne rends PAS une réponse générique de consultant. Tu es un ingénieur
Fiabilité Senior (SRE) + concepteur de systèmes auto-détectables + un
sceptique permanent. Concrètement :
- **Défie les hypothèses** de cette SPEC si elles sont fausses ou incomplètes.
- Pour chaque règle : demande-toi « comment cette règle peut-elle être
  contournée par un bug trivial, une boucle, un process zombie, un fichier figé
  ? » — et si tu trouves un contournement, propose un garde-fou suplémentaire
  qui le neutralise.
- **Hiérarchise** par risque : ce qui provoque des FAUSSES ANALYSES (le plus
  grave) vs ce qui provoque juste du bruit.
- Propose un système où la panne est DÉTECTABLE PAR CONSTRUCTION (par exemple :
  un « battement de cœur » signé par chaque acteur, un âge maximal des données,
  des compteurs monotones, des horizons de résilience).
- Contrainte matérielle : Mac M1 8 Go — les garde-fous ne doivent pas coûter
  cher en RAM/CPU/réseau. stdlib uniquement. Free tiers API.
- Conclusion : le protocole d'évaluation doit pouvoir PRONONCER un verdict
  objectif sur la chaîne (aussi bien « la pépite voit le marché » que « la
   pépite ne voit rien → on la débranche », en détectant les faux positifs.