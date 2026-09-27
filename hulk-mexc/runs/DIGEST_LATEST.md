# Hulk DIGEST — 2026-09-27T16:09:44Z

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
| PYTHUSDT | IDLE | 1.87 | 6.98 | 5.7 | 0.06 | 2147801.13 | 4.81 | skipped_fast |
| WUSDT | IDLE | 1.48 | 9.59 | 1.24 | 0.2 | 3927615.56 | 13.71 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 16.63 | 1.46 | 0.55 | 5967654.83 | 16.63 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 2.43 | 1.56 | -0.02 | 44310506.31 | 2.63 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.28 | 0.85 | 0.0 | 190464677.68 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.51 | 0.92 | 0.67 | 0.01 | 450196518.46 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 42.2 | 18.84 | 0.22 | 23087.08 | 137.22 | skipped_fast |
| CCUSDT | IDLE | 2.56 | 4.61 | 3.45 | -0.04 | 535771.9 | 11.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.95 | 6.08 | 4.7 | -0.09 | 97711.51 | 12.74 | skipped_fast |
| HBARUSDT | IDLE | 1.69 | 3.07 | 2.04 | -0.01 | 678470.63 | 2.13 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 7.94 | 6.5 | -0.1 | 141264.91 | 84.17 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.18 | 1.61 | 0.06 | 176136.79 | 6.7 | skipped_fast |
| BIOUSDT | IDLE | 1.64 | 3.05 | 1.47 | -0.03 | 96678.4 | 9.51 | skipped_fast |
| ZBCNUSDT | IDLE | 0.94 | 1.75 | 0.83 | -0.02 | 214054.41 | 13.24 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 2.2 | 0.92 | 0.01 | 64953.79 | 14.1 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 7.78 | 0.74 | 0.17 | 148186.95 | 21.3 | skipped_fast |
| RIZEUSDT | IDLE | 0.58 | 2.1 | 1.62 | -0.06 | 46351.85 | 20.84 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.75 | 0.28 | 0.02 | 1536.1 | 21.46 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.85 | 0.28 | 0.01 | 56430.55 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.7 | 0.59 | 0.01 | 39757.3 | 37.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
