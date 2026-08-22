# Hulk DIGEST — 2026-08-22T04:07:00Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.78 | 12.16 | 0.13 | 0.19 | 9859657.51 | 12.91 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 12.22 | 1.76 | 0.19 | 166701183.52 | 3.82 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.03 | 10.63 | 0.35 | 0.2 | 714713.45 | 13.13 | skipped_fast |
| HBARUSDT | IDLE | 2.1 | 6.03 | 0.46 | 0.1 | 1010200.86 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.91 | 5.36 | 3.09 | -0.02 | 457920.65 | 3.04 | skipped_fast |
| BIOUSDT | IDLE | 3.05 | 7.36 | 3.05 | 0.06 | 199598.07 | 3.03 | skipped_fast |
| WUSDT | IDLE | 1.98 | 7.18 | 1.08 | 0.13 | 427393.46 | 9.76 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.58 | 0.13 | 537185.29 | 19.54 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.05 | 80468.04 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.1 | 59150.84 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.9 | 0.21 | 157832.8 | 20.57 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.53 | 0.13 | 67558.06 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.8 | 0.77 | 0.09 | 178569.57 | 8.92 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.46 | 0.07 | 174268.32 | 5.12 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56318.26 | 8.02 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
