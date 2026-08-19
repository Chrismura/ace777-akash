---
statut: AUTORISE
ts: 2026-08-16T09:30Z
pertinence: PERTINENT
sentiment: TRANQUILLE
auteur: Christophe (via Buffy)
---

# ✅ AUTORISATION Christophe — ACE re-scellé le 16/08 (FIX-LAST-LOSS)

**À toutes les veilleuses (Cortana, superviseur, agents) : la modification du champion ACE
du 16/08 est AUTORISÉE et documentée. Aucune alerte à lever.**

## Quoi exactement

- Fichier : `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` (symlink `genesis_manifest.txt`)
- Re-scellage : md5 `95d93d50…` → **`8bce77b1…`** (prefix `8bce77b1`)
- Nature : **FIX-LAST-LOSS** — le TTL revenge du duo Scout/Hunter se base désormais sur le
  champ `last_loss_ts` (nouveau) au lieu de figer `ts_ms` (fix du 15/08 qui avait éteint le
  revenge : 0 revenge, PnL +0.28 au lieu de +2 à +28).

## Pourquoi (résumé)

Le fix du 15/08 (FIX-HEARTBEAT) a tué le mécanisme revenge du HUNTER (ALPHA) : 12 fills au lieu
de 26–65, PnL ALPHA −0.08. Christophe a choisi la recommandation nvidia (verdict famille du
15/08) : TTL revenge 120s (`DUO_REVENGE_TTL_SEC`) sur `last_loss_ts`, heartbeat toujours frais.
Détail complet : `ANALYSE_RUNS_2026-08-16.md`.

## Mise à jour 11:00Z — 2ᵉ re-scellage du jour (FIX-PRICE-STASIS)

Le champion a été re-scellé une 2ᵉ fois dans la journée (toujours AUTORISÉ par Christophe) :
md5 `8bce77b1…` → **`8bce77b1…`** (nouveau hash complet, même préfixe).

- Nature : **FIX-PRICE-STASIS** — garde-fou « prix figé » : plus d'entrée si le prix n'a pas
  bougé d'au moins 0.5 bps sur 30s (élimine les fills à pnl 0.00000000 sur marché mort, 8/10
  dans le run du matin). Verdict famille 4/4 GO-AVEC-RÉSERVE : `CONSULTATION_FAMILLE_PRICE_STASIS_20260816/VERDICT_FAMILLE.md`.
- Le FIX-LAST-LOSS du matin est conservé intact (le check price_stasis se fait APRÈS le duo).
- Backup : `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_avant_fix_price_stasis_20260816` (md5 `3d760592…`).
- Chantier : `Index_Maison/CHANTIER_FIX_PRICE_STASIS_2026-08-16.md`.

## Preuves / traçabilité

- Chantier : `Index_Maison/CHANTIER_FIX_LAST_LOSS_TTL_2026-08-16.md`
- Analyse : `Index_Maison/ANALYSE_RUNS_2026-08-16.md`
- Backup avant modif : `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_avant_fix_last_loss_ttl_20260816`
- Rollback documenté dans le chantier (1 commande `cp` + réfs md5)
- Vérifié : `bash -n` OK, `ruby -c` OK, test fonctionnel 4/4, réfs md5 à jour partout.

## Checks md5 mis à jour (16/08)

| Fichier | Avant | Après |
|---------|-------|-------|
| `GO_VORTEX_V2.sh` | 95d93d50 | 8bce77b1 ✅ |
| `GO_USINE_NUAGE.sh` (4 occurrences) | 37fca367 | 8bce77b1 ✅ |
| `scripts/preflight_ace777.sh` | 95d93d50 | 8bce77b1 ✅ |
| `scripts/verif_pre_run_3x.sh` | 95d93d50 | 8bce77b1 ✅ |
| `scripts/verif_setup_champion.sh` | 95d93d50 | 8bce77b1 ✅ |
| `scripts/superviseur_core.sh` | 37fca367 | 8bce77b1 ✅ |
| `scripts/cortana_cockpit_bridge.py` | 37fca367 | 8bce77b1 ✅ |
| `scripts/checkup_garage.sh` | 37fca367 | 8bce77b1 ✅ |
| `scripts/pulse_sous_loeil.sh` | 37fca367 | 8bce77b1 ✅ |

## Consigne

- **Cortana** : champion = OK (8bce77b1), pas d'alerte « modification de ace ».
- **Superviseur / pulse / checkup** : le check `Champion` doit repasser OK au prochain cycle.
- **Prochain run de test** : `cd ~/ace777-test-day1 && ./GO_VORTEX_V2.sh 02:00:00` (INDEX_COMMANDES §11).

---
*Note d'autorisation écrite le 16/08 par Christophe (via Buffy) — fait foi.*
