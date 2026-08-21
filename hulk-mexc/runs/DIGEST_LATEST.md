# Hulk DIGEST — 2026-08-21T20:19:14Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 2.97 | 0.09 | 5492706.87 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 4.21 | 2.96 | 0.12 | 129218440.17 | 2.18 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.29 | 0.16 | 153485.56 | 19.61 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.8 | 0.12 | 478005.71 | 22.06 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 3.91 | 1.45 | 0.08 | 633076.08 | 5.58 | skipped_fast |
| HBARUSDT | IDLE | 1.74 | 3.23 | 2.17 | 0.06 | 801979.33 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.58 | 0.08 | 510259.52 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.1 | 3.92 | 1.93 | 0.06 | 367401.12 | 13.79 | skipped_fast |
| BIOUSDT | IDLE | 2.55 | 5.33 | 3.04 | 0.01 | 190139.9 | 6.33 | skipped_fast |
| EDELUSDT | IDLE | 2.66 | 4.65 | 4.44 | -0.05 | 80243.08 | 11.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.54 | 0.02 | 56215.91 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 37.5 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.68 | 0.1 | 61223.13 | 11.2 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2802.39 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.42 | 3.39 | 2.06 | 0.01 | 183714.73 | 32.41 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 2.65 | 1.38 | 0.04 | 59935.37 | 6.24 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54457.62 | 24.95 | skipped_fast |
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
