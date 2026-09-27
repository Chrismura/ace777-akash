# Hulk DIGEST — 2026-09-27T18:12:10Z

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
| WUSDT | IDLE | 1.82 | 11.52 | 3.62 | 0.16 | 4281487.61 | 13.81 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 5.56 | 1.61 | 0.11 | 2284857.46 | 7.01 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 22.14 | 4.54 | 0.48 | 6210875.71 | 9.81 | skipped_fast |
| XRPUSDT | IDLE | 0.97 | 1.83 | 0.7 | -0.01 | 43917020.95 | 1.97 | skipped_fast |
| ETHUSDT | IDLE | 0.68 | 1.22 | 0.89 | 0.0 | 192771296.49 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.95 | 0.66 | 0.01 | 444381682.58 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 42.2 | 23.42 | 0.04 | 24969.37 | 18.25 | skipped_fast |
| CCUSDT | IDLE | 1.85 | 3.68 | 0.07 | 0.01 | 560229.87 | 6.57 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 8.08 | 6.2 | -0.12 | 129925.49 | 47.84 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 4.7 | 0.81 | 0.06 | 173409.95 | 9.8 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.64 | 0.15 | 0.0 | 669935.9 | 1.06 | skipped_fast |
| CHIPUSDT | IDLE | 1.74 | 3.29 | 1.33 | -0.05 | 100852.87 | 14.77 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 1.69 | 1.02 | -0.01 | 203522.95 | 9.5 | skipped_fast |
| BIOUSDT | IDLE | 1.22 | 2.35 | 0.6 | -0.03 | 89496.57 | 9.48 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 6.22 | 1.21 | 0.16 | 160173.03 | 5.34 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 1.65 | 0.09 | 0.0 | 63997.11 | 7.61 | skipped_fast |
| RIZEUSDT | IDLE | 0.5 | 1.94 | 0.54 | -0.03 | 45950.83 | 64.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.12 | 0.0 | 0.03 | 1601.23 | 20.06 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.0 | 0.42 | 0.01 | 56614.15 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.24 | 0.46 | 0.09 | 0.01 | 39502.75 | 36.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
