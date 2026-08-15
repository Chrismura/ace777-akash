# VERDICT FAMILLE — Contrat JSON Cortana ↔ moteur Hulk (15/08/2026)

**Avis reçus** : gemini (85%), nvidia (72%) = 2/4 (openrouter 502, réseau).

## Verdict : GO-AVEC-RÉSERVE (convergent) — ADVISORY STRICT
GO pour le **contrat JSON** (structure, fail-safe, traçabilité) + **mode ADVISORY**.
**NO-GO pour toute auto-application tant que le score global de Cortana < 60%** (à 44%, l'auto-application détériore mathématiquement l'espérance).

## A. Liste blanche + bornes (convergent)
| Paramètre | Bornes | Note |
|---|---|---|
| DIP_FLOOR_MULT | [0.85, 1.15] | ajustement fin |
| RIP_FLOOR_MULT | [0.85, 1.15] | idem |
| STOP_FLOOR_MULT | [0.90, 1.10] | ne jamais trop serrer un stop |
| NOTIONAL_MULT | [0.90, 1.10] | taille de position, pas de levier agressif |

**Interdits absolus** : régimes, sense gates, kill-switch, structure des bags, cadences.

## B. Mode d'application (vu 44%)
- **ADVISORY pur** : Cortana écrit le JSON → dashboard l'affiche → le moteur **ignore** les valeurs pour l'exécution tant que justesse < 60%.
- Exception nvidia : un indice à ≥60% (ex. bassine 3/3) peut être appliqué sur CE sous-ensemble avec clamp ±10%.

## C. Mesure d'impact (boucle d'apprentissage)
- Log de chaque proposition (appliquée ou non) : ts, param, valeur, + PnL de la fenêtre suivante (48h).
- A/B par fenêtres glissantes : delta_PnL par indice → si négatif après ~20 propositions → désactivation.
- (nvidia) score = fenêtre glissante des 30 dernières prédictions (pas le cumul historique).

## Schéma du contrat (corrigé famille)
```
{
  "ts": "...", "source": "cortana", "session_id": "...",
  "cortana_accuracy_score": 0.44,          # rappel du score au moment de l'écriture
  "enforced_mode": "ADVISORY",             # ADVISORY | AUTO
  "proposals": [
    {"param": "DIP_FLOOR_MULT", "param_class": "threshold_multiplier", "value": 0.85,
     "confidence": "moyenne", "reason": "...", "horizon": "48h", "expiry": "2026-08-17T00:00:00Z"}
  ]
}
```
**Anti-gaming** : max 1 modif/param/6h · confidence « haute » ignorée si score<60% · `expiry` obligatoire · `hash`/checksum anti-corruption · fail-safe = fichier absent/corrompu → **geler les paramètres actuels** (pas de défaut silencieux).

## Décision Buffy (supervision)
v1 = le contrat existe, Cortana écrit via un helper, le moteur lit/valide/log (traçabilité + données shadow pour A/B) mais **n'applique rien < 60%**. Le chemin d'application (clamp) sera ajouté quand elle dépassera 60% durablement. C'est la voie « zéro faute » : ne jamais être confiante à tort.
