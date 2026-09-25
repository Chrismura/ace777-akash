# Hulk DIGEST — 2026-09-25T20:27:28Z

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
| XRPUSDT | IDLE | 1.46 | 2.71 | 1.39 | 0.03 | 116652102.37 | 1.91 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.1 | 0.16 | 0.0 | 337574127.1 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.89 | 0.03 | -0.0 | 706204244.96 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.74 | 4.66 | 1.79 | 0.08 | 1224061.64 | 2.74 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 8.06 | 2.47 | 0.13 | 822575.27 | 6.95 | skipped_fast |
| HBARUSDT | IDLE | 1.85 | 3.62 | 0.48 | 0.03 | 903511.55 | 8.38 | skipped_fast |
| WUSDT | IDLE | 1.83 | 3.65 | 0.11 | 0.04 | 392444.25 | 10.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.63 | 3.73 | 2.45 | 0.05 | 247670.1 | 9.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.47 | 21.84 | 15.59 | 0.07 | 122057.43 | 155.28 | skipped_fast |
| QNTUSDT | IDLE | 1.02 | 5.1 | 1.12 | 0.12 | 593366.01 | 4.08 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 3.89 | 1.03 | 0.03 | 161190.02 | 12.27 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 3.49 | 0.71 | -0.0 | 79288.66 | 9.79 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 4.42 | 0.81 | 0.06 | 114668.02 | 9.11 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 3.08 | 0.88 | 0.08 | 136588.83 | 13.78 | skipped_fast |
| EDELUSDT | IDLE | 0.54 | 4.68 | 3.36 | 0.04 | 229404.46 | 30.39 | skipped_fast |
| RWAINCUSDT | IDLE | 0.49 | 1.85 | 0.51 | -0.07 | 17498.0 | 70.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.24 | 2.46 | 0.16 | 0.03 | 3384.99 | 22.1 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.77 | 0.66 | 0.0 | 112691.3 | 48.34 | skipped_fast |
| MNSRYUSDT | IDLE | 0.74 | 1.37 | 0.71 | 0.02 | 41409.83 | 33.07 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.33 | 0.73 | -0.01 | 55449.91 | 44.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
