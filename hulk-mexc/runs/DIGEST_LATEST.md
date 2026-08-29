# Hulk DIGEST — 2026-08-29T16:11:23Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 78.54 | 38.67 | -0.03 | 139213.99 | 54.2 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.62 | 0.65 | -0.01 | 25875683.21 | 2.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 4.76 | 0.31 | -0.02 | 1028691.93 | 12.07 | skipped_fast |
| KITEUSDT | IDLE | 3.32 | 10.27 | 4.75 | 0.07 | 69302.68 | 8.23 | skipped_fast |
| PYTHUSDT | IDLE | 2.12 | 4.07 | 1.19 | 0.02 | 352647.78 | 2.08 | skipped_fast |
| REDUSDT | IDLE | 2.54 | 6.18 | 4.59 | 0.06 | 76689.49 | 21.98 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 3.7 | 0.57 | 0.05 | 210709.96 | 9.49 | skipped_fast |
| RIZEUSDT | IDLE | 2.63 | 5.39 | 2.64 | -0.03 | 26029.19 | 55.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.3 | 0.29 | -0.05 | 189690.3 | 15.24 | skipped_fast |
| WUSDT | IDLE | 1.09 | 2.17 | 0.12 | 0.0 | 201946.73 | 15.24 | skipped_fast |
| BIOUSDT | IDLE | 0.82 | 1.57 | 0.43 | -0.01 | 68376.86 | 3.61 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.53 | 0.26 | 0.01 | 230711.12 | 1.32 | skipped_fast |
| TELUSDT | IDLE | 0.88 | 1.62 | 0.97 | -0.03 | 72975.62 | 46.03 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.37 | 0.11 | 0.01 | 30548.96 | 4.88 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.56 | 0.0 | 0.01 | 2052.39 | 0.76 | skipped_fast |
| RWAINCUSDT | IDLE | 0.39 | 0.78 | 0.0 | -0.02 | 4175.82 | 111.3 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.5 | 0.08 | -0.02 | 54426.28 | 16.45 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
