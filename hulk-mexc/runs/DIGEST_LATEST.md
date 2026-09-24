# Hulk DIGEST — 2026-09-24T20:22:46Z

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
| XRPUSDT | IDLE | 1.77 | 3.4 | 1.0 | 0.03 | 69010322.85 | 1.31 | skipped_fast |
| ETHUSDT | IDLE | 1.04 | 1.98 | 0.68 | 0.0 | 344492242.19 | 0.22 | skipped_fast |
| BTCUSDT | IDLE | 0.89 | 1.67 | 0.79 | -0.0 | 707388573.63 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.11 | 7.43 | 4.85 | 0.08 | 1325949.87 | 1.48 | skipped_fast |
| CCUSDT | IDLE | 2.88 | 5.72 | 0.22 | 0.05 | 483648.91 | 10.44 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 31.49 | 8.61 | 0.31 | 56924.72 | 45.73 | skipped_fast |
| CHIPUSDT | IDLE | 3.18 | 15.49 | 3.1 | 0.14 | 84713.38 | 18.93 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.32 | 14.23 | 0.37 | 0.16 | 9674.32 | 9.31 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 2.56 | 0.65 | 0.03 | 820578.9 | 1.08 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 5.99 | 0.42 | 0.02 | 154931.82 | 10.57 | skipped_fast |
| WUSDT | IDLE | 1.44 | 2.69 | 1.33 | 0.05 | 241619.37 | 5.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 3.02 | 1.48 | 0.01 | 217767.93 | 20.82 | skipped_fast |
| BIOUSDT | IDLE | 1.79 | 5.64 | 1.74 | 0.1 | 84759.64 | 9.65 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 3.67 | 1.04 | 0.07 | 100791.41 | 8.07 | skipped_fast |
| TELUSDT | IDLE | 2.58 | 4.77 | 2.54 | -0.04 | 110845.78 | 24.27 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 2.44 | 0.79 | 0.01 | 65874.68 | 16.5 | skipped_fast |
| QNTUSDT | IDLE | 1.42 | 9.1 | 0.05 | 0.23 | 221860.22 | 16.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 2.6 | 0.28 | 0.05 | 2498.52 | 19.17 | skipped_fast |
| RWAUSDT | IDLE | 0.75 | 1.4 | 0.73 | 0.01 | 56240.73 | 7.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.25 | 0.14 | 0.0 | 37455.36 | 7.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
