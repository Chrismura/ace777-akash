# 📡 PROTOCOLE ANALYSE DE DIVERGENCE — Hulk (29/08/2026)

> **Document fondateur du pattern « avance / retard ». À lire PAR LA PROCHAINE IA avant toute
> utilisation du rapport de divergence.** Rédigé par Buffy (chef scientifique), validé par
> Christophe le 29/08.

---

## 1. Pourquoi ce protocole existe

Le 29/08, en croisant les données Hulk avec le panier, on a découvert un patron :
**certaines cryptos du portefeuille divergent du mouvement général, et cette divergence
n'est pas du bruit — elle PRÉCÈDE ou SUIT le marché avec un délai mesurable.**

Notre limite : **2 jours de données seulement** (début de pattern, pas une preuve).
Ce protocole fait que les prochains jours, **la même analyse se relance sur les données
accumulées** et produit un rapport horodaté → le pattern se confirme ou s'infirme
avec le temps. C'est la seule façon de transformer une intuition en certitude chiffrée.

---

## 2. Les 3 angles mesurés (et ce qu'ils veulent dire)

### Angle 1 — DIVERGENCE ACTUELLE
Chaque crypto vs la **moyenne du panier** (m6 = mouvement 6h, moyenne horaire) :
- fenêtre **récente** = 6 dernières heures
- fenêtre **passé** = les 30h avant
→ `DIV 6h` positif = la crypto surperforme le panier MAINTENANT ; négatif = sousperforme.

