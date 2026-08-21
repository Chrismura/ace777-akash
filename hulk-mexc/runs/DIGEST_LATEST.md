# Hulk DIGEST — 2026-08-21T20:36:17Z

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
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.44 | 0.08 | 5536435.32 | 4.2 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 4.21 | 3.13 | 0.1 | 128977549.33 | 2.18 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.79 | 0.17 | 154037.07 | 20.32 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 10.86 | 5.16 | 0.12 | 478444.93 | 8.96 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.49 | 0.08 | 633714.89 | 1.84 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.81 | 0.05 | 809982.4 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.34 | 0.08 | 514042.76 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.58 | 0.06 | 368321.17 | 7.39 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.76 | 0.02 | 189060.94 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.81 | 5.01 | 4.44 | -0.05 | 80957.46 | 11.33 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10934.71 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.68 | 0.02 | 56290.3 | 47.09 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.61 | 0.1 | 60742.85 | 12.11 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 183210.88 | 21.46 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.74 | 0.04 | 59970.01 | 6.26 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53871.42 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
