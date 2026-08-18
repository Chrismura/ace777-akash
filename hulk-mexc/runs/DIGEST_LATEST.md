# Hulk DIGEST — 2026-08-18T00:17:20Z

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
| XRPUSDT | IDLE | 0.29 | 0.56 | 0.12 | 0.01 | 12163455.66 | 1.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.21 | 5.74 | 3.52 | -0.01 | 341673.74 | 7.22 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.69 | 1.04 | -0.07 | 256433.89 | 10.0 | skipped_fast |
| EDELUSDT | IDLE | 1.73 | 3.16 | 2.04 | -0.0 | 66264.96 | 13.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.07 | 1.92 | 1.48 | 0.01 | 228951.97 | 23.41 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.13 | 2.73 | -0.05 | 3971.62 | 60.2 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 5.85 | 2.24 | -0.05 | 130908.39 | 21.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 7.23 | 5.89 | 0.06 | 88782.41 | 45.39 | skipped_fast |
| PYTHUSDT | IDLE | 0.87 | 1.56 | 1.2 | 0.01 | 143253.72 | 2.59 | skipped_fast |
| WUSDT | IDLE | 0.75 | 1.31 | 1.23 | -0.04 | 136249.72 | 13.38 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.11 | 0.88 | 0.01 | 57009.32 | 26.53 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.18 | 1.05 | 0.02 | 80230.03 | 4.06 | skipped_fast |
| KITEUSDT | IDLE | 0.69 | 1.24 | 0.87 | -0.01 | 60711.27 | 16.26 | skipped_fast |
| RWAINCUSDT | IDLE | 0.41 | 0.76 | 0.41 | -0.03 | 1053.49 | 58.58 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 1.61 | 1.23 | 0.0 | 35394.66 | 7.03 | skipped_fast |
| HBARUSDT | IDLE | 0.3 | 0.61 | 0.0 | 0.03 | 122771.88 | 1.51 | skipped_fast |
| FLUIDUSDT | IDLE | 0.62 | 1.24 | 0.0 | -0.02 | 741.14 | 22.61 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.61 | 0.17 | 0.02 | 49518.71 | 25.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
