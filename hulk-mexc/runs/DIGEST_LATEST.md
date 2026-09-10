# Hulk DIGEST — 2026-09-10T18:16:42Z

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
| ETHUSDT | IDLE | 1.49 | 2.87 | 0.68 | -0.01 | 451518536.63 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 1.97 | 1.28 | -0.05 | 46266657.98 | 1.48 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 1.0 | 0.62 | -0.02 | 558385138.38 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.92 | 4.44 | 2.7 | -0.08 | 883863.22 | 1.94 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 16.37 | 11.91 | 0.06 | 261299.48 | 27.21 | skipped_fast |
| CCUSDT | IDLE | 2.35 | 4.15 | 3.62 | -0.05 | 559528.8 | 7.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 44.57 | 22.37 | -0.52 | 121459.48 | 144.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.28 | 1.58 | 0.0 | 197716.58 | 5.96 | skipped_fast |
| WUSDT | IDLE | 1.12 | 3.07 | 1.42 | -0.08 | 220150.94 | 11.43 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 3.83 | 1.08 | -0.04 | 57447.84 | 19.95 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 3.1 | 1.87 | -0.07 | 81496.76 | 3.98 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 2.93 | 2.45 | -0.09 | 68217.8 | 19.94 | skipped_fast |
| CHIPUSDT | IDLE | 0.97 | 4.51 | 2.97 | -0.18 | 86859.11 | 17.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.38 | 1.55 | -0.03 | 5121.99 | 33.76 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 1.76 | 1.13 | -0.04 | 285990.36 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.5 | 1.29 | -0.02 | 36158.64 | 6.1 | skipped_fast |
| TELUSDT | IDLE | 1.44 | 2.68 | 1.39 | -0.02 | 82131.07 | 67.34 | skipped_fast |
| MNSRYUSDT | IDLE | 0.61 | 1.17 | 0.39 | -0.03 | 29781.78 | 19.53 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.69 | 0.15 | -0.05 | 52863.77 | 15.2 | skipped_fast |
| FLUIDUSDT | IDLE | 0.47 | 0.94 | 0.0 | -0.07 | 2232.87 | 21.76 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
