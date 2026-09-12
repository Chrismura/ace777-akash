# Hulk DIGEST — 2026-09-12T15:37:54Z

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
| ETHUSDT | IDLE | 0.33 | 0.61 | 0.35 | -0.03 | 340871006.4 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.34 | 0.62 | 0.36 | -0.02 | 26263641.87 | 1.46 | skipped_fast |
| BTCUSDT | IDLE | 0.16 | 0.31 | 0.11 | -0.02 | 421616605.07 | 0.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 6.86 | 6.11 | -0.03 | 224399.26 | 10.95 | skipped_fast |
| PYTHUSDT | IDLE | 1.78 | 4.28 | 0.47 | 0.02 | 386715.8 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 3.02 | 7.97 | 1.86 | 0.01 | 81005.32 | 17.97 | skipped_fast |
| RIZEUSDT | IDLE | 1.63 | 57.62 | 21.48 | 0.58 | 147935.95 | 1125.24 | skipped_fast |
| RWAINCUSDT | IDLE | 2.8 | 5.17 | 4.86 | -0.01 | 11829.09 | 27.68 | skipped_fast |
| EDELUSDT | IDLE | 1.58 | 4.25 | 1.1 | 0.07 | 164939.3 | 17.18 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.67 | 1.54 | -0.02 | 254462.72 | 7.15 | skipped_fast |
| WUSDT | IDLE | 0.88 | 1.75 | 0.03 | -0.01 | 123763.96 | 12.15 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.57 | 0.73 | -0.0 | 72620.71 | 7.79 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.72 | 1.06 | 0.02 | 62137.89 | 18.69 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.32 | 0.77 | -0.03 | 60493.31 | 12.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.05 | 1.24 | -0.08 | 90181.7 | 29.97 | skipped_fast |
| HBARUSDT | IDLE | 0.35 | 0.69 | 0.08 | -0.02 | 201235.57 | 1.34 | skipped_fast |
| RWAUSDT | IDLE | 1.03 | 1.85 | 1.46 | 0.01 | 54587.95 | 29.56 | skipped_fast |
| QNTUSDT | IDLE | 0.46 | 0.84 | 0.6 | -0.02 | 41059.58 | 4.66 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.71 | 0.06 | -0.0 | 23780.65 | 5.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.0 | 1327.32 | 22.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
