# Hulk DIGEST — 2026-08-28T20:06:37Z

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
| XRPUSDT | IDLE | 3.05 | 5.46 | 4.29 | -0.05 | 53323061.83 | 1.45 | n/a |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 17.52 | 11.35 | 0.05 | 1033472.98 | 2.39 | no_map |
| PYTHUSDT | IDLE | 2.8 | 5.81 | 3.71 | -0.05 | 842875.98 | 2.14 | tvl≈107,720,136 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.61 | 6.89 | -0.06 | 194160.88 | 12.58 | n/a |
| CCUSDT | IDLE | 2.34 | 4.24 | 2.95 | -0.02 | 359382.56 | 10.02 | no_map |
| WUSDT | IDLE | 2.52 | 5.41 | 4.01 | -0.06 | 205141.54 | 13.22 | tvl≈1,521,785,002 |
| HBARUSDT | IDLE | 2.77 | 5.29 | 1.61 | -0.02 | 442658.75 | 1.31 | empty_tvl |
| BIOUSDT | IDLE | 2.65 | 5.85 | 4.03 | -0.05 | 94604.06 | 7.24 | n/a |
| KITEUSDT | IDLE | 2.6 | 5.04 | 1.04 | 0.01 | 80079.25 | 8.67 | no_map |
| EDELUSDT | IDLE | 2.19 | 4.01 | 2.4 | -0.05 | 72200.18 | 17.54 | no_map |
| REDUSDT | IDLE | 1.83 | 4.63 | 0.64 | -0.0 | 67472.59 | 12.32 | tvl≈1,966,229 |
| QAITUSDT | IDLE | 1.06 | 13.93 | 10.98 | -0.19 | 73425.07 | 67.41 | no_map |
| RIZEUSDT | IDLE | 1.58 | 4.58 | 1.02 | -0.03 | 39822.05 | 48.16 | no_map |
| RWAINCUSDT | IDLE | 1.78 | 3.87 | 0.0 | 0.02 | 19225.31 | 48.09 | no_map |
| RWAUSDT | IDLE | 2.46 | 4.33 | 3.91 | 0.0 | 54580.72 | 16.63 | no_map |
| QNTUSDT | IDLE | 2.06 | 3.71 | 2.75 | -0.03 | 42788.25 | 6.56 | n/a |
| FLUIDUSDT | IDLE | 2.31 | 4.19 | 2.88 | -0.05 | 4475.04 | 21.59 | tvl≈2,599,245,874 |
| TELUSDT | IDLE | 1.5 | 3.42 | 3.14 | -0.1 | 102587.75 | 22.81 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
