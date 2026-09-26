# Hulk DIGEST — 2026-09-26T12:56:58Z

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
| XRPUSDT | IDLE | 0.72 | 1.3 | 1.0 | -0.04 | 72220317.76 | 1.95 | skipped_fast |
| PYTHUSDT | IDLE | 2.58 | 7.91 | 2.56 | 0.06 | 1156211.88 | 2.59 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.66 | 0.35 | -0.01 | 206127523.18 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.49 | 0.33 | -0.01 | 471221484.25 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 4.36 | 1.79 | 0.12 | 995953.91 | 9.49 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 10.52 | 5.68 | 0.09 | 793133.56 | 5.8 | skipped_fast |
| WUSDT | IDLE | 1.88 | 4.86 | 2.14 | 0.05 | 479067.19 | 7.87 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 5.0 | 1.23 | 0.02 | 173738.8 | 3.28 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 5.93 | 5.17 | 0.02 | 6194.82 | 60.45 | skipped_fast |
| BIOUSDT | IDLE | 1.78 | 3.18 | 2.49 | 0.02 | 124851.93 | 3.07 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 1.5 | 1.15 | -0.02 | 601624.11 | 1.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.54 | 2.82 | 1.74 | -0.0 | 133211.21 | 12.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.52 | 0.4 | -0.01 | 222150.99 | 24.83 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 2.49 | 2.35 | -0.02 | 57741.07 | 7.74 | skipped_fast |
| RIZEUSDT | IDLE | 1.36 | 8.55 | 3.96 | -0.14 | 49058.04 | 84.45 | skipped_fast |
| RWAUSDT | IDLE | 2.28 | 4.23 | 2.21 | 0.0 | 55809.16 | 14.56 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 2.01 | 0.01 | 0.04 | 73721.55 | 9.51 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 2.71 | 2.09 | -0.05 | 121686.66 | 81.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.95 | 1.9 | 0.0 | 0.01 | 3388.79 | 21.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.05 | 0.0 | 39063.05 | 6.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
