# Cockpit ACE777 — Look figé (Arcade Radar)

**Statut :** 🟡 **ZONE TEST** — CRT maquette × data live · essai sur runs  
*(« fusée » = métaphore — pas de UI fusée)*

**Statut peau :** 🟢 photocopie maquette arcade-radar + data CSV/thermo/Cortana  
**Date figement :** 2026-07-29 · refresh CRT 2026-07-30 · **entrée test 2026-07-30 soir**  
**Maquette :** [[maquettes/ace777-cockpit-maquette-arcade-radar]] · sprite `cockpit/cortana_punk.png`  
**App live :** `Index_Maison/cockpit/index.html`  
**Hygiène :** `scripts/cockpit_hygiene_check.sh` · Attention [[2026-07-30_cockpit_zone_test]]

---

## Verdict Christophe

> Look validé (« wahoo / j’adore ») — chat punk Cortana OK (Main Coon vibes).

---

## Direction visuelle (non négociable v1)

| Oui | Non |
|-----|-----|
| Arcade + radar CRT (grain, scanlines soft) | Terminal coloré / mur de logs |
| Ambre + vert acide sur fond encre | Violet AI / glassmorphism / Inter |
| Gros **score** display + jauges / radar / HP | Tableaux CSV comme héros |
| 1 composition, 3 onglets | Dashboard 40 widgets |
| Cortana = sprite chat punk coin bas-droit qui « sniffe » | Boîte chat générique |

**Brand :** `ACE777 COCKPIT` dominant en haut (pas un eyebrow).

---

## Onglets (4)

1. **OPS** — score PnL, duo BETA/ALPHA, Hulk bags, radar  
2. **THERMO** — petit clin d’œil (F&G / funding / deltas)  
3. **BOARD** — page `thermo/index.html` complète (SIMPLE / COMPLET · A/B/C gardés)  
4. **VOL** — plan de vol + sniff + journal après-midi  

---

## Indicateurs figés (formes)

| ID | Nom | Forme UI | Remplissage plus tard |
|----|-----|----------|------------------------|
| I1 | Radar froid | Cercle + anneau seuil **0.85** | C19 / vacuum |
| I2 | Bassine / mur | Jauge verticale réservoir | C18 / C20 / wall_drop |
| I3 | Verre d’eau | HP bar DRY→WET | C22 / GlobalStop / DD |
| I4 | Score PnL | Gros chiffre + sparkline | CSV fills ACE |
| I5 | BETA / ALPHA | 2 barres d’énergie | duo status |
| I6 | SKIP combo | Étoiles / compteur arcade | C21 |
| I7 | Plan de vol | Cartouche 3 bullets max | GO / Index mission |
| I8 | Cortana sniff | Sprite Main-Coon punk | file `10_ATTENTION` / Punk |

**Règle :** 1 info = 1 forme. Si ça nécessite une phrase pour être lu → mauvais widget.

---

## FX autorisés (légers)

- Glow soft sur chiffre actif  
- Pulse lampe LIVE  
- Scanline / grain CRT léger  
- Son bip = **off** par défaut  

Pas de particules lourdes (Mac Air 8 Go).

---

## En test (après-midi 30 juil.)

OPS · THERMO · VOL + Index live · Cortana (orb, news lente ~14 s, alertes) · bags Hulk · shoot fills · pont `:17777`.

## Hors scope

- Boutons d’**entrée** / taille / levier depuis l’UI  
- Electron lourd  
- LIQ/ETF payants (free = souvent n/d)  

**Exception validée (plan) :** bouton **ROUGE urgence** — sortie seule · modes A (propre) / B (crash) · double confirm · [[PLAN_DE_VOL]] · C-05.

---

## Prochaine étape

Stabiliser lecture pendant runs test + hygiène indicateurs systématique.

**Thermo Index board (A/B/C + free Binance) :**
```bash
python3 /Users/christophe/ace777-test-day1/Index_Maison/scripts/thermo_quotidien_free.py
open /Users/christophe/ace777-test-day1/Index_Maison/thermo/index.html
```

Hygiène + ouvrir cockpit :
```bash
bash /Users/christophe/ace777-test-day1/Index_Maison/scripts/cockpit_hygiene_check.sh
python3 /Users/christophe/ace777-test-day1/Index_Maison/scripts/cortana_cockpit_bridge.py
open /Users/christophe/ace777-test-day1/Index_Maison/cockpit/index.html
```

[[PROTOCOLE_VALIDATION_PATTERN_V8]] · [[THERMO_DERNIER]] · [[01_TABLEAU_VIVANT]] · [[2026-07-30_cockpit_zone_test]]
