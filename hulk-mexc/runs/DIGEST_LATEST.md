# Hulk DIGEST — 2026-08-22T02:24:49Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 9.45 | 0.54 | 0.15 | 6976501.93 | 1.93 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 10.44 | 0.67 | 0.17 | 154868075.06 | 3.32 | skipped_fast |
| HBARUSDT | IDLE | 2.33 | 5.05 | 0.35 | 0.08 | 962300.85 | 3.72 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.79 | 0.09 | 543204.01 | 16.94 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 6.32 | 0.1 | 0.15 | 655686.86 | 6.95 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 5.07 | 0.75 | -0.01 | 474458.74 | 6.04 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.09 | 8.18 | 0.0 | 0.1 | 193022.22 | 5.87 | skipped_fast |
| WUSDT | IDLE | 1.85 | 5.09 | 0.11 | 0.1 | 402175.07 | 11.02 | skipped_fast |
| EDELUSDT | IDLE | 2.49 | 5.02 | 3.15 | -0.03 | 79688.2 | 33.54 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.89 | 0.11 | 61340.51 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.35 | 0.17 | 157147.2 | 13.0 | skipped_fast |
| QNTUSDT | IDLE | 2.23 | 4.89 | 0.1 | 0.08 | 171106.55 | 1.49 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.71 | 0.12 | 61830.94 | 12.61 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.01 | 9379.52 | 54.17 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.11 | 1.48 | 0.04 | 178532.43 | 67.41 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.08 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54867.58 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
