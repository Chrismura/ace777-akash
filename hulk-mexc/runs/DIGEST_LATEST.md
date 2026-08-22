# Hulk DIGEST — 2026-08-22T02:08:47Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.08 | 0.13 | 6895561.37 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 10.03 | 0.75 | 0.16 | 154199840.98 | 2.0 | skipped_fast |
| HBARUSDT | IDLE | 2.31 | 4.9 | 0.47 | 0.07 | 952700.34 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.51 | 9.63 | 3.27 | 0.08 | 546486.43 | 22.4 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.12 | 0.15 | 654188.68 | 6.98 | skipped_fast |
| CHIPUSDT | IDLE | 1.71 | 3.91 | 0.27 | 0.02 | 515523.49 | 6.08 | skipped_fast |
| BIOUSDT | IDLE | 2.91 | 6.4 | 0.06 | 0.09 | 190554.67 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.74 | 4.41 | 0.5 | 0.08 | 399743.38 | 8.1 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 5.02 | 1.52 | -0.01 | 79571.18 | 44.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.8 | 0.11 | 61137.28 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.15 | 0.17 | 156818.83 | 19.42 | skipped_fast |
| QNTUSDT | IDLE | 2.31 | 4.89 | 1.33 | 0.06 | 171294.5 | 4.54 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.8 | 0.11 | 61373.89 | 12.61 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9241.73 | 69.8 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.28 | 0.04 | 179053.67 | 67.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.9 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 54659.59 | 8.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
