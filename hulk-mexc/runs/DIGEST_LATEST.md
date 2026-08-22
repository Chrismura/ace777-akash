# Hulk DIGEST — 2026-08-22T16:47:31Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 10.19 | 0.63 | 0.08 | 49965914.93 | 5.73 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 7.64 | 2.75 | 0.07 | 214818968.81 | 2.69 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 3.03 | 0.59 | 0.0 | 1132071.19 | 3.86 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.06 | 0.08 | 761543.12 | 10.23 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.86 | -0.1 | 627160.98 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.47 | -0.01 | 544702.88 | 8.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.49 | 1.09 | -0.03 | 314787.15 | 5.1 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 4.35 | 1.01 | 0.03 | 86661.6 | 12.42 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 6.91 | 6.46 | -0.09 | 225114.58 | 53.35 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.02 | 74695.01 | 22.75 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.55 | -0.15 | 128223.9 | 12.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 3.47 | 0.35 | 0.05 | 46586.98 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.8 | -0.01 | 181139.98 | 3.14 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.63 | 0.0 | 136584.24 | 16.01 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7704.25 | 113.06 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.14 | 0.32 | 0.02 | 56510.81 | 16.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.27 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
