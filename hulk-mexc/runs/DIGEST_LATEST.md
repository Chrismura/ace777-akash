# Hulk DIGEST — 2026-10-29T16:18:16Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.48 | 2.84 | 0.78 | 0.01 | 266494179.64 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 4.25 | 10.02 | 4.33 | 0.02 | 995623.26 | 5.49 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 2.5 | 0.77 | -0.0 | 25829488.31 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 1.3 | 2.53 | 0.48 | 0.01 | 387017380.2 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 3.09 | 7.26 | 1.26 | 0.04 | 408241.73 | 8.68 | skipped_fast |
| CHIPUSDT | IDLE | 3.23 | 9.75 | 2.94 | 0.04 | 171954.55 | 11.73 | skipped_fast |
| BIOUSDT | IDLE | 2.8 | 5.58 | 1.24 | 0.03 | 73066.37 | 8.63 | skipped_fast |
| WUSDT | IDLE | 1.37 | 2.6 | 0.91 | -0.02 | 401762.69 | 12.81 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 2.82 | 0.73 | -0.03 | 309847.77 | 3.18 | skipped_fast |
| QNTUSDT | IDLE | 2.02 | 3.87 | 1.14 | 0.02 | 435509.98 | 4.04 | skipped_fast |
| HBARUSDT | IDLE | 1.74 | 3.38 | 0.73 | -0.01 | 475520.09 | 6.66 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 3.87 | 0.73 | 0.0 | 63516.87 | 16.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 2.33 | 0.23 | -0.0 | 239781.94 | 37.98 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.86 | 0.44 | 0.0 | 59249.84 | 9.54 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 2.01 | 0.21 | -0.05 | 32350.87 | 7.04 | skipped_fast |
| LAUSDT | IDLE | 2.31 | 4.49 | 0.88 | 0.01 | 58988.61 | 24.0 | skipped_fast |
| IOTAUSDT | IDLE | 1.72 | 3.44 | 0.58 | -0.01 | 95206.56 | 16.96 | skipped_fast |
| FLUIDUSDT | IDLE | 1.74 | 3.62 | 3.06 | -0.05 | 7776.36 | 21.51 | skipped_fast |
| WAXLUSDT | IDLE | 1.72 | 4.25 | 0.85 | -0.01 | 53481.1 | 50.4 | skipped_fast |
| RIZEUSDT | IDLE | 0.43 | 0.78 | 0.56 | -0.03 | 39961.3 | 51.64 | skipped_fast |
| MNSRYUSDT | IDLE | 1.06 | 2.04 | 0.58 | -0.01 | 37072.98 | 24.89 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.97 | 0.16 | -0.0 | 55054.6 | 16.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
