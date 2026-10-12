# Hulk DIGEST — 2026-10-12T09:28:24Z

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
| WUSDT | IDLE | 0.67 | 13.08 | 2.59 | 0.73 | 13320745.71 | 7.3 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.77 | 8.1 | 0.49 | 0.09 | 1383805.61 | 3.54 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.43 | 0.97 | 0.02 | 236525869.67 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.01 | 23204568.58 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.11 | 1.03 | 0.0 | 230418969.31 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.17 | 3.95 | 2.57 | -0.01 | 838315.88 | 2.11 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 7.86 | 5.58 | -0.01 | 202648.93 | 12.61 | skipped_fast |
| REDUSDT | IDLE | 2.9 | 7.41 | 0.44 | 0.09 | 75882.21 | 16.03 | skipped_fast |
| EDELUSDT | IDLE | 1.69 | 2.98 | 2.66 | -0.04 | 252973.49 | 10.72 | skipped_fast |
| RIZEUSDT | IDLE | 2.19 | 14.29 | 5.37 | 0.14 | 46427.62 | 76.85 | skipped_fast |
| CCUSDT | IDLE | 0.9 | 1.61 | 1.28 | 0.03 | 395894.09 | 9.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.41 | 2.67 | 2.16 | 0.05 | 280066.32 | 17.18 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.83 | 1.72 | 0.02 | 461977.05 | 4.28 | skipped_fast |
| BIOUSDT | IDLE | 1.31 | 2.31 | 2.13 | -0.0 | 100656.35 | 6.79 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.14 | 0.94 | 0.02 | 63285.15 | 7.76 | skipped_fast |
| TELUSDT | IDLE | 2.11 | 3.97 | 1.63 | 0.0 | 185796.79 | 34.29 | skipped_fast |
| RWAINCUSDT | IDLE | 0.75 | 2.14 | 1.4 | -0.01 | 20364.59 | 20.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.78 | 1.37 | 1.25 | 0.01 | 37427.64 | 5.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.45 | 3.47 | 0.38 | 0.05 | 63373.96 | 21.24 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.54 | 0.23 | 0.03 | 52650.99 | 7.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
