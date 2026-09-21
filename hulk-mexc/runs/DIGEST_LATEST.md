# Hulk DIGEST — 2026-09-21T05:04:05Z

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
| XRPUSDT | IDLE | 1.36 | 2.51 | 1.36 | 0.03 | 40004449.2 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 1.29 | 2.36 | 1.48 | 0.03 | 336381806.72 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.49 | 0.79 | 0.01 | 444274692.55 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 31.66 | 16.97 | -0.13 | 39390.18 | 65.39 | skipped_fast |
| HBARUSDT | IDLE | 1.4 | 4.06 | 1.87 | 0.08 | 1263317.41 | 2.31 | skipped_fast |
| WUSDT | IDLE | 2.53 | 9.67 | 2.54 | 0.1 | 531219.24 | 14.09 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 4.3 | 2.72 | 0.04 | 545183.58 | 4.91 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 4.04 | 1.61 | 0.06 | 420101.13 | 9.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 3.78 | 0.56 | 0.03 | 196446.85 | 17.7 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 4.8 | 3.12 | 0.02 | 81399.32 | 21.16 | skipped_fast |
| BIOUSDT | IDLE | 1.63 | 3.15 | 0.67 | 0.03 | 81725.44 | 14.28 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 2.4 | 1.29 | 0.02 | 59888.4 | 11.25 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 2.05 | 0.89 | 0.0 | 81150.77 | 7.27 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 7.11 | 2.44 | 0.49 | 196008.08 | 55.38 | skipped_fast |
| RWAINCUSDT | IDLE | 1.41 | 2.77 | 0.29 | 0.01 | 7501.38 | 5.87 | skipped_fast |
| QNTUSDT | IDLE | 1.41 | 2.71 | 0.73 | 0.01 | 113653.28 | 4.59 | skipped_fast |
| TELUSDT | IDLE | 1.44 | 2.65 | 1.48 | 0.04 | 87479.59 | 32.75 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.33 | 1.61 | 0.0 | 4016.62 | 22.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.57 | 1.1 | 0.29 | 0.0 | 39841.9 | 3.96 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.17 | 0.65 | 0.02 | 55090.9 | 21.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
