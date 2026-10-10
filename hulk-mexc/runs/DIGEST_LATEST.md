# Hulk DIGEST — 2026-10-10T14:57:41Z

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
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.79 | 10.34 | 1.34 | 0.04 | 1064793.51 | 15.36 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.95 | 0.29 | 0.01 | 88497865.18 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.73 | 0.26 | 0.02 | 16717212.18 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.36 | 0.09 | -0.0 | 193473942.39 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.9 | 3.49 | 2.13 | -0.01 | 1130429.25 | 1.6 | skipped_fast |
| PYTHUSDT | IDLE | 0.96 | 2.47 | 1.77 | -0.09 | 1021323.47 | 2.56 | skipped_fast |
| EDELUSDT | IDLE | 3.2 | 6.53 | 4.44 | 0.01 | 227338.77 | 2.61 | skipped_fast |
| KITEUSDT | IDLE | 2.34 | 6.2 | 1.11 | 0.07 | 72331.01 | 10.78 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.8 | 0.82 | -0.01 | 385324.18 | 7.46 | skipped_fast |
| ZBCNUSDT | IDLE | 0.9 | 1.8 | 0.0 | -0.0 | 210294.53 | 9.97 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 2.85 | 2.73 | 0.07 | 86992.3 | 11.62 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.93 | 0.28 | 0.03 | 82891.08 | 6.92 | skipped_fast |
| REDUSDT | IDLE | 1.11 | 2.16 | 0.41 | 0.04 | 55127.74 | 9.93 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.69 | 0.43 | 0.03 | 327240.35 | 2.15 | skipped_fast |
| TELUSDT | IDLE | 1.75 | 3.06 | 2.91 | -0.02 | 109461.06 | 49.93 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.78 | 0.29 | -0.0 | 9624.54 | 48.73 | skipped_fast |
| RIZEUSDT | IDLE | 0.6 | 1.56 | 0.77 | 0.01 | 45266.45 | 55.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 1.94 | 1.18 | -0.0 | 15535.13 | 21.91 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.71 | 0.47 | -0.01 | 53976.86 | 7.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.67 | 0.2 | 0.0 | 39208.96 | 12.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
