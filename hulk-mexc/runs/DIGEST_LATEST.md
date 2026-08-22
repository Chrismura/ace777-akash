# Hulk DIGEST — 2026-08-22T04:14:50Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 13.13 | 0.22 | 0.2 | 10363692.73 | 16.49 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 12.22 | 1.3 | 0.2 | 167352836.2 | 3.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 11.56 | 0.09 | 0.22 | 724007.3 | 8.94 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 6.2 | 0.05 | 0.11 | 1005204.54 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.85 | 5.36 | 2.32 | -0.0 | 449628.98 | 3.01 | skipped_fast |
| BIOUSDT | IDLE | 3.03 | 7.36 | 2.61 | 0.07 | 199878.51 | 6.0 | skipped_fast |
| WUSDT | IDLE | 1.96 | 7.18 | 0.49 | 0.14 | 429392.02 | 9.71 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 1.07 | 0.11 | 535147.8 | 20.4 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.58 | -0.05 | 80357.13 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.98 | 0.1 | 59145.61 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.4 | 0.21 | 159715.66 | 25.43 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.35 | 0.13 | 67581.11 | 11.51 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.6 | 3.22 | 0.01 | 9433.64 | 64.83 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.41 | 0.09 | 178504.63 | 4.44 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.4 | 0.06 | 56319.15 | 24.05 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.56 | 0.07 | 173819.77 | 35.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
