# CHANTIER — Branchement ONCHAIN (baleines BTC) → Cortana + Ada (15/08/2026)

**Statut** : ✅ LIVRÉ et TESTÉ · famille GO-AVEC-RÉSERVE (gemini 75% / nvidia 72%) · réversible

## Contexte
Le module `surveiller_whales.py` (scan mempool.space, gros blocs ≥1000 BTC + fragmentation
≥500 BTC, 4 adresses vérifiées) tournait depuis le 14/08 mais **rien n'injectait ses données**
dans le contexte Cortana/Ada, et son lanceur était un daemon `/tmp` (mort au reboot).

## Ce qui a été fait
| Livrable | Détail |
|---|---|
| `scripts/pont_onchain.py` | Lit le scan → injecte la section `onchain` dans `thermo/live.json` (atomique, idempotent, kill-switch). Clés : blocs N/BTC, frag N/BTC, cumul 24h, moy7j, direction, source, écart seuil, alerte, dernierEvtMin, **synthèse textuelle** |
| `cortana_analyse.py` | Indice `onchain` dans LEXIQUE + branche build_facts → Cortana reçoit la **synthèse pré-mâchée** (pas les chiffres bruts — verdict famille) |
| `ada_gardienne.py` | `calculer_voilure(p, thermo)` : modulateur onchain ±10% (outflow massif → ×0.93, inflow fort → ×1.05, sinon 1.0), jamais de blocage |
| `plists/com.ace777.whales.plist` | Launchd StartInterval=300, remplace le daemon /tmp (survit aux reboots) |

## Tests réels (5/5 + bout en bout)
1. Pont : injection section onchain ✅ · autres clés live intactes ✅
2. Ada : sans thermo = inchangé (91.4) · outflow massif = 85.0 (×0.93) ✅ · inflow = 96.0 (×1.05) ✅ · calme = inchangé ✅ · extrême jamais 0 ✅
3. Cortana : `--list` reconnaît onchain ✅ · analyse réelle via hub : **NEUTRE, confiance faible** (disciplinée à 46%) — « les baleines restent à l'ancre » ✅
4. Plist : chargée (launchctl), premier scan 19:50:08Z loggé, daemon /tmp arrêté, **un seul scan** ✅

## Erreurs du codeur corrigées par la supervision
1. **Code invalide** : `from pathliblib_check = lambda p: True` (ne compile pas) + `Path` utilisé avant import
2. **Structures fausses** : lisait `transactions`/`amount_btc`/`seuil_btc`/`labels` — réelles : `gros_blocs`/`fragmentations`/`btc`/`portefeuilles[]`
3. **Diffs Cortana/Ada inventés** (variables inexistantes) → branchés sur les vrais points d'ancrage (LEXIQUE/build_facts, calculer_voilure)
4. **plist chemin faux** `/Users/ace/...` → `/Users/christophe/...`

## Réversibilité
- `launchctl unload ~/Library/LaunchAgents/com.ace777.whales.plist` + `rm` → daemon /tmp
  peut être relancé (lancer_whales.py toujours là) ou la plist réinstallée.
- `rm pont_onchain.py` + retirer la section onchain de live.json = retour à l'état antérieur.
- Modifs cortana_analyse/ada_gardienne : minimales et documentées (rollback = inverse).
- Release Receipt : RELEASE_RECEIPT_onchain_2026-08-15.md
