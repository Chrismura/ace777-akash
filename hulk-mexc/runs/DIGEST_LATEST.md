# Hulk DIGEST — 2026-08-21T20:50:28Z

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
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.56 | 0.08 | 5558691.29 | 4.2 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.64 | 0.1 | 128520686.79 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.03 | 0.17 | 153430.98 | 10.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.4 | 0.12 | 478988.18 | 40.94 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.35 | 0.1 | 641885.35 | 8.28 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.9 | 0.05 | 811304.29 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.64 | 0.08 | 514272.52 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.07 | 3.92 | 1.41 | 0.06 | 367728.95 | 18.97 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.76 | 0.01 | 188245.19 | 3.15 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.96 | 5.73 | 5.42 | -0.06 | 82626.79 | 68.26 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.49 | 0.02 | 56274.34 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 32.14 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 4.0 | 2.23 | 0.11 | 61185.74 | 11.16 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 181331.01 | 48.27 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.81 | 0.03 | 59848.55 | 7.82 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.02 | 2798.65 | 182.9 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53975.27 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
