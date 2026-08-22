# Hulk DIGEST — 2026-08-22T11:12:01Z

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
| PYTHUSDT | IDLE | 2.2 | 9.66 | 8.1 | -0.0 | 51657708.81 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.52 | 0.07 | 217947203.23 | 4.03 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 10.24 | 7.92 | 0.1 | 812430.9 | 7.81 | skipped_fast |
| HBARUSDT | IDLE | 1.47 | 5.26 | 3.65 | 0.0 | 1254110.37 | 5.19 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.72 | 0.02 | 587509.09 | 9.53 | skipped_fast |
| ZBCNUSDT | IDLE | 2.34 | 5.93 | 5.25 | -0.04 | 400014.13 | 31.23 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 2.21 | -0.11 | 645116.04 | 6.75 | skipped_fast |
| EDELUSDT | IDLE | 2.77 | 4.93 | 4.04 | -0.05 | 78773.24 | 34.19 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.64 | 4.09 | -0.05 | 238383.48 | 3.28 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 4.3 | 1.55 | 0.04 | 73620.4 | 11.83 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.46 | -0.04 | 169332.44 | 48.22 | skipped_fast |
| QAITUSDT | IDLE | 2.25 | 4.16 | 2.21 | 0.0 | 2493.13 | 63.67 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 5.2 | 0.02 | 154654.27 | 21.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | -0.01 | 11311.88 | 59.83 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.99 | -0.0 | 189022.35 | 9.38 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.68 | 0.01 | 49281.04 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.38 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.8 | 1.69 | 0.01 | 57483.08 | 24.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
