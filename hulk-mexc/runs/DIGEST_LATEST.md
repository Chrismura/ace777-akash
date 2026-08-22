# Hulk DIGEST — 2026-08-22T17:02:07Z

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
| PYTHUSDT | IDLE | 1.71 | 8.33 | 0.83 | 0.09 | 49194474.18 | 3.82 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.22 | 0.06 | 214538651.9 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.96 | -0.0 | 1125093.13 | 6.45 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 4.14 | 0.66 | 0.1 | 773489.92 | 9.22 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.73 | -0.1 | 631121.35 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.36 | -0.01 | 543911.69 | 12.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.35 | -0.02 | 312661.99 | 11.25 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.52 | -0.07 | 226112.04 | 3.34 | skipped_fast |
| EDELUSDT | IDLE | 1.66 | 3.0 | 2.13 | -0.02 | 74794.38 | 34.23 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 3.22 | 1.19 | 0.03 | 87636.1 | 18.63 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.65 | -0.13 | 125393.92 | 10.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.44 | 0.05 | 46184.94 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.96 | -0.01 | 181141.76 | 3.14 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.05 | -0.0 | 136176.48 | 37.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 91.62 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.16 | 0.02 | 56354.5 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
