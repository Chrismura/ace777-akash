# REPRISE — Setup NUAGE amélioré (2026-07-18)

**Lis ceci en premier** à la prochaine ouverture Cursor / Terminal.  
Rien n’a été écrasé : l’**original usine** est dans `00_ORIGINAL_USINE/`.

## État figé

| Élément | Valeur |
|---------|--------|
| Champion | md5 `37fca367…` — **INTACT** (ne jamais modifier) |
| Snapshot usine | `launch_…NUAGE_V2.2.1.sh` cksum **`812033996 22672`** — INDEX SYNC: **OFF** |
| Lanceur confiance | `./GO_USINE_NUAGE.sh` (défaut **4h**) |
| Setup | `vide_froid_binance` — BETA 200 / ALPHA 800 USDT — testnet |

## Améliorations incluses (couches au-dessus de l’usine)

1. **Wait-timer** — fin de mission = timer, pas wrappers (dans `GO_USINE`)
2. **A1** — `scripts/swarm_telemetry.rb` (`tmp.$$` + flock)
3. **A2 léger** — `scripts/irm_tension.rb` (météo lecture seule, pas de SKIP live)
4. **Hygiène Mac** — `scripts/hygiene_mac_ram.sh` (WebKit orphelins stale)
5. **Règle Cursor** — `ace777-run-test-protocol.mdc` (hygiène avant run)
6. **Bilans** — `generate_pnl_report.rb` + `update_state_md.sh` (PnL correct)

## Lancer un run (Terminal de Christophe — pas l’agent)

```bash
cd /Users/christophe/ace777-test-day1
./scripts/hygiene_mac_ram.sh
./scripts/verif_sterilite.sh --pre-run   # STERILE=OK
./GO_USINE_NUAGE.sh
```

Boot attendu : `INDEX SYNC: OFF` + `IRM météo` + `attente timer`.

## Vérifier que ce coffre est intact

```bash
cd /Users/christophe/ace777-test-day1
./29\$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/VERIFY.sh
```

## Restaurer un fichier du setup amélioré (si écrasé)

Exemple :

```bash
ROOT=/Users/christophe/ace777-test-day1
C="$ROOT/29\$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/01_SETUP_AMELIORE_ACTUEL"
cp -p "$C/GO_USINE_NUAGE.sh" "$ROOT/"
cp -p "$C/scripts/"* "$ROOT/scripts/"
cp -p "$C/cursor_rules/ace777-run-test-protocol.mdc" "$ROOT/.cursor/rules/"
```

**Original usine** (jamais « améliorer » le fichier snapshot vivant sans copie) :

```bash
# déjà aussi dans V3.5/snapshots/ — cksum 812033996 22672
ls -la "$ROOT/29\$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/00_ORIGINAL_USINE/"
```

## Historique plus large

Voir `04_HISTORIQUE_LIENS/OU_EST_LHISTORIQUE.md`  
+ coffre V3.5 + `engle/INVENTAIRE_SETUPS_LEGER.md` (févr.–mars + juillet).
