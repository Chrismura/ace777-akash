# Hulk DIGEST — 2026-09-22T16:12:39Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 20.05 | 10.0 | 0.02 | 1533956.06 | 7.54 | skipped_fast |
| XRPUSDT | IDLE | 2.56 | 4.8 | 2.13 | 0.04 | 116972912.89 | 3.2 | skipped_fast |
| ETHUSDT | IDLE | 0.94 | 1.73 | 1.03 | -0.01 | 493089063.98 | 0.91 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.42 | 0.52 | 0.0 | 905864456.37 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.81 | 6.44 | 1.77 | 0.05 | 1277561.55 | 2.06 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 14.07 | 12.28 | -0.0 | 265519.72 | 71.43 | skipped_fast |
| CCUSDT | IDLE | 2.48 | 4.35 | 4.04 | -0.02 | 490146.85 | 8.71 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.89 | 1.27 | 0.0 | 375751.66 | 4.21 | skipped_fast |
| RIZEUSDT | IDLE | 2.03 | 24.12 | 6.07 | -0.18 | 42195.27 | 75.97 | skipped_fast |
| CHIPUSDT | IDLE | 2.46 | 4.48 | 2.87 | -0.02 | 140117.25 | 21.86 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 3.11 | 0.48 | 0.01 | 242713.4 | 34.58 | skipped_fast |
| QNTUSDT | IDLE | 2.6 | 8.3 | 2.46 | 0.08 | 186042.58 | 12.38 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.34 | 8.79 | 1.02 | 0.07 | 104245.63 | 45.95 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 6.13 | 1.8 | 0.14 | 113039.4 | 23.65 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 2.78 | 0.89 | 0.0 | 115181.15 | 3.46 | skipped_fast |
| REDUSDT | IDLE | 1.27 | 2.47 | 0.53 | 0.02 | 65831.38 | 8.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.85 | 1.61 | 0.55 | 0.04 | 26299.81 | 27.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.11 | 2.07 | 0.97 | 0.02 | 9378.54 | 21.4 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.95 | 0.51 | -0.01 | 54333.61 | 7.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.09 | 0.17 | 0.05 | -0.0 | 40049.87 | 7.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
