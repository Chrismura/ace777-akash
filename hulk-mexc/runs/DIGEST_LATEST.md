# Hulk DIGEST — 2026-08-22T12:13:56Z

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.92 | 0.12 | 215178947.71 | 4.63 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 7.83 | 4.08 | 0.02 | 51609096.85 | 70.39 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.24 | 0.03 | 1251628.12 | 5.14 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.28 | 0.14 | 775007.86 | 1.7 | skipped_fast |
| WUSDT | IDLE | 1.53 | 6.27 | 3.07 | 0.02 | 578663.57 | 13.66 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 5.77 | 4.1 | -0.03 | 371459.28 | 4.63 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 0.92 | -0.1 | 616212.63 | 3.33 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.28 | 0.04 | 82634.1 | 11.45 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.2 | -0.03 | 78022.68 | 22.78 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 5.65 | 1.04 | -0.02 | 240845.81 | 3.17 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.76 | 0.03 | 153542.79 | 11.49 | skipped_fast |
| TELUSDT | IDLE | 2.18 | 5.61 | 4.14 | -0.02 | 164768.29 | 47.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 3.47 | 1.27 | 0.01 | 187857.07 | 1.55 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.91 | 0.44 | -0.05 | 48115.1 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.29 | 0.02 | 57749.34 | 16.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 21.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
