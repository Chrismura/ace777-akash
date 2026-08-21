# Hulk DIGEST — 2026-08-21T20:48:53Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.7 | 0.08 | 5557158.77 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 4.21 | 3.7 | 0.1 | 128533270.5 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.62 | 0.17 | 153365.05 | 17.9 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 10.86 | 6.0 | 0.12 | 478656.27 | 21.61 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.35 | 0.09 | 641845.47 | 3.68 | skipped_fast |
| HBARUSDT | IDLE | 1.74 | 3.23 | 2.1 | 0.05 | 811286.38 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.58 | 0.08 | 514263.33 | 6.19 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.56 | 0.06 | 367746.7 | 13.73 | skipped_fast |
| BIOUSDT | IDLE | 2.54 | 5.33 | 2.88 | 0.01 | 188206.87 | 3.16 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.96 | 5.73 | 5.42 | -0.06 | 82581.69 | 34.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.43 | 0.02 | 56275.09 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 48.14 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.48 | 0.11 | 61197.23 | 13.96 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.16 | 0.01 | 181342.03 | 26.76 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.85 | 0.03 | 59867.63 | 7.83 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.02 | 2798.65 | 175.02 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.15 | 0.03 | 54027.86 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
