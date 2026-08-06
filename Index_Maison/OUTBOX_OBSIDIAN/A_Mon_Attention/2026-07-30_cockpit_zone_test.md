# Attention — Cockpit prototype en ZONE TEST

**Date :** 2026-07-30  
**Statut :** `GARDÉ` · S22 → **TEST**  
**Canon :** [[COCKPIT_LOOK_FIGE]] · `Index_Maison/cockpit/index.html`

## Décision
On sort de la zone maquette pure : le **prototype cockpit** entre en **test sur les runs**.  
Vérifier les **indicateurs cockpit** fait désormais partie de l’**hygiène** (pas un à-côté).

## Après-midi livré (en un endroit)
| Bloc | Contenu |
|------|---------|
| OPS | Duo α/β live · Hulk bags (crypto/qty/entrée/mark/PV) · histo BUY/SELL · shoot FX |
| THERMO | Petit clin d’œil F&G · MC · funding/OI |
| BOARD | Page thermo complète SIMPLE/COMPLET · indicateurs A/B/C gardés (`thermo/index.html`) |
| VOL | Plan de vol + sniff + carte « après-midi en test » |
| Cortana | Orb · mute/speak · news ~14 s + chime doux · pré-son avant TTS · pont 17777 |
| Hygiène | `scripts/cockpit_hygiene_check.sh` branché dans `grosse_hygiene` + checkup garage |
| Journal produit | [[JOURNAL_COCKPIT]] — horloge / évolution (≠ journal erreurs trading) |

## Commandes
```bash
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_hygiene_check.sh
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_cockpit_bridge.py
open ~/ace777-test-day1/Index_Maison/cockpit/index.html
```

## Règle
Cockpit = **lecture** pendant les tests. GO trading = toujours Terminal + humain.  
Évolution / bugs UI → [[JOURNAL_COCKPIT]].
