# AVIS DEEPSEEK (task deepseek.analyse · Google Gemini · 2026-09-01T07:32Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 85 %

HYPOTHÈSES :
1. Le satellite `satellite_aspiration.py` garantit l'atomicité de l'écriture de `aspiration_live.json` via un fichier temporaire + `os.replace()`, empêchant toute lecture de JSON corrompu par le moteur.
2. Le cockpit lit les états via `mission.json` ou `live.js` sans modifier l'état persistant du moteur, servant de simple vue de restitution.

CE QUI CHANGERAIT L'AVIS :
- Preuve dans le code que le fallback inline de `paper_diprip.py` effectue des appels bloquants ou surcharge l'API MEXC en cas de coupure prolongée du satellite.
- Divergence non résumée entre le calcul du cash du cockpit (`totCash`) et le solde réel persisté par le moteur.

AMÉLIORATION PROPOSÉE :
1. **Contrat de fraîcheur unique** : Extraire la logique de validation du seuil (>45 s) dans un utilitaire partagé minimal (ex. `hulk-mexc/utils/freshness.py`) consommé à la fois par `sante_index.py` et `paper_diprip.py` pour éliminer le risque de double sémantique (R2).
2. **Normalisation du schéma UI** : Imposer un dictionnaire de typage strict dans le moteur exporté dans le JSON d'état (`type: "trade_position" | "house_bag" | "seed_holding"`), interdisant au cockpit de deviner la sémantique (R3).
3. **Plafond de perte DCA (R6)** : Forcer un paramètre de stop absolu (ex: `-50%` du prix d'entrée initial) même pour les états `bag` pour éviter le risque d'enlisement infini.

SYNTHÈSE (5 lignes max)
Le moteur `paper_diprip.py` et son cockpit forment un ensemble cohérent mais souffrent de redondances de sémantique et de gestion du fallback. Le mode LIVE reste strictement interdit. Un GO-AVEC-RÉSERVES est accordé sous condition de centraliser la logique de fraîcheur du flux d'aspiration et de figer le schéma de données UI. Toute modification doit respecter les frontières strictes entre moteur, supervision et affichage.
