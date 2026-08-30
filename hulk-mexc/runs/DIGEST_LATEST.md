# Hulk DIGEST — 2026-08-30T17:25:18Z

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
| ETHUSDT | IDLE | 1.63 | 3.05 | 1.41 | 0.02 | 211565965.42 | 0.32 | skipped_fast |
| XRPUSDT | IDLE | 1.3 | 2.44 | 1.13 | 0.02 | 20429919.77 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.58 | 0.76 | 0.01 | 275373790.58 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 7.33 | 6.01 | -0.03 | 512712.8 | 2.51 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 9.26 | 5.43 | -0.06 | 195912.83 | 45.14 | skipped_fast |
| PYTHUSDT | IDLE | 3.07 | 5.66 | 3.23 | 0.02 | 391067.14 | 14.4 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 5.99 | 3.23 | 0.07 | 72662.37 | 16.71 | skipped_fast |
| WUSDT | IDLE | 1.6 | 3.02 | 1.2 | 0.04 | 222523.44 | 13.69 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 1.62 | 1.55 | 0.01 | 255973.11 | 7.63 | skipped_fast |
| REDUSDT | IDLE | 1.13 | 2.02 | 1.57 | 0.02 | 62385.53 | 11.84 | skipped_fast |
| KITEUSDT | IDLE | 1.03 | 1.8 | 1.77 | -0.02 | 61201.58 | 8.64 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.65 | 0.76 | -0.0 | 79654.63 | 3.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.27 | 4.02 | 3.55 | -0.07 | 37446.91 | 62.12 | skipped_fast |
| TELUSDT | IDLE | 2.21 | 4.37 | 0.34 | -0.0 | 83137.34 | 46.06 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.63 | 0.0 | 0.02 | 1921.2 | 120.81 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.21 | 0.37 | 0.0 | 133111.65 | 2.65 | skipped_fast |
| QNTUSDT | IDLE | 0.54 | 0.97 | 0.72 | 0.01 | 38439.01 | 3.24 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.22 | 0.08 | 0.02 | 52719.87 | 24.22 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.01 | 32216.57 | 32.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 34.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
