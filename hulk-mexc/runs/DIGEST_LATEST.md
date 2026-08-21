# Hulk DIGEST — 2026-08-21T20:47:00Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.7 | 0.08 | 5552997.76 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.52 | 0.1 | 128747657.92 | 2.92 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.35 | 0.18 | 153344.78 | 9.74 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.89 | 0.12 | 478684.01 | 20.07 | skipped_fast |
| CCUSDT | IDLE | 1.4 | 3.91 | 0.1 | 0.1 | 641295.19 | 6.43 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.23 | 1.95 | 0.05 | 811176.54 | 2.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.61 | 0.08 | 514434.95 | 3.09 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.54 | 0.06 | 367727.49 | 13.72 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.7 | 0.01 | 188316.55 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 5.01 | 3.68 | -0.05 | 81452.46 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.45 | 0.02 | 56269.29 | 45.14 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 26.73 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.53 | 0.1 | 61125.92 | 12.11 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.16 | 0.01 | 181696.62 | 26.76 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.65 | 1.89 | 0.03 | 59911.06 | 6.27 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 54036.36 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.53 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.01 | 2795.49 | 314.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
