# Hulk DIGEST — 2026-08-28T04:06:58Z

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
| PYTHUSDT | IDLE | 1.54 | 3.59 | 3.0 | 0.02 | 21159915.58 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.91 | 3.37 | 3.01 | 0.01 | 56337221.15 | 2.8 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 9.97 | 7.26 | 0.04 | 775952.19 | 5.25 | skipped_fast |
| CCUSDT | IDLE | 2.12 | 3.75 | 3.33 | -0.04 | 468920.14 | 11.68 | skipped_fast |
| BIOUSDT | IDLE | 2.92 | 5.18 | 4.45 | -0.01 | 98086.12 | 7.01 | skipped_fast |
| WUSDT | IDLE | 2.42 | 4.27 | 3.76 | 0.0 | 189115.57 | 8.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 3.77 | 3.47 | 0.06 | 232344.69 | 13.44 | skipped_fast |
| KITEUSDT | IDLE | 1.77 | 3.15 | 2.54 | 0.02 | 79117.83 | 8.62 | skipped_fast |
| REDUSDT | IDLE | 1.9 | 3.73 | 0.46 | 0.03 | 82666.3 | 19.69 | skipped_fast |
| QAITUSDT | IDLE | 0.4 | 19.2 | 14.69 | -0.22 | 60671.8 | 55.57 | skipped_fast |
| HBARUSDT | IDLE | 1.65 | 2.88 | 2.8 | 0.0 | 329443.39 | 1.29 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 7.75 | 4.39 | -0.19 | 113725.8 | 56.56 | skipped_fast |
| EDELUSDT | IDLE | 0.61 | 4.43 | 3.74 | 0.1 | 36112.68 | 43.12 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 2.57 | 2.3 | 0.02 | 122548.28 | 32.03 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.39 | 2.02 | -0.01 | 44998.82 | 3.22 | skipped_fast |
| RWAINCUSDT | IDLE | 0.17 | 0.64 | 0.0 | -0.05 | 21560.19 | 16.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 3.34 | 3.23 | -0.02 | 9108.23 | 21.43 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.92 | 0.08 | 0.01 | 54366.19 | 24.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
