# Hulk DIGEST — 2026-08-21T20:04:21Z

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
| PYTHUSDT | IDLE | 1.35 | 4.78 | 3.6 | 0.07 | 5462625.0 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.3 | 0.11 | 128903895.27 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.41 | 0.16 | 154381.53 | 10.64 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.54 | 10.86 | 7.67 | 0.08 | 481591.48 | 40.99 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.73 | 0.07 | 635303.15 | 8.41 | skipped_fast |
| HBARUSDT | IDLE | 1.8 | 3.23 | 2.9 | 0.05 | 793775.06 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 4.81 | 4.26 | 0.09 | 513613.78 | 6.23 | skipped_fast |
| WUSDT | IDLE | 2.17 | 3.92 | 2.74 | 0.05 | 365862.87 | 5.34 | skipped_fast |
| BIOUSDT | IDLE | 2.61 | 5.33 | 3.93 | -0.0 | 189952.75 | 3.19 | skipped_fast |
| EDELUSDT | IDLE | 2.42 | 4.29 | 3.68 | -0.05 | 79739.9 | 33.8 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.61 | 0.01 | 56211.04 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.25 | 4.3 | 1.32 | 0.04 | 11067.79 | 42.85 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 3.12 | 0.1 | 61286.24 | 11.24 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2867.01 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.54 | 0.01 | 183656.62 | 32.56 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.75 | 0.04 | 59959.63 | 4.69 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.16 | 0.82 | 0.04 | 54379.15 | 8.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.14 | 0.07 | 4276.39 | 22.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
