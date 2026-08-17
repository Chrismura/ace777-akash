# Hulk DIGEST — 2026-08-17T08:10:49Z

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
| XRPUSDT | IDLE | 0.37 | 0.65 | 0.56 | -0.0 | 9707048.07 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 3.12 | 15.04 | 2.35 | 0.16 | 336532.96 | 15.65 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 2.97 | 0.6 | 0.01 | 64014.81 | 4.03 | skipped_fast |
| RIZEUSDT | IDLE | 1.38 | 11.21 | 2.01 | 0.13 | 48425.47 | 54.53 | skipped_fast |
| WUSDT | IDLE | 0.96 | 1.68 | 1.65 | 0.01 | 185992.55 | 8.33 | skipped_fast |
| CCUSDT | IDLE | 0.71 | 1.34 | 0.48 | -0.01 | 251286.75 | 9.43 | skipped_fast |
| PYTHUSDT | IDLE | 1.01 | 1.96 | 0.4 | 0.0 | 166232.37 | 2.54 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.75 | 2.27 | -0.05 | 57965.73 | 18.99 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.54 | 2.41 | -0.01 | 53793.55 | 12.85 | skipped_fast |
| EDELUSDT | IDLE | 1.31 | 2.49 | 0.9 | 0.04 | 55309.55 | 25.84 | skipped_fast |
| ZBCNUSDT | IDLE | 0.57 | 1.1 | 0.23 | 0.01 | 176553.41 | 15.22 | skipped_fast |
| QAITUSDT | IDLE | 0.96 | 2.41 | 0.0 | -0.01 | 2368.59 | 61.12 | skipped_fast |
| RWAINCUSDT | IDLE | 0.55 | 1.02 | 0.56 | -0.02 | 2234.64 | 62.55 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.57 | 0.67 | 0.0 | 108657.03 | 1.53 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 1.65 | 1.49 | -0.0 | 87580.98 | 20.58 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.28 | 0.62 | -0.03 | 31551.64 | 1.79 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.66 | 1.28 | 0.01 | 823.44 | 21.91 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.17 | 0.01 | 48754.9 | 17.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
