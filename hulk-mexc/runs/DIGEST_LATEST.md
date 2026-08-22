# Hulk DIGEST — 2026-08-22T01:20:46Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.78 | 10.07 | 0.06 | 0.15 | 6668444.04 | 3.9 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 8.4 | 0.63 | 0.15 | 149944903.12 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.79 | 0.08 | 955217.39 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.93 | 0.09 | 546331.87 | 29.56 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 7.18 | 0.1 | 0.16 | 659494.85 | 9.6 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.65 | 0.97 | 0.08 | 392175.96 | 10.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.56 | 1.25 | -0.01 | 522415.25 | 6.15 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.57 | 0.88 | 0.04 | 186526.56 | 3.07 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79560.3 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.16 | 0.11 | 60559.46 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.33 | 0.18 | 159146.2 | 11.92 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.85 | 0.07 | 170457.05 | 7.53 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.77 | 0.05 | 181068.07 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 4.63 | 0.06 | 0.12 | 60832.86 | 12.61 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9620.22 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 22.39 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 55140.73 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
