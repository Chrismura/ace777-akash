# Hulk DIGEST — 2026-10-18T15:02:56Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 8.52 | 6.94 | -0.12 | 1521484.38 | 4.04 | skipped_fast |
| ETHUSDT | IDLE | 1.35 | 2.43 | 1.81 | -0.02 | 95615850.71 | 1.01 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 2.36 | 1.79 | -0.02 | 23142683.48 | 1.56 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.47 | 1.28 | -0.0 | 221577584.87 | 0.2 | skipped_fast |
| WUSDT | IDLE | 1.81 | 4.25 | 3.29 | -0.08 | 1003526.59 | 14.59 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 16.85 | 14.18 | 0.0 | 51912.98 | 16.85 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.55 | 10.08 | 9.16 | -0.01 | 24272.27 | 21.77 | skipped_fast |
| QNTUSDT | IDLE | 3.44 | 6.26 | 4.12 | -0.05 | 492191.24 | 7.84 | skipped_fast |
| HBARUSDT | IDLE | 1.91 | 4.13 | 2.06 | 0.05 | 632501.5 | 7.97 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 3.01 | 2.59 | -0.06 | 253432.61 | 7.08 | skipped_fast |
| CHIPUSDT | IDLE | 2.26 | 4.31 | 3.48 | -0.08 | 70697.29 | 12.17 | skipped_fast |
| REDUSDT | IDLE | 2.12 | 3.8 | 2.93 | -0.03 | 95116.71 | 16.93 | skipped_fast |
| BIOUSDT | IDLE | 1.98 | 3.58 | 2.54 | -0.05 | 83520.92 | 4.27 | skipped_fast |
| EDELUSDT | IDLE | 1.33 | 3.33 | 2.19 | -0.08 | 226775.37 | 11.37 | skipped_fast |
| KITEUSDT | IDLE | 1.7 | 3.07 | 2.17 | -0.05 | 71305.18 | 13.22 | skipped_fast |
| ZBCNUSDT | IDLE | 0.85 | 1.53 | 1.12 | -0.03 | 190670.05 | 1.44 | skipped_fast |
| FLUIDUSDT | IDLE | 2.69 | 4.71 | 4.44 | -0.05 | 3708.58 | 21.31 | skipped_fast |
| WAXLUSDT | IDLE | 2.09 | 9.16 | 7.29 | -0.05 | 73263.9 | 48.23 | skipped_fast |
| IOTAUSDT | IDLE | 2.39 | 4.35 | 2.91 | -0.06 | 68659.65 | 27.06 | skipped_fast |
| LAUSDT | IDLE | 2.27 | 4.56 | 3.68 | -0.07 | 56985.9 | 30.62 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.29 | 0.71 | -0.0 | 50279.57 | 31.97 | skipped_fast |
| MNSRYUSDT | IDLE | 0.05 | 0.1 | 0.0 | -0.0 | 34934.74 | 12.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
