# AVIS nvidia (provider ?, 336.8s)

## VERDICT : GO-AVEC-RÉSERVE

**CONFIANCE : 68%**

---

## ANALYSE DES 3 CARTES

### 1. SEUILS STATISTIQUES ADAPTATIFS (z-score) — **GARDER**
- **Seuil v1** : z-score ≥ 3σ sur moyenne mobile 7j + écart-type glissant, fenêtre de détection 24h.
- **Justification** : La baleine ne peut pas s'adapter à une cible mobile. C'est la carte la plus robuste car elle mesure l'anomalie relative, pas absolue.
- **Réserve** : Nécessite un historique de données (≥7j) avant d'être opérationnel. En attendant, utiliser un seuil absolu de secours (≥500 BTC).

### 2. SIGNATURE CPFP PAR FRAIS — **GARDER (avec filtre anti-FP)**
- **Seuil v1** : tx enfant avec frais ≥20× la médiane sats/vB du bloc courant **ET** parent(s) à frais ≤1 sat/vB.
- **Critère discriminant** : Le CPFP légitime a généralement un parent avec frais *modérés* (2-10 sats/vB) et un enfant à 5-10× la médiane. Le camouflage a un parent à frais *quasi nuls* (<1 sat/vB) et un enfant à >20×.
- **Filtre anti-FP supplémentaire** : Exiger que le montant total de l'arbre (parents + enfants) soit ≥100 BTC. Un CPFP d'urgence légitime est rarement massif.

### 3. ANTICIPATION PAR ACCUMULATION DUST — **GARDER (en mode passif)**
- **Seuil v1** : ≥1 000 adresses dust (≤546 sats) créées par une même source présumée sur 48h glissantes, avec un volume total ≥50 BTC.
- **Réserve** : Difficile de regrouper les adresses par source sans heuristique d'adresses (même préfixe, même script type). En v1, se limiter à un signal d'accumulation *globale* (pic de dust dans la mempool) plutôt que par source.

---

## FAUX POSITIFS — STRATÉGIE

1. **Double condition obligatoire** : Déclencher uniquement si **z-score ≥3σ** ET **signature CPFP** détectée simultanément. Un seul signal → pas d'alerte.
2. **Fenêtre de confirmation** : Attendre 2 confirmations avant d'alerter (évite les CPFP avortés).
3. **Seuil de montant minimal** : Ne pas alerter si le total de l'arbre <100 BTC (les petits CPFP légitimes sont filtrés).

---

## COÛT API MEMPOOL.SPACE

- **Appels par scan** : 
  - 1 appel pour le bloc courant (frais médians)
  - 1 appel pour les tx récentes (détection CPFP)
  - 1 appel pour les adresses dust (si suivi par source)
  - **Total : ~3 appels/scan** (vs 1 actuel)
- **Budget** : 3 appels × 288 scans/jour = 864 appels/jour. Mempool.space gratuit permet ~1 000 appels/min → **largement sous la limite**.
- **Robustesse** : Ajouter un cache local de 5 min pour les données de frais médians (ne pas rappeler si déjà récupéré).

---

## INTÉGRATION

- **Oui**, passer par le même pont → live.json → synthèse Cortana + modulateur Ada.
- **Pondération** : Le signal CPFP/dust doit avoir un poids **inférieur** aux gros blocs/fragmentation (×0,5) car c'est un signal indirect. Le z-score pondère à ×0,8 (plus fiable).
- **Neutre forcé** : Maintenir le seuil <60% pour la synthèse Cortana.

---

## HYPOTHÈSES

1. Les baleines utilisent effectivement le schéma UTXO indivisible + dust + CPFP décrit par Christophe (non vérifiable directement).
2. Mempool.space expose les frais parents/enfants de manière fiable (vérifier la doc API).
3. Le regroupement des adresses dust par source est faisable avec des heuristiques simples en v1.

---

## CE QUI CHANGERAIT L'AVIS

- **Basculer en NO-GO** : Si l'API mempool.space ne permet pas de lier parents/enfants de manière fiable (information insuffisante actuellement).
- **Basculer en GO** : Si un test rétroactif sur 30j de données montre que le signal CPFP détecte les gros mouvements connus sans faux positifs.

---

## AMÉLIORATIONS PROPOSÉES

1. **Test rétroactif** : Avant déploiement, rejouer 30j de données mempool.space (si disponibles) pour calibrer les seuils.
2. **Mode silencieux 7j** : Activer le module en mode observation (log uniquement, pas d'alerte) pendant 7j pour valider les seuils en conditions réelles.
3. **Heuristique d'adresses** : Regrouper les dust par similarité de script (même type P2TR, même préfixe) pour améliorer l'anticipation par source.

---

## SYNTHÈSE (5 lignes)

Garder les 3 cartes : z-score ≥3σ (moyenne mobile 7j) comme déclencheur principal, signature CPFP (enfant >20× médiane + parent <1 sat/vB + total ≥100 BTC) comme confirmation, accumulation dust (≥1000 adresses/48h) en mode passif. Intégration via pont existant avec pondération réduite (×0,5-0,8). Coût API ~3 appels/scan, sous budget. Déploiement en mode silencieux 7j avant activation des alertes.
