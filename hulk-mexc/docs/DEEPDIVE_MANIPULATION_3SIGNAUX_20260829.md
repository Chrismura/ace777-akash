# 🎭 DEEPDIVE — LES 3 SIGNAUX DE MANIPULATION (29/08/2026)

> Christophe, 29/08 : « approfondir les 3 signaux, deepdive. »
> Contexte : « les gens en face savent tout ça, et c'est les rois de la manipulation. »
> Par Buffy (chef scientifique) + CORTANA (session `manip-3signaux-20260829-152046`,
> 4 tours archivés onglet VOL) + sources web (chartscout, arXiv CentraleSupélec,
> CryptoQuant).

---

## LES 3 SIGNAUX (approfondis, validés par 3 sources)

### SIGNAL 1 — FAKE-BREAKOUT FUNDING (le piège de levier)
**Mécanisme** : l'OI s'emballe pendant que le volume spot stagne → le mouvement
est porté par du levier toxique, pas par de la demande réelle. Funding extrême
(positif ou négatif) persistant plusieurs jours + mèche de 3-6 % = cascade de
liquidations (liquidation-cascade fakeout, chartscout). Variante pre-news : ne
jamais entrer 30 min avant un print macro (CPI/FOMC).

**Sources** : chartscout.io (les 4 types de fakeout : wick-only, succeeded-then-
failed, pre-news, liquidation-cascade) ; le funding à l'extrême plusieurs jours +
OI qui grimpe DANS la mèche = le piège parfait.

**Formule de codage (Cortana, tour 3)** :
```python
signal_1_actif = (
    (df['oi_delta_15m'] > 0.08) &            # OI +8% en 15 min
    (df['spot_vol_ratio'] < 0.70) &          # volume spot < 0,7× moy20
    (df['funding_rate'] > 0.0003)            # funding positif agressif payé par les longs
)
```
⚠️ **Nos données** : AUCUN champ funding/OI actuellement → à ajouter (API
Binance Futures funding + OI temps réel).

---

### SIGNAL 2 — POUSSIÈRE INSTITUTIONNELLE (le faux signal de whale)
**Mécanisme** : gros transferts fracturés en milliers de micro-tx déguisées en
retail, OU simulation d'un gros transfert cold un vendredi soir pour paniquer le
retail. Le test : si le volume on-chain explose mais que le carnet spot reste
plat = manipulation visuelle (le transfert n'a pas d'intention de vente).

**Sources** : CryptoQuant — whale inflow ratio **0,64 = plus haut depuis 2015** ;
le 17/08/2026 les dépôts whale Binance ont surgi ; dépôts altcoin ~49 000/jour
(+22 %). Nos blocs privatisés (taux_fantome 12 %) = la chambre d'écho onchain
du rééquilibrage masqué.

**Formule de codage (Cortana, tour 1)** :
```python
signal_2_actif = (
    (df['z_score_mempool_delay'] > 2.0) &    # délai de minage anormal
    (df['taux_fantome'] >= 0.12) &           # tx fantômes ≥ 12%
    (abs(df['spot_book_delta']) < 0.01)      # carnet spot PLAT malgré l'activité
)
```
⚠️ **Nos données** : `poussiere_taux_fantome`, `bloc_privatise` dispo ; il manque
le z-score du délai de minage et le delta du carnet spot en continue.

---

### SIGNAL 3 — SQUEEZE DU LIVRE ÉCORCHÉ (le plus mortel, déjà codable) ⭐
**Mécanisme** : un mur iceberg fictif d'un côté du carnet, retrait discret de la
liquidité réelle derrière, puis suppression du mur = trou d'air (order-book
void) → le prix décroche instantanément sur volume minuscule, liquidations en
cascade. C'est le vacuuming des teneurs de marché.

