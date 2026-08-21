# Hulk DIGEST — 2026-08-21T20:18:33Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 2.97 | 0.09 | 5491155.55 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 4.21 | 2.87 | 0.12 | 129230123.8 | 2.9 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.22 | 0.16 | 153473.48 | 19.61 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.66 | 0.11 | 477695.57 | 27.02 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 3.91 | 1.42 | 0.08 | 633111.98 | 8.38 | skipped_fast |
| HBARUSDT | IDLE | 1.74 | 3.23 | 2.17 | 0.06 | 795645.73 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.58 | 0.08 | 510255.39 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.1 | 3.92 | 1.93 | 0.06 | 367845.86 | 16.97 | skipped_fast |
| BIOUSDT | IDLE | 2.55 | 5.33 | 3.01 | 0.02 | 190180.72 | 6.33 | skipped_fast |
| EDELUSDT | IDLE | 2.65 | 4.65 | 4.33 | -0.05 | 80187.06 | 11.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.59 | 0.02 | 56223.16 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.72 | 0.1 | 61279.13 | 11.2 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2802.39 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.42 | 3.39 | 2.06 | 0.01 | 183714.73 | 27.01 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 2.65 | 1.38 | 0.04 | 59922.55 | 4.68 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54436.97 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
