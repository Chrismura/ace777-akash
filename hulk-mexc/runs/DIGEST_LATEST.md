# Hulk DIGEST — 2026-08-22T04:09:50Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 12.59 | 0.2 | 0.2 | 10150447.65 | 1.84 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 12.22 | 1.61 | 0.19 | 166822949.98 | 2.55 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.09 | 11.5 | 0.0 | 0.22 | 720358.91 | 12.97 | skipped_fast |
| HBARUSDT | IDLE | 2.09 | 6.03 | 0.25 | 0.11 | 1008440.99 | 2.4 | skipped_fast |
| CHIPUSDT | IDLE | 2.94 | 5.36 | 3.5 | -0.02 | 458690.46 | 6.04 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.55 | 0.07 | 200021.95 | 3.01 | skipped_fast |
| WUSDT | IDLE | 1.97 | 7.18 | 0.76 | 0.14 | 428532.36 | 11.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.61 | 0.13 | 536239.42 | 14.78 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 4.07 | 3.91 | -0.05 | 80365.22 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.04 | 0.09 | 59127.63 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.91 | 0.2 | 157868.25 | 18.96 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.35 | 0.13 | 67573.41 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.6 | 2.32 | 0.02 | 9399.91 | 16.34 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 3.8 | 0.8 | 0.09 | 178560.73 | 4.46 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56360.82 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.4 | 0.31 | 0.07 | 174197.72 | 51.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 20.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
