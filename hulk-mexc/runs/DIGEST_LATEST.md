# Hulk DIGEST — 2026-10-05T16:37:00Z

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
| QNTUSDT | IDLE | 2.39 | 5.38 | 3.55 | -0.01 | 2929734.65 | 6.68 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 2.38 | 2.11 | -0.01 | 37564792.05 | 0.67 | skipped_fast |
| BTCUSDT | IDLE | 1.12 | 1.99 | 1.65 | -0.0 | 672928588.05 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 1.03 | 1.85 | 1.36 | -0.0 | 389565831.27 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 3.31 | 5.88 | 4.94 | -0.02 | 585647.53 | 7.87 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.76 | 37.31 | 15.43 | 0.31 | 58643.9 | 32.36 | skipped_fast |
| WUSDT | IDLE | 2.39 | 4.28 | 3.36 | -0.04 | 427941.92 | 10.63 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 10.04 | 7.84 | -0.08 | 20041.59 | 139.27 | skipped_fast |
| BIOUSDT | IDLE | 2.7 | 5.14 | 1.69 | 0.03 | 91444.4 | 9.41 | skipped_fast |
| EDELUSDT | IDLE | 1.67 | 3.18 | 1.05 | 0.02 | 336753.87 | 12.2 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 2.28 | 1.21 | -0.02 | 419544.48 | 6.43 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.96 | 21.25 | 5.85 | 0.22 | 53862.11 | 21.63 | skipped_fast |
| KITEUSDT | IDLE | 2.2 | 3.9 | 3.38 | -0.05 | 63006.63 | 9.37 | skipped_fast |
| HBARUSDT | IDLE | 1.69 | 2.97 | 2.68 | -0.02 | 461482.72 | 5.97 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 3.55 | 1.58 | 0.06 | 143988.33 | 18.33 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.7 | 1.76 | -0.02 | 87447.29 | 9.46 | skipped_fast |
| ZBCNUSDT | IDLE | 0.79 | 1.47 | 1.12 | 0.02 | 254574.78 | 15.02 | skipped_fast |
| TELUSDT | IDLE | 2.19 | 4.04 | 2.32 | 0.0 | 146438.98 | 41.32 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.74 | 0.51 | -0.0 | 52021.38 | 14.68 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.36 | 0.08 | -0.0 | 40353.92 | 30.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
