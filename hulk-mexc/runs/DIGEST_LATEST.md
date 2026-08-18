# Hulk DIGEST — 2026-08-18T19:44:36Z

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
| XRPUSDT | IDLE | 0.5 | 0.94 | 0.37 | 0.0 | 10418205.16 | 1.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 7.03 | 5.5 | -0.02 | 8856.01 | 29.65 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 5.0 | 4.22 | -0.07 | 216916.51 | 3.77 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.99 | 6.77 | 5.18 | -0.05 | 35356.15 | 50.13 | skipped_fast |
| PYTHUSDT | IDLE | 2.01 | 3.74 | 1.91 | -0.0 | 172197.95 | 7.77 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.45 | 2.1 | -0.02 | 175923.94 | 13.46 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 7.76 | 5.08 | 0.08 | 134184.66 | 23.61 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.71 | 0.78 | 0.0 | 237472.37 | 9.91 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.84 | 1.64 | -0.01 | 64659.59 | 4.08 | skipped_fast |
| WUSDT | IDLE | 0.64 | 1.16 | 0.77 | -0.02 | 133582.86 | 16.04 | skipped_fast |
| EDELUSDT | IDLE | 1.07 | 3.12 | 2.1 | -0.03 | 74604.94 | 53.69 | skipped_fast |
| TELUSDT | IDLE | 2.12 | 4.2 | 1.84 | 0.02 | 104511.15 | 41.75 | skipped_fast |
| KITEUSDT | IDLE | 0.55 | 1.03 | 0.5 | -0.01 | 63798.41 | 12.0 | skipped_fast |
| QAITUSDT | IDLE | 0.43 | 5.83 | 3.41 | -0.18 | 18425.18 | 60.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.29 | 2.19 | -0.01 | 169.07 | 23.63 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 1.75 | 0.8 | -0.02 | 34321.9 | 8.92 | skipped_fast |
| HBARUSDT | IDLE | 0.48 | 0.93 | 0.2 | 0.01 | 96457.97 | 3.02 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.7 | 0.52 | -0.01 | 50279.92 | 17.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
