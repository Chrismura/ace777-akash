# Hulk DIGEST — 2026-09-21T23:05:06Z

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
| XRPUSDT | IDLE | 1.85 | 5.52 | 0.57 | 0.11 | 108586110.12 | 1.92 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.55 | 0.83 | 0.06 | 737003678.42 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 1.0 | 1.87 | 0.94 | 0.07 | 1051838243.16 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 18.24 | 13.65 | 0.09 | 264278.36 | 9.95 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 3.38 | 0.26 | 0.08 | 1142577.37 | 1.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.53 | 3.83 | 1.03 | 0.03 | 712964.63 | 1.57 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 3.27 | 0.63 | 0.09 | 595406.97 | 9.34 | skipped_fast |
| ZBCNUSDT | IDLE | 2.54 | 6.77 | 3.09 | 0.08 | 255550.67 | 41.05 | skipped_fast |
| WUSDT | IDLE | 0.9 | 2.18 | 0.03 | 0.02 | 554211.08 | 5.91 | skipped_fast |
| RIZEUSDT | IDLE | 1.54 | 11.17 | 8.67 | -0.19 | 48552.68 | 38.9 | skipped_fast |
| RWAINCUSDT | IDLE | 2.55 | 7.23 | 1.02 | 0.1 | 19713.32 | 87.58 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 5.1 | 1.29 | 0.1 | 147050.86 | 19.2 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 1.89 | 0.03 | 0.05 | 104091.33 | 3.44 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.98 | 0.0 | 0.03 | 81230.14 | 9.19 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.52 | 0.28 | 0.0 | 103484.73 | 14.48 | skipped_fast |
| QNTUSDT | IDLE | 1.5 | 2.84 | 1.06 | 0.05 | 111352.88 | 5.95 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 3.18 | 2.07 | 0.09 | 115723.44 | 42.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.07 | 2.43 | 1.7 | 0.07 | 11627.45 | 20.63 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.16 | 0.57 | 0.01 | 57965.44 | 28.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.76 | 1.5 | 0.13 | 0.04 | 42339.99 | 69.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
