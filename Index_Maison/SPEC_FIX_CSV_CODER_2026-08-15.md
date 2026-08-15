# SPEC CODEUR — Correctif CSV (logging-only) — genesis scellé

**Statut :** validé famille 4/4 (gemini, nvidia, juge, ultra) le 15/08/2026.
**Rôle :** toi = codeur (code.ia) · Buffy = superviseur (vérifie ton diff, ne code pas).
**Fichier cible :** `~/ace777-test-day1/genesis_manifest.txt` (scellé md5 `8d9ee8d6`).

## But

Rendre chaque ligne CSV conforme à son en-tête (12 colonnes). L'en-tête (ligne 393) :
`ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg`

Aujourd'hui les 16 écritures CSV (`grep '>> "$LOG_FILE"'`) sortent **11 champs** :
la colonne 11 (holdSec) contient le message de diagnostic, la colonne 12 (msg)
n'est jamais écrite, et pour FILLED la durée `$hold_done` (calculée ligne 2490,
affichée au terminal ligne 2516) n'arrive pas au CSV.

## Règle de transformation (uniforme)

Insérer **un champ supplémentaire** juste après le 10e champ (exitReason) et
avant le message :
- ligne **FILLED** (2507) → insérer `$hold_done` (durée en secondes) ;
- les **15 autres** lignes → insérer un champ **vide**.

Aucune autre modification. Ne toucher ni la logique de trading, ni les 10
premiers champs, ni l'en-tête.

## Lignes concernées (16)

1523 (gap_guard_pause), 1537 (duo_partner_pause), 1706 (hashrate_block),
1801 (radar_block), 1813 (impulse_resonance_wait), 1821 (vacuum_filter),
1835 (tactic_mismatch), 1851 (stase_ecoute), 1869 (OBSERVE), 1931 (duo_wait),
1981 (qty_too_small), 2039 (llm_gate), 2067 (ENTRY_ERROR), 2119 (ENTRY_ERROR),
2441 (EXIT_ERROR), 2507 (FILLED).

## Exemple exact

**2507 AVANT :**
```
echo "$(date -u +%FT%TZ),$i,$side,FILLED,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,radar=$radar_direction conf=$radar_conf size_note=$dynamic_size_note soft=$cycle_soft_mode pct=$pct tension=$tension_score bid_drop=$wall_drop_bid_pct ask_drop=$wall_drop_ask_pct" >> "$LOG_FILE"
```
**2507 APRÈS :**
```
echo "$(date -u +%FT%TZ),$i,$side,FILLED,$entry_price,$exit_price,$qty,$bps,$pnl_usdt,$reason,$hold_done,radar=$radar_direction conf=$radar_conf size_note=$dynamic_size_note soft=$cycle_soft_mode pct=$pct tension=$tension_score bid_drop=$wall_drop_bid_pct ask_drop=$wall_drop_ask_pct" >> "$LOG_FILE"
```

**1801 AVANT :** `...,0,radar_block,reason=$radar_reason conf=...` (11 champs)
**1801 APRÈS :**  `...,0,radar_block,,reason=$radar_reason conf=...` (12 champs, holdSec vide)

## Consommateurs (à vérifier, pas forcément à modifier)

- `scripts/irm_tension.rb` : lit `cols[11]` d'abord → déjà compatible.
- `Index_Maison/scripts/cockpit_mission_feed.py` : `DictReader` par nom (holdSec/msg) → compatible.
- `Index_Maison/scripts/rapport_perf_bots.py` : `DictReader` par nom → compatible.
- `scripts/verifier_test.sh` : ne vérifie que sha256/md5 → non impacté.

## Livrable demandé

1. Le **diff exact** (before/after) pour chacune des 16 lignes.
2. La liste des consommateurs qui casseraient réellement (avec la preuve), ou
   la confirmation qu'ils sont forward-compatibles.
3. La procédure de smoke test (3-5 cycles → vérifier 12 colonnes partout,
   `holdSec` numérique sur FILLED, `msg` rempli) avant re-scellement.

Réponds en diff exact, pas de paraphrase.
