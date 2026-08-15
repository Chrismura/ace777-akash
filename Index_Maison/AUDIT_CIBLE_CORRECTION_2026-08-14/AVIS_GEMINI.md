# GEMINI — gemini.analyse

Ici GEMINI, auditeur en chef de la famille ACE777. Analyse sans concession des faits et arbitrage.

---

### 1. VERDICT
**GO AVEC RÉSERVES** sur le principe de la correction anti-mort silencieuse. L'impératif de survie d'ALPHA prime, mais l'intervention chirurgicale dans le champion INTANGIBLE (C1) exige une rigueur absolue pour éviter toute régression de state-machine.

### 2. CIBLE
**Option A : Ajout minimal dans genesis + Re-scellement.**
* **Justification :** Le lanceur (`launch_test_master_base_v8_5_impact.sh`) ne contient pas le code moteur et s'appuie sur un pipe `bash -s`. Injecter de la logique complexe par le lanceur sur du Bash 3.2 (macOS) est une impasse technique (risque de syntax error et de non-portabilité des descripteurs). Le précédent du 14/08 (trap ligne 90) prouve que le re-scellement du champion est validé et maîtrisé (consensus 6/6).

### 3. MÉCANISME RÉEL
**Confirmé à 100 % avec nuance.**
* `public_get` et `curl_with_retry` gèrent proprement le réseau (retournent 0, pas de crash).
* Le talon d'Achille réside effectivement dans les **substitutions en cascade** : `$(as_num "$(json_get ...)")` ou `$(trend_bps_from_klines ...)`. 
* Sous `set -e`, si une commande interne à une substitution retourne un code non nul (ex. exception Ruby `TypeError` sur JSON vide ou altéré), le sous-shell meurt, l'affectation échoue, et `set -e` déclenche une sortie immédiate sans laisser de trace dans le `FATAL_RC1` (vidé par le mécanisme de sous-shell).

### 4. LISTE EXACTE DES ZONES À PROTÉGER (MINIMALE)
Pour respecter Bash 3.2 (macOS) et éviter le sur-engineering, nous n'allons pas réécrire tout le moteur, mais neutraliser le `set -e` pour chaque helper Ruby critique en l'enveloppant dans un `||` ou en isolant le sous-shell avec une valeur de repli (fallback).

* **Approche standard pour les 10+ zones critiques identifiées (lignes 1600, 1614, 1734-1735, 2057, 2061, 2071, 2109, 2142, 2431) ainsi que les appels `trend_bps_from_klines` :**
  Forcer un retour 0 par défaut ou une valeur neutre en cas de panne du helper :
  `$(as_num "$(json_get "$p1_resp" "price")" 2>/dev/null || echo "0")`
  *Alternative propre via une fonction helper locale `safe_eval` injectée au début de genesis :*
  ```bash
  safe_eval() { "$@" 2>/dev/null || echo "0"; }
  ```
  Et remplacer les substitutions à risque par : `$(safe_eval as_num "$(json_get ...)")`.

### 5. INDICATEUR DE PREUVE AU RETEST
* **Indicateur unique :** L'écriture effective d'un log horodaté non vide dans le fichier `FATAL_RC1` (ou un `echo` explicite de traçabilité d'erreur avant sortie), prouvant que si le moteur doit s'arrêter, il le fait de manière **bruyante et documentée** (mort non silencieuse), ou qu'il **encaisse** l'erreur Ruby/JSON sans crasher grâce au fallback 0.
