# Hulk DIGEST — 2026-08-29T05:10:32Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.45 | 0.88 | 0.17 | -0.02 | 44203709.81 | 2.88 | n/a |
| CHIPUSDT | IDLE | 1.72 | 8.91 | 0.72 | 0.08 | 1134213.43 | 9.41 | no_map |
| QAITUSDT | IDLE | 2.35 | 20.42 | 14.43 | -0.02 | 96080.9 | 10.17 | no_map |
| PYTHUSDT | IDLE | 0.82 | 1.48 | 1.04 | -0.02 | 523867.61 | 4.21 | tvl≈107,753,096 |
| RIZEUSDT | IDLE | 2.56 | 6.2 | 2.09 | -0.04 | 29254.17 | 56.03 | no_map |
| CCUSDT | IDLE | 0.95 | 1.75 | 0.95 | -0.01 | 244028.79 | 8.1 | no_map |
| WUSDT | IDLE | 1.01 | 1.92 | 0.72 | -0.02 | 209415.11 | 11.94 | tvl≈1,521,619,275 |
| KITEUSDT | IDLE | 1.5 | 2.76 | 1.65 | -0.0 | 73605.67 | 8.64 | no_map |
| EDELUSDT | IDLE | 1.32 | 5.29 | 1.4 | -0.08 | 90523.19 | 18.89 | no_map |
| REDUSDT | IDLE | 1.37 | 3.09 | 1.14 | -0.01 | 61260.06 | 15.64 | tvl≈1,998,746 |
| HBARUSDT | IDLE | 0.69 | 1.23 | 0.98 | -0.02 | 468316.54 | 1.32 | empty_tvl |
| ZBCNUSDT | IDLE | 0.67 | 1.87 | 0.07 | -0.06 | 173031.19 | 7.1 | n/a |
| BIOUSDT | IDLE | 0.5 | 0.94 | 0.39 | -0.02 | 83485.39 | 7.18 | n/a |
| TELUSDT | IDLE | 1.63 | 3.0 | 1.74 | -0.05 | 94695.12 | 57.05 | no_map |
| RWAINCUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 3438.94 | 76.67 | no_map |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
