# Hulk DIGEST — 2026-08-22T00:18:29Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.88 | 0.1 | 6324627.25 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 2.07 | 8.23 | 2.71 | 0.13 | 143722641.59 | 1.39 | skipped_fast |
| HBARUSDT | IDLE | 2.84 | 6.36 | 2.27 | 0.07 | 929860.92 | 1.27 | skipped_fast |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.41 | 0.1 | 519383.64 | 6.82 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 7.42 | 2.14 | 0.12 | 644523.59 | 8.09 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.03 | 0.08 | 384525.02 | 13.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 3.56 | 0.61 | 0.05 | 545196.49 | 6.13 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.77 | 0.02 | 186629.93 | 9.3 | skipped_fast |
| EDELUSDT | IDLE | 2.6 | 5.5 | 1.63 | -0.01 | 79890.36 | 22.1 | skipped_fast |
| RIZEUSDT | IDLE | 2.22 | 9.82 | 2.65 | 0.14 | 59507.99 | 45.1 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.72 | 0.06 | 189936.34 | 46.4 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.42 | 1.72 | 0.05 | 170604.49 | 12.15 | skipped_fast |
| REDUSDT | IDLE | 0.56 | 4.91 | 1.8 | 0.2 | 157682.44 | 8.81 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 3.12 | 0.63 | 0.1 | 61436.06 | 10.14 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.02 | 9753.94 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.73 | 0.03 | 54650.66 | 24.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
