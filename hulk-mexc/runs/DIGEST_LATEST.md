# Hulk DIGEST — 2026-08-21T21:04:48Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.68 | 0.09 | 5579711.14 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.18 | 3.73 | 2.7 | 0.1 | 128113546.88 | 2.91 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 8.19 | 6.0 | 0.08 | 480131.79 | 41.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.62 | 3.82 | 0.08 | 514285.94 | 3.1 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.14 | 0.15 | 0.1 | 640918.09 | 5.51 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.04 | 1.57 | 0.06 | 808083.31 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.83 | 0.92 | 0.06 | 368044.58 | 10.5 | skipped_fast |
| BIOUSDT | IDLE | 2.48 | 5.2 | 2.79 | 0.01 | 187798.83 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.54 | 0.16 | 152882.08 | 12.33 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.12 | 3.19 | -0.06 | 82274.96 | 22.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.42 | 0.01 | 56240.11 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.04 | 10893.0 | 48.17 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.12 | 0.11 | 61194.95 | 12.07 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.53 | 0.01 | 180842.05 | 21.49 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.04 | 60180.31 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 159.24 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.17 | 0.99 | 0.03 | 53744.35 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
