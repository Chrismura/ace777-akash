# Hulk DIGEST — 2026-08-21T22:58:46Z

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
| PYTHUSDT | IDLE | 1.51 | 5.77 | 0.12 | 0.12 | 5925215.19 | 2.03 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.67 | 6.54 | 0.22 | 0.15 | 137058221.04 | 2.07 | n/a |
| CCUSDT | IDLE | 1.89 | 7.47 | 0.21 | 0.14 | 661745.3 | 6.18 | no_map |
| HBARUSDT | IDLE | 2.23 | 5.03 | 0.15 | 0.09 | 878024.37 | 1.26 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 9.96 | 0.0 | 0.16 | 508439.83 | 34.84 | n/a |
| WUSDT | IDLE | 2.68 | 6.91 | 0.27 | 0.09 | 372982.65 | 13.18 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.11 | 0.05 | 542960.85 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.89 | 0.03 | 187784.63 | 3.1 | n/a |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.69 | 0.19 | 157260.79 | 10.47 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.03 | 82528.51 | 21.81 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10217.99 | 16.16 | no_map |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.05 | 186739.68 | 10.36 | no_map |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.1 | 0.1 | 61339.9 | 9.22 | no_map |
| QNTUSDT | IDLE | 2.46 | 4.91 | 0.0 | 0.07 | 88645.09 | 1.5 | n/a |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.94 | 0.06 | 56402.51 | 46.99 | no_map |
| QAITUSDT | IDLE | 2.43 | 4.38 | 3.15 | -0.01 | 3896.16 | 309.3 | no_map |
| RWAUSDT | IDLE | 1.01 | 2.0 | 0.16 | 0.04 | 54186.49 | 24.58 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.81 | tvl≈2,590,200,853 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
