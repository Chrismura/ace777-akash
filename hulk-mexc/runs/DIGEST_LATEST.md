# Hulk DIGEST — 2026-08-22T02:15:37Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.08 | 0.14 | 6926947.15 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 10.08 | 0.71 | 0.17 | 153940602.02 | 2.67 | skipped_fast |
| HBARUSDT | IDLE | 2.29 | 4.9 | 0.15 | 0.08 | 955400.35 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.51 | 9.63 | 3.33 | 0.08 | 545480.41 | 35.48 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.14 | 0.0 | 0.15 | 654351.59 | 10.45 | skipped_fast |
| CHIPUSDT | IDLE | 2.04 | 4.72 | 0.0 | -0.01 | 512275.4 | 6.01 | skipped_fast |
| BIOUSDT | IDLE | 2.99 | 6.88 | 0.33 | 0.09 | 192510.63 | 5.94 | skipped_fast |
| WUSDT | IDLE | 1.76 | 4.61 | 0.06 | 0.09 | 401308.97 | 18.1 | skipped_fast |
| EDELUSDT | IDLE | 2.36 | 5.02 | 1.3 | -0.01 | 79536.3 | 32.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.84 | 0.11 | 61210.51 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.97 | 0.18 | 156905.24 | 16.98 | skipped_fast |
| QNTUSDT | IDLE | 2.28 | 4.89 | 0.84 | 0.07 | 171231.58 | 7.53 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.01 | 9604.71 | 27.14 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.41 | 0.12 | 61506.63 | 8.99 | skipped_fast |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.18 | 0.04 | 179394.17 | 57.1 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 20.42 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54896.08 | 16.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
