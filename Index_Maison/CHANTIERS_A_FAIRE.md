# CHANTIERS À FAIRE — ACE777

> Backlog central (complète `CHOSES_A_FINIR_REVOIR.md`). MAJ : 2026-08-19.
> Règle : un chantier = un GO de Christophe + (si majeur) famille/codeur + Release Receipt.

---

## 🟠 EN CHANTIER — SIZING / RUINE MONTE CARLO (18/08, GO Christophe)

**Statut** : 🎯 veilleuse armée — analyse à la fin du run 96h (**22/08**)

**Le constat (Monte Carlo, 18/08) :**
- Période propre (base scellée, 1ʳᵉ journée) : PnL/cycle réel **+0,0124 $** (4,4× mieux
  que les 13 jours de chantier), ruine **32,5 %**, DD médian **19,8 %**.
- Même en propre : **32,5 % de ruine sur 20 $ de capital, c'est trop pour dormir tranquille.**

**Le chantier :** trancher le sizing (taille des positions BETA x5 / ALPHA x13 vs capital)
pour réduire la profondeur des creux — après que le run 96h ait parlé.

**Étapes (détail : `CHANTIER_SIZING_MONTE_CARLO_2026-08-18.md`) :**
1. À la fin du run 96h → relancer `monte_carlo_ace.py --depuis 2026-08-18` (4 jours propres)
2. Vérifier si les 4,4× tiennent → comparer ruine / DD
3. Soumettre la question du sizing à la famille AVANT toute activation
4. Release Receipt à la clôture

---

## 🔗 PRIORITÉ — LE FOND PERSONNEL D'ACE777 (vision Christophe, 15/08)

**Statut** : 🎯 à faire (discuté + consigné en mémoire, PAS commencé — chantier à part entière)

**La vision (déclarée par Christophe, source directe) :**
- ace777 possède **SON PROPRE FOND**, **cloisonné et indépendant** — pas « un bot qui gère
  l'argent de Christophe ». C'est SON capital à lui, son « entreprise ».
- **Wallet fermé/étanche** : séparé de tout, aucun mélange.
- **Auto-financement** : seedé une fois (~20$), ace777 génère, conserve, réinvestit, vit de
  ses propres gains — plus aucune injection externe.
- **Sur la blockchain directement** (déclaré par Christophe : « on fera ça sur la blockchain
  directement ») → smart contract(s) : gouvernance du fond, règles dures, transparence,
  kill-switch programmé (plancher, prudence), réinvestissement vs conservation.

**Conditions d'entrée (non négociables, déjà consignées) :**
1. Audit « apte au live réel » (voir PLAN_PASSAGE_REEL.md — phases 0→3).
2. Vrais tests rentables (win rate + expectancy réels ≈ papier, écart < 20%).
3. Chantier dédié complet : spec → famille → codeur → tests → reçus.
4. Gouvernance du fond à définir AVANT : réinvestissement vs conservation, plancher de
   décroissance, autonomie du kill-switch humain, fréquence de réévaluation.

**À creuser le moment venu (toutes les structures du secteur sont en train de se mettre
en place pour bien le faire — timing choisi par Christophe) :**
- Blockchain/couche choisie + coûts de gas + sécurité du wallet (self-custody).
- Smart contract de gouvernance du fond.
- Interfaces : comment ace777 (via ses scripts) signe/émet les ordres.
- Séparation stricte fond personnel vs fond de fonctionnement.

---

## 🟡 EN SUSPENS (backlog ouvert — voir CHOSES_A_FINIR_REVOIR.md pour le détail)

