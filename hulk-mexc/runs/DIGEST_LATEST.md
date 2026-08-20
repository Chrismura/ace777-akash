# Hulk DIGEST — 2026-08-20T10:13:12Z

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
| XRPUSDT | IDLE | 1.49 | 5.78 | 0.89 | 0.15 | 54058988.59 | 0.87 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 8.52 | 7.45 | 0.09 | 248268.29 | 7.19 | skipped_fast |
| BIOUSDT | IDLE | 2.18 | 19.0 | 2.99 | 0.3 | 256609.07 | 21.36 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 5.07 | 1.25 | 0.15 | 426735.42 | 5.79 | skipped_fast |
| PYTHUSDT | IDLE | 1.36 | 5.51 | 1.08 | 0.14 | 372134.54 | 2.26 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.79 | 9.55 | 0.26 | 187674.21 | 9.99 | skipped_fast |
| WUSDT | IDLE | 1.68 | 3.68 | 0.32 | 0.09 | 305551.06 | 11.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.06 | 4.32 | 0.0 | 0.16 | 239802.01 | 15.72 | skipped_fast |
| RIZEUSDT | IDLE | 1.3 | 8.62 | 5.44 | 0.12 | 68844.04 | 44.42 | skipped_fast |
| QAITUSDT | IDLE | 2.02 | 5.78 | 3.83 | 0.01 | 10331.02 | 65.65 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.37 | 0.07 | 0.08 | 407616.12 | 1.38 | skipped_fast |
| QNTUSDT | IDLE | 2.22 | 5.59 | 0.31 | 0.1 | 39992.55 | 8.08 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 1.84 | 0.33 | 0.07 | 60463.51 | 13.44 | skipped_fast |
| EDELUSDT | IDLE | 0.55 | 4.3 | 2.39 | 0.21 | 103012.17 | 44.4 | skipped_fast |
| TELUSDT | IDLE | 0.87 | 4.12 | 1.14 | 0.13 | 201061.24 | 36.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.68 | 4.58 | 0.65 | 0.1 | 2871.92 | 21.59 | skipped_fast |
| RWAINCUSDT | IDLE | 0.66 | 1.88 | 1.01 | 0.04 | 17326.82 | 61.82 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.78 | 0.34 | 0.01 | 52983.93 | 34.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
