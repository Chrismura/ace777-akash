# Hulk DIGEST — 2026-08-28T06:07:19Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| PYTHUSDT | IDLE | 1.79 | 3.65 | 2.92 | 0.02 | 18610917.59 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 2.17 | 3.83 | 3.35 | 0.01 | 56521245.3 | 1.4 | skipped_fast |
| QAITUSDT | IDLE | 1.07 | 55.46 | 32.26 | -0.2 | 73033.19 | 50.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.01 | 9.97 | 4.29 | 0.07 | 679806.2 | 5.1 | skipped_fast |
| CCUSDT | IDLE | 2.1 | 3.96 | 1.6 | -0.03 | 461752.14 | 9.71 | skipped_fast |
| WUSDT | IDLE | 2.78 | 5.02 | 3.66 | 0.01 | 204993.97 | 12.68 | skipped_fast |
| BIOUSDT | IDLE | 2.96 | 5.25 | 4.49 | 0.01 | 95692.54 | 7.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 4.42 | 3.26 | 0.05 | 258243.45 | 2.39 | skipped_fast |
| KITEUSDT | IDLE | 2.01 | 3.7 | 2.19 | 0.0 | 78734.81 | 21.05 | skipped_fast |
| REDUSDT | IDLE | 1.65 | 3.09 | 1.45 | 0.02 | 82327.73 | 14.46 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.24 | 2.07 | 0.01 | 314681.37 | 2.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.94 | 11.77 | 2.66 | -0.17 | 119668.05 | 53.43 | skipped_fast |
| TELUSDT | IDLE | 2.03 | 3.58 | 3.19 | 0.01 | 124429.7 | 37.85 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 4.52 | 4.33 | 0.1 | 41006.81 | 34.72 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.49 | 1.61 | -0.0 | 45542.46 | 1.6 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 3.34 | 1.83 | 0.01 | 7985.78 | 19.74 | skipped_fast |
| RWAINCUSDT | IDLE | 0.44 | 1.35 | 1.33 | -0.03 | 20708.18 | 150.86 | skipped_fast |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
