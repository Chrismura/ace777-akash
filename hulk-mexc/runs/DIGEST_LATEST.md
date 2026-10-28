# Hulk DIGEST — 2026-10-28T12:35:53Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.1 | 1.93 | 1.75 | 0.0 | 20500606.69 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 1.87 | 1.83 | 0.01 | 241113373.0 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.22 | 1.19 | 0.01 | 312562629.0 | 0.39 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.44 | 11.76 | 8.56 | -0.02 | 167984.78 | 17.16 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 6.32 | 5.94 | -0.0 | 298991.16 | 18.3 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.0 | 9.66 | 0.19 | 0.07 | 49867.59 | 31.16 | skipped_fast |
| WUSDT | IDLE | 1.19 | 2.12 | 1.77 | -0.02 | 573381.76 | 23.59 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 2.45 | 2.14 | -0.03 | 417678.5 | 2.81 | skipped_fast |
| QNTUSDT | IDLE | 2.22 | 3.93 | 3.34 | -0.03 | 463846.55 | 3.56 | skipped_fast |
| EDELUSDT | IDLE | 1.25 | 2.26 | 1.66 | 0.0 | 275563.09 | 27.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.71 | 3.17 | 2.53 | -0.03 | 224128.22 | 64.46 | skipped_fast |
| HBARUSDT | IDLE | 1.18 | 2.08 | 1.85 | -0.01 | 424433.76 | 6.63 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.0 | 1.96 | 0.01 | 85502.2 | 17.79 | skipped_fast |
| KITEUSDT | IDLE | 1.04 | 1.82 | 1.79 | 0.01 | 60749.32 | 11.29 | skipped_fast |
| REDUSDT | IDLE | 0.83 | 1.45 | 1.42 | 0.03 | 53974.7 | 15.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.01 | 1.79 | 1.56 | 0.02 | 36418.16 | 66.34 | skipped_fast |
| IOTAUSDT | IDLE | 1.35 | 2.36 | 2.3 | -0.01 | 76344.5 | 24.01 | skipped_fast |
| WAXLUSDT | IDLE | 1.21 | 2.15 | 1.8 | -0.0 | 56298.03 | 20.67 | skipped_fast |
| LAUSDT | IDLE | 1.0 | 1.74 | 1.71 | 0.01 | 59556.8 | 20.5 | skipped_fast |
| FLUIDUSDT | IDLE | 0.65 | 1.84 | 1.81 | -0.0 | 6687.14 | 21.4 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.37 | 0.16 | 0.01 | 54916.11 | 39.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.65 | 1.25 | 0.39 | 0.01 | 36221.48 | 54.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
