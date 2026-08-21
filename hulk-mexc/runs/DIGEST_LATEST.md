# Hulk DIGEST — 2026-08-21T20:03:00Z

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
| PYTHUSDT | IDLE | 1.37 | 4.78 | 3.91 | 0.06 | 5455200.81 | 4.26 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 4.21 | 3.65 | 0.11 | 128832148.05 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.63 | 0.16 | 154356.92 | 20.56 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 10.86 | 8.77 | 0.07 | 481310.24 | 22.77 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.71 | 0.07 | 635070.61 | 7.47 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 3.23 | 3.1 | 0.05 | 793933.52 | 1.32 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 4.81 | 4.35 | 0.08 | 514597.98 | 3.12 | skipped_fast |
| WUSDT | IDLE | 2.2 | 3.92 | 3.17 | 0.04 | 365888.75 | 7.51 | skipped_fast |
| BIOUSDT | IDLE | 2.63 | 5.33 | 4.33 | -0.0 | 189979.1 | 3.21 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 4.29 | 4.01 | -0.05 | 79684.78 | 33.76 | skipped_fast |
| RWAINCUSDT | IDLE | 2.19 | 4.3 | 0.58 | 0.05 | 11066.49 | 5.35 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.44 | 0.02 | 56223.4 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.41 | 0.09 | 61281.27 | 11.29 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2867.01 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.54 | 0.01 | 183669.04 | 32.57 | skipped_fast |
| QNTUSDT | IDLE | 1.47 | 2.65 | 1.97 | 0.04 | 59921.44 | 6.27 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.08 | 0.99 | 0.04 | 54338.21 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.14 | 0.07 | 4276.39 | 21.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
