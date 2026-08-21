# Hulk DIGEST — 2026-08-21T21:08:28Z

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
| PYTHUSDT | IDLE | 1.22 | 4.51 | 1.93 | 0.08 | 5585538.61 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 3.73 | 2.53 | 0.1 | 128034674.81 | 0.73 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 8.19 | 5.76 | 0.09 | 480543.73 | 29.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 4.62 | 3.91 | 0.08 | 514059.9 | 6.21 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.14 | 0.45 | 0.1 | 641926.93 | 10.13 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.04 | 1.55 | 0.06 | 805852.75 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.83 | 0.97 | 0.06 | 368089.21 | 11.55 | skipped_fast |
| BIOUSDT | IDLE | 2.48 | 5.2 | 2.92 | 0.01 | 188064.96 | 6.33 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.49 | 0.16 | 153400.19 | 10.68 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 4.12 | 2.86 | -0.06 | 82249.99 | 34.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.54 | 1.53 | 0.01 | 56246.98 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.04 | 10900.38 | 26.77 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.0 | 2.34 | 0.11 | 61166.29 | 11.16 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.22 | 0.01 | 180351.99 | 32.14 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.04 | 60147.57 | 6.26 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 178.96 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.17 | 1.07 | 0.03 | 53742.62 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 21.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
