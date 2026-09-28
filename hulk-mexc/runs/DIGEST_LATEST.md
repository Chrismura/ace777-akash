# Hulk DIGEST — 2026-09-28T11:22:08Z

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
| QNTUSDT | IDLE | 1.48 | 48.63 | 16.48 | 0.47 | 19314989.13 | 9.5 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.44 | 23.07 | 1.99 | 0.22 | 5358609.74 | 11.21 | skipped_fast |
| WUSDT | IDLE | 1.33 | 5.74 | 2.01 | -0.02 | 3444142.75 | 7.74 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 14.75 | 9.5 | -0.03 | 1169086.25 | 12.78 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 4.6 | 1.94 | -0.06 | 1590927.59 | 2.47 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.63 | 0.54 | -0.03 | 52635028.86 | 2.02 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.12 | 0.18 | -0.02 | 306146138.02 | 0.19 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.85 | 0.38 | -0.02 | 646625901.85 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.49 | 12.1 | 2.08 | -0.05 | 184218.28 | 22.03 | skipped_fast |
| KITEUSDT | IDLE | 2.2 | 6.75 | 5.99 | -0.08 | 103689.38 | 8.08 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 3.69 | 2.41 | -0.07 | 104574.17 | 3.38 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.24 | 0.63 | -0.04 | 200314.61 | 25.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.43 | 2.12 | -0.1 | 87371.73 | 18.1 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 2.82 | 0.63 | -0.04 | 60582.79 | 14.09 | skipped_fast |
| TELUSDT | IDLE | 2.2 | 4.04 | 2.46 | -0.01 | 167230.57 | 44.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.67 | 6.39 | 4.81 | 0.13 | 32659.14 | 61.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.39 | 2.34 | 0.93 | -0.15 | 59745.66 | 75.84 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 2.38 | 0.86 | -0.05 | 3474.62 | 21.38 | skipped_fast |
| RWAUSDT | IDLE | 0.86 | 1.53 | 1.29 | -0.02 | 59794.39 | 36.22 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.73 | 0.18 | -0.02 | 35371.55 | 66.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
