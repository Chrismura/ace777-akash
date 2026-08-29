# Hulk DIGEST — 2026-08-29T11:10:41Z

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
| CHIPUSDT | IDLE | 2.22 | 10.29 | 7.19 | -0.04 | 1267956.72 | 4.85 | skipped_fast |
| XRPUSDT | IDLE | 0.49 | 0.93 | 0.32 | -0.03 | 40204404.74 | 2.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.32 | 1.78 | -0.03 | 423501.85 | 2.14 | skipped_fast |
| CCUSDT | IDLE | 1.73 | 3.33 | 0.81 | -0.0 | 201881.77 | 8.87 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.59 | 2.48 | -0.05 | 210755.73 | 14.37 | skipped_fast |
| REDUSDT | IDLE | 1.82 | 5.6 | 0.58 | 0.08 | 71436.37 | 23.69 | skipped_fast |
| EDELUSDT | IDLE | 1.23 | 4.55 | 3.78 | -0.13 | 91572.4 | 29.51 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.92 | 1.67 | -0.07 | 199394.42 | 13.34 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.82 | 1.61 | -0.04 | 84368.23 | 3.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.58 | 3.21 | 1.75 | -0.01 | 27562.27 | 58.52 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.97 | 0.09 | 0.01 | 62123.68 | 12.48 | skipped_fast |
| QAITUSDT | IDLE | 0.43 | 4.07 | 0.66 | -0.01 | 84997.43 | 5.11 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.05 | 0.85 | -0.04 | 372664.36 | 1.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.28 | 2.23 | -0.03 | 3674.22 | 88.35 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.25 | 0.81 | -0.03 | 41016.36 | 1.63 | skipped_fast |
| TELUSDT | IDLE | 0.78 | 1.45 | 0.68 | -0.05 | 80541.66 | 40.2 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.74 | 0.66 | 0.01 | 57234.94 | 8.25 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 0.66 | 0.65 | -0.06 | 3665.9 | 21.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
