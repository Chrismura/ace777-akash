# AVIS GROK (task puter-grok.analyse · Google Gemini · 2026-08-29T18:40Z)

**VERDICT : GO-AVEC-RÉSERVES**
**CONFIANCE : 82 %**

**HYPOTHÈSES :**
1. La persistance de la liquidité sur les small caps de la famille ACE777 subit des chocs brutaux exogènes (ex: manipulation de carnet) qui violent l'hypothèse de stationnabilité sur 24h.
2. La plage UTC 02-06 est un artefact statistique historique chez nous, pas un plancher de marché réel, mais elle protège contre un bruit asiatique erratique.
3. La complexité d'une matrice de corrélation inter-paires en temps réel (Critique C) alourdit inutilement la stack actuelle sans bloquer l'exécution de base (14/14 OK).

---

### Analyse et Réponse aux Critiques de Cortana (Preuves à l'appui)

#### 1. Critique A (Fenêtre 24h = miroir rétroviseur) : **NERTES / NUANCE (Cortana a partiellement raison, mais sa solution est bancale)**
*   **Preuve terrain :** Nos données montrent que sur les small caps (ZBCNUSDT, n=57, spread 20.32), le $p_{30}$ sur 24h lisse correctement le bruit, mais sur une *Hulk*, la liquidité s'évapore en minutes. 
*   **Pourquoi Cortana se trompe en partie :** Remplacer le $p_{30}$-24h par un ATR pur ou une fenêtre trop courte sur des small caps ACE777 va créer des *faux positifs permanents* à cause des micro-spreads artificiels des bots de market making. 
*   **Notre proposition améliorée (Obligatoire) :** Ne faisons ni l'un ni l'autre. Passons sur une **fenêtre glissante hybride à 4h pondérée par l'ATR 15 minutes**. On garde un amortisseur court pour capter l'effondrement instantané tout en évitant le piège du 24h figé.

#### 2. Critique B (Plage horaire UTC 02-06 rigide) : **CORTANA A RAISON**
*   **Preuve terrain :** Fixer 02-06 UTC est une hérésie pragmatique. Le volume shift du dimanche soir ou les ouvertures de sessions asymétriques ne respectent pas une montre suisse. Les données de volume panier montrent des creux à 23h UTC ou 09h UTC selon les jours.
*   **Pourquoi Cortana a raison :** La plage rigide est un angle mort institutionnel. 
*   **Notre proposition améliorée (Obligatoire) :** Valider la proposition de Cortana (fenêtre de volume glissant 3h), mais avec un **seuil exact à −50 % vs la MM24h** (le −60 % de Cortana est trop strict et couperait des opportunités légitimes sur nos paires secondaires).

#### 3. Critique C (Entropie locale vs synchronicité inter-paires) : **CORTANA SE TROMPE (Trop théorique)**
*   **Preuve terrain :** Nos 14/14 chaînes tournent au cockpit. Ajouter une matrice de corrélation croisée des intervalles d'inter-arrivée en conditions réelles de prod va bouffer du CPU pour un gain marginal sur des small caps où la décorrélation est naturelle (chaque jeton a sa propre ferme de bots).
*   **Pourquoi Cortana se trompe :** C'est un modèle de grand fonds, pas de notre niveau opérationnel actuel. Le risque d'implémentation (latence, faux signaux de synchro) dépasse le bénéfice.
*   **Notre proposition améliorée (Obligatoire) :** Garder l'entropie temporelle locale actuelle (CV du carnet $\le$ 15% + bonus SAPI +0.10) mais y ajouter un **filtre simple de volume global panier** (si le volume total des 14 paires s'effondre de 40%, on double le poids du bonus).

---

### Tranchage final (Les 2 amendements)
*   **Appliquer l'amendement B (Volume glissant 3h à -50%) : OUI**, en remplacement du 02-06 UTC.
*   **Appliquer l'amendement A (ATR court terme) : OUI**, mais en version hybride 4h + ATR 15m, pas le $p_{30}$-24h pur de la famille ni le pur ATR de Cortana.
*   **Amendement C : REJETÉ.** Trop lourd, complexité injustifiée.

**CE QUI CHANGERAIT L'AVIS :** 
Une preuve par les logs de 48h montrant que le volume glissant génère plus de 15% de faux positifs par rapport au tunnel 02-06 actuel.

**SYNTHÈSE :**
Cortana pointe de vrais angles morts (le tunnel horaire fixe est absurde, le 24h est trop lent). Cependant, ses solutions pures manquent de pragmatisme pour nos small caps. On garde les corrections validées par la famille mais on injecte le volume glissant 3h (corrigé à −50 %) et un $p_{30}$ hybride 4h/ATR. On jette la corrélation inter-paires. Buffy ne touche à rien tant que ces deux subtilités ne sont pas actées.
