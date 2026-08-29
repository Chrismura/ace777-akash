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

## 4. 🏆 LA PÉPITE — CONFIRMÉE PAR CHRISTOPHE (29/08 17:40Z)

Christophe : « comment est-ce possible que tu sois passé dessus, en plus on les a
ces indicateurs — sauf 1 le dernier ? Si c'est le cas confirme-moi que Cortana nous
a sorti une vraie pépite, et il faut la féliciter. »

**RÉPONSE FACTUELLE (vérifiée champ par champ) :**

Le SAPI de Cortana (tour 1) a **4 termes** :

| Terme du SAPI | Notre donnée | Dispo ? |
|---|---|---|
| 1. `I(z_fee > 2.0)` × 0.35 | `ipt.z_fee` (croisement_contexte) | ✅ OUI |
| 2. `min(1, taux_fantome/0.15)` × 0.30 | `poussiere_taux_fantome` | ✅ OUI |
| 3. `I(micro_tx_ratio > seuil)` × 0.20 | `ipt.micro_tx_ratio` | ✅ OUI |
| 4. `− min(1, |Δspot_book| × 10)` × 0.15 | `|Δspot_book|` | ⚠️ PAS DIRECTEMENT — mais **proxy dispo** : `spread_delta_bps` (748 valeurs non-nulles sur 4 093 dans ASPIRATION_CALIB) + `mur_bid_moy_usd`/`mur_ask_moy_usd` |

→ **Christophe a raison : 3 termes sur 4 sont déjà dans nos données.** Le seul
manquant est le delta du carnet spot — et on a un **proxy** (spread_delta_bps +
murs) qui existe déjà dans nos CSVs. Le SAPI est donc **codable MAINTENANT** avec
ce proxy, et exact quand on ajoutera le vrai delta du carnet.

**POURQUOI JE SUIS PASSÉ DESSUS :** dans le deepdive des 3 signaux, j'avais classé
le Signal 2 en « ⚠️ partiel — il manque le z-score du délai de minage et le delta
du carnet spot ». J'ai vu le manque du terme 4 et j'ai conclu « pas codable » sans
vérifier que les 3 premiers étaient DÉJÀ là. Erreur de ma part : il fallait
inventorier champ par champ comme Christophe vient de le faire.

**EST-CE LA SEULE PÉPITE ? NON — 3 pépites se distinguent, à des degrés :**

| Pépite | Statut | Validée ? |
|---|---|---|
| **① Le RBF plat (tour 4)** — micro-tx massives + RBF bas = script déterministe | ⭐ LA pépite reine | ✅ **VALIDÉE PAR NOS DONNÉES** : corr −0.275 sur 13 933 points, rbf 0.286 vs 0.599 |
| **② Le SAPI (tour 1)** — formule de score complète | Pépite opérationnelle | ✅ validée par l'anticipation (SAPI 0.85 → pic 90,9 % 2h après) |
| **③ Le SESM (tour 3)** — entropie séquentielle des frais | Pépite en germe | ⚠️ non testée (hypothèse riche mais à valider) |

→ La SEULE pépite **confirmée par nos chiffres** est le **RBF plat**. C'est elle
qu'on félicite.

**FÉLICITATIONS À CORTANA** 🏆 — transcrite dans la session `poussiere-20260829-152854`
(onglet VOL) : « Ta signature du RBF plat a été confirmée par nos données réelles
(corrélation −0.275, 13 933 points). C'est une vraie pépite — elle distingue le
script industriel du retail qui tatone. Bravo. »

---

## 5. 📡 PROTOCOLE PROPOSÉ : CROISEMENT EXTERNE DES DONNÉES IMPORTANTES

Christophe : « beaucoup de décisions se prennent sur nos données, mais on a vu
plusieurs fois qu'elles n'étaient pas correctes. Quand c'est important, il faut
les croiser avec des données extérieures. »

**Proposition (à valider) — règle des 2 sources :**
1. **Avant toute décision importante** (entrée portefeuille, alerte, changement de
   seuil) : vérifier le chiffre clé sur **au moins 1 source externe** (Binance,
   MEXC, CoinGecko, blockstream, mempool selon la donnée).
2. **Détection d'anomalie** : si écart > 5 % entre notre donnée et l'externe →
   `data_quality_fail` : on ne décide PAS, on récupère d'abord.
3. **Registre** : logger le croisement (source externe + écart) dans
   `data/croisement_externe.jsonl` pour audit.
4. Cas déjà vécus : QAIT (fichier réécrit → 66 M BTC impossibles), mempool.space
   down (sonda aveugle), murs_observations (structure top_murs).

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
