# Hulk DIGEST — 2026-08-22T11:46:01Z

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
| PYTHUSDT | IDLE | 2.15 | 9.66 | 6.49 | 0.01 | 51615358.22 | 6.13 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.44 | 0.08 | 216661350.0 | 2.01 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.57 | 0.13 | 787571.75 | 7.7 | skipped_fast |
| HBARUSDT | IDLE | 1.45 | 5.26 | 3.22 | 0.02 | 1256108.74 | 3.87 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.55 | 0.02 | 582878.84 | 13.73 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.21 | -0.03 | 388017.11 | 33.43 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.52 | -0.1 | 623042.55 | 6.7 | skipped_fast |
| EDELUSDT | IDLE | 2.8 | 4.93 | 4.48 | -0.04 | 79154.16 | 45.56 | skipped_fast |
| KITEUSDT | IDLE | 2.45 | 5.93 | 0.0 | 0.05 | 80630.3 | 11.43 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 6.64 | 1.82 | -0.04 | 243446.44 | 3.21 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.56 | -0.03 | 167276.53 | 37.5 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2456.68 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.27 | 0.04 | 154532.94 | 16.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 76.09 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.77 | -0.03 | 48680.81 | 37.86 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.82 | 0.0 | 188354.48 | 10.91 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.52 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.01 | 57731.48 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
