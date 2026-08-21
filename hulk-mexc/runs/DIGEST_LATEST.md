# Hulk DIGEST — 2026-08-21T21:56:33Z

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
| PYTHUSDT | IDLE | 1.21 | 4.74 | 0.06 | 0.1 | 5681211.47 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.44 | 0.12 | 130000189.07 | 0.71 | skipped_fast |
| HBARUSDT | IDLE | 2.1 | 4.71 | 0.55 | 0.08 | 834172.32 | 1.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.52 | 0.05 | 526928.16 | 3.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.91 | 8.19 | 2.54 | 0.11 | 492273.84 | 27.3 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 3.89 | 0.15 | 0.11 | 635629.5 | 9.12 | skipped_fast |
| WUSDT | IDLE | 2.11 | 4.19 | 0.19 | 0.07 | 367640.71 | 15.58 | skipped_fast |
| BIOUSDT | IDLE | 2.37 | 5.2 | 1.17 | 0.04 | 186099.78 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.33 | 0.19 | 153816.3 | 18.65 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.03 | 10.4 | 1.07 | 0.05 | 56177.77 | 45.14 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.9 | 0.03 | 10238.87 | 37.34 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 4.12 | 1.32 | -0.04 | 83583.44 | 55.83 | skipped_fast |
| TELUSDT | IDLE | 2.54 | 6.45 | 0.98 | 0.05 | 191889.14 | 46.72 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 1.01 | 0.11 | 61325.12 | 12.84 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.65 | 0.25 | 0.05 | 62425.13 | 6.17 | skipped_fast |
| RWAUSDT | IDLE | 0.69 | 1.33 | 0.33 | 0.04 | 54142.49 | 32.98 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 20.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
