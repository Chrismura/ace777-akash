# Hulk DIGEST — 2026-10-11T02:04:11Z

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
| XRPUSDT | IDLE | 0.51 | 0.93 | 0.64 | -0.01 | 12177841.04 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.17 | 0.34 | 0.04 | 0.01 | 131890325.14 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.1 | 0.19 | 0.1 | 0.0 | 144410941.1 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.23 | 4.02 | 1.72 | 0.03 | 1242298.89 | 10.13 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 1.87 | 1.6 | -0.04 | 1287742.8 | 2.53 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 2.9 | 1.06 | -0.04 | 753270.51 | 2.55 | skipped_fast |
| EDELUSDT | IDLE | 2.5 | 4.54 | 3.08 | -0.04 | 272738.5 | 13.04 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 6.26 | 5.55 | -0.11 | 33523.04 | 46.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.15 | 10.76 | 4.13 | 0.31 | 275984.18 | 18.83 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 2.91 | 1.95 | 0.01 | 88676.67 | 6.86 | skipped_fast |
| TELUSDT | IDLE | 2.49 | 4.84 | 3.96 | -0.07 | 144279.9 | 40.13 | skipped_fast |
| CCUSDT | IDLE | 0.56 | 1.09 | 0.25 | -0.02 | 238259.15 | 5.87 | skipped_fast |
| ZBCNUSDT | IDLE | 0.82 | 1.48 | 1.07 | 0.02 | 170574.31 | 16.57 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 1.69 | 0.82 | 0.04 | 75255.63 | 10.19 | skipped_fast |
| REDUSDT | IDLE | 0.65 | 1.21 | 0.66 | 0.0 | 56831.23 | 15.98 | skipped_fast |
| HBARUSDT | IDLE | 0.58 | 1.1 | 0.42 | -0.0 | 309204.23 | 6.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.73 | 1.29 | 1.12 | -0.01 | 12221.42 | 29.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.91 | 1.64 | 1.23 | -0.01 | 36710.64 | 1.36 | skipped_fast |
| FLUIDUSDT | IDLE | 0.52 | 0.91 | 0.9 | 0.01 | 7810.5 | 21.48 | skipped_fast |
| RWAUSDT | IDLE | 0.09 | 0.16 | 0.08 | 0.0 | 53738.49 | 15.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
