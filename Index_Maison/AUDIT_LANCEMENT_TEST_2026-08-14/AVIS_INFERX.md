# INFERX — inferx.analyse

**INFERX [Famille ACE777] — Analyse logique et flux bas-niveau**

1. **Verdict global** : GO AVEC RÉSERVES (Le piège bash *stderr avalé / rc=1 silencieux* est identifié, mais la chaîne de scripts présente une incohérence critique entre les versions de lanceurs).

2. **Q1 (Lanceur)** : **c** — *Ajouter d'abord le crash dump à GEMINI_TEST, puis lancer avec GEMINI_TEST*. 
   *Justification* : Le run crashé du 13/08 tournait sur GEMINI_TEST ; pour obtenir la cause racine exacte sans biais, il faut reproduire le run dans les conditions exactes du crash tout en capturant le dump immédiat.

3. **Q2 (Champion)** : **a** — *RE-SCELLER af307996*. 
   *Justification* : Le trap ERR est validé par la famille pour diagnostiquer la mort silencieuse d'Alpha, et le diff prouve qu'aucune logique métier n'a été altérée.

4. **Q3 (Plan de retour)** : **oui** (avec réserve : s'assurer que le script obsolète `GO_VORTEX_V2` est explicitement neutralisé ou mis à jour pour éviter un refus bloquant au moment de l'appel).

5. **Amélioration concrète GO-sized** : 
   Avant le `bash` de lancement, exporter explicitement `BASH_XTRACEFD=7` et `exec 7>>runs/bash_trace_$(date +%s).log` couplé à un `set -x` dans le bloc d'init du lanceur. Cela garantit qu'aucune sous-shell silencieuse ne passera sous le radar si le trap ERR rate une exception non capturée par `pipefail`.
