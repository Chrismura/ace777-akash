# Hulk DIGEST — 2026-10-25T10:01:12Z

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
| ETHUSDT | IDLE | 1.21 | 2.16 | 1.68 | -0.02 | 128195563.91 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 1.95 | 1.47 | 0.01 | 22689435.58 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.02 | 0.71 | -0.0 | 202636503.12 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.17 | 3.96 | 2.48 | -0.04 | 811008.42 | 19.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.78 | 3.31 | 1.62 | 0.01 | 484499.86 | 2.83 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 3.33 | 3.02 | -0.08 | 546231.98 | 23.7 | skipped_fast |
| REDUSDT | IDLE | 2.45 | 4.39 | 3.35 | -0.05 | 74008.28 | 14.55 | skipped_fast |
| QNTUSDT | IDLE | 2.22 | 4.04 | 2.71 | 0.01 | 392418.32 | 1.11 | skipped_fast |
| BIOUSDT | IDLE | 2.08 | 3.77 | 2.54 | -0.04 | 65729.54 | 4.5 | skipped_fast |
| CCUSDT | IDLE | 1.11 | 2.04 | 1.21 | -0.02 | 196115.67 | 7.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 3.11 | 1.67 | -0.02 | 56597.98 | 5.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.46 | 4.36 | 2.17 | 0.04 | 88558.48 | 18.11 | skipped_fast |
| KITEUSDT | IDLE | 1.57 | 2.87 | 1.84 | -0.05 | 58987.83 | 11.67 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.73 | 1.1 | 0.01 | 229842.6 | 13.94 | skipped_fast |
| WAXLUSDT | IDLE | 2.74 | 5.62 | 4.36 | -0.05 | 53880.4 | 54.33 | skipped_fast |
| LAUSDT | IDLE | 1.34 | 9.18 | 5.56 | -0.13 | 93229.47 | 22.51 | skipped_fast |
| IOTAUSDT | IDLE | 1.81 | 3.29 | 2.14 | -0.02 | 66563.86 | 27.94 | skipped_fast |
| FLUIDUSDT | IDLE | 1.96 | 3.43 | 3.31 | -0.06 | 7703.06 | 21.48 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.89 | 1.31 | 0.01 | 200814.24 | 12.99 | skipped_fast |
| RIZEUSDT | IDLE | 0.31 | 0.86 | 0.37 | -0.04 | 41438.33 | 43.73 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.59 | 0.24 | 0.01 | 51744.7 | 55.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.76 | 0.26 | -0.01 | 37479.23 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
