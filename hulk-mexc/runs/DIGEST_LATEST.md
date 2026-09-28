# Hulk DIGEST — 2026-09-28T08:39:27Z

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
| WUSDT | IDLE | 2.38 | 8.07 | 7.3 | -0.07 | 4396812.41 | 10.66 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.64 | 13.64 | 1.15 | 0.1 | 1977544.64 | 10.41 | skipped_fast |
| PYTHUSDT | IDLE | 2.19 | 5.78 | 4.38 | -0.08 | 1759947.33 | 5.01 | skipped_fast |
| QNTUSDT | IDLE | 0.56 | 17.68 | 11.83 | 0.42 | 17128878.44 | 8.96 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 2.22 | 1.71 | -0.04 | 50398000.86 | 1.35 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.91 | 9.05 | 5.37 | 0.01 | 956131.39 | 8.73 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.04 | 0.78 | -0.02 | 625117625.29 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.91 | 0.63 | -0.03 | 296150508.53 | 0.19 | skipped_fast |
| KITEUSDT | IDLE | 2.29 | 5.73 | 5.39 | -0.1 | 105944.99 | 9.38 | skipped_fast |
| BIOUSDT | IDLE | 2.2 | 4.78 | 4.3 | -0.08 | 102238.39 | 3.38 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 3.57 | 2.74 | -0.09 | 64055.13 | 6.82 | skipped_fast |
| TELUSDT | IDLE | 2.87 | 5.74 | 4.03 | 0.03 | 175623.8 | 50.43 | skipped_fast |
| EDELUSDT | IDLE | 1.06 | 5.76 | 2.9 | -0.14 | 185141.34 | 43.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.27 | 3.73 | 3.2 | -0.1 | 88841.96 | 15.85 | skipped_fast |
| ZBCNUSDT | IDLE | 0.89 | 1.62 | 1.06 | -0.05 | 215361.33 | 21.77 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 5.39 | 5.11 | -0.05 | 3627.16 | 21.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.65 | 6.09 | 5.12 | 0.15 | 32343.03 | 69.69 | skipped_fast |
| RIZEUSDT | IDLE | 0.33 | 1.99 | 0.78 | -0.15 | 59273.54 | 54.36 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.3 | 0.93 | -0.02 | 59563.49 | 28.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.75 | 0.27 | -0.02 | 36497.45 | 29.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
