# Hulk DIGEST — 2026-08-21T21:15:36Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.52 | 0.08 | 5604680.0 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 1.98 | 0.1 | 128190977.94 | 2.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.32 | 0.06 | 515462.77 | 3.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.99 | 8.19 | 4.97 | 0.09 | 482758.36 | 21.37 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.14 | 0.5 | 0.1 | 642658.76 | 10.14 | skipped_fast |
| HBARUSDT | IDLE | 1.6 | 3.04 | 1.05 | 0.06 | 809505.95 | 2.58 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.83 | 0.64 | 0.06 | 367052.16 | 10.49 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.2 | 2.7 | 0.01 | 187666.54 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.03 | 0.17 | 153545.01 | 12.27 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.02 | 10271.93 | 10.75 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.12 | 3.19 | -0.06 | 82446.49 | 34.03 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.54 | 1.53 | 0.01 | 56205.8 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.16 | 0.11 | 61047.42 | 12.07 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.27 | 0.01 | 179307.77 | 37.52 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.04 | 61170.37 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.75 | 3.21 | 1.91 | -0.02 | 2825.52 | 261.08 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.82 | 0.03 | 53718.81 | 24.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 21.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
