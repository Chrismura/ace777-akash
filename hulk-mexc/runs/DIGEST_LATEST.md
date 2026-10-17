# Hulk DIGEST — 2026-10-17T08:57:31Z

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
| WUSDT | IDLE | 3.35 | 6.49 | 1.37 | -0.01 | 1263827.1 | 14.15 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 2.74 | 1.01 | -0.09 | 1592118.92 | 3.52 | skipped_fast |
| ETHUSDT | IDLE | 0.38 | 0.74 | 0.07 | -0.01 | 171961245.87 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.36 | 0.66 | 0.35 | -0.03 | 23474053.68 | 0.76 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.4 | 0.06 | -0.01 | 297120306.89 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.33 | 5.81 | 1.84 | -0.04 | 208475.39 | 17.61 | skipped_fast |
| QNTUSDT | IDLE | 1.41 | 2.71 | 0.71 | -0.01 | 679279.61 | 1.47 | skipped_fast |
| KITEUSDT | IDLE | 2.56 | 4.81 | 2.03 | 0.01 | 56718.16 | 12.11 | skipped_fast |
| CCUSDT | IDLE | 1.01 | 1.82 | 1.33 | -0.02 | 345539.21 | 10.63 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.49 | 2.36 | -0.03 | 179111.2 | 6.9 | skipped_fast |
| RWAINCUSDT | IDLE | 1.56 | 6.3 | 1.78 | -0.07 | 23853.66 | 5.34 | skipped_fast |
| CHIPUSDT | IDLE | 0.86 | 2.43 | 0.81 | -0.07 | 107619.04 | 12.91 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 1.85 | 1.34 | -0.04 | 74168.3 | 15.44 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 3.14 | 1.73 | -0.04 | 50891.71 | 61.51 | skipped_fast |
| BIOUSDT | IDLE | 0.82 | 1.49 | 1.03 | -0.04 | 64767.84 | 4.01 | skipped_fast |
| HBARUSDT | IDLE | 0.49 | 0.91 | 0.5 | -0.03 | 275843.12 | 7.14 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 1.95 | 1.79 | -0.05 | 86095.79 | 17.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.8 | 1.54 | 0.41 | 0.02 | 4126.52 | 21.8 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.12 | 0.16 | -0.01 | 51977.98 | 23.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.28 | 0.14 | -0.0 | 29109.95 | 22.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
