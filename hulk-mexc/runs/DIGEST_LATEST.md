# Hulk DIGEST — 2026-08-22T16:56:42Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.19 | 0.45 | 0.09 | 49206220.45 | 1.9 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.25 | 0.06 | 214663162.89 | 4.05 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.97 | -0.01 | 1131706.53 | 7.74 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.23 | 0.08 | 761335.32 | 6.82 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.73 | -0.1 | 629709.59 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.55 | -0.01 | 544882.35 | 13.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.31 | -0.02 | 312454.18 | 19.93 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.74 | -0.08 | 226216.44 | 3.35 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 4.35 | 1.22 | 0.03 | 86805.93 | 2.66 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 3.0 | 2.91 | -0.03 | 74843.07 | 46.03 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.62 | -0.14 | 127162.63 | 10.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 3.47 | 0.49 | 0.05 | 46444.02 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.94 | -0.01 | 181181.55 | 4.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.02 | 7704.25 | 113.06 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.94 | -0.0 | 136244.08 | 80.36 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.23 | 0.16 | 0.02 | 56402.33 | 8.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 20.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
