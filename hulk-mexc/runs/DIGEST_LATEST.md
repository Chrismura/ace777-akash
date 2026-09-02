# Hulk DIGEST — 2026-09-02T01:28:43Z

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
| XRPUSDT | IDLE | 0.77 | 1.37 | 1.18 | -0.03 | 35886915.72 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.08 | 0.65 | -0.02 | 347469175.61 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.9 | 0.49 | -0.02 | 522948488.71 | 0.0 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.69 | 8.04 | 1.01 | 0.07 | 749783.68 | 1.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 6.44 | 6.03 | 0.12 | 762257.75 | 4.64 | skipped_fast |
| WUSDT | IDLE | 2.73 | 4.82 | 4.27 | 0.02 | 420028.89 | 11.55 | skipped_fast |
| ZBCNUSDT | IDLE | 2.82 | 5.2 | 4.69 | -0.03 | 195615.97 | 0.56 | skipped_fast |
| RIZEUSDT | IDLE | 2.66 | 7.87 | 4.89 | -0.05 | 42568.78 | 77.43 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 3.74 | 3.1 | 0.06 | 119445.9 | 9.78 | skipped_fast |
| CCUSDT | IDLE | 0.52 | 1.21 | 0.54 | -0.06 | 330327.85 | 6.16 | skipped_fast |
| EDELUSDT | IDLE | 1.02 | 9.32 | 1.65 | -0.02 | 166743.37 | 62.14 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.36 | 0.34 | 0.04 | 68896.28 | 11.26 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.74 | 0.78 | -0.04 | 69601.04 | 3.92 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.59 | 1.49 | -0.0 | 253827.21 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.8 | 0.48 | 0.05 | 47072.8 | 6.25 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 1.95 | 0.29 | -0.01 | 5787.07 | 104.53 | skipped_fast |
| TELUSDT | IDLE | 1.25 | 2.32 | 1.14 | -0.03 | 92459.92 | 30.22 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 1.01 | 0.38 | -0.03 | 58385.27 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.41 | -0.02 | 35084.98 | 13.75 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 0.96 | 0.62 | -0.04 | 249.95 | 21.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
