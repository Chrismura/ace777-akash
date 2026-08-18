# Hulk DIGEST — 2026-08-18T04:08:25Z

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
| XRPUSDT | IDLE | 0.89 | 1.58 | 1.27 | -0.01 | 12630506.7 | 2.02 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 28.73 | 19.26 | -0.02 | 8236.15 | 3.26 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 2.69 | 0.0 | -0.04 | 292464.76 | 13.06 | skipped_fast |
| CHIPUSDT | IDLE | 0.88 | 4.4 | 1.16 | -0.02 | 332728.39 | 10.66 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 2.76 | 2.46 | -0.03 | 179714.5 | 2.65 | skipped_fast |
| WUSDT | IDLE | 1.52 | 2.7 | 2.21 | -0.05 | 131892.96 | 12.34 | skipped_fast |
| BIOUSDT | IDLE | 1.67 | 3.04 | 2.06 | -0.0 | 82476.6 | 4.13 | skipped_fast |
| REDUSDT | IDLE | 1.93 | 4.14 | 0.01 | 0.05 | 57677.33 | 23.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.13 | 2.0 | 1.7 | -0.0 | 208151.8 | 17.3 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 2.78 | 0.9 | -0.01 | 66563.15 | 39.09 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.26 | 0.0 | -0.01 | 60182.46 | 10.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.63 | 4.62 | 2.56 | 0.03 | 81824.4 | 72.73 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.2 | 1.72 | 0.0 | 38338.56 | 5.35 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.35 | 0.97 | 0.01 | 141469.41 | 1.53 | skipped_fast |
| RWAINCUSDT | IDLE | 0.44 | 0.77 | 0.76 | -0.04 | 773.14 | 52.89 | skipped_fast |
| TELUSDT | IDLE | 0.9 | 1.88 | 1.07 | -0.05 | 134590.56 | 43.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.2 | 2.13 | 1.83 | -0.04 | 601.86 | 22.68 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.69 | 0.6 | 0.0 | 49401.9 | 17.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
