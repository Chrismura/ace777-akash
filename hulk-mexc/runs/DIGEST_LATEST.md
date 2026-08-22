# Hulk DIGEST — 2026-08-22T12:12:40Z

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
| PYTHUSDT | IDLE | 1.72 | 7.83 | 4.58 | 0.02 | 51608114.82 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.98 | 0.12 | 215218665.0 | 4.63 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.27 | 0.03 | 1251870.89 | 5.14 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 8.38 | 4.45 | 0.13 | 775022.75 | 6.8 | skipped_fast |
| WUSDT | IDLE | 1.54 | 6.27 | 3.14 | 0.02 | 578469.96 | 10.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.23 | 5.77 | 4.18 | -0.03 | 375522.83 | 29.37 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 0.96 | -0.1 | 616395.37 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.58 | 6.24 | 0.0 | 0.04 | 82645.57 | 10.57 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.31 | -0.03 | 78022.62 | 11.4 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 5.65 | 0.82 | -0.02 | 240848.1 | 3.18 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.12 | 0.02 | 153557.84 | 11.51 | skipped_fast |
| TELUSDT | IDLE | 2.18 | 5.61 | 4.24 | -0.03 | 164769.02 | 53.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 3.47 | 1.27 | 0.01 | 187853.13 | 1.55 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.91 | 0.39 | -0.05 | 48026.55 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.53 | 0.01 | 57766.55 | 8.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 22.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
