# Hulk DIGEST — 2026-08-21T19:34:55Z

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
| PYTHUSDT | IDLE | 1.35 | 4.99 | 3.86 | 0.07 | 5421768.71 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.13 | 4.21 | 2.53 | 0.13 | 129380895.31 | 2.17 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.57 | 11.37 | 9.58 | 0.05 | 483909.16 | 19.22 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 26.97 | 13.08 | 0.17 | 152026.72 | 54.47 | skipped_fast |
| CCUSDT | IDLE | 2.08 | 5.44 | 2.61 | 0.06 | 625825.09 | 10.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.22 | 4.81 | 3.49 | 0.1 | 519603.5 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.15 | 3.92 | 2.85 | 0.05 | 359874.68 | 8.56 | skipped_fast |
| BIOUSDT | IDLE | 2.64 | 5.33 | 4.42 | -0.0 | 191094.21 | 3.22 | skipped_fast |
| HBARUSDT | IDLE | 1.44 | 2.85 | 2.05 | 0.07 | 750184.87 | 1.3 | skipped_fast |
| RIZEUSDT | IDLE | 2.28 | 11.27 | 4.18 | 0.0 | 56470.55 | 17.79 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 4.29 | 3.9 | -0.05 | 79607.96 | 22.52 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.48 | 0.09 | 60688.44 | 13.18 | skipped_fast |
| RWAINCUSDT | IDLE | 2.25 | 4.3 | 1.27 | 0.05 | 11033.79 | 113.06 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | 0.0 | 3154.82 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 4.46 | 2.16 | 0.03 | 184044.88 | 37.66 | skipped_fast |
| QNTUSDT | IDLE | 1.63 | 3.01 | 1.72 | 0.04 | 60235.34 | 4.69 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.16 | 0.82 | 0.04 | 54396.4 | 16.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4371.2 | 19.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
