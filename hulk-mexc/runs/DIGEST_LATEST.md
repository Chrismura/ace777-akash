# Hulk DIGEST — 2026-09-02T10:38:37Z

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
| XRPUSDT | IDLE | 1.67 | 2.96 | 2.58 | -0.04 | 39177116.65 | 2.28 | skipped_fast |
| ETHUSDT | IDLE | 1.63 | 2.87 | 2.57 | -0.04 | 391423440.25 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.95 | 1.67 | 1.54 | -0.02 | 507429474.57 | 0.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.83 | 8.6 | 3.94 | 0.15 | 974638.29 | 4.46 | skipped_fast |
| PYTHUSDT | IDLE | 1.55 | 4.84 | 4.53 | 0.07 | 863228.06 | 1.86 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 15.86 | 8.08 | 0.02 | 172335.24 | 25.07 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.52 | 3.08 | -0.0 | 406727.51 | 14.68 | skipped_fast |
| KITEUSDT | IDLE | 2.41 | 9.6 | 2.59 | 0.13 | 82168.02 | 9.72 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 2.9 | 2.1 | -0.07 | 325432.08 | 8.91 | skipped_fast |
| RWAINCUSDT | IDLE | 2.76 | 8.35 | 2.64 | 0.08 | 10712.86 | 59.35 | skipped_fast |
| RIZEUSDT | IDLE | 2.1 | 7.95 | 6.46 | -0.13 | 40612.16 | 48.26 | skipped_fast |
| QNTUSDT | IDLE | 3.01 | 6.12 | 4.75 | 0.03 | 69010.66 | 4.7 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 2.07 | 1.17 | -0.03 | 233091.17 | 19.73 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.48 | 2.22 | -0.04 | 76441.51 | 7.97 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 1.82 | 1.45 | 0.01 | 153711.67 | 13.56 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.57 | 1.53 | -0.02 | 257250.17 | 1.37 | skipped_fast |
| TELUSDT | IDLE | 1.71 | 3.02 | 2.63 | -0.03 | 85883.12 | 36.08 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.52 | 1.49 | -0.04 | 328.21 | 21.34 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.62 | 0.38 | 0.0 | 50577.32 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.75 | 0.67 | -0.02 | 36664.64 | 27.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
