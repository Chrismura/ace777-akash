# Hulk DIGEST — 2026-08-22T12:32:58Z

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.76 | 0.12 | 215930422.52 | 1.98 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 7.83 | 2.2 | 0.04 | 51604567.82 | 7.95 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 4.63 | 2.12 | 0.03 | 1260601.18 | 6.42 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.88 | 0.14 | 777476.57 | 5.86 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.56 | 0.02 | 577880.52 | 12.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.19 | 5.77 | 3.5 | -0.02 | 338077.91 | 8.7 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.32 | -0.1 | 605422.67 | 3.35 | skipped_fast |
| KITEUSDT | IDLE | 2.66 | 6.37 | 0.46 | 0.04 | 83423.64 | 6.17 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 3.89 | 2.43 | -0.02 | 78129.59 | 22.57 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 5.65 | 1.57 | -0.02 | 242054.22 | 15.99 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.16 | 2.56 | -0.01 | 2400.49 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.29 | 0.01 | 153163.77 | 19.55 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.88 | -0.03 | 163529.08 | 47.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.55 | -0.0 | 188072.12 | 7.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.17 | -0.0 | 46775.94 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57782.28 | 8.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 22.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
