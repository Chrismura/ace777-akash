# Hulk DIGEST — 2026-08-17T19:13:32Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.56 | 1.01 | 0.77 | 0.0 | 12786451.35 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 9.58 | 8.54 | -0.02 | 349181.57 | 3.55 | skipped_fast |
| EDELUSDT | IDLE | 3.78 | 6.84 | 4.8 | 0.02 | 66202.6 | 38.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.44 | 4.83 | 0.4 | 0.02 | 197691.02 | 13.14 | skipped_fast |
| REDUSDT | IDLE | 2.83 | 5.41 | 1.67 | -0.01 | 58511.01 | 17.47 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 3.16 | 2.74 | -0.05 | 231303.28 | 4.41 | skipped_fast |
| QAITUSDT | IDLE | 2.65 | 5.09 | 1.41 | -0.01 | 1047.96 | 62.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.24 | 11.55 | 7.37 | 0.14 | 86286.46 | 47.31 | skipped_fast |
| PYTHUSDT | IDLE | 1.06 | 1.92 | 1.35 | -0.01 | 162366.59 | 5.17 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.49 | 1.75 | 0.01 | 82197.0 | 4.05 | skipped_fast |
| WUSDT | IDLE | 1.0 | 1.74 | 1.68 | -0.03 | 149780.69 | 16.94 | skipped_fast |
| TELUSDT | IDLE | 1.9 | 3.44 | 2.36 | -0.03 | 119336.62 | 42.55 | skipped_fast |
| KITEUSDT | IDLE | 0.55 | 1.02 | 0.47 | -0.02 | 60399.16 | 16.19 | skipped_fast |
| FLUIDUSDT | IDLE | 2.04 | 3.61 | 3.17 | -0.03 | 761.15 | 21.61 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.19 | 0.75 | 0.01 | 144671.4 | 1.52 | skipped_fast |
| RWAINCUSDT | IDLE | 0.3 | 0.52 | 0.52 | -0.03 | 1225.45 | 63.97 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.51 | 0.94 | -0.0 | 36713.06 | 7.0 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.69 | 0.52 | 0.01 | 49518.24 | 8.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
