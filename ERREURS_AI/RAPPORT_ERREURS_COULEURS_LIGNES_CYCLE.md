# Rapport d'erreurs — Couleurs sur les lignes de cycle

**Date :** 27 février 2026  
**Statut :** Corrigé (exécuté)

---

## Format appliqué

Chaque ligne de cycle affiche maintenant :

| Élément | Couleur | Règle |
|--------|---------|-------|
| **Heure** | Cyan | Toujours |
| **x13** (levier) | Vert si x13, Jaune si ≤x5, Cyan sinon | Niveau levier |
| **#cycle** | Bleu | Toujours |
| **SKIP** | Jaune | Toujours |
| **PNL + BUY/SELL** | Vert si +, Rouge si -, Jaune si 0 | Plus-value |
| **Tension** | Rouge si ≥2, Magenta si 1–2, Jaune si 0.85–1, Cyan sinon | Niveau tension |
| **Hold** | Magenta si ≥120s, Jaune si ≥60s, Cyan sinon | Durée |
| **Détails** | Cyan | Après \| |

---

## Ligne ORDER (exemple)

```
12:00:00 [ALPHA_X13_BURST13] 11:58:00 x13 #42 BUY 0.25 tension=1.2 hold=45s | bps=12 pct=0.12% close=11:59:30
```

---

## Ligne SKIP (exemple)

```
12:00:00 [BETA_X5] 12:00:00 x5 #15 SKIP tension=0.5 | radar spread_too_wide
```

---

## Fichiers modifiés

- `genesis_manifest.txt` — ORDER + tous les SKIP
- `launch_test_master_base_v8_5_impact.sh` — heure colorée en cyan
