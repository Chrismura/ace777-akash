# Hulk DIGEST — 2026-10-16T07:23:52Z

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
| WUSDT | IDLE | 2.44 | 6.45 | 1.45 | 0.03 | 2212923.86 | 7.19 | skipped_fast |
| PYTHUSDT | IDLE | 0.56 | 3.5 | 0.29 | 0.12 | 3965489.75 | 1.05 | skipped_fast |
| XRPUSDT | IDLE | 0.82 | 1.63 | 0.13 | 0.03 | 30751189.19 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.41 | 0.03 | 0.04 | 219800405.79 | 0.45 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.87 | 0.14 | 0.01 | 410747380.13 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 3.9 | 1.33 | 0.06 | 1176632.69 | 5.29 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 3.67 | 0.89 | 0.0 | 413801.78 | 9.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 6.53 | 4.2 | 0.12 | 193050.35 | 10.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.64 | 3.13 | 1.11 | 0.05 | 183581.07 | 12.5 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 3.44 | 1.92 | 0.03 | 70146.78 | 9.79 | skipped_fast |
| EDELUSDT | IDLE | 1.02 | 2.83 | 0.44 | -0.06 | 214137.6 | 23.57 | skipped_fast |
| BIOUSDT | IDLE | 1.25 | 2.48 | 0.12 | 0.06 | 67668.0 | 3.84 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 3.22 | 1.01 | -0.04 | 91877.64 | 9.98 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 3.08 | 0.41 | 0.06 | 153223.46 | 6.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.61 | 1.47 | 0.02 | 27851.26 | 133.76 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 1.73 | 0.28 | 0.05 | 62514.98 | 52.76 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 2.94 | 1.65 | 0.04 | 92287.48 | 27.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.89 | 1.78 | 0.0 | -0.01 | 7843.73 | 19.36 | skipped_fast |
| RWAUSDT | IDLE | 0.46 | 0.88 | 0.24 | 0.02 | 52741.05 | 7.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.37 | 0.35 | 0.0 | 39743.59 | 9.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
