# Hulk DIGEST — 2026-08-21T21:44:44Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.66 | 0.1 | 5660615.64 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.57 | 0.11 | 129264490.52 | 1.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.43 | 0.04 | 522708.88 | 3.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 8.19 | 2.92 | 0.11 | 491491.57 | 19.92 | skipped_fast |
| CCUSDT | IDLE | 1.28 | 3.75 | 0.33 | 0.1 | 651685.43 | 8.24 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.28 | 0.01 | 0.07 | 819293.63 | 5.1 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.83 | 0.1 | 0.07 | 368901.16 | 10.41 | skipped_fast |
| BIOUSDT | IDLE | 2.41 | 5.2 | 1.81 | 0.02 | 187712.78 | 6.25 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.23 | 0.17 | 154199.85 | 20.49 | skipped_fast |
| EDELUSDT | IDLE | 1.93 | 4.12 | 0.99 | -0.04 | 83583.92 | 22.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.01 | 0.03 | 55815.83 | 47.31 | skipped_fast |
| QAITUSDT | IDLE | 2.36 | 4.38 | 2.29 | -0.02 | 3819.28 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.4 | 0.11 | 61111.31 | 11.05 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 4.81 | 1.41 | 0.02 | 183252.18 | 63.46 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.65 | 0.55 | 0.04 | 62647.58 | 4.64 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.17 | 0.33 | 0.03 | 53914.41 | 24.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
