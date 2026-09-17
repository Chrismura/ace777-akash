# Hulk DIGEST — 2026-09-17T11:16:31Z

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
| XRPUSDT | IDLE | 0.7 | 1.28 | 0.81 | 0.01 | 56975380.23 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 0.52 | 0.95 | 0.62 | 0.01 | 370681068.56 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.65 | 0.43 | 0.01 | 483144524.7 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 5.01 | 1.92 | 0.11 | 636076.35 | 6.94 | skipped_fast |
| CHIPUSDT | IDLE | 2.95 | 9.1 | 3.6 | 0.04 | 142901.19 | 18.28 | skipped_fast |
| PYTHUSDT | IDLE | 0.91 | 1.64 | 1.17 | 0.03 | 544235.66 | 9.28 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 6.5 | 4.22 | -0.1 | 204317.76 | 24.59 | skipped_fast |
| REDUSDT | IDLE | 1.95 | 4.14 | 0.49 | 0.03 | 64418.25 | 17.03 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 4.72 | 4.3 | 0.05 | 68357.31 | 12.43 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.23 | 1.51 | 0.02 | 170273.16 | 13.87 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.6 | 0.32 | 0.0 | 492219.22 | 1.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 2.93 | 2.84 | -0.01 | 17744.93 | 29.18 | skipped_fast |
| WUSDT | IDLE | 0.59 | 1.12 | 0.42 | 0.04 | 220874.95 | 12.95 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 14.53 | 7.91 | -0.24 | 55892.4 | 123.64 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.85 | 1.02 | 0.01 | 68397.29 | 15.95 | skipped_fast |
| RWAUSDT | IDLE | 1.69 | 3.31 | 0.52 | 0.02 | 58727.76 | 22.48 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.17 | 1.51 | -0.01 | 109243.39 | 34.86 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 2.35 | 0.5 | 0.03 | 35814.36 | 14.64 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.63 | 0.42 | 0.01 | 38168.64 | 29.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.66 | 0.36 | 0.0 | 1261.39 | 21.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
