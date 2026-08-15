# VERDICT FAMILLE — Architecture Hulk « portefeuille intelligent » (15/08/2026)

**Consultation** : `consulter_famille_hulk_architecture_20260815.py`
**Avis reçus** : gemini (90%), nvidia (78%) = **2/4**.
**Manquants** : openrouter-juge + openrouter-ultra → **HTTP 502 répété** (provider injoignable via le hub, contrainte réseau WiFi/alpage). Pas re-demandé — même cause racine que le chantier Hulk lui-même.

---

## Verdict convergent : GO-AVEC-RÉSERVE (confiance 78-90%)

Les 2 modèles disponibles **convergent fortement**, sans divergence de fond.

### 1. Architecture 2 étages — VALIDÉE (les 2)
Moteur déterministe (exécution, ordres) + Cortana (cerveau, paramétrage, hors boucle d'ordre) = la bonne séparation, conforme à la doctrine C2/C3. **Aucun LLM dans la boucle d'ordre.**

### 2. Transposition du moteur ACE — ÉCARTÉE (les 2, unanime)
Transposer le champion (scalper futures BTC à levier x5→x13, revenge 6s) sur du spot small-cap = **non-sens technique et financier**. Hulk doit rester un **moteur dédié spot** reprenant la **philosophie** du champion (radar/sense/prudence), déjà empruntée. → La question « moteur champion pour Hulk » est **tranchée : non, garder Hulk dédié**.

### 3. Ordre des chantiers (convergent)
1. **Veille robuste** (trou n°1) — vital, sinon le moteur est aveugle. Timeout strict + back-off exponentiel + circuit-breaker + fallback STANDBY.
2. **Kill-switch déterministe global** + **mode îlot dégradé hors-ligne** (STANDBY/OFFLINE_SAFE par défaut) — étage manquant identifié par nvidia (le système reste en WATCH sans protection explicite).
3. **Brancher Cortana** (trou n°2) — pilote de paramètres, une fois veille fiable + kill-switch en place.

---

## Améliorations proposées (captées pour le chantier)

| # | Source | Amélioration |
|---|---|---|
| 1 | gemini+nvidia | **Mode îlot dégradé** `OFFLINE_SAFE`/`STANDBY` par défaut : si veille muette, le moteur gère ses bags en autonomie pure (carnet d'ordres local), sans dépendre des digests extérieurs. |
| 2 | nvidia | **Kill-switch déterministe global** : arrêt total des ordres si réseau dégradé ou veille muette > X heures. |
| 3 | nvidia | **Journal de bord local JSON** écrit à chaque décision, lisible par Cortana → reprise après coupure. Cortana en « conseil différé » à la reconnexion. |
| 4 | nvidia | **Seuil de dégradation** : veille muette > 6h → STANDBY auto + vente des 3 positions les plus volatiles. |
| 5 | gemini | **Contrat d'interface JSON/config** entre Cortana et le moteur (pas de modif directe hasardeuse des variables). |
| 6 | gemini | **Ada = voilure macro** (risque global selon état connexion/marché). |

---

## Réserves qui conditionnent le GO

- **gemini** : vérifier que `paper_diprip.py` fonctionne en autonomie locale **sans** `VEILLE_ALERT.md` (si non → revoir avant tout).
- **nvidia** : un test réel montrant des bugs de logique moteur (pas seulement réseau) → basculer NO-GO, revoir le moteur d'abord.

---

## Décision Buffy (supervision)

Le cadrage est validé. Prochain pas = **chantier n°1 : veille Hulk robuste au réseau** (timeout + back-off + circuit-breaker + fallback STANDBY), qui inclut aussi la réserve gemini (vérifier l'autonomie locale du moteur). Le kill-switch (nvidia) sera intégré au même chantier ou au suivant, avant tout branchement de Cortana.
