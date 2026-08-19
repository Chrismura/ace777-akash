# SPEC — Garde-fou PRIX FIGÉ (price_stasis) — 16/08/2026

**Statut :** à consulter famille · **Fichier cible :** `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt`
**Constat terrain :** run de test 16/08 07:19Z → 8 fills BETA sur 10 à pnl = 0.00000000
(entrée = sortie au même prix, hold 7–8s). Ex. fill #100 : tension=10.67, bid_drop=69.4%,
conf=0.9993 … prix FIGÉ à 63035.10 depuis 5 min. Le radar entre sur des signaux de carnet
(bid_drop) alors que le prix ne bouge pas (marché sans liquidité) → trades nuls + frais.

## Le bug

Le SCOUT (et le HUNTER en revenge) peut entrer quand `tension`/`bid_drop` sont hauts mais que
le **prix est figé** : les murs d'ordres bougent sans mouvement de prix (marché mort/testnet)
→ fausse « rupture imminente » → ordre → sortie flat 8s plus tard (`shock_inversion_stop`).
Pattern déjà présent au run de nuit (69/160 fills BETA flat = 43%).

## Le fix (minimal, 3 blocs + 1 variable)

Principe : **ne pas entrer si le prix n'a pas bougé d'au moins X bps sur la fenêtre Y s**.

### 1. Variables (près des autres `PRICE_*` / `STASE_*`)

```bash
PRICE_STASIS_GUARD="${PRICE_STASIS_GUARD:-TRUE}"        # garde-fou prix figé
PRICE_STASIS_MIN_MOVE_BPS="${PRICE_STASIS_MIN_MOVE_BPS:-1.0}"   # mouvement mini sur la fenêtre
PRICE_STASIS_WINDOW_SEC="${PRICE_STASIS_WINDOW_SEC:-30}"        # fenêtre d'observation
```

### 2. État glissant (avant la boucle principale, avec les autres `prev_*`)

```bash
price_stasis_ref_px=""
price_stasis_ref_ts=""
```

### 3. Le check (JUSTE AVANT l'exécution de l'ordre, après toutes les gates
radar → tension → tactic → stase → duo → qty → llm_gate ; `p2` = prix du cycle)

```bash
if [ "$PRICE_STASIS_GUARD" = "TRUE" ]; then
  now_ps="$(now_sec)"
  if [ -n "$price_stasis_ref_px" ]; then
    dt_ps=$((now_ps - price_stasis_ref_ts)); [ "$dt_ps" -le 0 ] && dt_ps=1
    if [ "$dt_ps" -ge "$PRICE_STASIS_WINDOW_SEC" ]; then
      move_bps="$(ruby -e 'a=(Float(ARGV[0]) rescue 0.0); b=(Float(ARGV[1]) rescue 0.0); a=1.0 if a<=0.0; printf("%.6f", ((b-a).abs/a)*10000.0)' -- "$price_stasis_ref_px" "$p2")"
      if num_lt "$move_bps" "$PRICE_STASIS_MIN_MOVE_BPS"; then
        echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,price_stasis,,reason=price_frozen move_bps=$move_bps window=${dt_ps}s" >> "$LOG_FILE"
        sleep "$SLEEP_SEC"
        continue
      fi
      price_stasis_ref_px="$p2"; price_stasis_ref_ts="$now_ps"
    fi
  else
    price_stasis_ref_px="$p2"; price_stasis_ref_ts="$now_ps"
  fi
fi
```

Logique : on pose un point de référence ; quand la fenêtre (30s) est atteinte, on compare le
prix courant à la référence → mouvement < 1 bps = prix figé = SKIP `price_stasis` (raison
visible dans CSV + log) ; sinon entrée OK et nouvelle référence. Premier cycle : référence
posée sans blocage (pas de ref → pas de check). Le check est dans la section d'entrée COMMUNE
→ s'applique au SCOUT (BETA) ET au HUNTER (ALPHA).

## Contraintes

1. Ne modifier QUE ces 3 blocs + la variable. Aucune autre ligne.
2. `num_lt` / `num_sub` / `now_sec` existent déjà (réutiliser, pas de nouvelle fonction).
3. Le skip utilise le format CSV exact : `,,0,price_stasis,,reason=...` (12 colonnes).
4. Défaut `TRUE` (le but est de bloquer les trades nuls) — réversible par env `PRICE_STASIS_GUARD=FALSE`.

## Effets attendus

- Marché figé : 0 entrée (fini les fills à pnl 0.00000000 + frais).
- Marché vivant (> 1 bps / 30s) : aucune entrée bloquée.
- Le duo n'est pas touché : le check se fait APRÈS le duo → un revenge reste possible dès que
  le prix bouge (le fix last_loss_ts du matin est conservé intact).

## Questions pour la famille

1. Seuils : 1.0 bps / 30s raisonnables ? (BTC actif ≈ 0.1–1 bps/s)
2. Défaut TRUE ou FALSE (sécurité vs comportement attendu) ?
3. Le skip doit-il compter comme un `duo_wait`/skip classique (juste visible) ou faut-il une
   métrique dédiée (ex. compteur dans le rapport) ?
4. Risque de faux positifs sur les entrées « wall collapse » légitimes (rupture de mur SANS
   mouvement de prix encore) — faut-il une exception (ex. tension > seuil très haut) ?
