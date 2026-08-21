# Hulk DIGEST — 2026-08-21T20:58:09Z

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
| PYTHUSDT | IDLE | 1.3 | 4.78 | 2.11 | 0.09 | 5569360.26 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.31 | 0.1 | 128329130.9 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.7 | 0.17 | 152970.06 | 15.44 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 10.86 | 7.93 | 0.1 | 479532.96 | 94.71 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.38 | 0.1 | 642023.58 | 5.52 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.9 | 0.06 | 809002.14 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.73 | 0.08 | 514576.28 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.92 | 0.99 | 0.07 | 368185.64 | 11.55 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.48 | 0.01 | 188046.19 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.89 | 5.73 | 4.33 | -0.05 | 82488.27 | 22.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.71 | 0.36 | 0.03 | 56223.38 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 53.56 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 4.0 | 2.21 | 0.11 | 61337.5 | 13.96 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.43 | 0.01 | 181276.99 | 32.21 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.03 | 60175.25 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 198.65 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.03 | 53911.53 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
