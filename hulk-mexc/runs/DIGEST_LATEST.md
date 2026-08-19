# Hulk DIGEST — 2026-08-19T02:44:40Z

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
| XRPUSDT | IDLE | 0.37 | 0.66 | 0.51 | 0.0 | 10953955.01 | 1.0 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 7.82 | 6.89 | 0.01 | 166788.95 | 15.65 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 4.05 | 3.3 | -0.07 | 181984.03 | 3.84 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 1.99 | 1.64 | -0.01 | 223340.18 | 11.09 | skipped_fast |
| PYTHUSDT | IDLE | 0.93 | 1.68 | 1.26 | 0.0 | 165327.99 | 2.61 | skipped_fast |
| ZBCNUSDT | IDLE | 0.58 | 1.1 | 0.44 | -0.01 | 152989.56 | 13.36 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.68 | 0.24 | 0.02 | 64243.6 | 8.07 | skipped_fast |
| WUSDT | IDLE | 0.54 | 1.02 | 0.46 | -0.01 | 131183.69 | 16.1 | skipped_fast |
| EDELUSDT | IDLE | 0.78 | 2.29 | 1.58 | -0.02 | 74238.9 | 26.85 | skipped_fast |
| RWAINCUSDT | IDLE | 0.92 | 1.92 | 0.82 | -0.02 | 10760.5 | 5.93 | skipped_fast |
| KITEUSDT | IDLE | 0.4 | 0.71 | 0.59 | -0.01 | 65290.84 | 15.33 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 2.19 | 0.09 | 0.03 | 107725.63 | 1.48 | skipped_fast |
| RIZEUSDT | IDLE | 1.64 | 4.37 | 1.94 | -0.04 | 28783.9 | 194.58 | skipped_fast |
| QAITUSDT | IDLE | 0.34 | 2.97 | 0.51 | -0.17 | 11975.73 | 62.72 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 1.88 | 0.89 | 0.04 | 86898.12 | 20.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.19 | 1.18 | -0.02 | 206.74 | 22.15 | skipped_fast |
| QNTUSDT | IDLE | 0.4 | 0.79 | 0.11 | -0.0 | 38529.92 | 8.92 | skipped_fast |
| RWAUSDT | IDLE | 0.19 | 0.35 | 0.26 | -0.01 | 51829.47 | 8.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
