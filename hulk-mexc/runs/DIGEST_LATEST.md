# Hulk DIGEST — 2026-08-21T22:09:40Z

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
| PYTHUSDT | IDLE | 1.31 | 5.0 | 0.04 | 0.11 | 5704559.14 | 4.09 | skipped_fast |
| XRPUSDT | IDLE | 1.53 | 5.44 | 0.82 | 0.13 | 131362200.7 | 2.1 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.71 | 0.47 | 0.08 | 846157.67 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 5.25 | 0.0 | 0.12 | 644155.51 | 10.78 | skipped_fast |
| CHIPUSDT | IDLE | 1.5 | 4.54 | 1.54 | 0.06 | 533529.23 | 6.12 | skipped_fast |
| WUSDT | IDLE | 2.32 | 4.67 | 0.0 | 0.08 | 367620.33 | 14.44 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 6.5 | 0.0 | 0.12 | 496573.99 | 27.55 | skipped_fast |
| BIOUSDT | IDLE | 2.21 | 5.01 | 0.09 | 0.04 | 185407.96 | 3.08 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.38 | 0.18 | 155083.3 | 8.92 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.62 | 0.06 | 186757.61 | 5.17 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.17 | 4.07 | 1.8 | 0.01 | 10246.19 | 48.12 | skipped_fast |
| EDELUSDT | IDLE | 1.86 | 4.12 | 0.0 | -0.03 | 82382.55 | 55.16 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.71 | 0.11 | 61231.73 | 12.84 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.71 | 0.06 | 56402.21 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.0 | 0.43 | 0.05 | 65324.79 | 19.93 | skipped_fast |
| RWAUSDT | IDLE | 0.9 | 1.75 | 0.33 | 0.04 | 54225.6 | 8.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 10.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
