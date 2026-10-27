# Hulk DIGEST — 2026-10-27T20:27:25Z

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
| ETHUSDT | IDLE | 0.63 | 1.19 | 0.49 | 0.01 | 228793360.81 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.59 | 1.11 | 0.46 | 0.02 | 19346770.54 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.7 | 0.13 | 0.01 | 319236180.34 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.3 | 5.0 | 3.87 | 0.04 | 671171.7 | 16.35 | skipped_fast |
| EDELUSDT | IDLE | 1.26 | 2.23 | 1.91 | 0.01 | 481707.6 | 21.61 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.75 | 0.76 | -0.01 | 375474.11 | 2.74 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 2.27 | 0.52 | -0.01 | 712457.23 | 5.48 | skipped_fast |
| CHIPUSDT | IDLE | 2.03 | 5.11 | 0.84 | 0.06 | 130493.49 | 16.46 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.26 | 2.17 | -0.01 | 223782.7 | 10.21 | skipped_fast |
| RWAINCUSDT | IDLE | 1.87 | 4.2 | 1.69 | -0.05 | 63506.72 | 6.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.08 | 2.94 | 2.15 | 0.02 | 237659.19 | 27.87 | skipped_fast |
| BIOUSDT | IDLE | 1.6 | 3.08 | 0.75 | 0.02 | 58822.95 | 8.85 | skipped_fast |
| REDUSDT | IDLE | 1.37 | 2.91 | 0.93 | 0.07 | 60057.39 | 16.09 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 2.38 | 1.73 | 0.04 | 57848.69 | 12.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.71 | 3.34 | 0.55 | -0.0 | 32574.57 | 55.83 | skipped_fast |
| LAUSDT | IDLE | 2.63 | 5.38 | 2.21 | 0.03 | 58563.63 | 34.83 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.75 | 0.59 | -0.01 | 271016.36 | 1.31 | skipped_fast |
| IOTAUSDT | IDLE | 1.03 | 1.82 | 1.55 | -0.01 | 79659.22 | 31.0 | skipped_fast |
| WAXLUSDT | IDLE | 0.78 | 1.5 | 0.38 | 0.04 | 56013.0 | 34.58 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.29 | 0.32 | -0.0 | 57252.08 | 31.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 1.47 | 0.12 | 0.01 | 2620.62 | 21.35 | skipped_fast |
| MNSRYUSDT | IDLE | 0.44 | 0.78 | 0.69 | -0.0 | 37693.59 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