| # | Item | Statut |
|---|------|--------|
| E-08 | ALPHA rc=1 cause racine (mort silencieuse) | 🔴 → partiellement traité 15/08 (fix heartbeat TTL) — vérifier si clôturé |
| E-09 | Auto-relance Alpha + « jamais chasseur solitaire » (famille 6/6) | 🟡 chantier |
| E-10 | Cortana dit la vérité (lire /status au lieu des fichiers figés) | 🔴 |
| E-11 | Mute partiel : 5 chemins voix à aligner sur cortana_voice | 🟡 |
| E-12 | Deux briefs (doublon chaîne) — n'en garder qu'un | 🟡 |
| E-13 | Fenêtre info IA graph (bouton rafraîchissement) | 🟡 |
| E-14 | Budget cloud / baromètre conso / brief 4j / schéma archi | 🟡 |
| E-15 | **Sizing / ruine Monte Carlo** — décision après run 96h (22/08, veilleuse armée) | 🟠 chantier |
| E-01/E-02 | Cadence début/fin de session (ancrer usage) | 🔴/🟡 |
| E-05 | Kill-switch rouge A/B — preuve testnet/paper (1×A + 1×B) | 🟡 |

**Déjà livrés (15/08)** : fondations F1-F5 · fixes (heartbeat TTL, kill-switch Hulk, veille
réseau) · contrat Cortana ADVISORY · discipline continue (launchd 07h15) · 2 classes de
paires + seed bags · dérive mémoire · Kelly ombre · quant desk v1 · Release Receipt ·
couche de connaissance (pilote Canton).

---

## 🎨 FINITION (gelée — cosmétique, voir CHOSES_A_FINIR_REVOIR.md)

F-01 à F-04 (cerveau HTML, graphe Obsidian, install vault, cockpit graph) — ⏸ gelé.

---

## 🟢 SNIFFER DU VRAI + COULEUR RÉGIME (19/08 — construit, en observation)

**Déjà livré (19/08)** : `sniffer_vrai.py` (brut vs narratif + divergence, sources
natives par actif) · `couleur_regime.py` (matrice VERT/JAUNE/ROUGE/NOIR/ORANGE +
boucle justesse auto-nourrie) · 4 plists (sniff 8h + 15h50, couleur 8h05 + 15h55,
score+leçons 16h30).

