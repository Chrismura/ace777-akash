# 📡 PROTOCOLE DE CROISEMENT EXTERNE DES DONNÉES (29/08/2026, GO Christophe)

> Christophe : « beaucoup de décisions se prennent sur nos données, mais on a vu
> plusieurs fois qu'elles n'étaient pas correctes. Quand c'est important, il faut
> les croiser avec des données extérieures pour être sûr qu'elles sont bonnes. »
> Validé et implémenté le 29/08 17:45-17:55Z.

---

## LA RÈGLE DES 2 SOURCES

1. **Avant toute décision importante** (entrée portefeuille, alerte, changement
   de seuil) : vérifier le chiffre clé sur **au moins 1 source externe** (MEXC,
   Binance, CoinGecko, blockstream, mempool selon la donnée).
2. **Écart > 5 % entre notre prix et la source externe** → `data_quality_fail` :
   **on ne décide PAS**, on récupère d'abord.
3. **Registre** : chaque croisement (source externe + écart + verdict) est loggé
   dans `Index_Maison/data/croisement_externe.jsonl` pour audit.

## CE QUI EST CROISÉ (v1 — les 2 données les plus critiques pour Hulk)

| Donnée | Notre source | Source externe | Règle | Verdict |
|---|---|---|---|---|
| **PRIX** (la donnée critique d'exécution) | `hulk-mexc/runs/croisement_contexte.jsonl` (dernier par paire) | Ticker live **MEXC** (batch) + **Binance** (BTC/ETH) | écart > **5 %** → fail | **⛔ FAIL bloquant** (alerte data_quality) |
| **MURS** (ordre de grandeur) | `hulk-mexc/runs/murs_observations.json` (moyenne historique) | Profondeur **5 niveaux MEXC** (snapshot instantané) | ratio hors x0.05-x20 → warn | **⚠️ WARN informatif** (pas d'alerte) |

**Pourquoi les murs sont en warn et pas en fail** : notre mur moyen est une
moyenne historique (depuis le 16/08) et la profondeur externe est un snapshot
instantané. Le ratio varie naturellement de 0.1× à 200× quand le carnet se
déséquilibre (ex. 29/08 : bid BTC quasi vide 2 103 $ vs moyenne historique
356 k$). Ce n'est PAS une donnée corrompue, c'est le marché. Seul le prix
(qui détermine l'exécution) bloque.

## SORTIES

- **Registre** : `Index_Maison/data/croisement_externe.jsonl` (append, horodaté)
- **État récent** (pour le cockpit) : `Index_Maison/data/croisement_externe_etat.json`
- **Alerte** : `Index_Maison/data/alertes/ALERTE_data_quality.json` — écrite
  UNIQUEMENT si ≥ 1 fail PRIX (pas de fausse alerte), supprimée sinon

## EXÉCUTION

- Script : `Index_Maison/scripts/croiser_donnees_externes.py`
- Plist : `com.ace777.croisement-externe` (StartInterval 1800 = toutes les 30 min
  + RunAtLoad)
- Stdlib uniquement, fail-open (une API en panne ne casse pas les autres)

## TESTS EFFECTUÉS (29/08 15:53Z)

| Test | Résultat |
|---|---|
| Données réelles (20 vérifications) | ✅ 0 fail prix, 1-2 warns murs (carnet déséquilibré) |
| **Prix XRP corrompu ×10** (simulation) | ✅ **Détecté : écart 900,86 % → FAIL + alerte écrite** |
| Structure `top_murs` (paires dans la liste) | ✅ 10 paires croisées correctement |

## LES CAS VÉCUS QUI MOTIVENT CE PROTOCOLE

- **QAIT** : fichier réécrit en boucle → 66 M BTC impossibles (supply total ~19,7 M)
- **mempool.space down** (29/08) : sonde whales aveugle 2 h sans alerte
- **murs_observations** : structure `top_murs` mal lue au premier essai
- **Leçon appliquée** : toujours dédupliquer (par txid), vérifier la structure
  (top_murs), et maintenant croiser les prix avec une source externe.

## PROCHAINES ÉTAPES (proposées)

- Brancher l'état de croisement dans le cockpit (bulle data_quality)
- Ajouter le croisement des indicateurs on-chain (bloc privatisé vs blockstream)
- Élargir aux données funding/OI quand le Signal 1 sera branché

## Fichiers liés
- Script : `Index_Maison/scripts/croiser_donnees_externes.py`
- Plist : `Index_Maison/plists/com.ace777.croisement-externe.plist`
- Registre : `Index_Maison/data/croisement_externe.jsonl`
- Doc parent : `hulk-mexc/docs/POUSSIERE_INSTITUTIONNELLE_VISION_20260829.md`
  (section 5 — protocole proposé, maintenant implémenté)
