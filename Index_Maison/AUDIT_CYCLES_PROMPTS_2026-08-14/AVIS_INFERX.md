# INFERX — inferx.analyse

**VERDICT GLOBAL** : **GO AVEC RÉSERVES** — Le setup trade (PnL positif) mais souffre d'un taux de bruit/zéro élevé et d'un risque de blocage des scripts bash par excès de complexité promptée.

---

### SUJET 1 — ANALYSE DES CYCLES

*   **S1-1. Verdict santé du setup : À SURVEILLER.**
    *   *Raison* : Le moteur génère du profit (`+2.65`), prouvant que la logique de déclenchement finale fonctionne, mais l'inactivité à ~0 (morte-saison algorithmique) montre un sous-dimensionnement de la sensibilité ou un filtre trop strict.
*   **S1-2. L'hypothèse de Christophe (« trop de décimales ~0 = pas bon signe ») est-elle fondée ?**
    *   *Oui, avec nuance.* Ce n'est pas un bug de calcul (les décimales sont mathématiquement valides), mais un **symptôme d'asphyxie du signal**. Avoir 60% à 80% des cycles à `tension=0.00000000` ou `momentum_too_small` indique que le seuil de déclenchement (gate) est trop haut pour la volatilité réelle du testnet, ou que la source de données est anémique.
*   **S1-3. Le filtre `wall_not_collapsed` rejette-t-il trop ?**
    *   *C'est un comportement voulu, mais mal calibré.* Des tensions à `0.74 – 0.97` rejetées signifient que le "mur" demande une condition trop absolue. 
    *   *Piste de réglage* : Introduire une dégradation temporelle du mur (decay) : si le mur résiste N cycles avec une tension $> 0.7$, la résistance s'érode pour permettre un fill avant le faux positif.
*   **S1-4. Amélioration GO-sized (Sujet 1)** :
    *   Implémenter un **Dynamic Dead-Zone Filter** en bash/python : si 5 cycles consécutifs affichent `momentum_too_small`, abaisser automatiquement le seuil de détection de 10% pour le cycle suivant, avec reset dès qu'un fill ou une tension $>0.5$ survient.

---

### SUJET 2 — CHAÎNE D'APPROBATION PAR PROMPTS

*   **S2-1. Verdict sur la proposition : GO AVEC RÉSERVES.**
    *   *Raison* : Graver des prompts canoniques dans le double coffre (Obsidian + GitHub) sécurise la traçabilité (règle maker ≠ checker respectée), mais alourdit le flux opérationnel si les scripts bash d'exécution ne valident pas automatiquement les prérequis.
*   **S2-2. Ce qui manque / à corriger dans le catalogue P1–P4** :
    *   Il manque un **chemin d'erreur explicite (rollback)** dans chaque prompt. Si un testnet plante (crash dump), quel prompt prend le relais ? Actuellement, le catalogue suppose un monde idéal. Ajouter systématiquement une clause `[EN CAS D'ÉCHEC : RESTORE <backup_id>]`.
*   **S2-3. Amélioration concrète de la chaîne (GO-sized)** :
    *   **L'automate de garde-fou Bash** : Interdire l'exécution du prompt P1 si le hash du commit GitHub et le dernier état de la note Obsidian ne sont pas strictement identiques (`git diff --exit-code`). Zéro exécution manuelle hors de la chaîne scriptée.
