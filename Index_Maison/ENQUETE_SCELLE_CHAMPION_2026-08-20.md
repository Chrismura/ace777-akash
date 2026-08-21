# ENQUÊTE — SCELLÉ CHAMPION (md5) — 20/08/2026

**Statut :** ✅ RÉSOLU — re-scellage `01c38510` · **PULSE=NOK expliqué et corrigé**

## Le constat (20/08, SOUS_L_OEIL : `PULSE=NOK`)

- Champion scellé (16/08) : `8bce77b1…` — **n'existe plus sur disque**
- Champion disque : `01c3851013e17a9b5c3e71064023c7ed`
- `GO_USINE_NUAGE.sh` et `preflight_ace777.sh` refusaient tout lancement : "champion disque altéré"

## La vérité (pas une altération)

| Vérification | Résultat |
|---|---|
| `git status` champion | ✅ propre (aucune modif non tracée) |
| md5 disque vs md5 HEAD git | ✅ identiques (`01c38510…`) |
| Dernier commit | `1e318498` **S-10 #1,#2,#3 : le bot pense en NET et reduit ses frais** (19/08 15:43) |

**Le champion a été légitimement patché par le commit S-10 le 19/08** (migration Algo Order API V4 + mode NET/MAKER)… mais **personne n'a re-scellé** : `CHAMPION_ACTIF` disait encore `5a0a6797` (17/08) et `GO_USINE_NUAGE.sh` disait `8bce77b1` (16/08).

## ⚠️ Le point important

Le patch S-10 est arrivé **pendant le run 96h** (`MASTER_VORTEX_V2_COLLAB_4H`), dont le commit lui-même dit "Prend effet au prochain relancement". **Mais les relances automatiques ont rechargé le nouveau champion à mi-course** → les stops ont basculé sur algoOrder V4 → `stop_market_fail` (`-2021 Order would immediately trigger`) en série → positions sans stop → pire trade −82 $.

**Le scellé n'était pas le problème : c'est la procédure qui a sauté** (patch en plein vol + relances auto sans re-vérification).

## Actions faites (20/08)

1. `Index_Maison/strategie/CHAMPION_ACTIF` → `01c38510` (backup : `/tmp/CHAMPION_ACTIF.bak_20260820`)
2. `GO_USINE_NUAGE.sh` → `EXPECT_MD5_PREFIX="01c38510"` + 3 checks `[[ "$_md5_disk" == 01c38510* ]]`
3. Vérification : check champion ✅ intègre, zéro référence `8bce77b1` restante

## Règle pour la suite

- **Tout patch du champion = re-scellage immédiat** (`CHAMPION_ACTIF` + `GO_USINE_NUAGE.sh` + préfixe vérifié), même si le patch est "au prochain relancement".
- **Jamais de patch en plein run** : si un run 96h tourne avec relances auto, un patch devient actif à mi-course sans que personne ne le décide.
