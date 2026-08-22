# Hulk DIGEST — 2026-08-22T17:10:11Z

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
| PYTHUSDT | IDLE | 1.72 | 8.45 | 0.38 | 0.1 | 49185702.65 | 3.8 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.64 | 4.01 | 0.05 | 213986347.66 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.93 | -0.0 | 1108836.49 | 3.87 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 4.25 | 0.22 | 0.1 | 771977.8 | 7.51 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.06 | -0.1 | 631070.49 | 6.71 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.57 | -0.01 | 534776.14 | 11.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.3 | -0.01 | 310326.33 | 12.78 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.83 | -0.08 | 226348.64 | 3.35 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 3.0 | 2.91 | -0.02 | 74907.58 | 45.98 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 3.22 | 0.58 | 0.04 | 87533.91 | 11.47 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.65 | -0.14 | 122391.6 | 10.9 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.63 | 0.34 | 0.05 | 46173.01 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.07 | -0.02 | 181156.64 | 4.73 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 86.25 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.1 | -0.0 | 136217.11 | 42.87 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 56157.17 | 8.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
