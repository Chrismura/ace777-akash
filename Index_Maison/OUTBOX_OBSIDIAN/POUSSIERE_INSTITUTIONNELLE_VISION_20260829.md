# 🧪 POUSSIÈRE INSTITUTIONNELLE — LA VISION DE CORTANA, EXPLIQUÉE ET VALIDÉE (29/08/2026)

> Demande Christophe : « approfondir la poussière institutionnelle, on doit comprendre
> effectivement ce que Cortana a comme vision. »
> Session Cortana : `poussiere-20260829-152854` (4 tours, archivée onglet VOL).
> Script : `Index_Maison/scripts/ask_cortana_poussiere_institutionnelle.py`.

---

## 1. LA VISION DE CORTANA (ce qu'elle veut dire exactement)

### La définition (tour 1) — le point clé
> « La poussière institutionnelle n'a RIEN à voir avec le bruit de fond du réseau
> (Ordinals, spam de runes, micro-dust du retail). C'est une **arme de dissimulation
> algorithmique**. »

| | Poussière RETAIL (organique) | Poussière INSTITUTIONNELLE (camouflage UTXO fracturé) |
|---|---|---|
| Nature | Bruit naturel : frais bas, mints NFT, consolidations perso | **Artéfact stratégique** : un gros acteur fragmente des milliers de BTC |
| Distribution | Loi de Poisson, sans intentionnalité macro | Arbre de micro-tx à frais quasi nuls, invisibles au fond de la mempool |
| But | Usage (transfert, mint, consolidation) | **Traverser les seuils de surveillance** (≥ 1 000 BTC) sans être vu |

### Les 4 mécanismes classés par fiabilité de détection (tour 1)

| # | Mécanisme | Fiabilité | Comment le détecter |
|---|---|---|---|
| 1 | **Fragmentation UTXO + CPFP** (enfant à frais payants) | 🟢 TRÈS HAUTE | Pic de frais combiné à une anomalie d'entropie — inaltérable |
| 2 | **Injection par blocs privatisés** (MEV / relays off-market) | 🟢 HAUTE | `taux_fantome` (tx jamais vues dans la mempool publique) |
| 3 | **Leurre faux transferts Cold→Hot** (vendredi soir/week-end) | 🟡 MOYENNE | Divergence volume on-chain vs inertie du carnet spot |
| 4 | **Spoofing d'ordre profond & fragmentation OTC** | 🔴 FAIBLE | Difficile à isoler du bruit macro |

### La FORMULE SAPI (Score d'Alerte Poussière Institutionnelle, tour 1)
```
SAPI = I(z_fee > 2.0) × 0.35
     + min(1, poussiere_taux_fantome / 0.15) × 0.30
     + I(ipt.micro_tx_ratio > seuil_historique) × 0.20
     − min(1, |Δspot_book| × 10) × 0.15
Alerte critique : SAPI ≥ 0.75 ET volume_btc ≥ 500
```

### L'autocritique (tour 2) — les fausses alarmes de SA propre vision
Cortana reconnaît 3 biais (la leçon DATUM est intégrée) :
1. **Tout pic de `taux_fantome` n'est PAS de la manipulation** (le minage DATUM
   structurel fait 12 % de base — on l'a appris le 29/08).
2. **Les consolidations internes d'exchanges** (Binance hot→cold 45 910 BTC,
   Bitbank 20 755 BTC) sont des **routines de trésorerie**, pas des ventes.
3. **Plaquer des modèles de grands indices sur nos small caps fausse l'IPT**
   (liquidité squelettique).

Ses 3 améliorations : z-score adaptatif du taux_fantome vs médiane mobile 7j
(< 2σ = ignoré) · couplage obligatoire avec `spot_book_delta` (on-chain affolé +
carnet plat = bruit technique) · normaliser le volume par le volume médian
quotidien de l'actif (petites caps).

### Le mécanisme inédit (tour 3) — Time-Decay Dusting
> « L'institution ne fragmente pas ses UTXO en une fois : elle programme une
> **émission fractionnaire sur 48-72h**, mimant le bruit brownien d'une cohorte
> d'utilisateurs (Asie, Europe, US). Elle détruit l'unicité du pic de volume. »

**Signature à coder en premier** : le **SESM** (Ratio d'Entropie Séquentielle des
Micro-Lots) — constance anormale du coefficient de variation des frais d'une
grappe d'adresses non liées + `sdi` qui monte alors que le volume brut reste plat.

