# VERDICT FAMILLE — Branchement ONCHAIN (baleines BTC) → Cortana + Ada (15/08/2026)

**Avis reçus** : gemini (75%), nvidia (72%) = 2/4 (openrouter 502 réseau, habituel).

## Verdict : GO-AVEC-RÉSERVE (convergent)

## 1. Pont dans live.json — VALIDÉ, avec cloisonnement strict
- **OUI** : injecter dans `live.json` (point de convergence Cortana/Ada déjà existant).
  Un fichier dédié créerait un 3ᵉ canal de lecture → désynchronisation.
- **Préfixe OBLIGATOIRE `onchain_*`** (pas `whale_*`) → évite la collision/confusion avec
  `whaleN`/`whaleUsd` (proxy aggTrades = dérivés/carnet, PAS le réel).
- **Regrouper sous une sous-section `onchain`** dans live.json (ne pas polluer le namespace racine).

## 2. Clés — validées + complétées
Base validée : blocs N, blocs BTC, frag N, frag BTC, direction, alerte.
**Ajouts demandés (convergents)** :
- `onchain_dernier_evt_min` : âge en minutes du dernier événement (fraîcheur → Cortana pondère)
- `onchain_whaleCumul24hBtc` : Σ BTC sur 24h glissantes (tendance, pas pic isolé → Ada)
- `onchain_whaleSource` : adresses étiquetées impliquées (ex. « Binance hot » vs « Genesis »)
- `onchain_whaleEcartSeuil` : distance % au seuil de déclenchement (force du signal → Ada)

## 3. ADA — modulateur, pas déclencheur (convergent)
- **Mécanisme** : `onchain_whaleCumul24hBtc` = **modulateur** de la voilure existante
  (multiplicateur/facteur de friction 0.8-1.2), PAS un déclencheur ni un blocage.
- **Pondération** : 5-10% du poids total (vs 40-50% price action) — plafond ±10% de la voilure.
- **Seuil auto-appris** : cumul > 2× moyenne mobile 7j → réduire voilure 5-8% (sortie
  exchange = pression vendeuse) ; sinon voilure normale. JAMAIS de blocage.
- Reste dans la philosophie : voilure continue, seuil X relatif auto-appris.

## 4. CORTANA — contexte pré-mâché, pas chiffres bruts (convergent)
- ⚠ À 44%, ajouter un indice NUMÉRIQUE brut brouillerait son signal (infobésité déjà
  présente sur funding/fearGreed).
- **Mode d'ajout** : synthèse TEXTUELLE pré-calculée par le pont
  (ex. « Tendance onchain : 2 gros blocs sortants vers Binance, pression vendeuse modérée »)
  + condition contextuelle dans le prompt (« si prix en range → lecture baissière »).
- **`onchain_whaleSource` + `onchain_whaleDir` = plus informatifs que funding/fearGreed**
  (événements discrets, pas du bruit continu) — nvidia.
- **Test A/B obligatoire** : justesse Cortana avec/sans onchain sur 7 jours avant activation
  définitive.

## 5. Pérennisation — IMPÉRATIVE (convergent)
- Remplacer le daemon `/tmp/lancer_whales.py` par une **plist launchd** (StartInterval=300)
  → survit aux reboots, visible launchctl, réversible.

## Améliorations captées
1. **Log de corrélation** : corrélation quotidienne `onchain_whaleCumul24hBtc` vs prix 4h
   plus tard → ajuster la pondération Ada dynamiquement — nvidia.
2. **Alerte visuelle terminal** : afficher source + montant en clair (pas seulement booléen) — nvidia.
3. **Vérification étiquettes 48h** avant GO plein (fiabilité ≥90% requise) — nvidia.

## Décision Buffy (supervision)
- Design validé tel quel avec les ajouts (cumul 24h, source, écart seuil, fraîcheur).
- **Ada** : modulateur plafonné ±10%, seuil auto-appris — conforme philosophie.
- **Cortana** : injection TEXTUELLE pré-mâchée (pas de clé numérique brute dans son prompt),
  A/B 7 jours avant activation.
- **Pérennisation** : plist launchd — la priorité (daemon /tmp = mort au reboot).
- Chantier = connaissance/veille, zéro touche moteur Hulk → réversible.
