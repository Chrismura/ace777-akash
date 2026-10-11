# Hulk DIGEST — 2026-10-11T15:19:02Z

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
| XRPUSDT | IDLE | 0.47 | 0.93 | 0.09 | -0.0 | 9969863.67 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.11 | -0.0 | 168057765.79 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.34 | 0.16 | 0.0 | 121816384.88 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.89 | 1.3 | -0.04 | 943191.64 | 7.43 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 31.62 | 15.89 | 0.06 | 54156.34 | 23.33 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.41 | 11.9 | 8.28 | -0.02 | 28590.73 | 79.05 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 2.41 | 1.63 | -0.03 | 986765.0 | 4.55 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 1.87 | 1.08 | -0.02 | 725640.29 | 3.91 | skipped_fast |
| CCUSDT | IDLE | 2.45 | 4.83 | 0.47 | 0.04 | 308259.79 | 9.59 | skipped_fast |
| CHIPUSDT | IDLE | 1.05 | 10.03 | 1.76 | 0.34 | 414767.71 | 14.4 | skipped_fast |
| TELUSDT | IDLE | 3.89 | 7.16 | 4.14 | -0.04 | 147375.18 | 40.33 | skipped_fast |
| EDELUSDT | IDLE | 1.26 | 2.3 | 1.5 | 0.01 | 389280.84 | 5.18 | skipped_fast |
| BIOUSDT | IDLE | 1.96 | 3.78 | 0.99 | 0.04 | 74142.52 | 6.68 | skipped_fast |
| RIZEUSDT | IDLE | 2.39 | 6.54 | 2.32 | -0.06 | 35615.4 | 61.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.54 | 1.41 | -0.01 | 161225.1 | 14.96 | skipped_fast |
| REDUSDT | IDLE | 1.49 | 2.87 | 0.76 | 0.0 | 58067.51 | 10.62 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.88 | 0.64 | -0.03 | 70640.04 | 10.24 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.22 | 0.15 | -0.0 | 249526.3 | 6.48 | skipped_fast |
| RWAUSDT | IDLE | 0.85 | 1.67 | 0.16 | 0.01 | 51518.74 | 15.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.73 | 0.11 | -0.01 | 30941.58 | 16.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
