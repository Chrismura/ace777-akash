# CHANTIER — VIGIE MEMPOOL (pépite de Christophe) — 2026-08-16

> **Pépite** : `hulk-mexc/scripts/vigie_mempool_pepite_christophe.py` (commit `5334e1df`, 16/08 07:50).
> **Règle maison** : maker ≠ checker. Cette spec est pour le **codeur** (écrit) + la **famille/juge** (valide). Buffy orchestre, ne touche pas la logique moteur sans verdict.
> **MAJ 16/08 (Christophe)** : Juge = **model-agnostic** (pas obligé GLM-5.2, n'importe quel LLM du hub). Nouveau signal → **Ada + Cortana en profitent aussi, MAIS avec parcimonie** (un seul indice, là où c'est utile, pas de surdosage).

---

## 1. Ce que c'est (rappel)

Deux idées en un fichier :

1. **VIGIE** — détecter les blocs « privatisés » : une transaction présente dans un bloc miné mais **absente de la mempool publique** = OTC privée / CPFP masqué. Sortie : `taux_fantôme`, `volume_btc`, `nb_tx_cachees`.
2. **JUGE** — matrice d'orchestration globale (**model-agnostic** : GLM-5.2 possible, mais tout LLM capable du hub convient) :
   - `taux_fantôme > 35 %` **et** `volume > 1000 BTC` → **Alerte Impact** : suspendre les shorts, et long de suivi max 2× si BTC monte dans les 30 s.
   - `taux_fantôme > 15 %` **et** `volume < 500 BTC` → bruit, ignorer.
   - **Règle suprême** : drawdown session ≥ 1,5 % → couper TOUS les bots, 100 % stablecoins.

---

## 2. État des lieux (vérifié ce jour)

| Brique | État | Détail |
|---|---|---|
| `detecter_cpfp.py` (Carte 1-3) | ✅ **branché** | launchd `com.ace777.cpfp`, toutes les 10 min, **mode OBSERVATION** (silencieux, bilan 7 j en cours) |
| `surveiller_whales.py` | ✅ **branché** | launchd `com.ace777.whales`, toutes les 5 min (4 adresses, gros blocs, fragmentations) |
| `pont_onchain.py` | ✅ **branché** | agrège whales + CPFP → section `onchain` dans `thermo/live.json` → **déjà lu par Cortana + Ada** |
| `vigie_live.py` | ✅ **branché** | launchd `com.ace777.vigie-live` (KeepAlive) |
| **`vigie_mempool_pepite_christophe.py`** | ❌ **PAS branché** | script autonome, `time.sleep(2)` de simulation, aucun launchd |
| **Juge** (matrice) | ❌ **n'existe pas** | ce n'est qu'un prompt en commentaire dans la pépite |

→ La **vigie** existe déjà (CPFP + whales + pont). Ce qui manque : l'angle **« bloc privatisé / tx fantômes »** et le **Juge**.

---

## 3. Analyse technique (les vrais risques, dans l'ordre)

### 🔴 P0 — Faux-positif de timing (rend la détection inutilisable en l'état)
Le script compare un snapshot de mempool pris à T0 avec le bloc miné à T0+2 s. Or la mempool change en continu → **toute tx normale entrée entre T0 et le bloc est faussement « fantôme »**. Résultat : des centaines de faux positifs par bloc, volume fantôme surévalué.

**Correctif** (au choix du codeur, à valider) :
- (a) Websocket mempool.space (`wss://mempool.space/api/v1/ws`) : on capte le nouveau bloc en temps réel et on fige la mempool **au moment exact** ;
- (b) Poll du tip toutes les ~2 s + snapshot immédiat au changement de tip ;
- (c) **Recommandé** : historique local persistant des txids vus dans nos snapshots de mempool (plusieurs minutes) — une tx n'est « fantôme » que si elle n'a **jamais** été vue. Élimine la course au premier coup.

### 🟠 P1 — Protection API (doctrine free tier, déjà en vigueur)
`for txid in txids_bloc: requests.get(...)` = explosion d'appels dès qu'il y a des « fantômes ». Reprendre la doctrine de `detecter_cpfp.py` : **pré-filtre, backoff, cache, quota**. (P0 doit être réglé AVANT, sinon le pré-filtre est noyé.)

### 🟡 P2 — Division du travail (3 vigies qui se chevauchent)
- `detecter_cpfp.py` = frais/CPFP (cartes 1-3)
- `surveiller_whales.py` = adresses baleines
- pépite = tx fantômes / bloc privatisé

**Décision (recommandée par Buffy, faute de réponse technique de Christophe)** : faire de la pépite la **« Carte 4 » (bloc privatisé)** du détecteur existant, **pas un 4ᵉ script séparé**. Raison : un seul fichier = moins de redondance, aligné avec « pas de surdosage ». → soumis à la famille.

### 🟢 P3 — Le Juge (la vraie valeur, et le morceau le plus sensible)
La matrice n'existe pas. C'est de l'orchestration qui touche les bots HF et le capital → **à construire en SHADOW d'abord** (comme `cortical_shadow_glm.sh` : il écrit ses décisions sans rien appliquer), puis validation, puis branchement réel. **Model-agnostic** : le hub choisit le LLM disponible (pas verrouillé sur GLM-5.2). La règle 1,5 % doit être recoupée avec le kill-switch existant (`STOP` / `STOP_ALL`).

### 🔵 P4 — Distribution aux gardiens (Ada + Cortana), AVEC PARCIMONIE
Le nouveau signal (taux_fantôme / bloc privatisé) doit profiter à Ada + Cortana **sans surdosage**, en réutilisant le circuit existant (`pont_onchain.py` → `thermo/live.json` → section `onchain`) :
- **Cortana** : + **1 seul indice** `bloc_privatise` (synthèse textuelle pré-mâchée, pas de chiffres bruts) — comme l'indice `onchain` actuel.
- **Ada** : + **1 seul modulateur** voilure (ex. privatisation forte → ×0.93, borné ±10 %, **jamais de blocage**) — comme le modulateur outflow actuel.
- **PAS** de nouveau consommateur, pas de nouveau canal, pas de chiffres bruts injectés. On enrichit ce qui existe, on n'ajoute rien de lourd.

---

## 4. Plan (proposé)

| Phase | Tâche | Qui |
|---|---|---|
| **P0** | Corriger le faux-positif de timing (historique mempool local) | codeur → famille |
| **P1** | Pré-filtre API + backoff + quota (doctrine free tier) | codeur |
| **P2** | Intégrer en « Carte 4 » du détecteur CPFP (pas de script séparé) | codeur → famille |
| **P3** | Juge en SHADOW (matrice + règle 1,5 %), model-agnostic, sans application | codeur → famille |
| **P4** | Distribution Ada + Cortana (1 indice + 1 modulateur, via `pont_onchain.py`) | codeur |
| **P5** | Branchement réel (launchd + veilleuse) | après GO Christophe |

---

## 5. Décisions (état)

1. **Emplacement** : la pépite est dans `hulk-mexc/scripts/`, mais tout l'onchain vit dans `Index_Maison/scripts/`. **Recommandation Buffy** : consolider dans `Index_Maison/scripts/` (cohérence). À confirmer.
2. **Forme** : **« Carte 4 » du détecteur CPFP** (recommandé, cf. P2). — *Christophe ne tranche pas (pas assez technique), Buffy recommande, famille valide.*
3. **Juge** : **SHADOW d'abord** (recommandé). — *idem : Buffy recommande, famille valide.*

---

*Spec rédigée par Buffy (orchestration) — aucun code modifié. À passer au codeur + famille.*
