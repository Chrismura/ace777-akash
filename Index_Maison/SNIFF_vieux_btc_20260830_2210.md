# SNIFFER DU VRAI — bitcoin · vieux BTC qui bougent — 2026-08-30T22:10Z
> Provider : Buffy (vérification sources) · scan onchain mempool.space direct + croisement Galaxy Research

## 1. FAITS BRUTS

### Scan direct (mempool.space, 30/08 22:07Z, 4 derniers blocs ≈ 40 min, seuil 50 BTC)
- **35 grosses tx** détectées sur la fenêtre · **0 vieux coin** (âge du plus vieil input ≥ 2 ans).
- Les gros mouvements récents (2 440 BTC ×3, 835, 657 ×4, 187 BTC ×7…) sont des **flux d'exchange frais** (inputs âgés de moins d'un jour) — pas de réveil de baleine dormante dans la dernière heure.
- **Faille de notre veille onchain confirmée** : `surveiller_whales.py` ne surveille que les adresses étiquetées (Binance Cold/Hot, Bitbank…) → il **rate** les vieux coins qui partent vers des adresses non étiquetées.

### Événements vérifiés (Galaxy Research, 16→26/08) : 6 wallets dormants → 553,59 BTC ≈ 40,15 M$
| Date | Bloc | BTC | Dormance | Destination |
|---|---|---|---|---|
| 16/08 | 962 770 | 8,54 | depuis 13/06/2011 (15,2 ans) | adresse sans label |
| 18/08 | — | 212,00 | depuis 10/08/2012 (14 ans) | sans label · **lié procès NY** « Noah Doe #1396 · Salomon Client Dusted » |
| 18/08 | — | 10,74 | depuis 17/06/2011 | sans label |
| 22/08 | 963 519 | 132,31 (cluster 3 adresses 2011) | 15 ans | sans label exchange (4,45 M$ + 0,40 M$ + 5,51 M$) |
| 22/08 | — | 150,00 | depuis 26/12/2014 | sans label · **lié procès NY** « Noah Doe #1680 » |
| 26/08 | 964 127 | 40,00 | depuis 28/05/2012 (14,2 ans) | **Boerse Stuttgart Digital** (custody allemand) |

- **5/6 transferts → adresses SANS lien exchange** : aucune preuve onchain de vente.
- **1 seul vers entité connue** : Boerse Stuttgart Digital = fournisseur de custody/infra (réorganisation ou OTC, pas un dump).
- Le 20/08 : **28 wallets dormants → 1 314 BTC (94 M$)** dont 1 214 BTC d'adresses 2014 (21 tx de 50 BTC exactement, même format → probablement 1-2 holders, réorganisation).
- Contexte juillet : 5 908 BTC (383 M$) après 8,5 ans de dormance.

### Le procès NY « Noah Doe » (facteur clé de lecture)
- Plainte : contrôle de **39 069 adresses dormantes (~3,7 M BTC** visés, y compris wallets Satoshi et Mt.Gox) sous la loi « abandoned property » (Article 7-B).
- Les plaignants envoient des **tx « dust »** de notification → adresses étiquetées « Salomon-dusted » (2 des 6 wallets récents portent ce label).
- **Les adresses qui bougent sont retirées de la plainte** : 44 wallets déjà retirés en juillet (21 443 BTC au dépôt → 46 334 BTC bougés depuis → 3 097 BTC restants).
- Le procès est **en pause** (juin, juge Kathy J. King) avant audience de juillet.

### Autre explication possible (à ne pas écarter)
- **Faille firmware Coldcard** (mars 2021) : 4 vagues de drain ≈ **1 816 BTC retirés de 5 294 adresses** depuis fin juillet. Les vieux holders ayant importé leurs clés 2011-2014 dans un Coldcard affecté peuvent bouger par **sécurité**, pas par vente.

