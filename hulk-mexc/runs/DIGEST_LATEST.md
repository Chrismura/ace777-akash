# Hulk DIGEST — 2026-08-22T02:56:47Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.63 | 11.02 | 0.92 | 0.15 | 7354389.73 | 3.81 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.54 | 13.33 | 0.47 | 0.2 | 159153693.23 | 3.88 | skipped_fast |
| HBARUSDT | IDLE | 2.57 | 6.7 | 0.07 | 0.1 | 990116.07 | 1.22 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.09 | 9.69 | 0.0 | 0.18 | 663958.38 | 8.4 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 9.63 | 2.71 | 0.11 | 541398.06 | 29.02 | skipped_fast |
| CHIPUSDT | IDLE | 2.58 | 5.95 | 0.03 | -0.0 | 450698.48 | 5.95 | skipped_fast |
| BIOUSDT | IDLE | 3.21 | 8.18 | 2.11 | 0.08 | 194377.97 | 8.99 | skipped_fast |
| WUSDT | IDLE | 2.04 | 6.24 | 0.01 | 0.11 | 415995.3 | 12.88 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 5.02 | 2.61 | -0.03 | 79929.12 | 22.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.44 | 0.1 | 61387.25 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.62 | 0.2 | 157965.72 | 13.55 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9385.21 | 5.43 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.22 | 0.09 | 172672.47 | 5.95 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.15 | 0.12 | 62392.89 | 9.85 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 5.11 | 0.82 | 0.06 | 173940.92 | 61.98 | skipped_fast |
| RWAUSDT | IDLE | 1.68 | 3.33 | 0.24 | 0.05 | 56199.27 | 16.17 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
