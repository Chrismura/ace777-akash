# Hulk DIGEST — 2026-08-22T01:40:22Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.87 | 10.86 | 0.97 | 0.16 | 6798984.51 | 11.71 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.27 | 9.41 | 0.09 | 0.16 | 151390248.05 | 2.01 | n/a |
| HBARUSDT | IDLE | 2.98 | 6.36 | 0.32 | 0.09 | 959453.32 | 1.24 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.89 | 0.09 | 550772.25 | 1.45 | n/a |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.14 | 0.17 | 663222.48 | 6.11 | no_map |
| WUSDT | IDLE | 2.69 | 6.65 | 0.54 | 0.09 | 392815.51 | 9.14 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.82 | 0.01 | 513304.65 | 6.13 | no_map |
| BIOUSDT | IDLE | 2.51 | 5.57 | 0.79 | 0.04 | 186380.98 | 6.14 | n/a |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.74 | -0.02 | 79516.12 | 22.12 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.02 | 0.11 | 60836.75 | 45.81 | no_map |
| REDUSDT | IDLE | 0.98 | 8.27 | 5.15 | 0.16 | 158620.49 | 17.64 | tvl≈2,226,572 |
| TELUSDT | IDLE | 2.6 | 6.19 | 1.38 | 0.05 | 182027.1 | 20.73 | no_map |
| KITEUSDT | IDLE | 1.59 | 5.17 | 0.06 | 0.13 | 61685.51 | 12.54 | no_map |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.84 | 0.07 | 170731.14 | 7.53 | n/a |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | no_map |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.48 | 0.03 | 9209.71 | 80.32 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 19.82 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54716.5 | 24.6 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
