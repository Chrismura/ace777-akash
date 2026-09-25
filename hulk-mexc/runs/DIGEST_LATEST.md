# Hulk DIGEST — 2026-09-25T02:41:46Z

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
| XRPUSDT | IDLE | 1.2 | 2.13 | 1.83 | 0.02 | 72435071.42 | 1.31 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.07 | 0.53 | 0.0 | 723255297.46 | 0.11 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.87 | 0.65 | -0.0 | 356779510.48 | 0.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.53 | 38.5 | 23.98 | 0.08 | 185929.83 | 77.3 | skipped_fast |
| PYTHUSDT | IDLE | 1.11 | 3.94 | 1.27 | 0.08 | 1014745.08 | 1.46 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 34.66 | 15.23 | 0.48 | 94115.0 | 37.5 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 3.24 | 0.7 | 0.05 | 514355.32 | 6.09 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.78 | 1.6 | 0.03 | 901860.23 | 2.15 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.07 | 5.38 | 5.08 | -0.04 | 65694.44 | 12.67 | skipped_fast |
| CHIPUSDT | IDLE | 1.84 | 9.31 | 8.5 | 0.08 | 102206.01 | 15.23 | skipped_fast |
| WUSDT | IDLE | 1.21 | 2.12 | 2.0 | 0.03 | 255323.12 | 11.14 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 2.01 | 1.44 | 0.01 | 225907.86 | 16.66 | skipped_fast |
| REDUSDT | IDLE | 1.45 | 3.36 | 0.76 | 0.08 | 124530.9 | 17.13 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 9.66 | 5.92 | 0.26 | 302969.41 | 6.71 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 2.37 | 2.31 | 0.06 | 90734.85 | 13.15 | skipped_fast |
| TELUSDT | IDLE | 2.19 | 4.06 | 3.9 | -0.06 | 112137.26 | 43.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.19 | 5.68 | 4.98 | 0.16 | 13031.16 | 70.24 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.26 | 0.22 | 0.01 | 59042.79 | 14.61 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.41 | 0.42 | 0.01 | 39768.32 | 37.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.59 | 1.13 | 0.27 | 0.04 | 1081.64 | 21.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
