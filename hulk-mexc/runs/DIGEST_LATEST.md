# Hulk DIGEST — 2026-08-22T16:00:29Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.44 | 0.04 | 51474965.53 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.03 | 0.03 | 215790435.35 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 5.65 | 1.8 | 0.1 | 764172.37 | 8.5 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.53 | -0.02 | 1150946.29 | 5.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.58 | 3.36 | 1.49 | -0.09 | 624963.53 | 13.52 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 2.07 | -0.02 | 553964.24 | 10.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 2.05 | -0.05 | 320002.36 | 26.77 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.26 | -0.07 | 218706.53 | 3.32 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 4.35 | 1.72 | 0.03 | 85610.64 | 9.82 | skipped_fast |
| EDELUSDT | IDLE | 1.35 | 2.41 | 1.9 | -0.02 | 75112.86 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.54 | -0.15 | 134019.88 | 13.75 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.13 | 0.03 | 56510.89 | 45.5 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 2.69 | 2.62 | -0.03 | 184289.54 | 6.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.58 | -0.0 | 138589.8 | 42.69 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.02 | 56526.95 | 24.36 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.04 | 4625.53 | 20.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
