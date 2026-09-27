# Hulk DIGEST — 2026-09-27T02:05:16Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 61.63 | 7.64 | 0.81 | 3450710.2 | 11.68 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 8.38 | 2.64 | 0.13 | 1419127.36 | 4.85 | skipped_fast |
| XRPUSDT | IDLE | 0.65 | 1.24 | 0.4 | -0.03 | 39684063.64 | 1.97 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.11 | 0.21 | 0.0 | 122609033.69 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.64 | 0.13 | 0.0 | 339234303.98 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.8 | 8.86 | 2.98 | 0.09 | 696898.14 | 15.67 | skipped_fast |
| CCUSDT | IDLE | 2.28 | 4.56 | 0.74 | 0.03 | 787511.79 | 8.72 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.82 | 8.28 | 6.68 | -0.03 | 171617.68 | 31.24 | skipped_fast |
| KITEUSDT | IDLE | 1.57 | 5.76 | 0.52 | 0.12 | 152065.78 | 8.49 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.16 | 8.19 | 0.0 | 0.07 | 128965.9 | 28.71 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.96 | 0.83 | -0.02 | 186913.52 | 27.49 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.48 | 0.57 | -0.02 | 568755.35 | 1.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 2.97 | 0.93 | -0.01 | 107376.9 | 16.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.6 | 3.97 | 0.83 | 0.08 | 45616.48 | 38.36 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.77 | 0.59 | -0.01 | 109088.48 | 9.35 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.9 | 0.49 | -0.02 | 59392.02 | 19.51 | skipped_fast |
| RWAINCUSDT | IDLE | 0.22 | 0.83 | 0.0 | 0.04 | 10100.65 | 92.84 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.94 | 0.07 | 0.04 | 56485.09 | 7.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.95 | 0.25 | -0.0 | 38879.58 | 15.34 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.08 | 0.74 | -0.0 | 973.55 | 21.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
