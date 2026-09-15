# Hulk DIGEST — 2026-09-15T18:36:36Z

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
| XRPUSDT | IDLE | 3.26 | 6.39 | 4.57 | -0.04 | 81148393.69 | 2.87 | skipped_fast |
| ETHUSDT | IDLE | 1.87 | 4.03 | 2.32 | -0.04 | 505346958.13 | 1.4 | skipped_fast |
| BTCUSDT | IDLE | 1.21 | 2.3 | 0.8 | -0.03 | 587062598.06 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 34.62 | 6.16 | 0.58 | 488846.68 | 60.63 | skipped_fast |
| PYTHUSDT | IDLE | 2.27 | 4.28 | 2.96 | -0.05 | 567896.57 | 29.97 | skipped_fast |
| ZBCNUSDT | IDLE | 3.03 | 6.57 | 1.01 | 0.0 | 213428.76 | 69.77 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 3.29 | 1.82 | -0.04 | 323184.79 | 12.8 | skipped_fast |
| CHIPUSDT | IDLE | 2.35 | 8.03 | 5.01 | -0.1 | 97574.92 | 26.41 | skipped_fast |
| HBARUSDT | IDLE | 2.25 | 4.08 | 2.77 | -0.01 | 438853.11 | 21.91 | skipped_fast |
| WUSDT | IDLE | 1.67 | 3.44 | 2.71 | -0.06 | 184457.51 | 18.04 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 3.83 | 2.85 | -0.05 | 8341.18 | 11.49 | skipped_fast |
| KITEUSDT | IDLE | 2.33 | 4.19 | 3.18 | -0.02 | 64338.35 | 90.69 | skipped_fast |
| REDUSDT | IDLE | 1.04 | 5.38 | 4.06 | -0.05 | 101290.33 | 19.52 | skipped_fast |
| BIOUSDT | IDLE | 1.83 | 3.45 | 1.45 | -0.04 | 77914.18 | 59.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 9.74 | 7.32 | 0.06 | 50978.59 | 91.87 | skipped_fast |
| TELUSDT | IDLE | 1.32 | 4.37 | 1.77 | -0.04 | 100591.01 | 51.58 | skipped_fast |
| QNTUSDT | IDLE | 1.18 | 2.22 | 0.87 | -0.02 | 49488.93 | 11.19 | skipped_fast |
| RWAUSDT | IDLE | 1.38 | 2.56 | 1.32 | -0.0 | 52167.76 | 59.52 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.63 | 1.8 | -0.06 | 1665.53 | 49.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 0.98 | 0.68 | -0.01 | 32050.07 | 32.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
