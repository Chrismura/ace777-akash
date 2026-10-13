# Hulk DIGEST — 2026-10-13T20:08:28Z

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
| WUSDT | IDLE | 2.04 | 13.52 | 5.98 | -0.2 | 4890656.23 | 7.04 | skipped_fast |
| PYTHUSDT | IDLE | 2.19 | 7.01 | 4.06 | -0.03 | 2128168.22 | 11.31 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.81 | 10.52 | 0.98 | -0.04 | 1652108.92 | 4.98 | skipped_fast |
| ETHUSDT | IDLE | 0.59 | 1.1 | 0.53 | -0.01 | 236082287.47 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.59 | 1.15 | 0.21 | 0.01 | 37357216.19 | 2.18 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.9 | 0.53 | 0.0 | 393327026.1 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.33 | 2.98 | 0.04 | 630700.99 | 5.53 | skipped_fast |
| RIZEUSDT | IDLE | 3.11 | 10.22 | 4.97 | -0.07 | 66075.27 | 59.03 | skipped_fast |
| RWAINCUSDT | IDLE | 2.51 | 4.82 | 1.28 | 0.03 | 31057.61 | 19.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.6 | 2.89 | 2.04 | -0.01 | 220695.51 | 12.7 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 4.28 | 0.38 | -0.01 | 136246.13 | 14.82 | skipped_fast |
| EDELUSDT | IDLE | 1.31 | 2.81 | 0.75 | 0.01 | 258545.52 | 23.2 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.92 | 0.14 | -0.02 | 75763.73 | 3.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.14 | 2.65 | 0.62 | -0.03 | 106190.09 | 6.92 | skipped_fast |
| TELUSDT | IDLE | 2.06 | 3.74 | 2.55 | 0.01 | 116225.79 | 34.13 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.77 | 0.19 | -0.02 | 327531.3 | 5.69 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.59 | 0.12 | 0.0 | 60373.07 | 12.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 2.02 | 0.6 | 0.03 | 26318.55 | 21.42 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.62 | 0.54 | -0.0 | 52557.39 | 15.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.49 | 0.15 | -0.01 | 38541.14 | 11.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
