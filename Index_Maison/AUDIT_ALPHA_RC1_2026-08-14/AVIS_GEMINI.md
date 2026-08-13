# GEMINI — gemini.analyse

**1) Verdict sur le diagnostic : GO AVEC RÉSERVES**
*Raison :* Le piège `ERR` va attraper le coupable, mais l'hypothèse d'une commande isolée sous `set -e` ignore un angle mort : si le plantage survient à l'intérieur d'une boucle `while` ou d'un pipeline complexe, la ligne capturée pointera vers la structure globale et non vers la fonction interne défaillante. De plus, laisser Alpha mort transforme le run en "session à une jambe" pendant 2 heures, brisant la symétrie DUO.

**2) La commande la plus probablement fautive :**
Le mécanisme exact est un **appel `curl` ou un parseur JSON (Ruby/jq) encapsulé dans une substitution de commande (`x=$(...)`) ou une condition `if` sans `|| true` au sein d'une boucle d'ordre/fill**. 
*Scénario précis :* À 18:25:34, le cycle 81 (`shock_inversion_stop`) déclenche une requête API critique. Si l'API Binance/Testnet tousse (timeout de 5s ou HTTP 429/5xx), la fonction de récupération de position (`json_get` ou un helper de calcul de prix) renvoie un code de sortie non-zéro. Sous `set -e`, si cette commande est stockée dans une variable ou évaluée dans un test sans gestion d'erreur locale (`|| true` ou `|| fallback`), le script s'arrête net sans atteindre les blocs de journalisation `EXIT_ERROR` (qui sont protégés).

**3) Amélioration concrète (Stabilité / Architecture) :**
**Auto-réparation et supervision de niveau process (Supervisor Watchdog) :**
Ne pas modifier seulement le lanceur bash pour relancer bêtement, mais implémenter une **politique de ré-arrimage DUO** : 
Si le lanceur détecte la mort d'ALPHA (rc=1), il doit :
1. Tuer proprement BETA pour éviter une asymétrie de portefeuille (dé-risquage immédiat des deux jambes).
2. Tenter un `re-spawn` d'ALPHA avec un compteur de crash (max 3) *uniquement* si l'état du carnet le permet, ou relancer le DUO complet dans un état de repli. 
*Règle d'or ACE777 :* Pas de chasseur solitaire en production. Si le Hunter meurt, le Scout ne doit pas courir seul pendant 2 heures.
