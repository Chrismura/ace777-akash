# Hulk DIGEST — 2026-09-11T09:17:35Z

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
| ETHUSDT | IDLE | 0.8 | 1.54 | 0.38 | 0.0 | 466632111.55 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.74 | 1.38 | 0.67 | -0.02 | 39335756.63 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.78 | 0.26 | -0.01 | 539600390.85 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 42.67 | 27.79 | 0.1 | 138988.39 | 217.96 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 6.62 | 3.98 | -0.06 | 125140.97 | 8.77 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.7 | 0.75 | -0.04 | 451614.53 | 6.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.24 | 0.96 | -0.01 | 345312.69 | 3.88 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.18 | 2.07 | -0.01 | 139775.64 | 5.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.0 | 1.92 | 0.54 | -0.02 | 199089.44 | 20.4 | skipped_fast |
| EDELUSDT | IDLE | 0.79 | 3.53 | 1.94 | -0.06 | 198096.38 | 46.84 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 1.87 | 0.0 | 0.03 | 58497.53 | 11.89 | skipped_fast |
| REDUSDT | IDLE | 0.89 | 1.55 | 1.49 | -0.02 | 59680.54 | 13.22 | skipped_fast |
| RWAINCUSDT | IDLE | 1.04 | 1.85 | 1.49 | -0.0 | 3093.7 | 5.6 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.17 | 1.07 | -0.02 | 72101.56 | 4.02 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.79 | 1.68 | -0.02 | 189301.81 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.25 | 2.26 | 1.59 | -0.04 | 96067.1 | 40.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.26 | 2.04 | -0.03 | 2138.71 | 21.81 | skipped_fast |
| QNTUSDT | IDLE | 0.56 | 0.99 | 0.81 | -0.03 | 36221.85 | 1.55 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.92 | 0.15 | -0.01 | 50371.38 | 7.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.6 | 0.03 | -0.01 | 36154.13 | 4.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
