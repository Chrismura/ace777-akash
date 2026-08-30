# Hulk DIGEST — 2026-08-22T05:11:39Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.46 | 15.45 | 11.11 | 0.08 | 14698370.7 | 56.25 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 19.3 | 10.5 | 0.18 | 186034666.26 | 34.15 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.48 | 20.82 | 16.79 | -0.13 | 527080.57 | 46.01 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 2.82 | 10.33 | 6.96 | 0.09 | 1188266.0 | 32.17 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.56 | 4.02 | 0.17 | 752968.25 | 13.52 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 10.43 | 9.3 | 0.08 | 474973.61 | 96.34 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 6.36 | 5.98 | 0.07 | 538901.12 | 77.07 | skipped_fast |
| REDUSDT | IDLE | 1.98 | 15.51 | 13.12 | 0.14 | 157950.4 | 63.79 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.39 | 22.23 | 14.49 | -0.02 | 204830.21 | 488.31 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 10.8 | 9.67 | 0.04 | 188427.14 | 64.04 | skipped_fast |
| KITEUSDT | IDLE | 2.01 | 6.62 | 5.11 | 0.1 | 68361.38 | 40.61 | skipped_fast |
| RWAINCUSDT | IDLE | 2.36 | 4.48 | 1.62 | 0.02 | 10400.07 | 32.03 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.28 | 1.31 | -0.03 | 83672.19 | 44.2 | skipped_fast |
| TELUSDT | IDLE | 2.0 | 5.52 | 1.28 | 0.09 | 185722.69 | 15.01 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.11 | 7.38 | 6.87 | 0.05 | 4051.28 | 77.6 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 4.41 | 3.91 | 0.09 | 58678.5 | 44.52 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 3.38 | 1.2 | 0.06 | 57126.38 | 8.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
