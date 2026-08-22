# Hulk DIGEST — 2026-08-22T12:14:52Z

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
| PYTHUSDT | IDLE | 1.69 | 7.83 | 3.65 | 0.03 | 51616202.85 | 6.05 | skipped_fast |
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.91 | 0.12 | 215239193.8 | 5.28 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.22 | 0.03 | 1251640.92 | 2.57 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.14 | 0.13 | 774878.52 | 6.79 | skipped_fast |
| WUSDT | IDLE | 1.53 | 6.27 | 2.94 | 0.02 | 577949.58 | 10.5 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 5.77 | 3.96 | -0.03 | 371532.42 | 27.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 0.89 | -0.1 | 615174.4 | 3.33 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.33 | 0.04 | 82611.26 | 6.17 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.2 | -0.02 | 78047.69 | 34.15 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 5.65 | 0.79 | -0.02 | 240650.59 | 6.34 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.83 | -0.02 | 164750.36 | 47.91 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.51 | 0.03 | 153488.26 | 35.25 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 3.47 | 1.18 | 0.01 | 187969.35 | 3.1 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.91 | 0.44 | -0.05 | 48110.02 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.02 | 57673.03 | 16.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 21.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
