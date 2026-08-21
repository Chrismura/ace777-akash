# Hulk DIGEST — 2026-08-21T20:51:08Z

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
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.42 | 0.08 | 5560077.18 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.52 | 0.1 | 128490104.1 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.9 | 0.17 | 153426.5 | 13.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.4 | 0.12 | 478972.58 | 44.43 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.17 | 0.1 | 641753.82 | 5.51 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.91 | 0.05 | 811603.18 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.64 | 0.08 | 514290.42 | 6.19 | skipped_fast |
| WUSDT | IDLE | 2.06 | 3.92 | 1.35 | 0.06 | 367815.53 | 13.69 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.33 | 2.55 | 0.01 | 188223.6 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.89 | 5.73 | 4.44 | -0.06 | 82626.79 | 56.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.71 | 0.28 | 0.02 | 56268.56 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 26.79 | skipped_fast |
| KITEUSDT | IDLE | 1.24 | 4.0 | 2.31 | 0.11 | 61178.64 | 12.09 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 181340.8 | 42.94 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 59844.42 | 6.25 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.02 | 2798.65 | 198.65 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53975.27 | 8.32 | skipped_fast |
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
