# Hulk DIGEST — 2026-08-22T00:03:35Z

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
| PYTHUSDT | IDLE | 1.75 | 6.39 | 1.13 | 0.11 | 6246597.25 | 2.04 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.0 | 8.23 | 0.98 | 0.15 | 142365375.61 | 2.74 | skipped_fast |
| HBARUSDT | IDLE | 2.75 | 6.36 | 0.82 | 0.09 | 908289.15 | 2.5 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 11.25 | 2.48 | 0.12 | 515215.25 | 26.44 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 7.42 | 0.65 | 0.14 | 645156.35 | 7.97 | skipped_fast |
| WUSDT | IDLE | 2.76 | 6.91 | 1.38 | 0.08 | 379135.32 | 11.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.0 | 0.05 | 542139.53 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.8 | 0.03 | 187115.51 | 3.1 | skipped_fast |
| RIZEUSDT | IDLE | 2.27 | 9.82 | 4.21 | 0.13 | 58947.47 | 15.15 | skipped_fast |
| EDELUSDT | IDLE | 2.57 | 5.5 | 1.19 | -0.01 | 79996.8 | 21.98 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.36 | 0.06 | 189852.95 | 20.53 | skipped_fast |
| QNTUSDT | IDLE | 2.48 | 5.42 | 0.24 | 0.07 | 166714.67 | 7.48 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 4.91 | 2.05 | 0.19 | 157878.35 | 8.84 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 3.12 | 0.64 | 0.1 | 61477.04 | 10.14 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54515.7 | 16.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.1 | 4934.79 | 44.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
