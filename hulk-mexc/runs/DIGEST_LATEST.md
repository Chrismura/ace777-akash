# Hulk DIGEST — 2026-08-22T03:06:49Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.27 | 9.55 | 0.45 | 0.15 | 7479129.62 | 13.27 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 11.15 | 0.55 | 0.2 | 160136188.06 | 1.94 | skipped_fast |
| HBARUSDT | IDLE | 2.15 | 5.29 | 0.33 | 0.1 | 996299.66 | 1.22 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 8.96 | 0.2 | 0.19 | 666799.62 | 3.35 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.06 | 195341.79 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 4.28 | 0.45 | -0.0 | 445752.88 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.77 | 5.61 | 0.13 | 0.12 | 417666.4 | 13.79 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 5.16 | 2.6 | 0.12 | 541461.28 | 69.58 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.24 | 0.09 | 61376.41 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.83 | 0.21 | 158024.05 | 18.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 21.72 | skipped_fast |
| EDELUSDT | IDLE | 1.85 | 3.83 | 1.74 | -0.02 | 79905.9 | 44.4 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.12 | 0.0 | 0.12 | 63740.56 | 13.41 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3931.36 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.97 | 0.21 | 0.09 | 172793.43 | 7.44 | skipped_fast |
| TELUSDT | IDLE | 0.8 | 1.88 | 0.56 | 0.06 | 172847.94 | 5.12 | skipped_fast |
| RWAUSDT | IDLE | 1.18 | 2.31 | 0.32 | 0.05 | 56120.02 | 16.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
