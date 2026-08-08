# INVENTAIRE LÉGER — setups / enveloppes / archives

> Généré: 2026-07-17 23:19 · mode économe · pas de lecture profonde des CSV/logs

## Lecture rapide

Deux couches sur le disque :

1. **~3 mois (févr.–mars 2026)** — l’« avant Engle nommé »  
   - `SESSION_MEMO_NEXT.md` (27/02) : sniper BUY=500, radar 0.95, index ON, soft ON  
   - `master_base/` + `master_plus_value/` (mars) : modèles / setups / pnl  
   - `closure_20260225_1756/` + `deploy/` : archives  

2. **Juillet 2026** — NUAGE (hasard vocal → trading)  
   - Usine : `29$/…/snapshots/…NUAGE_V2.2.1.sh`  
   - Confiance : `GO_USINE_NUAGE.sh`  
   - Théorie déjà écrite : `29$/…/PARTIE_04_THEORIE.md` (gate 800 ms, whipsaw)  
   - Profils : `config_profiles/vide_froid_*.env`, `vortex_v2_collab.env`  

Pour retrouver Engle : **SESSION_MEMO + master_base + PARTIE_04** d’abord — les `SAUVE_*.sh` de juillet sont surtout des filets, pas la source.

## Sauvegarde figée setup juillet (2026-07-18)

- Coffre : `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/` → lire `REPRISE.md`
- Tar : `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718.tar.gz`
- Pointeur racine : `SAUVEGARDE_SETUP_ACTUEL.md` — **original usine inclus** + setup amélioré + champion

## Priorité

1. `SESSION_MEMO_NEXT.md` + CSV `run_sniper_v1_500_*`
2. `master_base/` / `master_plus_value/setups`
3. `29$/…/PARTIE_04_THEORIE.md`
4. Snapshots usine NUAGE dans `29$/`
5. `config_profiles/` + `bonnet_forme_champion/`

## Liste (date mtime · chemin · intention)

