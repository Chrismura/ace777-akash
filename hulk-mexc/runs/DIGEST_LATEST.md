# Hulk DIGEST — 2026-08-28T03:06:03Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.5 | 3.69 | 1.74 | 0.05 | 21659474.8 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.89 | 3.37 | 2.7 | 0.02 | 56362289.1 | 2.79 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 9.97 | 6.66 | 0.05 | 800138.72 | 2.61 | skipped_fast |
| CCUSDT | IDLE | 1.93 | 3.43 | 2.91 | -0.04 | 463688.57 | 11.61 | skipped_fast |
| BIOUSDT | IDLE | 2.77 | 4.88 | 4.42 | -0.0 | 100539.4 | 3.5 | skipped_fast |
| WUSDT | IDLE | 2.4 | 4.23 | 3.75 | 0.01 | 189231.73 | 11.63 | skipped_fast |
| QAITUSDT | IDLE | 0.47 | 22.39 | 16.79 | -0.21 | 59613.1 | 70.25 | skipped_fast |
| REDUSDT | IDLE | 1.93 | 3.73 | 0.9 | 0.03 | 81419.4 | 14.41 | skipped_fast |
| ZBCNUSDT | IDLE | 0.98 | 3.11 | 2.81 | 0.06 | 228801.63 | 27.08 | skipped_fast |
| KITEUSDT | IDLE | 1.52 | 2.73 | 2.11 | 0.01 | 75105.52 | 12.47 | skipped_fast |
| HBARUSDT | IDLE | 1.43 | 2.49 | 2.41 | 0.01 | 327488.97 | 1.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 8.26 | 1.54 | -0.17 | 113081.02 | 50.82 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 3.29 | 1.93 | -0.05 | 21560.19 | 10.69 | skipped_fast |
| EDELUSDT | IDLE | 0.42 | 3.18 | 1.83 | 0.12 | 31598.24 | 25.41 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.53 | 2.34 | -0.01 | 44276.99 | 4.83 | skipped_fast |
| TELUSDT | IDLE | 0.83 | 1.54 | 1.41 | 0.03 | 122373.02 | 21.15 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 3.34 | 3.23 | -0.03 | 9181.82 | 21.45 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 1.0 | 0.16 | 0.01 | 54598.7 | 16.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
