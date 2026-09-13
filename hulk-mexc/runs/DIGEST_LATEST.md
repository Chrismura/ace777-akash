# Hulk DIGEST — 2026-09-13T19:40:36Z

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
| ETHUSDT | IDLE | 0.77 | 1.47 | 0.43 | -0.0 | 258937424.41 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.7 | 1.33 | 0.47 | -0.01 | 14637037.84 | 2.22 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.71 | 0.22 | 0.0 | 271911283.15 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.58 | 4.98 | 1.23 | 0.03 | 445754.64 | 1.76 | skipped_fast |
| RIZEUSDT | IDLE | 2.26 | 32.72 | 20.16 | -0.07 | 73172.22 | 90.31 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.03 | 8.28 | 0.45 | 0.14 | 200140.83 | 14.9 | skipped_fast |
| WUSDT | IDLE | 1.7 | 3.09 | 2.13 | 0.0 | 264206.47 | 11.91 | skipped_fast |
| CCUSDT | IDLE | 0.76 | 1.42 | 0.65 | -0.01 | 297251.54 | 10.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.06 | 2.01 | 0.75 | 0.01 | 195500.87 | 13.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.27 | 3.48 | 2.93 | -0.09 | 82569.45 | 11.53 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.79 | 1.93 | 0.0 | 61415.22 | 24.43 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 2.22 | 1.68 | 0.01 | 63323.37 | 10.26 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.7 | 1.09 | 0.0 | 68216.79 | 7.85 | skipped_fast |
| RWAINCUSDT | IDLE | 0.85 | 1.7 | 0.0 | -0.01 | 6623.69 | 5.58 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.54 | 0.8 | 0.02 | 208192.72 | 1.31 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.61 | 2.01 | 0.0 | 35674.16 | 10.88 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.84 | 1.37 | -0.05 | 81335.21 | 37.93 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.2 | 0.15 | 0.01 | 54351.11 | 14.81 | skipped_fast |
| FLUIDUSDT | IDLE | 0.63 | 1.11 | 1.05 | -0.01 | 1495.4 | 21.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.23 | 0.45 | 0.01 | 0.0 | 31382.81 | 23.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
