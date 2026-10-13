# Hulk DIGEST — 2026-10-13T05:11:38Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.27 | 13.1 | 1.61 | 0.09 | 3778613.59 | 1.15 | tvl≈187,461,878 |
| WUSDT | IDLE | 0.69 | 11.65 | 6.08 | -0.32 | 11482319.2 | 4.67 | tvl≈1,719,413,111 |
| XRPUSDT | IDLE | 2.41 | 4.89 | 0.28 | -0.03 | 35557435.57 | 2.19 | n/a |
| ETHUSDT | IDLE | 2.35 | 4.69 | 0.04 | -0.02 | 282507003.8 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.54 | 3.09 | 0.0 | -0.01 | 361402915.79 | 0.0 | no_map |
| CCUSDT | IDLE | 2.93 | 6.94 | 0.19 | -0.02 | 414688.23 | 11.3 | no_map |
| QNTUSDT | IDLE | 1.93 | 5.15 | 0.4 | -0.05 | 910509.73 | 1.31 | n/a |
| ZBCNUSDT | IDLE | 2.12 | 4.18 | 0.36 | -0.03 | 223578.8 | 17.06 | n/a |
| KITEUSDT | IDLE | 2.55 | 7.4 | 0.16 | -0.01 | 67331.76 | 10.18 | no_map |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.27 | 8.36 | 0.0 | -0.06 | 76122.1 | 7.08 | n/a |
| HBARUSDT | IDLE | 1.47 | 4.64 | 0.0 | -0.07 | 573950.93 | 2.27 | empty_tvl |
| CHIPUSDT | IDLE | 1.84 | 8.57 | 0.7 | -0.08 | 158290.12 | 15.02 | no_map |
| REDUSDT | IDLE | 1.06 | 7.82 | 0.42 | 0.03 | 300355.13 | 9.5 | tvl≈3,878,759 |
| EDELUSDT | IDLE | 0.91 | 3.88 | 1.22 | -0.13 | 286920.01 | 15.11 | no_map |
| FLUIDUSDT | IDLE | 3.43 | 6.8 | 0.34 | 0.04 | 13256.76 | 21.54 | tvl≈2,378,452,747 |
| RWAINCUSDT | IDLE | 1.34 | 3.85 | 0.1 | 0.03 | 39600.26 | 4.88 | no_map |
| TELUSDT | IDLE | 2.05 | 3.99 | 0.68 | 0.02 | 115200.88 | 28.35 | no_map |
| RIZEUSDT | IDLE | 0.47 | 3.0 | 0.67 | -0.08 | 67348.63 | 89.99 | no_map |
| RWAUSDT | IDLE | 0.91 | 1.81 | 0.08 | 0.0 | 53413.84 | 15.43 | no_map |
| MNSRYUSDT | IDLE | 1.23 | 2.36 | 0.73 | -0.02 | 40022.85 | 58.06 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
