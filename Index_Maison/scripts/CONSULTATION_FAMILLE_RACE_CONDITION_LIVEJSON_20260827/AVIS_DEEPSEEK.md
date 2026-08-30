# AVIS DEEPSEEK (task deepseek.analyse · Google Gemini · 2026-08-27T19:19Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 85 %

HYPOTHÈSES :
1. Le SafeLiveWriter actuel utilise un renommage atomique POSIX (`os.replace`) mais effectue une lecture-modification-écriture (RMW) en mémoire sans verrou inter-processus global (fcntl/flock), ce qui permet à deux processus d'écraser leurs modifications respectives.
2. Les 36 scripts lecteurs lisent de manière asynchrone et supportent un fichier temporaire ou un verrou de lecture partagé, à condition que le fichier cible ne soit jamais partiellement écrit.

CE QUI CHANGERAIT L'AVIS :
La preuve par le code que `SafeLiveWriter` implémente déjà un verrou exclusif multi-processus (`fcntl.flock(fd, fcntl.LOCK_EX)`) et que la corruption du 27/08 provient d'une autre cause (ex: troncature manuelle ou exception non gérée vidant le dictionnaire avant l'écriture).

AMÉLIORATION PROPOSÉE :
1. **Architecture Bus/IPC asynchrone (Propositions ACE777)** : Au lieu d'écrire tous dans un unique fichier JSON partagé, chaque producteur (thermo, onchain, sous-ensemble 11 clés) écrit son propre fragment validé dans un répertoire `thermo/fragments/` de manière atomique. Un daemon central unique (ou le lecteur principal) assemble le payload final de 64 clés à la volée.
2. **Verrouillage exclusif strict (fcntl)** : Forcer l'utilisation d'un fichier de verrou (`thermo/live.json.lock`) via le module `fcntl` natif de Python pour tout accès en écriture (lecture-fusion-écriture atomique), interdisant à un écrivain partiel de supprimer des clés qu'il ne possède pas dans son scope déclaré.

SYNTHÈSE :
La race condition est avérée par la suppression de 53 clés le 27/08. Un écrivain partiel ne doit jamais remplacer le payload global. Le fix structurel exige un verrouillage inter-processus obligatoire (`fcntl`) et un schéma de fusion ensembliste interdisant la suppression de clés absentes du payload entrant. L'approche fragments isolés élimine définitivement ce risque.
