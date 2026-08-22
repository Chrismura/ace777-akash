# Hulk DIGEST — 2026-08-22T01:28:46Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 10.58 | 0.21 | 0.16 | 6720082.47 | 15.53 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.17 | 8.42 | 0.16 | 0.15 | 150044331.92 | 4.05 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.74 | 0.08 | 951617.92 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.75 | 0.11 | 545263.7 | 0.97 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.28 | 0.24 | 0.16 | 660448.53 | 9.62 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.65 | 1.13 | 0.09 | 392188.51 | 12.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 3.56 | 1.76 | -0.02 | 515746.58 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.57 | 0.91 | 0.04 | 186046.97 | 9.23 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79570.22 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.13 | 0.11 | 60662.94 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.65 | 0.18 | 158683.85 | 19.14 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.97 | 0.07 | 170132.76 | 3.02 | skipped_fast |
| KITEUSDT | IDLE | 1.51 | 4.63 | 0.35 | 0.12 | 60923.64 | 9.91 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.82 | 0.05 | 181116.4 | 41.28 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9552.36 | 5.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 23.23 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54955.71 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
