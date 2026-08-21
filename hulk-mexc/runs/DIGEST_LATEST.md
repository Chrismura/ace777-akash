# Hulk DIGEST — 2026-08-21T21:52:32Z

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
| PYTHUSDT | IDLE | 1.16 | 4.51 | 0.43 | 0.09 | 5670807.58 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.08 | 3.73 | 0.52 | 0.11 | 129975621.54 | 0.71 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.4 | 0.05 | 527071.67 | 3.08 | skipped_fast |
| HBARUSDT | IDLE | 2.02 | 4.49 | 0.03 | 0.08 | 826293.69 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.31 | 3.89 | 0.25 | 0.1 | 638501.85 | 8.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.77 | 0.11 | 491497.75 | 47.27 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.97 | 0.0 | 0.07 | 368712.47 | 14.55 | skipped_fast |
| BIOUSDT | IDLE | 2.38 | 5.2 | 1.32 | 0.03 | 187327.38 | 6.22 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.79 | 0.18 | 154059.34 | 10.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.08 | 0.04 | 55836.88 | 31.52 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 10.66 | skipped_fast |
| EDELUSDT | IDLE | 1.89 | 4.12 | 0.44 | -0.03 | 83609.15 | 11.08 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.08 | 0.12 | 61279.28 | 11.01 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 4.81 | 0.68 | 0.03 | 185788.23 | 52.55 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.65 | 0.37 | 0.04 | 62569.92 | 7.7 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.17 | 0.33 | 0.04 | 54039.88 | 24.78 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 33.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
