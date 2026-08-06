# Cockpit ACE777 — Look figé (Arcade Radar)

**Statut :** 🟢 **FIGÉ** (peau) · 🟢 **BUILD v1** page locale demo · 🔵 data réelle = GO suivant  
**Date figement :** 2026-07-29  
**Maquette :** [[maquettes/ace777-cockpit-maquette-arcade-radar]] · Bureau  
**App live :** `Index_Maison/cockpit/index.html` — ouvrir dans le navigateur (fake data + anim)

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

## Onglets (3)

1. **THERMO** — climat / tension / bassine / verre d’eau  
2. **OPS** — score PnL, duo BETA/ALPHA, SKIP combo  
3. **VOL** — plan de vol + sniff + Cortana  

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

## Hors scope (pour l’instant)

- Brancher vrais logs / thermo  
- Boutons trade live  
- Electron lourd  
- Copier le hype X marketing  

---

## Prochaine étape (data)

Brancher thermo / CSV / plan de vol Index (sans casser la peau).

**Thermo Index board (A/B/C + free Binance) :**
```bash
python3 /Users/christophe/ace777-test-day1/Index_Maison/scripts/thermo_quotidien_free.py
open /Users/christophe/ace777-test-day1/Index_Maison/thermo/index.html
```

Ouvrir cockpit :
```bash
open /Users/christophe/ace777-test-day1/Index_Maison/cockpit/index.html
```

[[PROTOCOLE_VALIDATION_PATTERN_V8]] · [[THERMO_DERNIER]] · [[01_TABLEAU_VIVANT]]
