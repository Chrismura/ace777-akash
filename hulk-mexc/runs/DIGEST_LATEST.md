# Hulk DIGEST — 2026-08-29T20:11:42Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 70.44 | 38.01 | -0.02 | 137506.67 | 17.87 | skipped_fast |
| XRPUSDT | IDLE | 0.58 | 1.13 | 0.14 | 0.01 | 17851363.41 | 1.43 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 3.63 | 2.95 | -0.02 | 954804.82 | 4.91 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 9.92 | 5.92 | -0.07 | 39237.39 | 58.56 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.8 | 7.11 | 6.52 | 0.01 | 67622.84 | 8.59 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 3.52 | 2.05 | 0.03 | 330145.28 | 4.15 | skipped_fast |
| ZBCNUSDT | IDLE | 2.21 | 3.87 | 3.65 | -0.03 | 193830.69 | 37.01 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.18 | 0.66 | 0.07 | 206102.17 | 10.13 | skipped_fast |
| WUSDT | IDLE | 0.92 | 1.73 | 0.79 | 0.01 | 180225.96 | 11.99 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 1.83 | 1.47 | 0.02 | 76130.32 | 13.91 | skipped_fast |
| BIOUSDT | IDLE | 0.58 | 1.06 | 0.65 | -0.0 | 65120.35 | 3.63 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 1.8 | 1.11 | -0.05 | 2885.56 | 129.25 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.21 | 0.97 | -0.01 | 68753.05 | 40.26 | skipped_fast |
| HBARUSDT | IDLE | 0.29 | 0.57 | 0.13 | -0.01 | 181336.14 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 0.59 | 1.05 | 0.81 | 0.0 | 28853.37 | 6.54 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.58 | 0.08 | 0.01 | 54122.43 | 24.66 | skipped_fast |
| FLUIDUSDT | IDLE | 0.12 | 0.24 | 0.0 | 0.0 | 1876.26 | 21.47 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
