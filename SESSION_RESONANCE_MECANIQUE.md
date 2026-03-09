# Resonance Mecanique

Profil memorise pour test immediat:

- Nom session: `Resonance Mecanique` (Master Base V8.5 IMPACT)
- Lanceur principal: `./launch_test_master_base_v8_5_impact.sh`
- Lanceur compat: `./launch_test_master_base_v8_4_impact.sh`
- Lanceur legacy: `./launch_test_master_base_v8_3_synapse.sh`
- Duree: `27000s` (7h30)
- Base setup:
  - `MOMENTUM_THRESHOLD=0.85`
  - `ALPHA_REVENGE_MULT=1.618`
  - `GLOBAL_STOP_USDT=-16.00`
  - `STOP_LOSS_BPS=16`

Modele V8.5 Tension + Impact active:

- Capteur de Percussion: `IMPULSE_RESONANCE` via carnet d ordres (`drop >= 4%` en `128ms`)
- Filtre du Vide: entrees bloquees si `tension < 0.85` (froid absolu)
- Force-entry tension: si `tension >= 3.5`, bypass wall collapse + publication `true_vacuum`
- Run state checkpoint: `run_state.current_tier` + `run_state.start_ts` ecrits dans `runs/duo_session.json`
- Reprise rampe: lecture `run_state` au demarrage pour reprendre au palier precedent
- Etau scaling: passage auto des paliers `5 -> 8 -> 13` selon `total_pnl` (`1.0` puis `3.0`)
- Inducteur d Aspiration: entree forcee dans le sens du vide de liquidite
- Module Aspiration: masse `1.618` si angle de rupture `>= 37.8`
- Module Vide: verrous en pas de `16s` + `GLOBAL_STOP` en mode `HALT`
- Sortie Inversion de Choc: sortie immediate si vitesse de bougie quasi nulle
- BETA_SENTINEL (x3->x5): check a `256ms`, coupe immediate si `pnl < 0`
- ALPHA_STRIKE (x13): actif uniquement apres `true_vacuum` publie par BETA
- FLUID_EXIT: close total sur freinage/inversion du velocity vector

Convention de versionnage (a partir de maintenant):

- Base: `V8.5`
- Evolutions: `V8.5.1`, `V8.5.2`, `V8.5.3`, etc.
- Principe: on garde la base stable et on ajoute les updates incrementales.

Dernier PnL memorise (run complet):

- Run: `MASTER_BASE_V8_5_IMPACT_7H30`
- Fenetre: `2026-03-06T09:19:40Z` -> `2026-03-06T16:48:01Z`
- ALPHA: `orders=0` `net=0.0000`
- BETA: `orders=506` `win=226` `loss=191` `flat=89` `winrate=44.66%` `net=+4.5376`
- TOTAL: `net=+4.5376` `profit_factor=1.2321`
- Parties:
  - `PARTIE_1 net=+2.9149`
  - `PARTIE_2 net=+0.3147`
  - `PARTIE_3 net=+1.3080`

Relance propre:

```bash
cd /app
rm -f STOP STOP_ALPHA STOP_BETA runs/duo_state.json runs/duo_session.json
./launch_test_resonance_mecanique_v8.sh
# ou (recommande V8.5):
./launch_test_master_base_v8_5_impact.sh
```

Arret propre:

```bash
cd /app
touch STOP_ALPHA STOP_BETA
```