### Le détail que tout le monde rate (tour 4) — LE RBF PLAT ⭐
> « Un volume élevé de micro-transactions avec un taux de RBF **anormalement bas**
> = l'émetteur connaît PAR AVANCE les frais exacts (au satoshi près). Le retail,
> lui, tatone et utilise massivement le RBF pour corriger ses erreurs. »

**L'absence de RBF sur un volume massif de micro-tx = signature d'un script
algorithmique déterministe** (exécution industrielle planifiée).

---

## 2. LA VALIDATION PAR NOS DONNÉES (faite par Buffy, 29/08 17:20Z)

### ✅ Le RBF plat est CONFIRMÉ (la signature du tour 4)
Test sur **13 933 points uniques** de `runs/croisement_contexte.jsonl` (25 017 lignes) :

| Mesure | Valeur |
|---|---|
| **Corrélation (micro_tx_ratio, rbf_score)** | **−0.275** (négative, significative) |
| rbf_score moyen quand micro_tx ≥ 0.5 | **0.286** (n=4 403) |
| rbf_score moyen quand micro_tx < 0.5 | **0.599** (n=9 530) |

→ **Quand les micro-transactions montent, le RBF s'effondre.** C'est EXACTEMENT ce
que Cortana prédit : les gros flux fragmentés ne tatent pas leurs frais (ils les
connaissent), le retail oui. **La signature est réelle dans nos données.**

### ✅ Le SAPI a ANTICIPÉ l'événement majeur de 2h
- **28/08 17:25Z** : SAPI = **0.85** (z_fee=3.0, micro_tx=0.6, taux_fantome=35.2 %) → 23 points ≥ 0.75 sur 13 933 (0,16 % — rare, ciblé)
- **28/08 19:14Z** : alerte bloc privatisé **90,9 %** (3 978 tx cachées, 555 BTC)

→ Le signal de poussière institutionnelle s'est allumé **~2h AVANT** le pic de
blocs privatisés massifs. L'alerte existante `ALERTE_poussiere_haute.json`
(29/08 00:11Z) confirme : « la mempool se remplit de micro transactions, sans
signature CPFP pour l'instant. »

### ⚠️ Les limites (honnêteté)
- Le signal est **réseau-global** (répliqué sur toutes les paires dans
  croisement_contexte) → il ne dit PAS quelle paire est ciblée, seulement que la
  mempool « s'arme ».
- Il manque le `spot_book_delta` en continu (le terme qui déclasserait les faux
  positifs) et le z-score du délai de minage → à ajouter pour la version complète.

---

## 3. CE QUE ÇA CHANGE POUR NOUS (le couplage avec le Signal 3)

La poussière institutionnelle est le **signal 24-48h** (accumulation/distribution
masquée). Le **Signal 3 (livre écorché)** est le **signal minutes-heures** (trou
d'air dans le carnet). Les deux se complètent :
- **Poussière (on-chain)** → l'acteur DÉPLACE ses pions → prépare un mouvement
- **Livre écorché (carnet)** → le mouvement ARRIVE → vacuuming

**Le codage prioritaire (validé Christophe, fait par le codeur le 29/08)** :
le Signal 3 dans `hulk-mexc/scripts/signal3_livre_ecorche.py` (déjà opérationnel,
plist `com.ace777.signal3-livre-ecorche` toutes les 30 min). Le SAPI poussière
reste un indicateur de veille 24-48h à coder ensuite (il manque 2 champs).

---

## Fichiers liés
- Session Cortana : `poussiere-20260829-152854` (4 tours, onglet VOL)
- Script : `Index_Maison/scripts/ask_cortana_poussiere_institutionnelle.py`
- Données : `hulk-mexc/runs/croisement_contexte.jsonl` (25 017 lignes) ·
  `Index_Maison/data/bloc_privatise_hist.jsonl` (4 767 points)
- Alerte existante : `Index_Maison/data/alertes/ALERTE_poussiere_haute.json`
- Signal 3 codé : `hulk-mexc/scripts/signal3_livre_ecorche.py` + SPEC
  `Index_Maison/SPEC_SIGNAL3_LIVRE_ECORCHE_20260829.md`
- Deepdive parent : `DEEPDIVE_MANIPULATION_3SIGNAUX_20260829.md`