## 2. NARRATIF
- Fear & Greed : **69 (Greed)** · indice onchain maison : 48,2/100 (ÉLEVÉ — activité anormale OTC/CPFP) · poussière score 50/50 · blocs privatisés 4,77 %.
- News mainstream : « il devient millionnaire 12 ans après avoir tout perdu », « doctrine anti-crise Tether », « elles voulaient copier Strategy, elles ont perdu 80 Mds », « Bitcoin vivra mais le moment est périlleux », « point bas ? ».
- L'activité des wallets dormants est au **plus bas depuis 2022** (Galaxy) → ce n'est PAS une vague de distribution massive, un événement ponctuel.

## 3. DIVERGENCE(S)
- **D1 — La foule est en Greed (69) pendant que les vieux coins bougent en silence** : 553 BTC de 2011-2014 se sont déplacés en 10 jours sans bruit médiatique, 5/6 vers des adresses muettes. Le narratif parle de « moment périlleux », pas de réveil de baleines.
- **D2 — « Vieux coins qui bougent = vente » est FAUX ici** : 5/6 destinations sans exchange → pas de pression vendeuse. La seule entité connue est un custody (Boerse Stuttgart), pas un exchange spot. C'est de la réorganisation (sécurité / héritage / procès NY), pas de la distribution.
- **D3 — Notre sonde rate le signal** : l'alerte baleines maison ne voit que Binance/Bitbank (87 344 BTC de flux internes) et reste « neutral », pendant que le vrai événement (vieux coins) lui échappe totalement.

## 4. PRÉDICTIONS TESTABLES
- **H1 (pression vendeuse nulle)** : si les wallets 2011-2014 continuent de bouger vers des adresses sans label exchange, alors leur mouvement n'alimente PAS l'offre spot → impact prix faible/nul à moyen terme.
- **H2 (lien procès)** : si le procès NY reprend et que les plaignants gagnent du terrain, l'activité des adresses « Salomon-dusted » va ACCÉLÉRER (les holders bougent pour sortir de la plainte) → surveiller les blocs 963 519 / 964 127 et les 2 labels Noah Doe.
- **H3 (sécurité Coldcard)** : si de nouvelles vagues de drain Coldcard apparaissent (1 816 BTC déjà retirés), les vieux coins bougeront par vagues vers de nouveaux wallets self-custody → à ne PAS lire comme un signal de marché.

## 5. VERDICT
- **Brut fiable** : les 6 transferts sont documentés par Galaxy (blocs, dates, adresses, labels) et cohérents entre sources (crypto.news, CoinDesk, KuCoin, CoinMarketCap).
- **Lecture 2e degré** : ces mouvements sont de la **réorganisation de holders historiques** (procès NY + sécurité Coldcard + héritage), PAS un signal de distribution. 40 M$ sur 10 jours = microscopique face aux flux Binance (87 k BTC).
- **Ce qui manque pour conclure** : le suivi des 3 clusters (2011 ×3, 2014 ×2, 2012 ×1) dans les jours à venir — s'ils bougent VERS des exchanges, la lecture change.

---
## BRUT reçu (scan direct)
```json
{"ts": "2026-08-30T22:07:58Z", "hauteur_tip": 964793, "nb_blocs": 4, "seuil_btc": 50.0,
 "min_age_ans": 2.0, "nb_grosses_tx": 35, "nb_vieux_mouvements": 0,
 "note": "age_max = âge du plus vieil input de la tx (source mempool.space)"}
```

## SOURCES
- Galaxy Research (@glxyresearch) 26/08 — wallet 40 BTC 2012 → Boerse Stuttgart Digital, bloc 964127
- crypto.news 30/08 — « Bitcoin whales move $40M after decade-long dormancy »
- crypto.news 20/08 — « Bitcoin whale moves $86M after 11 years of dormancy » (28 wallets, 1 314 BTC, btcparser.com)
- CoinDesk 28/08 — « wallets untouched for 10 years moved $40M, most avoided exchanges »
- cryptonews.net / Yahoo Finance / KuCoin / CoinMarketCap (mêmes chiffres Galaxy)
