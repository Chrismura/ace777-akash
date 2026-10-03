# Hulk DIGEST — 2026-10-03T09:48:06Z

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
| QNTUSDT | IDLE | 1.91 | 9.26 | 2.59 | 0.13 | 4239969.96 | 6.86 | skipped_fast |
| XRPUSDT | IDLE | 0.43 | 0.78 | 0.48 | -0.03 | 52399994.4 | 1.35 | skipped_fast |
| ETHUSDT | IDLE | 0.27 | 0.52 | 0.18 | -0.02 | 383161978.42 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.12 | 0.22 | 0.15 | -0.02 | 639576158.13 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 0.9 | 7.69 | 3.55 | 0.18 | 732904.1 | 24.69 | skipped_fast |
| WUSDT | IDLE | 1.87 | 4.57 | 3.58 | -0.03 | 467803.28 | 8.3 | skipped_fast |
| PYTHUSDT | IDLE | 0.81 | 1.92 | 0.64 | 0.03 | 655380.89 | 7.61 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.52 | 1.01 | -0.05 | 839409.98 | 5.96 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 2.67 | 0.0 | 0.0 | 435722.63 | 10.68 | skipped_fast |
| KITEUSDT | IDLE | 2.55 | 4.9 | 1.39 | 0.01 | 82631.65 | 8.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.64 | 3.68 | 2.7 | -0.08 | 232952.72 | 19.3 | skipped_fast |
| BIOUSDT | IDLE | 1.8 | 4.11 | 3.6 | -0.01 | 88351.05 | 6.5 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 5.51 | 3.57 | -0.04 | 120281.59 | 13.79 | skipped_fast |
| CHIPUSDT | IDLE | 1.11 | 2.03 | 1.4 | -0.02 | 85005.91 | 11.6 | skipped_fast |
| FLUIDUSDT | IDLE | 2.74 | 5.33 | 1.04 | 0.03 | 5976.67 | 21.18 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 4.23 | 3.01 | 0.02 | 43863.74 | 55.43 | skipped_fast |
| RWAINCUSDT | IDLE | 0.51 | 1.39 | 1.13 | 0.03 | 6613.62 | 57.21 | skipped_fast |
| TELUSDT | IDLE | 0.83 | 2.32 | 1.82 | -0.11 | 139658.79 | 20.55 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.51 | 0.07 | -0.01 | 54576.49 | 7.28 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.51 | 0.49 | -0.02 | 36543.23 | 20.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
