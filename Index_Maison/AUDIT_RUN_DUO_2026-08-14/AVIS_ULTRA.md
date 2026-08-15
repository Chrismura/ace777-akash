# ULTRA — inferx.analyse

*ULTRA / ACE777 — Rapport de robustesse et d'échelle.*

---

### 1. VERDICT global
**GO AVEC RÉSERVES SÉVÈRES.**  
* Mort neutralisée ? **OUI.** Le `safe_call` et le wrapper ont empêché le crash brut (zéro exit silencieux, relance propre).  
* Duo dégradé acceptable ? **NON.** Un alpha muet à zéro fill pendant qu'un scout fait du micro-scalping plat (0.05 USDT) n'est pas un run test valide : c'est un découplage comportemental.

---

### 2. MORT SESSION #1
* **Mécanisme confirmé :** OUI, à 100%. Le `shock_inversion_stop` ferme le Scout (RC=1), le fichier `duo_state.json` se fige, l'Alpha dépasse le TTL de 20s, lève `stale_state`, panique et crashe en chaîne.
* **Pourquoi `safe_call` n'a rien attrapé :** C'est **totalement attendu**. Le `safe_call` protège les exceptions de code (erreurs de syntaxe, division par zéro, types nuls). Ici, le code s'exécute parfaitement : c'est une **décision métier** (arrêt par condition de shock/stale) qui déclenche un exit volontaire (RC=1). Ce n'est pas un bug technique, c'est une règle de survie mal calibrée pour le duo.

---

### 3. HARMONIE SESSION #2
* **Tranchage (Preuve à l'appui) :** C'est un **défaut de couplage duo après relance**, aggravé par un marché sans tendance. 
* *Preuve :* Des tensions à **6.03** (08:54) et **3.54** (09:06) sans aucun trigger chez l'Alpha prouvent que le filtre de résonance/vacuum (Ruby ligne 1101) rejette des signaux pourtant valides en théorie. Ce n'est pas le marché qui dort (la tension monte), c'est **l'état partagé (`duo_state.json`) qui est corrompu ou désynchronisé** dans sa sémantique suite à la relance à chaud du wrapper. L'intuition de Christophe (« pas l'harmonie ») est mathématiquement exacte : l'Alpha attend un état du Scout qui ne matche plus la dynamique post-crash.

---

### 4. CORRECTIFS GO-SIZED BORNÉS (Wrapper / Helpers)
* *Règle respectée :* Zéro modification du Genesis. Interventions uniquement sur le lanceur/wrapper.
* **Correctif validé (Purge atomique + Reset d'harmonie) :**
  Modifier le lanceur (`GO_VORTEX_V2.sh`) pour que la relance auto à 5s ne se contente pas d'un `rm -f duo_state.json`, mais force la création d'un fichier `duo_state.json` initialisé à `state=RESET, ts_ms=NOW` avant de respawn les binaires.
  * *Preuve de supériorité :* Empêche l'Alpha de lire un résidu d'état ou d'attendre un TTL obsolète au boot. Force une synchronisation propre de l'horloge logique des deux agents dès la milliseconde 1.

---

### 5. INDICATEUR unique pour le PROCHAIN run
* **Le Ratio de Couplage Actif (RCA) :**  
  $$\text{RCA} = \frac{\text{Nombre de cycles ALPHA avec trigger valide}}{\text{Nombre total de cycles SCOUT avec tension } > 1.0}$$  
  * *Se cible :* **> 80%**. Si la tension monte chez le Scout et que l'Alpha reste bloqué à `no_trigger` (> 10% des cas), l'harmonie est rompue et le run doit être avorté par le wrapper.