| Date | Type | Chemin | Intention |
|------|------|--------|-----------|
| 2026-07-17 | FILE | `engle/MATRICE_QUANT_ROBERT_ENGLE.md` | matrice / mémoire Engle (R&D) |
| 2026-07-17 | DIR | `engle` | matrice / mémoire Engle (R&D) |
| 2026-07-17 | FILE | `launch_vide_froid_4h_binance_NUAGE_TIMER_WAIT.sh` | enveloppe NUAGE + wait-timer |
| 2026-07-17 | FILE | `GO_USINE_NUAGE.sh` | enveloppe essaim NUAGE |
| 2026-07-17 | FILE | `launch_test_master_base_v8_6_fortress.sh` | couche fortress mince / master |
| 2026-07-17 | FILE | `launch_vide_froid_4h_binance_NUAGE_INDEX_SYNC.sh` | variante NUAGE index sync (à éviter vs usine OFF) |
| 2026-07-17 | FILE | `launch_vide_froid_8h_alpha_plus14_radar0618_8h.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/INDEX.md` | sauvegarde / point de restore |
| 2026-07-17 | FILE | `launch_vide_froid_hybrid_4h_live.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `launch_vide_froid_8h_binance.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `launch_vide_froid_8h_alpha_plus14.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `launch_test_master_base_v8_7_qwen_tween.sh` | à classer |
| 2026-07-17 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/parties/PARTIE_02_SEMANTIQUE.md` | sauvegarde / point de restore |
| 2026-07-17 | FILE | `launch_4h_fortress_exact.sh` | couche fortress mince / master |
| 2026-07-17 | FILE | `bonnet_forme_champion/genesis_manifest.txt` | bonnet forme champion (kit) |
| 2026-07-17 | FILE | `bonnet_forme_champion/CHECKSUMS.txt` | bonnet forme champion (kit) |
| 2026-07-17 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/parties/PARTIE_03_JALON_29USD.md` | sauvegarde / point de restore |
| 2026-07-17 | FILE | `config_profiles/cortical_shadow_glm.env` | profil config |
| 2026-07-17 | FILE | `launch_test_master_base_v8_5_impact_GEMINI_TEST.sh` | lanceur GEMINI test (levier/ramp) |
| 2026-07-17 | FILE | `config_profiles/vide_froid_classic.env` | setup vide froid binance |
| 2026-07-17 | FILE | `launch_vide_froid_4h.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/parties/PARTIE_01_STERILITE.md` | sauvegarde / point de restore |
| 2026-07-17 | FILE | `launch_vide_froid_8h.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `launch_vortex_v2_collab_4h_detached.sh` | vortex v2 collab Gemini/Cursor |
| 2026-07-17 | FILE | `launch_vide_froid_8h_400_400.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `launch_250_4h.sh` | à classer |
| 2026-07-17 | FILE | `launch_vide_froid_4h_binance.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `bonnet_forme_champion/REFERENCE.txt` | bonnet forme champion (kit) |
| 2026-07-17 | FILE | `REGLES_SCRIPTS_SETUPS.md` | règles setups |
| 2026-07-17 | FILE | `launch_production_officiel.sh` | à classer |
| 2026-07-17 | FILE | `config_profiles/vide_froid_hybrid_reference.env` | setup vide froid binance |
| 2026-07-17 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/conversation/README.md` | sauvegarde / point de restore |
| 2026-07-17 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/parties/PARTIE_05_OBSIDIAN.md` | sauvegarde / point de restore |
| 2026-07-17 | FILE | `config_profiles/masse_250.env` | profil config |
| 2026-07-17 | FILE | `launch_test_master_base_v8_5_impact.sh` | master impact v8.5 |
| 2026-07-17 | FILE | `bonnet_forme_champion/ARRETER.sh` | bonnet forme champion (kit) |
| 2026-07-17 | FILE | `launch_vide_froid_8h_alpha_plus14_radar060_2m.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `bonnet_forme_champion/LANCER.sh` | bonnet forme champion (kit) |
| 2026-07-17 | FILE | `config_profiles/vortex_v2_collab.env` | vortex v2 collab Gemini/Cursor |
| 2026-07-17 | FILE | `launch_vide_froid_hybrid_4h_binance.sh` | setup vide froid binance |
| 2026-07-17 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5.md` | sauvegarde / point de restore |
| 2026-07-17 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/parties/PARTIE_04_THEORIE.md` | sauvegarde / point de restore |
| 2026-07-17 | FILE | `launch_vortex_v2_collab_4h_binance.sh` | vortex v2 collab Gemini/Cursor |
| 2026-07-15 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/rapports/RAPPORT_PNL_AUTO_20260710_204206.md` | sauvegarde / point de restore |
| 2026-07-15 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/rapports/RAPPORT_PNL_AUTO_20260710_193940.md` | sauvegarde / point de restore |
| 2026-07-15 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/rapports/RAPPORT_PNL_AUTO_20260710_163716.md` | sauvegarde / point de restore |
| 2026-07-15 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/rapports/RAPPORT_PNL_AUTO_20260710_083706.md` | sauvegarde / point de restore |
| 2026-07-15 | FILE | `29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh` | enveloppe essaim NUAGE |
| 2026-07-15 | FILE | `29$/historique/snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh` | enveloppe essaim NUAGE |
| 2026-07-13 | FILE | `29$/historique/scripts/launch_test_master_base_v8_5_impact_GEMINI_TEST.sh` | lanceur GEMINI test (levier/ramp) |
| 2026-07-12 | FILE | `29$/historique/scripts/launch_vortex_v2_collab_4h_binance.sh` | vortex v2 collab Gemini/Cursor |
| 2026-07-12 | FILE | `29$/historique/scripts/launch_test_master_base_v8_5_impact.sh` | master impact v8.5 |
| 2026-07-12 | FILE | `launch_test_master_base_v8_5_impact_GEMINI_TEST.sh.SAUVE_20260712_avant_restore_final` | lanceur GEMINI test (levier/ramp) |
| 2026-07-12 | FILE | `launch_vortex_v2_collab_4h_binance.sh.SAUVE_20260712_avant_restore_final` | vortex v2 collab Gemini/Cursor |
| 2026-07-12 | DIR | `bonnet_forme_champion` | bonnet forme champion (kit) |
| 2026-07-12 | FILE | `bonnet_forme_champion/launch_vortex_v2_collab_4h_binance.sh` | vortex v2 collab Gemini/Cursor |
| 2026-07-12 | FILE | `launch_vortex_v2_collab_4h_binance.sh.SAUVE_20260712_avant_restore_identique` | vortex v2 collab Gemini/Cursor |
| 2026-07-12 | FILE | `launch_vortex_v2_collab_4h_binance.sh.SAUVE_20260712_avant_restore_champion204206` | vortex v2 collab Gemini/Cursor |
| 2026-07-11 | FILE | `launch_vortex_v2_collab_4h_binance.sh.SAUVE_avant_gravure_champion` | vortex v2 collab Gemini/Cursor |
| 2026-07-11 | FILE | `launch_vortex_v2_collab_4h_binance.sh.SAUVE_avant_purge_relaunch` | vortex v2 collab Gemini/Cursor |
| 2026-07-11 | FILE | `launch_test_master_base_v8_5_impact_GEMINI_TEST.sh.SAUVE_20260711_1336` | lanceur GEMINI test (levier/ramp) |
| 2026-07-11 | FILE | `launch_vortex_v2_collab_4h_binance.SAUVE_V2.sh` | vortex v2 collab Gemini/Cursor |
| 2026-07-11 | FILE | `launch_test_master_base_v8_5_impact.SAUVE_V2.sh` | master impact v8.5 |
| 2026-07-10 | FILE | `launch_test_master_base_v8_5_impact.ORIGINAL.sh` | master impact v8.5 |
| 2026-07-09 | DIR | `config_profiles` | profil config |
| 2026-07-08 | FILE | `SESSION_MEMO_NEXT.md` | mémo session suivante |
| 2026-03-12 | DIR | `master_plus_value` | à classer |
| 2026-03-12 | DIR | `master_base` | à classer |
| 2026-03-08 | DIR | `deploy` | déploiement |
| 2026-02-25 | DIR | `closure_20260225_1756` | closure archive |

_Total listé: 70 / 70 candidats · buckets ≥60j=4, 14–60j=0, <14j=66_
