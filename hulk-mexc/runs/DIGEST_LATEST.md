# Hulk DIGEST — 2026-09-27T03:05:41Z

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
| QNTUSDT | IDLE | 2.49 | 59.18 | 10.72 | 0.74 | 3932919.3 | 11.52 | skipped_fast |
| PYTHUSDT | IDLE | 1.75 | 6.74 | 2.99 | 0.11 | 1440328.17 | 3.65 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.04 | 0.68 | -0.03 | 39467812.56 | 1.97 | skipped_fast |
| ETHUSDT | IDLE | 0.43 | 0.81 | 0.28 | 0.0 | 125183009.41 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.25 | 0.49 | 0.09 | 0.01 | 333856757.95 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.38 | 7.81 | 0.66 | 0.12 | 740392.33 | 16.05 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 3.09 | 2.2 | 0.02 | 781725.74 | 6.64 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 8.5 | 6.76 | -0.04 | 170497.91 | 3.5 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.32 | 11.89 | 0.22 | 0.1 | 134131.21 | 27.69 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 2.95 | 1.5 | -0.02 | 186053.56 | 10.98 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 6.26 | 1.95 | 0.12 | 157110.71 | 10.29 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.93 | 0.27 | -0.01 | 546112.65 | 1.06 | skipped_fast |
| CHIPUSDT | IDLE | 0.94 | 2.18 | 1.64 | -0.01 | 108862.15 | 14.43 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.61 | 1.55 | -0.02 | 109876.78 | 9.44 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 1.81 | 0.13 | -0.01 | 58469.54 | 14.1 | skipped_fast |
| RIZEUSDT | IDLE | 1.21 | 3.01 | 0.14 | 0.09 | 45325.0 | 47.57 | skipped_fast |
| RWAINCUSDT | IDLE | 0.34 | 1.23 | 0.29 | 0.04 | 10005.64 | 102.56 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.94 | 0.29 | -0.0 | 38843.77 | 16.61 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.57 | 0.43 | 0.03 | 57171.63 | 7.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.88 | 0.0 | 0.0 | 1003.5 | 21.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
