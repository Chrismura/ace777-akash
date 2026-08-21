# Hulk DIGEST — 2026-08-21T21:05:26Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.64 | 0.09 | 5580846.72 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 3.73 | 2.62 | 0.1 | 128096916.1 | 0.73 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 8.19 | 6.08 | 0.08 | 480122.79 | 35.55 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 4.62 | 4.0 | 0.07 | 514326.0 | 6.2 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.14 | 0.18 | 0.1 | 641054.03 | 4.6 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.04 | 1.53 | 0.06 | 806002.61 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.83 | 0.93 | 0.06 | 368008.15 | 10.5 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.2 | 2.76 | 0.01 | 187832.59 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.58 | 0.16 | 152924.38 | 12.33 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.12 | 3.08 | -0.05 | 82299.99 | 22.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.42 | 0.01 | 56227.88 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.04 | 10893.0 | 42.8 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.12 | 0.11 | 61229.63 | 12.07 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.53 | 0.01 | 180842.05 | 21.49 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.68 | 0.04 | 60180.31 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 182.9 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.91 | 0.03 | 53747.96 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4286.4 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
