# Hulk DIGEST — 2026-09-27T02:32:39Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 61.63 | 10.58 | 0.74 | 3641909.97 | 9.19 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 8.38 | 1.45 | 0.13 | 1421157.57 | 7.19 | skipped_fast |
| XRPUSDT | IDLE | 0.64 | 1.24 | 0.25 | -0.03 | 39783594.92 | 2.62 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.14 | 0.09 | 0.0 | 124288875.27 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.64 | 0.04 | 0.01 | 339128908.11 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.81 | 8.86 | 3.04 | 0.09 | 707244.72 | 11.21 | skipped_fast |
| CCUSDT | IDLE | 2.44 | 4.56 | 2.99 | 0.01 | 784987.17 | 11.85 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 8.28 | 6.8 | -0.03 | 171999.46 | 13.92 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 6.37 | 0.0 | 0.13 | 152961.12 | 1.94 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.3 | 10.42 | 0.0 | 0.08 | 132263.97 | 50.75 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 2.96 | 1.16 | -0.02 | 187149.0 | 16.18 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.48 | 0.65 | -0.02 | 520079.37 | 1.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 2.97 | 0.59 | 0.0 | 108820.01 | 14.28 | skipped_fast |
| RIZEUSDT | IDLE | 1.62 | 3.97 | 1.16 | 0.08 | 45478.37 | 52.68 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.77 | 0.77 | -0.02 | 109766.53 | 3.12 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 1.9 | 0.41 | -0.01 | 58523.18 | 14.17 | skipped_fast |
| RWAINCUSDT | IDLE | 0.34 | 1.23 | 0.29 | 0.04 | 10102.97 | 102.56 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.94 | 0.07 | 0.04 | 56673.45 | 7.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.95 | 0.32 | 0.0 | 38919.56 | 15.33 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.08 | 0.04 | 0.0 | 993.52 | 21.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