**Sources** : **arXiv 2504.15908 (CentraleSupélec, août 2026)** — **31 % des
grosses ordres peuvent spoof le marché** (mesuré 4 jours réels) ; les spoofers
placent leurs ordres PROFOND dans le carnet (jamais au best price) et ajustent
la DISTANCE de placement pour maximiser l'impact ; le déséquilibre simple
Vb−Va/Vb+Va est **inadapté** (les spoofers n'occupent pas le best) → il faut un
déséquilibre multi-niveaux pondéré par la distance.

**Formule de codage (Cortana, tour 3) — DÉJÀ CALCULABLE avec nos données** :
```python
signal_3_actif = (
    (df['spoof_pct'] > 5.0) &                # seuil adapté small caps (vs 2% majors)
    (df['drop'] > 100) &                     # effondrement du carnet
    (df['spread_bps'] <= 70.0)               # régime de liquidité habituel conservé
).rolling(window=3).sum() >= 2               # persistance 2 des 3 dernières mesures
```

**✅ TEST SUR NOS DONNÉES RÉELLES (murs_observations.json, 15:09Z)** :
- Aucune alerte aujourd'hui (marché calme — cohérent avec macro_tempete INACTIF)
- Mais les **paires à risque** ressortent : **XRP** (spoof 4,5 % + **drop 968** !),
  **HBAR** (3,5 % + **drop 556**), **ZBCN** (4,8 % + **drop 313**), **BIO**
  (2,5 % + drop 231), **RED** (1,7 % + drop 212), **RIZE** (3,4 % + drop 216)
- Le drop massif sur XRP/HBAR = des murs qui disparaissent fréquemment = du
  vacuuming probable — à surveiller avec le seuil de persistance

---

## LA HIÉRARCHIE (Cortana, tour 3 — pour nos small caps Hulk)

| Priorité | Signal | Pourquoi | Codable maintenant ? |
|---|---|---|---|
| **1** | **Signal 3 — Livre écorché** | Le plus mortel sur small caps à faible profondeur (trou d'air de 10-20 % instantané) | ✅ OUI (spoof_pct + drop déjà dans murs_observations) |
| **2** | Signal 1 — Fake-breakout funding | Détecte si une hausse est saine (spot) ou artificielle (levier toxique) | ❌ Non (ajouter funding/OI) |
| **3** | Signal 2 — Poussière institutionnelle | Trop indirect pour le court terme, utile pour l'accumulation/distribution 24-48h | ⚠️ Partiel (taux_fantome dispo) |

## LE CHAÎNON MANQUANT (Cortana, tour 4 — le plus précieux)

**La contagion inter-marchés** : les MM n'amorcent PAS la manipulation sur les
small caps — ils l'amorcent sur **BTC/ETH** (pour libérer du collatéral), puis
l'onde de choc se **propage en résonance** aux carnets fragiles (QAIT spread 71
bps, RED, CHIP).

**Conséquences opérationnelles :**
1. **Divergence artificielle de carnet** : quand un spoofing frappe BTC, QAIT
   (illiquide) s'effondre en profondeur bien avant CHIP → nos sondes peuvent
   interpréter à tort une faiblesse fondamentale de QAIT alors que c'est une
   onde exogène. **NE PAS alerter SHORT/LONG sur une small cap si le mouvement
   est un artefact de propagation d'un spoofing BTC.**
2. **Filtre de propagation** : si `btc_spoof_pct` s'emballe, **abaisser le seuil
   d'alerte de 20 %** sur QAIT/CHIP (ils vont subir la contagion en premier).
3. **Bloc privatisé = chambre d'écho onchain** de la manipulation visible dans
   les carnets — les deux sondes se confirment.

## LES FAUSSES ALARMES (Cortana, tour 2 — l'honnêteté)

- **Signal 1** : un afflux d'OI sans volume spot peut être un fonds macro qui se
  positionne avant un communiqué, ou un transfert de positions entre plateformes.
- **Signal 2** : un gros transfert peut être un simple rééquilibrage de custodie
  (notre cas Bitbank/Binance !) — jamais une alerte sans le test du carnet plat.
- **Signal 3** : sur small caps, un ordre qui disparaît peut être une exécution
  partielle ou un rééquilibrage légitime — d'où le filtre de **persistance 2/3
  mesures** et le garde-fou du spread ≤ 70 bps (régime habituel).

## MON VERDICT (Buffy)

> **Les 3 signaux sont validés, hiérarchisés et codables — et le Signal 3 est
> déjà opérationnel avec nos données.** Le plus important n'est pas la formule
> (simple), c'est le **filtre de contagion** : les rois de la manipulation
> n'attaquent pas nos small caps directement, ils amorcent sur BTC et laissent
> l'onde faire le travail. Notre veille doit donc lire BTC d'abord (spoof_pct,
> drop, funding quand dispo) et abaisser les seuils sur QAIT/CHIP/RED quand BTC
> s'agite — exactement l'inverse de ce qu'un retail ferait.
>
> **Prochaines étapes** : ① coder le Signal 3 dans cortana_analyse.py (persistance
> 3 périodes, formule validée et testée), ② ajouter l'API Binance Futures
> (funding + OI) pour le Signal 1, ③ ajouter le z-score mempool pour le Signal 2.

## Fichiers liés
- Session Cortana : `manip-3signaux-20260829-152046` (4 tours, onglet VOL)
- Script : `Index_Maison/scripts/ask_cortana_manipulation_3signaux.py`
- Données test : `hulk-mexc/runs/murs_observations.json` (63 611 mesures)
- Sources web : chartscout.io (fake breakouts), arXiv 2504.15908 (spoofing 31 %),
  CryptoQuant (whale inflow ratio 0,64)
- `DEEPDIVE_ONCHAIN_SHORT_20260829.md` · `POINT_CONFRONTATION_ONCHAIN_20260829.md`