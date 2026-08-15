# AVIS gemini (provider Google Gemini, 7.6s)

### F1 — Réparer la justesse

* **Technique :** Faisabilité totale sur Mac Air 8 Go (scripts Python purs, `score_justesse.py`, manipulation de CSV). Risque faible de casser un consommateur si les sorties JSON/CSV conservent la même structure de clés. Nécessite de réécrire la logique de cross-référence (comparer funding/fearGreed à leur propre historique et non au BTC brut) et d'intégrer l'état `NEUTRE`.
* **Impact :** Restaure la crédibilité des métriques de l'équipe. Finit l'illusion d'une performance biaisée par un simple mouvement directionnel du Bitcoin.
* **Risque/Sécurité :** Zéro impact trading (lecture seule, évaluation a posteriori des analyses). Respecte totalement C2/C3.
* **Ordre de priorité :** À traiter en priorité absolue (le fondement de toute optimisation future repose sur une vérité mesurée correcte).

**VERDICT :** GO  
**CONFIANCE :** 98 %  
**HYPOTHÈSES :** 
1. Les historiques CSV contiennent assez de granularité pour calculer l'évolution propre de chaque indice.
2. Aucun script critique de reporting externe ne dépend strictement du bug actuel du score de justesse.  
**CE QUI CHANGERAIT L'AVIS :** Découverte que les indices non-BTC ne disposent pas d'historique séquentiel exploitable dans les CSV actuels.  
**AMÉLIORATION PROPOSÉE :** 
1. Ajouter un journal d'audit distinct pour les faux positifs dus au seuil de 0,3 %.  
2. Formaliser explicitement la définition mathématique du `NEUTRE` dans un fichier de config séparé.

---

### F2 — Carte d'identité ACE777

