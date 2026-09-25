# Hulk DIGEST — 2026-09-25T19:45:08Z

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
| XRPUSDT | IDLE | 1.61 | 2.93 | 1.89 | 0.03 | 116667374.13 | 1.28 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.1 | 0.27 | -0.0 | 345225384.89 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.1 | 0.15 | -0.01 | 716432175.53 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.29 | 5.97 | 3.4 | 0.06 | 1227632.4 | 5.57 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.03 | 9.28 | 0.66 | 0.15 | 815940.96 | 10.62 | skipped_fast |
| WUSDT | IDLE | 2.26 | 4.32 | 1.31 | 0.02 | 393223.06 | 10.79 | skipped_fast |
| ZBCNUSDT | IDLE | 2.93 | 7.27 | 0.58 | 0.07 | 240159.25 | 22.51 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.14 | 0.67 | 0.02 | 909385.62 | 1.06 | skipped_fast |
| CHIPUSDT | IDLE | 2.15 | 5.23 | 2.24 | 0.0 | 161369.86 | 16.35 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 6.98 | 1.06 | 0.14 | 606542.12 | 3.06 | skipped_fast |
| KITEUSDT | IDLE | 2.43 | 4.77 | 0.64 | -0.0 | 78319.67 | 8.28 | skipped_fast |
| BIOUSDT | IDLE | 1.7 | 5.24 | 0.36 | 0.07 | 115370.62 | 12.04 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 3.86 | 0.73 | 0.09 | 136903.46 | 5.73 | skipped_fast |
| EDELUSDT | IDLE | 0.47 | 4.19 | 2.68 | 0.05 | 227111.77 | 23.53 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 16.71 | 13.2 | 0.14 | 122873.28 | 202.69 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.08 | 0.54 | 0.0 | 110312.23 | 30.11 | skipped_fast |
| RWAINCUSDT | IDLE | 0.49 | 1.85 | 0.51 | -0.08 | 18767.4 | 86.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.25 | 2.46 | 0.24 | 0.03 | 3375.0 | 21.54 | skipped_fast |
| RWAUSDT | IDLE | 0.85 | 1.55 | 0.95 | -0.01 | 56736.74 | 7.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.43 | 0.5 | 0.02 | 41183.96 | 20.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
