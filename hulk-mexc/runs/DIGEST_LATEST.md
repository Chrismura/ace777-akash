# Hulk DIGEST — 2026-09-27T11:07:07Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 1.87 | 11.19 | 7.91 | 0.14 | 3120409.93 | 19.79 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 6.09 | 2.87 | 0.13 | 2049735.18 | 6.97 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 9.87 | 8.98 | 0.57 | 5217246.74 | 0.6 | skipped_fast |
| XRPUSDT | IDLE | 1.03 | 2.0 | 0.41 | -0.01 | 40968936.94 | 0.65 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.82 | 0.65 | 0.01 | 158887844.69 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.71 | 0.24 | 0.01 | 430113873.45 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.44 | 2.86 | 0.1 | 0.02 | 617431.66 | 0.73 | skipped_fast |
| EDELUSDT | IDLE | 2.41 | 5.84 | 4.15 | -0.05 | 148494.3 | 24.43 | skipped_fast |
| REDUSDT | IDLE | 2.49 | 4.43 | 3.7 | 0.01 | 64518.77 | 12.83 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.26 | 1.27 | 0.0 | 620580.17 | 4.23 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 5.21 | 4.8 | 0.09 | 170796.42 | 9.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 2.73 | 1.04 | -0.01 | 226852.09 | 12.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.15 | 2.7 | 1.83 | 0.0 | 120774.75 | 16.35 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.57 | 1.05 | -0.04 | 96523.72 | 6.27 | skipped_fast |
| RIZEUSDT | IDLE | 0.99 | 3.84 | 0.97 | -0.03 | 46693.1 | 61.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.88 | 3.68 | 0.0 | 0.07 | 7160.93 | 36.99 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 3.19 | 1.4 | 0.09 | 131371.11 | 39.9 | skipped_fast |
| MNSRYUSDT | IDLE | 0.96 | 1.9 | 0.16 | 0.01 | 39241.24 | 25.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.03 | 1.9 | 1.11 | 0.02 | 1017.93 | 21.54 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.85 | 1.12 | 0.04 | 55897.87 | 49.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
