# SPEC — Branchement ONCHAIN (baleines BTC) → Cortana + Ada (15/08/2026)

**Statut** : approuvée famille (GO-AVEC-RÉSERVE, gemini 75% / nvidia 72%) + arbitrage
supervision Buffy. **Zéro touche au moteur Hulk** — veille + contexte seulement.

---

## 1. Objectif

Brancher le scan onchain existant (`surveiller_whales.py`, mempool.space, 5 min) dans le
contexte de **Cortana** (analyse) et **Ada** (voilure), et **pérenniser** son lanceur
(plist launchd au lieu du daemon `/tmp` qui meurt au reboot).

## 2. Livrables

| Fichier | Rôle |
|---|---|
| `Index_Maison/scripts/pont_onchain.py` | Pont : lit le scan whales → injecte `onchain` dans `thermo/live.json` (atomique, idempotent) + synthèse textuelle pour Cortana |
| `Index_Maison/scripts/cortana_analyse.py` (modif) | Déclare la section onchain + synthèse dans son contexte (pas de clé numérique brute) |
| `Index_Maison/scripts/ada_gardienne.py` (modif) | Modulateur voilure ±10% basé sur `onchain_whaleCumul24hBtc` (seuil auto-appris) |
| `Index_Maison/plists/com.ace777.whales.plist` | Plist launchd StartInterval=300 (remplace le daemon /tmp) |

## 3. Pont — `pont_onchain.py`

Lit `data/whales_scan_latest.json` + `data/whales_mouvements.jsonl` (24h glissantes) →
injecte dans `thermo/live.json` une **sous-section `onchain`** (jamais dans le namespace racine) :

```json
"onchain": {
  "whaleBlocsN": 2,
  "whaleBlocsBtc": 2341.5,
  "whaleFragN": 1,
  "whaleFragBtc": 612.0,
  "whaleCumul24hBtc": 2953.5,
  "whaleDir": "outflow",
  "whaleSource": ["Binance hot wallet", "inconnu"],
  "whaleEcartSeuil": 12.5,
  "whaleAlerte": true,
  "whaleAlerteTexte": "2 gros blocs (2341.5 BTC) sortants vers Binance — pression vendeuse modérée",
  "dernierEvtMin": 3,
  "synthèse": "Tendance onchain : 2 gros blocs sortants vers Binance, pression vendeuse modérée."
}
```

- **`whaleDir`** : inflow / outflow / neutral selon les étiquettes de `whales.json`
  (entrée vers exchange étiqueté = inflow, sortie depuis exchange = outflow).
- **`whaleEcartSeuil`** : distance % du cumul au seuil de déclenchement (force du signal).
- **`dernierEvtMin`** : âge du dernier événement en minutes.
- **`synthèse`** : phrase pré-mâchée pour Cortana (elle ne reçoit PAS les chiffres bruts).
- **Écriture atomique** (mkstemp + os.replace), **kill-switch** respecté, **idempotent**,
  préserve toutes les autres clés de live.json.
- **Fenêtre 24h glissante** : cumul depuis `whales_mouvements.jsonl` (append-only).

## 4. Cortana — `cortana_analyse.py`

- Ajouter `onchain` dans le LEXIQUE (avec mention explicite « scan réel mempool — PAS le
  proxy aggTrades whaleN/whaleUsd » pour éviter le double comptage).
- **Injection TEXTUELLE** : le contexte reçoit `onchain.synthèse` + `onchain.whaleSource`
  + `onchain.whaleDir` (pas les chiffres bruts) — conformément verdict famille.
- Aucun changement de son mode de raisonnement ; le test A/B 7 jours sera mesuré par
  `score_justesse.py` (existant).

## 5. Ada — `ada_gardienne.py`

- **Modulateur** (pas déclencheur) : `facteur_onchain ∈ [0.8, 1.2]` appliqué à la voilure
  calculée par ailleurs.
- **Règle** : si `onchain_whaleCumul24hBtc > 2 × moyenne mobile 7j` (auto-apprise sur le
  journal) ET direction = outflow → facteur 0.92-0.95 (réduit voilure, pression vendeuse) ;
  si inflow massif → 1.05 max ; sinon 1.0.
- **Plafond ±10%** de la voilure — jamais de blocage, jamais de saut brutal (philosophie
  voilure continue).
- **Pondération** : le facteur ne compte que pour 5-10% du score global (poids faible).

## 6. Pérennisation — plist launchd

- `Index_Maison/plists/com.ace777.whales.plist` : `StartInterval=300`, Programme =
  `python3 Index_Maison/scripts/surveiller_whales.py --once` (le script écrit déjà son
  log propre). Logs : `/tmp/whales_launchd.log` + `.err`.
- **Avant installation** : arrêter proprement le daemon `/tmp/lancer_whales.py` (PID connu,
  double-fork) pour éviter le double scan (2 scans/5 min = I/O mempool doublé).
- **Installation** : `cp plist → ~/Library/LaunchAgents/` + `launchctl load`.

## 7. Tests (avant consignation)

1. `pont_onchain.py` : injecte la section onchain dans live.json, préserve les autres clés,
   idempotent (2 runs → pas de doublon), kill-switch respecté.
2. Cortana : le contexte contient la synthèse textuelle (pas les chiffres bruts).
3. Ada : facteur onchain appliqué (cas outflow cumul élevé → voilure réduite ≤10%),
   jamais de blocage.
4. Plist : `launchctl list | grep whales` → chargée ; daemon /tmp arrêté ; scan unique.

## 8. Réversibilité

- `rm` de `pont_onchain.py` + plist + `launchctl unload` → retour à l'état antérieur.
- Modifs cortana_analyse/ada_gardienne : diffs minimales documentées (rollback = inverse).
- Release Receipt à remplir à la fin.
