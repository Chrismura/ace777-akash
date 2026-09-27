# Hulk DIGEST — 2026-09-27T14:35:37Z

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
| WUSDT | IDLE | 2.08 | 12.35 | 9.25 | 0.14 | 3620909.04 | 10.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.85 | 6.98 | 5.28 | 0.08 | 2123562.51 | 8.38 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 15.85 | 7.39 | 0.57 | 5811813.24 | 14.88 | skipped_fast |
| XRPUSDT | IDLE | 1.04 | 1.86 | 1.46 | -0.01 | 42806996.16 | 2.62 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.11 | 0.93 | 0.0 | 175326667.22 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.67 | 0.45 | 0.01 | 443905202.62 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.16 | 3.78 | 3.64 | -0.02 | 530525.57 | 12.74 | skipped_fast |
| HBARUSDT | IDLE | 1.65 | 2.98 | 2.11 | -0.0 | 690058.76 | 1.07 | skipped_fast |
| EDELUSDT | IDLE | 2.54 | 5.84 | 4.85 | -0.07 | 138904.47 | 31.68 | skipped_fast |
| CHIPUSDT | IDLE | 2.35 | 5.73 | 3.99 | -0.02 | 121343.27 | 20.89 | skipped_fast |
| REDUSDT | IDLE | 1.96 | 3.51 | 2.69 | 0.0 | 64333.36 | 12.99 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.02 | 14.0 | 1.62 | 0.28 | 8811.87 | 80.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.14 | 2.02 | 1.78 | -0.03 | 222897.86 | 15.68 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 3.86 | 3.16 | 0.09 | 178031.52 | 8.77 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 2.61 | 1.89 | -0.02 | 98012.43 | 9.49 | skipped_fast |
| TELUSDT | IDLE | 1.53 | 6.6 | 0.0 | 0.16 | 137869.5 | 59.48 | skipped_fast |
| RIZEUSDT | IDLE | 0.3 | 1.11 | 0.67 | -0.04 | 46083.48 | 41.26 | skipped_fast |
| RWAUSDT | IDLE | 0.93 | 1.71 | 0.98 | 0.01 | 55843.34 | 28.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.0 | 1.9 | 0.72 | 0.02 | 1490.45 | 21.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.71 | 0.34 | 0.01 | 39821.44 | 41.75 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
