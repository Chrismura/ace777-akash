# CHANTIER — Kill-switch déterministe global Hulk (STANDBY veille muette) — 15/08/2026

**Statut : APPLIQUÉ + TESTÉ** · hors genesis (outil paper) · réversible.

## Contexte
La veille (digest_watch.py) peut mourir sur le réseau WiFi/alpage. Si muette trop longtemps, Hulk est AVEUGLE et ne doit plus ouvrir de NOUVELLE position. Kill-switch validé famille (nvidia, chantier Hulk n°2).

## Fix appliqué
- **Signal de fraîcheur** = mtime de `DIGEST_LATEST.md` (réécrit à chaque cycle de la veille).
- **`veille_stale()`** (veille_gates.py) : si mtime > `VEILLE_STALE_HOURS` (6h) → `(True, "veille_stale_Xh>6h")`. Fail-open si fichier absent/corrompu.
- **`buy()`** (paper_diprip.py) : gate globale AVANT le entry_gate_check → si stale → `STANDBY` + SKIP log, retour sans acheter. Les VENTES/stops/bags/DCA (existant) ne sont PAS touchés.
- **Heartbeat** : indicateur `STANDBY(...)` ajouté.
- **defaults.env** : `VEILLE_STALE_HOURS=6`.

## Fichiers modifiés
- `hulk-mexc/scripts/veille_gates.py` : + `veille_stale()`.
- `hulk-mexc/scripts/paper_diprip.py` : import + config + gate buy + heartbeat.
- `hulk-mexc/config/defaults.env` : + `VEILLE_STALE_HOURS=6`.

## Vérifications (toutes vertes)
1. `py_compile` veille_gates.py + paper_diprip.py → OK.
2. Test fonctionnel 5/5 : absent→(False,"") · frais→(False,"") · 10h→(True,"veille_stale_10.0h>6h") · 6h/max5h→(True) · 6h/max12h→(False).
3. Réel : `veille_stale(runs, 6h)` = (False,"") actuellement (digest 17:28 frais) → pas de faux déclenchement.
4. `sell_trade`/`stake_out_half`/bag/DCA non touchés.

## Prise d'effet
Le process Hulk tourne encore (PID 68481) → le kill-switch prend effet au **prochain redémarrage** de paper_diprip.py.

## Retour arrière (réversible)
- `git checkout -- hulk-mexc/scripts/veille_gates.py hulk-mexc/scripts/paper_diprip.py`
  ou ré-appliquer en inverse les 6 blocs OLD du `SPEC_FIX_KILLSWITCH_HULK_2026-08-15.md`.
- `defaults.env` : supprimer la ligne `VEILLE_STALE_HOURS=6`.

## Suite logique (validée famille)
3. **Brancher Cortana** en pilote de paramètres (contrat JSON Cortana↔moteur).
   Et en parallèle : chantier « 2 classes de paires » (core liquides vs small caps bag) validé ce jour.
