# Hulk DIGEST — 2026-08-21T20:15:36Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.34 | 0.08 | 5484127.85 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.42 | 0.11 | 128949324.32 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.51 | 0.17 | 153884.64 | 13.1 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 10.86 | 6.24 | 0.12 | 477741.32 | 33.15 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 3.91 | 1.94 | 0.07 | 632415.32 | 6.54 | skipped_fast |
| HBARUSDT | IDLE | 1.76 | 3.23 | 2.36 | 0.06 | 796034.59 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.85 | 0.08 | 512739.39 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.14 | 3.92 | 2.41 | 0.05 | 367354.38 | 11.72 | skipped_fast |
| BIOUSDT | IDLE | 2.56 | 5.33 | 3.19 | 0.02 | 190308.95 | 3.17 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 4.53 | 4.33 | -0.05 | 80185.11 | 11.32 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.65 | 0.01 | 56225.97 | 19.34 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.04 | 11178.26 | 42.87 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.69 | 0.1 | 61323.11 | 11.2 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2806.14 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.41 | 3.39 | 1.85 | 0.01 | 183558.08 | 32.41 | skipped_fast |
| QNTUSDT | IDLE | 1.44 | 2.65 | 1.49 | 0.04 | 59960.64 | 6.24 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54501.08 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
