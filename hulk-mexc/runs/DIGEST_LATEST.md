# Hulk DIGEST — 2026-08-17T02:10:17Z

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
| XRPUSDT | IDLE | 0.68 | 1.3 | 0.35 | -0.0 | 7624259.51 | 1.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 26.91 | 19.23 | 0.05 | 42772.88 | 49.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 7.65 | 4.03 | -0.0 | 298320.75 | 3.52 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.94 | 0.89 | -0.05 | 309828.43 | 9.41 | skipped_fast |
| WUSDT | IDLE | 1.56 | 2.94 | 1.15 | 0.01 | 183810.59 | 12.87 | skipped_fast |
| PYTHUSDT | IDLE | 0.88 | 1.67 | 0.62 | -0.01 | 152720.77 | 2.59 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 3.05 | 1.29 | 0.03 | 55610.53 | 52.02 | skipped_fast |
| ZBCNUSDT | IDLE | 0.76 | 1.48 | 0.28 | -0.0 | 186327.22 | 21.58 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 1.91 | 1.88 | -0.03 | 61699.0 | 15.16 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 1.97 | 1.41 | -0.01 | 54321.91 | 14.93 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.67 | 1.03 | -0.01 | 63282.83 | 4.15 | skipped_fast |
| QAITUSDT | IDLE | 0.93 | 2.41 | 0.0 | -0.02 | 2170.45 | 61.3 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 2.94 | 0.54 | -0.0 | 89996.27 | 47.8 | skipped_fast |
| QNTUSDT | IDLE | 1.24 | 2.28 | 1.4 | -0.03 | 33261.28 | 5.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 1.31 | 0.34 | 0.02 | 3880.76 | 96.45 | skipped_fast |
| HBARUSDT | IDLE | 0.67 | 1.26 | 0.49 | -0.0 | 93129.13 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.7 | 0.43 | 0.0 | 50266.77 | 17.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.62 | 1.16 | 0.53 | 0.01 | 369.37 | 21.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
