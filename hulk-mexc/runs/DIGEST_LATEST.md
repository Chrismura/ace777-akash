# Hulk DIGEST — 2026-08-29T05:09:00Z

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
| XRPUSDT | IDLE | 0.45 | 0.88 | 0.14 | -0.02 | 44211140.32 | 2.88 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 8.91 | 1.78 | 0.07 | 1134201.29 | 9.46 | skipped_fast |
| QAITUSDT | IDLE | 2.35 | 20.42 | 14.43 | -0.02 | 96080.9 | 10.17 | skipped_fast |
| PYTHUSDT | IDLE | 0.82 | 1.48 | 1.06 | -0.02 | 524414.17 | 2.11 | skipped_fast |
| RIZEUSDT | IDLE | 2.57 | 6.2 | 2.21 | -0.05 | 29247.9 | 30.13 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.75 | 0.97 | -0.01 | 243973.53 | 8.1 | skipped_fast |
| WUSDT | IDLE | 1.0 | 1.92 | 0.59 | -0.02 | 209042.44 | 13.02 | skipped_fast |
| EDELUSDT | IDLE | 1.33 | 5.29 | 1.49 | -0.08 | 90523.17 | 18.9 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 2.76 | 1.56 | -0.0 | 73592.55 | 10.21 | skipped_fast |
| REDUSDT | IDLE | 1.37 | 3.09 | 1.17 | -0.01 | 61271.83 | 20.22 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.23 | 1.07 | -0.03 | 468237.46 | 1.32 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.87 | 0.02 | -0.05 | 173530.5 | 7.1 | skipped_fast |
| BIOUSDT | IDLE | 0.5 | 0.94 | 0.39 | -0.02 | 83503.46 | 3.59 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 3.0 | 1.74 | -0.05 | 94675.76 | 51.33 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.61 | 1.58 | -0.04 | 3732.19 | 21.59 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.13 | 0.19 | -0.01 | 41158.97 | 1.62 | skipped_fast |
| RWAINCUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 3438.94 | 82.12 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.66 | 0.16 | 0.0 | 54168.87 | 8.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
