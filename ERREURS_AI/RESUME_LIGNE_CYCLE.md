# Résumé — Ligne de cycle ACE777

**Fichier :** `genesis_manifest.txt`

---

## Structure de la ligne (cycle FILLED)

```
entry=14:32:01 x13 #5 LONG tension=1.2 hold=90s sec=90 | exit=98500 conf=0.85 exit_time=14:35:22 pnl=2.50 bps=12 pct=0.5% total=15.30
```

---

## Champs affichés (dans l’ordre)

| Champ | Description | Couleur |
|-------|-------------|---------|
| **entry** | Heure d’entrée du trade (HH:MM:SS) | Cyan |
| **x13** | Levier (x5, x8, x13…) | Vert si ≥13, jaune si <5, cyan sinon |
| **#i** | Numéro du cycle | Cyan |
| **side** | Direction (LONG / SHORT) | Vert si gain, rouge si perte, jaune si nul |
| **tension** | Score de tension (0–2+) | Rouge si ≥2, vert si 1–2, jaune si 0.85–1, cyan sinon |
| **hold** | Durée du trade (ex. 90s) | Vert si ≥120s, jaune si ≥60s, cyan sinon |
| **sec** | Secondes (durée brute) | Même couleur que hold |
| **exit** | Prix de sortie | Normal |
| **conf** | Confiance radar (0–1) | Vert si ≥0.8, jaune si ≥0.5, rouge sinon |
| **exit_time** | Heure de sortie (HH:MM:SS) | Cyan |
| **pnl** | PNL du cycle (USDT) | Vert / rouge / jaune |
| **bps** | Points de base du cycle | Vert / rouge / jaune |
| **pct** | Pourcentage de variation (%) | Vert / rouge / jaune |
| **total** | PNL cumulé session (USDT) | Vert / rouge / jaune |

---

## PNL complet dernier cycle (fin de ligne)

1. **pnl** — PNL du cycle (USDT)
2. **bps** — Points de base du cycle
3. **pct** — Pourcentage de variation (%)
4. **total** — PNL cumulé de la session (USDT)

---

## Secondes

- **hold** : durée du trade (ex. `hold=90s`)
- **sec** : secondes brutes (ex. `sec=90`)
- **entry** : heure d’entrée avec secondes (HH:MM:SS)
- **exit_time** : heure de sortie avec secondes (HH:MM:SS)

---

## Lignes SKIP

Même structure de base (heure, levier, #cycle, tension) avec `SKIP` et la raison après `|`.
