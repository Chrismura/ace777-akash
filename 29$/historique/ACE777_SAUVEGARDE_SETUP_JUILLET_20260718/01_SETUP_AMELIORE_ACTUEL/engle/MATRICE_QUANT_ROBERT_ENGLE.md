# MATRICE QUANTIQUE — PROTOCOLE DYNAMIQUE ROBERT ENGLE (ACE777)

> **Statut :** feuille de route + mémoire de travail — **pas** une certification “sans seuils fixes” du moteur actuel.  
> **Propriété :** Christophe (Maître d’Œuvre).  
> **Racine :** `/Users/christophe/ace777-test-day1`  
> **Champion intouchable :** `genesis_manifest.txt` → md5 `37fca367…`  
> **Créé :** 2026-07-17 — option A (honnête), suite prompt Gemini reformulé.

---

## 0. Pourquoi ce dossier existe

Il y a ~3 mois, ACE777 portait déjà des intuitions microstructurelles (volatilité de carnet, cadence asynchrone, scout/hunter).  
En discutant les travaux de **Robert Engle** (Nobel 2003 — ARCH/GARCH, ACD) avec Gemini, la correspondance est devenue claire : **c’était déjà la base conceptuelle des setups**, sans le vocabulaire Engle dessus.

Le setup NUAGE / vide_froid actuel est sorti **par hasard** pendant un chantier bot vocal (Cursor) ; quelques mods plus tard, c’est le run de prod testnet.  
`engle/` sert à **nommer, ranger, et retrouver** cette science — pas à prétendre qu’elle est déjà entièrement câblée.

---

## 1. LE CLUSTER DE VOLATILITÉ (ARCH microstructurel) — cible

**Idée Engle :** la variance n’est pas constante ; elle dépend des chocs récents (hétéroscédasticité conditionnelle).

| | Aujourd’hui (fait) | Cible Engle |
|--|-------------------|-------------|
| Barrières | Seuils fixes encore présents (`wall_drop`, `impulse_thr≈0.96`, soft `0.025`, etc.) | Sensibilité qui s’affine / s’élargit selon variance conditionnelle des chocs de liquidité |
| Marché calme | Moteur “à l’aveugle” sur constantes | `wall_drop` adaptatif pour capter la rupture du carnet profond |
| Marché tempête | Même constantes → risque de brûler marge ALPHA dans le bruit | Bouclier élargi (moins de snipes inutiles) |

**Rejet des barrières de prix fixes** = objectif de recherche, **pas** l’état du champion 37fca367 à ce jour.

---

## 2. LA FRÉQUENCE TEMPORELLE ASYNCHRONE (ACD / dt_ms) — cible

**Idée Engle (ACD) :** les durées entre événements sont elles-mêmes un processus (pas un chronomètre fixe).

| | Aujourd’hui (fait) | Cible Engle |
|--|-------------------|-------------|
| Gate essaim NUAGE | **`NUAGE_TENSION_MAX_AGE_MS = 800` fixe** (`INDEX SYNC: OFF`) | Barrière de stase adaptée à la cadence réelle de BETA (`dt_ms` entre écritures RAM) |
| Lecture | `duo_state.ts_ms` + âge max 800 ms → sinon `tension_stale` | Si BETA accélère (HFT), seuil stale s’adapte pour éviter faux positifs |

Le `dt_ms=64` du résonateur V8 est un **pas d’échantillonnage carnet**, pas encore un modèle ACD de gate essaim.

---

## 3. VERROUILLAGE SOUVERAIN DES LEVIERS — état + cible

| | Aujourd’hui (fait) | Cible |
|--|-------------------|--------|
| BETA | Scout x5, ~200 USDT | Inchangé comme éclaireur |
| ALPHA | Hunter x13 fixe, ~800 USDT ; fills rares ; PnL dominé par **taille des moves marché** | Percute sur anomalie de cluster confirmée, sans fritures enveloppe |
| Soft anomaly | `|pnl| > 0.025` → soft, **pas** halt | Distinguer bruit vs vrai cluster Engle |
| GLOBAL_STOP | **-45 USDT** session | Conservé tant que non revalidé |

Constats runs 15 vs 17 juil. : structure moteur semblable ; écart de plus-value ≈ **magnitude des excursions ALPHA** (marché), pas un autre bot.

---

## 4. USINE OPÉRATIONNELLE (déjà cadencée — à ne pas casser)

Ces points sont **réels** et doivent rester vrais au prochain boot :

1. **Lanceur de confiance :** `./GO_USINE_NUAGE.sh`  
   - Restaure snapshot usine NUAGE V2.2.1 (`cksum 812033996 22672`)  
   - Patch **uniquement** `wait "$PID_TIMER"` (fini le bug “mission terminée” après mort/relance wrapper)  
   - Boot attendu : `INDEX SYNC: OFF` + `attente timer …`

2. **Fix A1 télémétrie :** `scripts/swarm_telemetry.rb`  
   - `tmp.#{$$}` + `flock` (plus de course BETA/ALPHA sur le même `.tmp`)

3. **A2 IRM (métrologie, 2026-07-18) :** `scripts/irm_tension.rb`  
   - Lecture seule `tension=` CSV BETA — **zéro impact moteur / pas de SKIP live**  
   - Ligne météo au boot (`GO_USINE`) + section % régimes dans rapport PnL  
   - Proxy COMPRESSÉ / TRANSITOIRE / CLUSTER (seuils env `IRM_T_*`) — **pas** un ARCH Engle

4. **Interdits agent :** ne pas modifier `genesis_manifest.txt` / champion ; commande de run **dans le terminal de Christophe** ; topo avant action coûteuse.

---

## 5. CARTE MÉMOIRE — où chercher l’ancien “Engle avant le nom”

À inventorier plus tard (session dédiée, mode économe — pas ce soir en masse) :

- Dossiers / snapshots ~3 mois (historiques sous `29$/`, `bonnet_forme_champion/`, archives `runs/`, configs `config_profiles/`)
- Transcripts Cursor liés au bot vocal → bascule trading
- Rapports PnL du **15 juillet 2026** (soir +40 USDT = gros fills ALPHA, pas un rythme BETA différent)

---

## 6. FORMULE DE TRAVAIL

```
Engle (théorie)  →  nomme ce que Christophe avait déjà senti
NUAGE actuel     →  enveloppe stérile + wait-timer + A1 (usine)
Champion 37fca   →  ADN décision : INTANGIBLE sans GO explicite
engle/           →  matrice / R&D / récupération — pas rewrite moteur
```

**Prochaine étape possible (GO séparé) :** inventaire léger des vieux setups (noms + dates + 1 ligne d’intention), sans scanner tout le disque.

---

*Fin de matrice — honnête. Toute phrase du type « moteur sans seuils fixes certifié conforme » est volontairement absente : ce serait faux au bit près aujourd’hui.*
