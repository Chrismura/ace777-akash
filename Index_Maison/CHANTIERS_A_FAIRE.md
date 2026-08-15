# CHANTIERS À FAIRE — ACE777

> Backlog central (complète `CHOSES_A_FINIR_REVOIR.md`). MAJ : 2026-08-15.
> Règle : un chantier = un GO de Christophe + (si majeur) famille/codeur + Release Receipt.

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

## Règle
Backlog = honnête, vivant. On finit l'essentiel avant la finition.
Un GO de Christophe = priorité. La cohérence s'applique à tout le monde, moi compris.
