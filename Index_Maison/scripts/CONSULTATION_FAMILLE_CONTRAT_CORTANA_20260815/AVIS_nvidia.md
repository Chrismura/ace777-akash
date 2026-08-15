# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 329.4s)

**AVIS (superviseur Buffy, 15/08/2026)**

---

### 1. Validation du schéma du contrat

**Corrections/ajouts obligatoires :**
- **Ajouter `"param_class"`** : `"threshold_multiplier"` (pour distinguer des paramètres de risque pur).
- **Ajouter `"expiry"`** : chaque proposition doit avoir une date d'expiration (ex. `"expiry": "2026-08-17T00:00:00Z"`). Une proposition sans expiration est un risque de dérive.
- **Ajouter `"session_id"`** : identifiant unique de la session Cortana (pour traçabilité et A/B testing).
- **Anti-gaming** : le moteur doit **ignorer** toute proposition avec `"confidence": "haute"` si le score global de Cortana < 60% (règle de sécurité absolue, indépendante du mode choisi).
- **Fail-safe** : si le fichier est corrompu ou absent → le moteur **gèle** les paramètres actuels (pas de valeurs par défaut silencieuses).

---

### 2. Trancher A, B, C

**A. Liste blanche + bornes (strictes) :**
| Paramètre | Borne min | Borne max | Justification |
|---|---|---|---|
| `DIP_FLOOR_MULT` | 0.85 | 1.15 | Ajustement fin, pas de révolution |
| `RIP_FLOOR_MULT` | 0.85 | 1.15 | Idem |
| `STOP_FLOOR_MULT` | 0.90 | 1.10 | Ne jamais trop serrer un stop |
| `NOTIONAL_USDT` | 0.90 | 1.10 | Taille de position, pas de levier agressif |

**Interdits absolus** : régimes, sense gates, kill-switch, structure des bags, cadences.

**B. Mode d'application (vu 44%) :**
**→ Mode (2) ADVISORY STRICT.**  
Cortana écrit ses propositions dans le JSON, le dashboard les affiche, mais **le moteur ne les applique PAS** tant que le score global < 60%.  
Exception : si un indice a un score ≥ 60% (ex. bassine 3/3), ses propositions sur CE sous-ensemble peuvent être appliquées en mode (1) avec clamp ±10%.  
**Justification** : à 44%, l'auto-application est un pari perdant. L'ADVISORY permet de collecter des données sans risque.

**C. Mesure d'impact (boucle d'apprentissage) :**
- **Log des overrides** : chaque proposition (appliquée ou non) est loggée avec timestamp, paramètre, valeur, et PnL de la fenêtre suivante (48h).
- **A/B par fenêtre glissante** : comparer le PnL des 48h après une proposition appliquée vs PnL des 48h sans proposition (baseline).
- **Métrique clé** : `delta_PnL_moyen` par indice. Si après 20 propositions, le delta est négatif ou nul → désactivation définitive de l'indice.

---

### 3. Risques précis

1. **Sur-apprentissage** : Cortana pourrait ajuster les seuils pour "plaire" au PnL court terme (ex. baisser `DIP_FLOOR_MULT` pour acheter plus tôt, ce qui gonfle le PnL sur 48h mais augmente le risque de bag). → Mitigation : borne stricte + mesure sur 48h uniquement.
2. **Dérive de confiance** : elle pourrait "apprendre" à proposer des valeurs extrêmes pour attirer l'attention. → Mitigation : toute proposition hors bornes est rejetée et loggée comme "anomalie".
3. **Bruit de marché** : à 44%, ses propositions sont quasi aléatoires. Le risque est de **suralimenter le dashboard** avec du bruit, noyant les vrais signaux. → Mitigation : limite de 3 propositions par cycle.

---

### VERDICT : **GO-AVEC-RÉSERVE**

**Précision** : GO pour le **contrat JSON** (structure, fail-safe, traçabilité) et le **mode ADVISORY**.  
**NO-GO** pour toute auto-application tant que le score global < 60%.

**CONFIANCE : 72%**

**HYPOTHÈSES :**
1. Le moteur Hulk est stable et ne sera pas modifié pendant la période de test.
2. Le PnL par fenêtre de 48h est une métrique fiable (pas de gaps MEXC majeurs).
3. Le dashboard peut afficher les propositions sans surcharge visuelle.

**CE QUI CHANGERAIT L'AVIS :**
- Si le score global passe ≥ 60% sur 2 semaines consécutives → passage en mode (1) auto-appliqué avec clamp ±20%.
- Si un indice atteint 80% de justesse sur 30 prédictions → activation auto-appliquée pour cet indice uniquement.
- Si le delta_PnL après 20 propositions est négatif → arrêt immédiat de l'ADVISORY.

**AMÉLIORATION PROPOSÉE :**
1. **Fenêtre de validation glissante** : ne considérer que les 30 dernières prédictions pour le score, pas le cumul historique (évite de traîner un mauvais passé).
2. **Double signature** : chaque proposition doit inclure un hash du contexte (régime actuel, funding, fearGreed) pour éviter les rejeux.
3. **Mode "silencieux"** : si Cortana propose 3 fois de suite la même valeur, elle est ignorée (anti-spam).

---

**SYNTHÈSE (5 lignes max) :**  
Contrat JSON validé avec ajouts (`expiry`, `session_id`, `param_class`). Mode ADVISORY strict (pas d'auto-application < 60%). Liste blanche limitée à 4 multiplicateurs avec bornes ±15%. Mesure d'impact par delta_PnL sur fenêtres de 48h, avec désactivation si négatif. GO-AVEC-RÉSERVE, confiance 72%.
