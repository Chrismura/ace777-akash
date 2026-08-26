# Hulk DIGEST — 2026-08-26T02:09:46Z

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
| PYTHUSDT | IDLE | 2.05 | 4.28 | 0.9 | -0.01 | 2124405.69 | 3.93 | skipped_fast |
| XRPUSDT | IDLE | 1.54 | 3.31 | 0.97 | -0.04 | 71163385.75 | 2.09 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 77.68 | 38.89 | 0.08 | 54512.6 | 404.61 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 3.39 | 2.08 | -0.04 | 537025.11 | 7.57 | skipped_fast |
| CHIPUSDT | IDLE | 1.8 | 5.18 | 1.79 | -0.0 | 403491.44 | 6.26 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.69 | 0.61 | -0.04 | 755275.67 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.43 | 2.82 | 0.55 | -0.03 | 309309.49 | 14.92 | skipped_fast |
| BIOUSDT | IDLE | 2.12 | 4.1 | 0.95 | -0.01 | 104732.43 | 3.43 | skipped_fast |
| REDUSDT | IDLE | 2.09 | 5.55 | 0.96 | 0.03 | 81184.57 | 20.48 | skipped_fast |
| KITEUSDT | IDLE | 1.79 | 3.51 | 0.48 | -0.03 | 61143.63 | 9.75 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 2.39 | 0.67 | 0.0 | 164202.61 | 13.18 | skipped_fast |
| EDELUSDT | IDLE | 0.58 | 8.27 | 6.34 | 0.06 | 156298.5 | 51.9 | skipped_fast |
| QAITUSDT | IDLE | 1.61 | 4.29 | 1.48 | 0.03 | 12851.48 | 37.64 | skipped_fast |
| RWAINCUSDT | IDLE | 1.08 | 1.88 | 1.84 | -0.02 | 2540.19 | 35.47 | skipped_fast |
| TELUSDT | IDLE | 1.15 | 2.18 | 0.82 | -0.04 | 98255.33 | 16.64 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.19 | 0.47 | -0.02 | 135752.63 | 4.73 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.41 | 1.31 | -0.04 | 56410.16 | 16.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.85 | 0.0 | -0.03 | 390.01 | 22.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
