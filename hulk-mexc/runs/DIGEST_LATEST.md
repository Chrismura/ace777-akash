# Hulk DIGEST — 2026-09-12T12:37:33Z

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
| XRPUSDT | IDLE | 0.44 | 0.85 | 0.2 | 0.02 | 44122980.02 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.7 | 0.09 | 0.02 | 575117747.67 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.09 | 0.16 | 0.08 | 0.0 | 512848615.66 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.77 | 9.06 | 4.68 | 0.01 | 237251.49 | 30.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.19 | 0.78 | 0.03 | 398703.77 | 3.75 | skipped_fast |
| RWAINCUSDT | IDLE | 3.44 | 6.94 | 2.55 | 0.04 | 16543.95 | 37.16 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 3.66 | 2.24 | 0.07 | 169424.57 | 26.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 4.04 | 1.1 | 0.03 | 84199.27 | 16.54 | skipped_fast |
| CCUSDT | IDLE | 0.62 | 1.09 | 0.97 | 0.01 | 311739.82 | 8.13 | skipped_fast |
| WUSDT | IDLE | 0.73 | 1.34 | 0.85 | 0.02 | 182922.95 | 12.27 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 2.09 | 0.15 | 0.03 | 76821.01 | 3.87 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.6 | 0.86 | 0.05 | 64310.36 | 18.66 | skipped_fast |
| RIZEUSDT | IDLE | 0.13 | 7.88 | 2.37 | 0.92 | 176419.19 | 36.17 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 1.67 | 0.06 | -0.03 | 61351.59 | 12.18 | skipped_fast |
| HBARUSDT | IDLE | 0.38 | 0.74 | 0.08 | 0.0 | 237525.68 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 2.96 | 1.76 | -0.03 | 100978.17 | 35.82 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.54 | 0.52 | -0.01 | 41912.04 | 7.75 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.74 | 0.37 | 0.03 | 55324.96 | 22.16 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.24 | 0.4 | 0.01 | 26376.15 | 38.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.05 | 1339.83 | 22.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
