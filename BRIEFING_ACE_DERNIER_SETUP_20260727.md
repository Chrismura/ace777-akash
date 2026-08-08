# ACE777 — Dernier setup de prod (briefing externe)

**Date briefing :** 2026-07-27  
**État machine :** ACE **arrêté** (aucun process GO/ALPHA/BETA). Hulk paper+veille tournent à part.  
**Venue :** Binance Futures **testnet** uniquement.

---

## 1. Identité moteur

| Élément | Valeur |
|---------|--------|
| Champion | `genesis_manifest.txt` → `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` |
| MD5 | `37fca36712d49aa8…` (**JAMAIS modifié**) |
| Lanceur | `GO_USINE_NUAGE.sh` (copie snapshot usine + patches runtime) |
| Stack usine | `vide_froid` NUAGE V2.2.1 |
| Duo | **BETA** = SCOUT (masse ~200 USDT) · **ALPHA** = HUNTER (masse ~800 USDT) |
| Bus hot | `/tmp/ace777_ram_exchange/{duo_state,swarm_telemetry}.json` |
| LLM hot path | **Non** (gate Ollama optionnel / fail-closed — pas le cœur) |

---

## 2. Dernier setup « qui a tourné » (référence 23 juil. 2026)

C’est la stack documentée dans Obsidian `Cahier/13_ACE_stack_et_molettes` — **meilleure référence opérationnelle récente**.

### Molettes (toutes ON sauf MIN_ENTRY variable)

| Molette | Env | Valeur | Rôle |
|---------|-----|--------|------|
| Duo PID watchdog | `NUAGE_DUO_PID_WATCHDOG` | **1** | Relance si jambe morte |
| BIDIR | `NUAGE_BIDIR_SIDES` | **1** | Côtés dynamiques |
| STORM_LATCH | `NUAGE_STORM_LATCH` | **1** | Bypass Mode Écoute si tension haute |
| STORM_HOLD | `NUAGE_STORM_SCOUT_HOLD` | **1** | Hold min ~20s en tempête |
| STORM_HUNTER | `NUAGE_STORM_HUNTER` | **1** | ALPHA peut armer sans revenge scout |
| **MIN_ENTRY** | `NUAGE_MIN_ENTRY_TENSION` | **2.5** (matin) / **3.0** (après-midi) | Vacuum / filtre entrée |
| Durée bloc | argv | **04:00:00** | Timer nominal 4h |
| Tag | argv | `NUAGE_PROD_4H` | |

### Commande type (à coller — **ne pas lancer sans GO humain**)

```bash
cd /Users/christophe/ace777-test-day1

NUAGE_BIDIR_SIDES=1 \
NUAGE_STORM_LATCH=1 \
NUAGE_STORM_SCOUT_HOLD=1 \
NUAGE_STORM_HUNTER=1 \
NUAGE_MIN_ENTRY_TENSION=2.5 \
./GO_USINE_NUAGE.sh 04:00:00 NUAGE_PROD_4H
```

Variante après-midi testée : `NUAGE_MIN_ENTRY_TENSION=3.0` (seule molette changée).

### Résultats observés (23 juil.)

| Fenêtre (UTC) | MIN_ENTRY | ALPHA | BETA | Combo |
|---------------|-----------|-------|------|-------|
| Matin ~06:37→10:37 | **2.5** | +~$14.71 | −~$0.87 | **≈ +$13.8** |
| Après-midi ~11:20→15:20 | **3.0** | +~$7.56 | +~$0.55 | **≈ +$8.1** |

**Caveat :** PnL souvent porté par **1 gros trade ALPHA** → edge fragile, pas encore « edge stable ».

### Signaux terrain récurrents

- `tension_stale age>800ms` = **latence alpage**, pas forcément bus duo mort  
- STORM_HUNTER peut **armer** sans fill si gate fraîcheur bloque  
- E16/E17 = patches anti faux-kill / boot (dans GO)

---

## 3. Dernière activité process (23–24 juil.)

| Artefact | Contenu |
|----------|---------|
| Nuit 23→24 | Run planifié fin `2026-07-24T00:31:21Z` · `WHY_ARRET=timer_nominal` (4h) |
| `NUIT_GHOST_RELANCE.log` | Armé 21:24Z · **pas de preuve** de 2ᵉ relance ACE dans ce fichier |
| Rapports erreurs 24 | Compteurs process/watchdog ; fills=0 sur certaines fenêtres de parse (rapports WHY à croiser avec PnL du 23) |
| Dernier LIVE_COLOR | `runs/NUAGE_PROD_4H_LIVE_COLOR.log` (mtime 24 juil.) — STORM_LATCH / STORM_HUNTER visibles |

**Depuis le 24 juil. :** focus Hulk (paper + veille + scoreur). ACE en pause volontaire.

---

## 4. Architecture en une phrase

Moteur bash **déterministe** (champion figé) + molettes via `GO_USINE` + duo SCOUT/HUNTER sur testnet ; **pas** de comité LLM dans le hot path ; Obsidian = leçons / bus décisions, pas le disque de fills.

---

## 5. Ce qu’on ne fait PAS (règles projet)

1. Ne pas modifier `genesis_manifest.txt`  
2. Ne pas lancer `GO_USINE` sans ordre humain explicite  
3. Ne pas confondre ACE (Binance testnet) et Hulk (MEXC paper)  
4. Une molette à la fois pour les prochains tests ACE  

---

## 6. Fichiers à lire pour un expert

1. `GO_USINE_NUAGE.sh` (ops)  
2. `genesis_manifest.txt` (lecture seule)  
3. Obsidian `Cahier/13_ACE_stack_et_molettes.md` · `03_ACE_lecons_molettes.md`  
4. `engle/JOURNAL_ERREURS.md` · `PLAN_STORM_WICK.md`  
5. Audit : `AUDIT_TROIS_JAMBES_SWARM_20260726.md` / `Cahier/14_…`

---

*Briefing prêt à coller chez un expert externe (Kimi / autre). ACE non relancé par ce document.*
