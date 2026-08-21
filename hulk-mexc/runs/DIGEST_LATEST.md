# Hulk DIGEST — 2026-08-21T21:09:13Z

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
| PYTHUSDT | IDLE | 1.22 | 4.51 | 1.95 | 0.08 | 5587077.0 | 4.19 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 3.73 | 2.53 | 0.1 | 127976956.7 | 1.45 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 8.19 | 5.66 | 0.08 | 480587.78 | 26.67 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 4.62 | 3.94 | 0.08 | 513853.89 | 3.11 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.35 | 0.1 | 642170.4 | 6.44 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.04 | 1.56 | 0.06 | 805719.79 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.83 | 0.91 | 0.06 | 368006.33 | 10.5 | skipped_fast |
| BIOUSDT | IDLE | 2.49 | 5.2 | 2.95 | 0.0 | 188053.52 | 3.17 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.44 | 0.16 | 153428.47 | 9.04 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 4.12 | 3.41 | -0.06 | 82274.98 | 45.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.54 | 1.53 | 0.01 | 56229.3 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.04 | 10900.38 | 32.19 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.0 | 2.32 | 0.11 | 61192.99 | 11.16 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.22 | 0.01 | 180311.1 | 32.14 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 155.29 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.74 | 0.03 | 60158.43 | 6.26 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.91 | 0.03 | 53798.22 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 22.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
