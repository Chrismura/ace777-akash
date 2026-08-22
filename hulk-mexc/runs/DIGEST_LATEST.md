# Hulk DIGEST — 2026-08-22T11:19:35Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 8.0 | 0.0 | 51648309.14 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 2.35 | 14.26 | 8.9 | 0.07 | 217486804.75 | 1.35 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 10.24 | 7.48 | 0.11 | 812603.44 | 6.91 | skipped_fast |
| HBARUSDT | IDLE | 1.48 | 5.26 | 3.81 | 0.01 | 1257365.09 | 6.5 | skipped_fast |
| WUSDT | IDLE | 1.57 | 6.27 | 4.05 | 0.01 | 583605.65 | 13.81 | skipped_fast |
| ZBCNUSDT | IDLE | 2.33 | 5.93 | 5.08 | -0.04 | 397122.14 | 7.79 | skipped_fast |
| CHIPUSDT | IDLE | 0.74 | 4.16 | 2.48 | -0.11 | 645451.99 | 3.39 | skipped_fast |
| EDELUSDT | IDLE | 2.79 | 4.93 | 4.37 | -0.05 | 78916.05 | 22.78 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.64 | 3.65 | -0.05 | 237160.94 | 3.26 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.66 | 6.75 | 5.81 | -0.04 | 169097.13 | 21.48 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 4.3 | 1.39 | 0.03 | 73726.38 | 12.71 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2502.14 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.49 | 6.02 | 5.17 | 0.01 | 154485.41 | 18.13 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 11345.68 | 38.12 | skipped_fast |
| QNTUSDT | IDLE | 1.1 | 3.47 | 2.43 | -0.0 | 188697.12 | 1.57 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.87 | 0.0 | 49259.09 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.4 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 1.8 | 1.61 | 0.01 | 57401.32 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
