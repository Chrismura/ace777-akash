# Hulk DIGEST — 2026-10-01T04:52:20Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| QNTUSDT | IDLE | 1.7 | 7.94 | 3.14 | 0.03 | 9352692.14 | 8.87 | skipped_fast |
| XRPUSDT | IDLE | 0.76 | 1.51 | 0.05 | 0.01 | 51810396.0 | 1.33 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.23 | 0.03 | 0.01 | 379773480.94 | 0.3 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.89 | 0.0 | 0.01 | 628872426.59 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.82 | 3.58 | 0.4 | 0.03 | 1317594.26 | 9.36 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.61 | 1.42 | 0.01 | 900123.92 | 5.52 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 13.03 | 6.2 | 0.02 | 452395.65 | 21.31 | skipped_fast |
| WUSDT | IDLE | 1.78 | 3.5 | 0.45 | 0.0 | 768842.73 | 7.33 | skipped_fast |
| PYTHUSDT | IDLE | 1.61 | 3.22 | 0.06 | -0.0 | 520903.24 | 5.1 | skipped_fast |
| RWAINCUSDT | IDLE | 2.43 | 5.55 | 0.04 | -0.01 | 11336.3 | 4.14 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 3.71 | 0.96 | 0.06 | 88302.86 | 8.97 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 5.02 | 0.47 | 0.13 | 78737.74 | 17.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 2.76 | 0.0 | -0.0 | 67936.61 | 9.1 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.98 | 0.73 | -0.0 | 91742.58 | 6.43 | skipped_fast |
| EDELUSDT | IDLE | 0.61 | 5.88 | 4.49 | 0.21 | 165753.96 | 54.32 | skipped_fast |
| TELUSDT | IDLE | 1.58 | 4.35 | 3.12 | 0.04 | 237542.01 | 43.57 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 2.0 | 1.56 | 0.03 | 38348.56 | 76.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.91 | 1.61 | 1.38 | -0.01 | 38427.82 | 26.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 1.03 | 0.22 | 0.0 | 1182.69 | 21.41 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.59 | 0.07 | -0.0 | 53975.03 | 43.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
