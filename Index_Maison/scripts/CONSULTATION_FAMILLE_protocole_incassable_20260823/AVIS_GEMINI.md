# AVIS GEMINI (task gemini.analyse · NaraRouter (7M tokens/jour gratuits) · 2026-08-23T18:08Z)

VERDICT : GO-AVEC-RÉSERVES

CONFIANCE : 74 %

HYPOTHÈSES :
1. « Incassable » doit être relu comme « aucune panne silencieuse tolérée au-delà d’un seuil défini », pas comme absence totale de panne.
2. La persistance est locale par fichiers ; il faut donc imposer single-writer, écriture atomique, checksum, mtime/sequence.
3. L’alerte doit rester locale ou peu coûteuse ; si elle dépend d’une API externe, elle crée une nouvelle panne possible.

CE QUI CHANGERAIT L’AVIS :
- Si plusieurs scripts peuvent écrire le même artefact sans verrou ni owner unique : bascule en NON.
- Si le label marché UP/DOWN/INDÉCIS et la fenêtre d’évaluation ne sont pas stabilisés : évaluation non fiable.
- Si les statuts réseau/API ne sont pas distingués : timeout, 404, rate-limit, réponse vide, SYN black-hole : détection incomplète.

AMÉLIORATION PROPOSÉE :
1. Ajouter un Health Controller indépendant : heartbeat signé par run avec seq monotone, hash, timestamp, durée, code de sortie, âge max des artefacts, quota d’appels, alerte si silence/stale/loop.
2. Imposer un contrat d’écriture : un seul writer par fichier, tmp+rename, manifest avec schema_version, seq, checksum, source_status ; lecteur refuse données trop vieilles ou sans manifest.
3. Évaluation honnête : séparer HIT/MISS/NO-TRADE/INDÉCIS, n_min par fenêtre, score uniquement si n suffisant, et test baseline/shuffle pour détecter les scores non prédictifs.

SYNTHÈSE :
La spec couvre bien les pannes réelles mais reste insuffisante contre écritures concurrentes, morts silencieuses et scores auto-justifiés.
Le point critique est la donnée : sans fraîcheur, intégrité et statut de source garantis, l’IA évaluera des artefacts.
Chaque brique doit produire des preuves : heartbeat, compteurs monotones, âge maximal, code d’erreur explicite.
L’évaluation doit refuser de conclure quand l’échantillon est faible ou le marché indécis.
Le protocole devient solide si ces garde-fous sont bloquants et audités automatiquement.
