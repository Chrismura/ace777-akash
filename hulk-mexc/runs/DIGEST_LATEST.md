# Hulk DIGEST — 2026-10-29T17:07:04Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 10.02 | 6.22 | 0.01 | 1020788.29 | 5.6 | skipped_fast |
| ETHUSDT | IDLE | 1.51 | 2.84 | 1.19 | 0.01 | 270670497.63 | 0.09 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 2.5 | 1.61 | -0.01 | 26094778.71 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 1.35 | 2.53 | 1.11 | 0.01 | 391934241.67 | 0.21 | skipped_fast |
| CCUSDT | IDLE | 2.74 | 6.2 | 2.75 | 0.02 | 388456.17 | 8.81 | skipped_fast |
| CHIPUSDT | IDLE | 3.27 | 9.68 | 4.29 | 0.04 | 139930.86 | 15.86 | skipped_fast |
| WUSDT | IDLE | 1.42 | 2.6 | 1.63 | -0.03 | 398497.68 | 9.67 | skipped_fast |
| BIOUSDT | IDLE | 2.81 | 5.58 | 1.36 | 0.03 | 72976.08 | 8.63 | skipped_fast |
| QNTUSDT | IDLE | 2.1 | 3.87 | 2.25 | 0.0 | 458135.5 | 6.64 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.62 | 0.95 | -0.03 | 323398.26 | 3.19 | skipped_fast |
| HBARUSDT | IDLE | 1.79 | 3.38 | 1.37 | -0.0 | 471399.7 | 5.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.19 | 2.33 | 0.3 | 0.01 | 229097.38 | 21.67 | skipped_fast |
| REDUSDT | IDLE | 1.6 | 3.05 | 1.0 | 0.0 | 63228.77 | 17.19 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.29 | 0.75 | 0.0 | 59168.85 | 9.58 | skipped_fast |
| LAUSDT | IDLE | 2.32 | 4.49 | 1.0 | 0.01 | 59775.74 | 36.03 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 1.92 | 0.0 | -0.03 | 31793.74 | 13.98 | skipped_fast |
| RIZEUSDT | IDLE | 0.87 | 1.55 | 1.25 | -0.03 | 67197.74 | 49.3 | skipped_fast |
| IOTAUSDT | IDLE | 1.75 | 3.44 | 1.04 | -0.0 | 95510.33 | 14.6 | skipped_fast |
| FLUIDUSDT | IDLE | 1.74 | 3.62 | 3.06 | -0.06 | 7766.37 | 21.49 | skipped_fast |
| WAXLUSDT | IDLE | 1.72 | 4.25 | 0.83 | -0.02 | 53514.52 | 56.72 | skipped_fast |
| MNSRYUSDT | IDLE | 1.06 | 2.04 | 0.6 | -0.01 | 37409.62 | 14.66 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.05 | 0.08 | -0.0 | 55093.16 | 8.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