* **Technique :** Faisabilité immédiate (création d'un fichier canonique markdown/JSON + injection dans les prompts système au boot). Zéro impact matériel sur 8 Go.
* **Impact :** Aligne tous les acteurs sur la même vision (carrosserie, moteur, philosophie, limites). Évite les dérives comportementales des modèles.
* **Risque/Sécurité :** Totalement sécurisé. Ne touche ni aux ordres ni au code d'exécution (pur niveau prompt/documentation).
* **Ordre de priorité :** Immédiat (doit précéder ou accompagner F3, F4 et F5 pour fixer le cadre sémantique).

**VERDICT :** GO  
**CONFIANCE :** 100 %  
**HYPOTHÈSES :** 
1. Les acteurs IA supportent l'injection de ce prompt canon sans saturer leur contexte limité.
2. Le GO humain validera le contenu textuel de la carte d'identité avant déploiement.  
**CE QUI CHANGERAIT L'AVIS :** Incompatibilité technique des modèles locaux (Ollama/Qwen) avec la taille du prompt canon unifié.  
**AMÉLIORATION PROPOSÉE :** 
1. Versionner la carte d'identité avec un hash SHA-256 dans les logs de démarrage pour garantir qu'aucune modification non autorisée n'a eu lieu.

---

### F3 — Cortana = dashboard

* **Technique :** Extension de `cortana_analyse.py` pour ingérer les formats CSV des fills ACE et des runs paper de Hulk. Faisable en Python natif sur 8 Go. Demande un nettoyage de la voix pour centraliser sur le hub.
* **Impact :** Donne enfin à Cortana une vue globale (trading + market) au lieu d'une focalisation aveugle sur le BTC, tout en consolidant son rôle exclusif de dashboard.
* **Risque/Sécurité :** Lecture seule stricte. Aucun pont vers l'exécution (respecte C2/C3).
* **Ordre de priorité :** Second (juste après F1 et F2).

**VERDICT :** GO-AVEC-RÉSERVE *(Réserve : s'assurer que l'unification de la voix sur le hub ne crée pas de goulet d'étranglement mémoire sur le Mac Air 8 Go lors des pics d'analyse)*  
**CONFIANCE :** 90 %  
**HYPOTHÈSES :** 
1. Les formats de fichiers CSV des fills ACE et de Hulk sont normalisés et lisibles par les scripts de Cortana.
2. Le hub gère proprement le routage des requêtes de Cortana sans latence excessive.  
**CE QUI CHANGERAIT L'AVIS :** Impossibilité technique de faire cohabiter les flux de données ACE/Hulk dans le script d'analyse sans saturer la RAM du Mac Air.  
**AMÉLIORATION PROPOSÉE :** 
1. Mettre en place une rotation/nettoyage automatique des anciens rapports CSV de Cortana pour préserver l'espace disque et la mémoire vive.

---

### F4 — Un seul aiguilleur

* **Technique :** Nettoyage du code Rust (`brain.rs`) pour supprimer les logiques parallèles (Gemini/Ollama) et forcer le passage exclusif par le hub (`routing.json`). Faisable, allège le binaire et le code.
* **Impact :** Supprime la redondance, clarifie l'architecture, élimine les comportements imprévisibles du moteur de décision.
* **Risque/Sécurité :** Critique car touche au code Rust central. Risque de coupure si le repli hors-ligne est mal implémenté. Doit conserver impérativement le mode dégradé hors-ligne.
* **Ordre de priorité :** Troisième (après la mise en place de la vérité et de l'identité).

**VERDICT :** GO-AVEC-RÉSERVE *(Réserve : le mécanisme de repli hors-ligne en Rust doit être rigoureusement testé avant suppression de l'ancienne logique pour éviter un blocage total en cas de panne du hub)*  
**CONFIANCE :** 85 %  
**HYPOTHÈSES :** 
1. Le hub est suffisamment robuste pour assumer 100% du routage sans l'aide des anciennes fonctions locales de `brain.rs`.
2. Le fichier `app.toml` peut être mis à jour proprement sans casser les dépendances de compilation Rust.  
**CE QUI CHANGERAIT L'AVIS :** Instabilité avérée du hub lors des tests de charge en conditions réelles.  
**AMÉLIORATION PROPOSÉE :** 
1. Implémenter un test unitaire en Rust simulant la panne du hub pour valider le basculement sur le repli hors-ligne.

---

### F5 — Nettoyer le prompt voix

* **Technique :** Édition simple de `persona.rs` (ou équivalent) pour purger toute mention d'exécution d'ordres Binance et y injecter la carte d'identité (F2) et le rôle dashboard (F3). Zéro risque technique.
* **Impact :** Aligne le discours de l'IA sur la stricte réalité réglementaire et architecturale (zéro ordre, dashboard pur). Supprime toute ambiguïté de persona.
* **Risque/Sécurité :** Renforce la sécurité en éliminant toute velléité d'autonomie non validée. Respecte à la lettre C2/C3 et le GO humain.
* **Ordre de priorité :** Quatrième (en coordination étroite avec F2 et F3).

**VERDICT :** GO  
**CONFIANCE :** 100 %  
**HYPOTHÈSES :** 
1. Aucun script dépendant ne lit les anciennes instructions obsolètes du persona vocal pour prendre des décisions.  
**CE QUI CHANGERAIT L'AVIS :** Aucun fait plausible (opération purement cosmétique et sécurisante).  
**AMÉLIORATION PROPOSÉE :** 
1. Ajouter une assertion dans les tests de démarrage vérifiant l'absence des mots-clés interdits (« exécute », « ordres », « Binance ») dans le prompt actif de Cortana.

---

### SYNTHÈSE
* **Ordre d'exécution recommandé :** F1 (vérité des scores) → F2 (carte d'identité) → F3 (dashboard unifié) → F4 (aiguilleur unique Rust) → F5 (nettoyage prompt voix).
* **Risque n°1 :** Une rupture du mécanisme de repli hors-ligne dans le code Rust (F4) lors de la centralisation sur le hub, menaçant la continuité de surveillance du cockpit sur les 8 Go.