### Angle 2 — TIMING (qui précède, qui suit)
**Corrélation croisée horaire** entre la crypto et le panier, testée pour un décalage
de **−4h à +4h**. On garde le décalage qui donne la corrélation maximale :
- `lag ≤ −2h` → la crypto **PRÉCÈDE** le marché (elle bouge avant) = potentiel **signal**
- `lag ≈ 0` → synchrone (pas d'info de timing)
- `lag ≥ +2h` → la crypto **SUIT** le marché (retardataire) = à éviter en entrée

### Angle 3 — SIGNAL DIRECTIONNEL (le plus important)
**Corrélation entre le mouvement de la crypto à l'heure H et le DELTA du panier
entre H et H+4h** :
- **positive** (+0,15 ou plus) → quand cette crypto bouge, le **marché monte ensuite**
  = 🟢 **LEADER** (signal d'achat / d'accumulation)
- **négative** (−0,15 ou moins) → quand cette crypto pompe, le **marché baisse ensuite**
  = 🔴 **POMPE-PIÈGE** (signal de sommet / avertissement de vente)
- proche de 0 → pas de signal directionnel.

### Angle 4 — Validation par les pics (confirmation)
Pour les cryptos avec signal, on regarde chaque **pic** (m6 > 6 %) et ce que fait le
panier **+2h et +4h après** :
- panier monte 0 % du temps après les pics → le signal négatif est **robuste**
- panier monte 60 %+ du temps → le signal positif est **robuste**

---

## 3. COMMENT RELANCER (la prochaine IA fait ça)

```bash
cd /Users/christophe/ace777-test-day1/hulk-mexc
python3 scripts/analyse_divergence.py
```

**Ce que ça fait** :
1. Lit `runs/croisement_contexte.jsonl` (les données que le moteur accumule en continu,
   ~1 point/pair/minute depuis le 27/08 — **ne jamais supprimer ce fichier**).
2. Calcule les 4 angles.
3. Écrit un rapport horodaté : `runs/DIVERGENCE_<AAAA-MM-JJ_HHMM>.md`
4. Affiche le tout en console.

**Fréquence conseillée** : 1×/jour au minimum (ou à chaque « point d'étape » avec
Christophe). Les rapports s'empilent dans `runs/` → on compare les rapports successifs
pour voir si le pattern se renforce.

---

## 4. COMMENT LIRE LE RAPPORT (checklist d'interprétation)

1. **Régression ?** → ouvrir les 2-3 rapports précédents, regarder si la liste
   LEADER / POMPE-PIÈGE est stable (mêmes cryptos) ou mouvante.
2. **Un LEADER stable 3+ jours** (corr > +0,2 chaque jour) → candidat sérieux à
   l'accumulation. **Un POMPE-PIÈGE stable 3+ jours** (corr < −0,2) → candidat à la
   sortie partielle.
3. **Toujours croiser avec les régimes** : un leader en baisse (COOLING + chg24 négatif)
   = opportunité de dip ; un leader en IMPULSE + chg24 énorme = risque de surachat.
4. **Ne jamais décider sur 1 seul rapport** — le seuil de confiance est 3 jours de
   stabilité (c'est le but de ce protocole).

---

## 5. Données & fichiers (ne pas casser)

| Fichier | Rôle | Règle |
|---|---|---|
| `runs/croisement_contexte.jsonl` | **Matière première** (écrite par le moteur à chaque tick) | NE JAMAIS SUPPRIMER / TRONQUER |
| `scripts/analyse_divergence.py` | La machine d'analyse (réutilisable) | Modifiable, mais documenter |
| `runs/DIVERGENCE_*.md` | Rapports horodatés (archive) | Garder — c'est la preuve du pattern |
| `strategie/universe_profils.json` | Profils (murs, calib, trailing) par paire | Lecture pour le deepdive |
| `runs/PAPER_V1_*_state.json` | État moteur (scores régimes, move24) | Lecture pour croiser régimes |

---

## 6. Résultats du 29/08 (première passe — À CONFIRMER)

| Crypto | Signal | Lecture du 29/08 |
|---|---|---|
| **CHIP** | 🟢 LEADER (+0,27) | Surperforme durablement, précède hausses, volume HOT, trailing armé. **Le seul leader haussier.** |
| **QAIT** | 🔴 POMPE-PIÈGE (−0,45) | m24 +38 % énorme → surchauffée, ses pics précèdent les baisses. |
| **EDEL** | 🔴 POMPE-PIÈGE (−0,47) | 8/8 pics → panier en baisse à +2h ET +4h. Avertissement net. |
| **TEL** | 🔴 POMPE-PIÈGE (−0,42) | Idem, sousperforme. |
| **RED / KITE** | 🔴 POMPE-PIÈGE (−0,15) | Frontière du seuil, à surveiller. |
| **XRP / RIZE / CC / PYTH** | 🟡 léger | Pas de signal directionnel clair. |
| **RWAINC / HBAR / TEL** | 📉 sousperformance durable | Retardataires faibles. |

> ⚠️ **2 jours seulement** : ce tableau est un **état des lieux**, pas une vérité.
> Le protocole existe pour transformer ça en certitude sur 1-2 semaines.

---

## 7. LE DISPOSITIF ANTI-OUBLI (réponse au risque n°1 de Christophe)

> Christophe, 29/08 : « journalise, mais faudra pas oublier ensuite, c'est ça le problème, le risque. »

**Le pattern est journalisé ET se rappelle tout seul** :

| Pièce | Rôle | Tourne quand ? |
|---|---|---|
| `scripts/analyse_divergence.py` | La machine d'analyse (rapport horodaté) | à la demande / via journal |
| `scripts/journal_divergence.py` | Journalise un point dans `runs/DIVERGENCE_SUIVI.jsonl` (qui est LEADER/POMPE-PIÈGE à l'instant T) + met à jour `runs/DIVERGENCE_ETAT.json` | **toutes les 6h** |
| `~/Library/LaunchAgents/com.ace777.divergence.plist` | Relance le journal toutes les 6h + au login | automatique (déjà chargée) |

**L'alerte anti-oubli** (`runs/DIVERGENCE_ETAT.json`) :
- `FRAIS` (< 12h) → 🟢 pattern suivi, recommande `OBSERVER`
- `STALE` (12-24h) → 🟡 vérifier le moteur (`croisement_contexte.jsonl`)
- `ALERTE` (> 24h) → ⚠️ **PERSONNE NE SUIT LE PATTERN** : relancer la confrontation (ce doc)

**Le cockpit peut lire `DIVERGENCE_ETAT.json`** (s'il n'est pas encore affiché, c'est un
chantier rapide) : on verra d'un coup d'œil si le pattern est suivi ou abandonné.

**Si on veut arrêter le dispositif** (jamais sans GO Christophe) :
```bash
launchctl unload ~/Library/LaunchAgents/com.ace777.divergence.plist
```

---

## 8. Liens avec les autres chantiers

- **Fix SELL full (déployé le 29/08)** : le POMPE-PIÈGE confirme qu'il faut des sorties
  partielles sur amplitude forte (EDEL/QAIT = positions surchauffées → cascade, pas de coupe).
- **Cortana / famille** : ce protocole leur donne un **signal quantifié réutilisable** à
  croiser avec leur analyse (le pattern doit être confronté, pas cru sur parole).
- **Prochain pas** : donner ce signal à Hulk (mode ADVISORY d'abord) + soumettre le
  pattern à Cortana (contexte complet, boucle « trouve »).