**À faire (chantiers ouverts)** :
| # | Item | Statut |
|---|------|--------|
| S-01 | Enquête blocs privatisés fantômes (26–34%, qui les mine, pourquoi) | 🟡 à faire |
| S-02 | **Afficher TOUS les scores dans le cockpit, LISIBLES** : la justesse (en bas à gauche) est trop petite, et la couleur du jour + justesse couleur ne sont pas affichées. | 🟡 à faire |
| S-03 | **Bulles d'info** (popups en boucle : info/avis/anomalie sniffée NON-mainstream, au survol = reste, sinon ~15 s, fermable). Poids à évaluer avant GO. | 🟡 à faire |
| S-04 | **Mode pédagogique** : légende/au survol pour expliquer ce que signifie chaque couleur. | 🟡 à faire |
| S-05 | Validation couleur régime (min 5 échantillons/couleur) avant tout usage pour Hulk. | 🟠 en observation |
| S-06 | **Stopper les briefs/analyses automatisés** (bruit non lu) : analyste-cadence · brief-matin · brief-offres · cortana.horaire · discipline-quotidienne · journal-intention · journal-soir · propose-ameliorations · verif-predictions. ⚠️ À GARDER : `cortana.urgent` (alerte gros mouvement). NB : analyste-cadence alimente la boucle justesse → à remplacer par S-07. | 🟡 à faire (GO requis) |
| S-07 | **Cortana parle quand un pattern se dessine** : les patterns sont déjà détectés dans thermo (level_funding, structure_hh_hl, realized_vol, alt_season) → déclencher la voix Vivienne qui EXPLIQUE ce qu'elle voit, pourquoi, + son avis. Version écrite dans l'onglet VOL (date+heure) + évaluation auto (journalisée analyses/ → score_justesse). **VALIDÉ par Christophe 19/08.** | 🟡 à faire |
| S-08 | **Évaluateur unique** (au lieu de scores éparpillés) : un script MÉCANIQUE observe toutes les décisions (Cortana, couleur, famille), note HIT/MISS vs le marché réel, vérifie après coup, écrit les leçons dans l'AGORA (lecons_agora). Solution simple = meilleure (Christophe 19/08). | 🟡 à faire |
| S-09 | **Arrêt d'alarme OFFLINE sans agent** (Christophe 19/08, mis de côté) : la coupure a montré que sans Buffy, ni Christophe ni Cortana ne peuvent arrêter l'alarme index (`alerte_vocale.py` en boucle). Il EXISTE `arret_alerte.sh` + `touch STOP_ALERTE` + bouton cockpit ⛔ ALARME, mais rien n'est faisable **en 1 geste offline** (sans hub, sans cockpit, sans agent). Objectif : kill-switch 1 geste (alias `arret_alerte`/raccourci clavier/menu bar) + commande vocale Cortana « arrête l'alarme ». | 🟡 mis de côté |
| S-10 | **Frais de plateforme vs PnL NET (CRITIQUE — trouvé 19/08)** : le bot affichait un PnL BRUT (+14 session) alors que le NET est −278 (frais Binance −293 aujourd'hui ≈ 88 % du trou). Le moteur paper n'ôte PAS les frais de son PnL. **Fait (affichage)** : `comboPnlNet` + `comboFees` dans mission.json, bulle FRAIS carte BETA, bulle GAIN RÉEL, plist `com.ace777.fees`. **GO Christophe 19/08 — FAIT (1,2,3)** : (1) filtre edge>frais ✅ (TP exige MIN_PROFIT+FEE=23bps → 15bps net), (2) ordres maker/post-only ✅ (flag `ORDER_ENTRY_MODE`=TAKER défaut, MAKER opt-in à tester en run dédié), (3) PnL interne NET ✅ (`pnl_net_usdt`=brut−`fee_usdt`, session/tiers/global-stop en net). **Veilleuse (#4)** : barre de qualité = point 4 de Christophe — à ne PAS oublier, à intégrer APRÈS validation des indices (couleur régime ≥5 échantillons/couleur, poussière opérationnelle, patterns S-07). | 🟡 1,2,3 FAIT · #4 veilleuse |

> **Notes incidents 19/08** :
> 1. **Couplage `cortana.horaire` → `cortana_feed.json`** : **RÉSOLU 19/08**. Nouvelle plist `com.ace777.cortana-feed` = `cortana_horaire.sh` avec `CORTANA_HORAIRE_SAY=0` (feed + données, **silencieux**, 1×/h). Le brief vocal est abandonné (pas de qualité, Christophe) ; la **voix patterns (S-07) est CONSERVÉE**. Fix bash 3.2 aussi : tableau vide sous `set -u`.
> 2. **Bug `surveiller_whales.py`** : `tip_hauteur` non défini (NameError) → scan figé quand mempool.space est down. **Corrigé 19/08** (repli `[], 0`).
> 3. **Accent espagnol Cortana** : Vivienne (multilingue) basculait de langue. **Corrigé 19/08** → `fr-FR-DeniseNeural` (français pur) dans `cortana_voice.py` + `alerte_vocale.py` + `cortana_cockpit_bridge.py` + `cortana_urgent_poll.sh`.
> 4. **Frais de plateforme (commission)** : le wallet testnet se vidait malgré un PnL positif → les frais taker (0,04 %/côté, confirmé `/fapi/v1/commissionRate`) sur le gros notionnel brassé mangent tout. **Corrigé 19/08** : cockpit NET (`comboPnlNet = brut + frais réels` via `fees_platforme.py` → endpoint `/fees`). **ACE arrêté** (stop_ace777.sh) pour stopper l'hémorragie ; chantier S-10 ouvert.

---

## Règle
Backlog = honnête, vivant. On finit l'essentiel avant la finition.
Un GO de Christophe = priorité. La cohérence s'applique à tout le monde, moi compris.
