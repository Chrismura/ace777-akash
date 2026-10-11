# Hulk DIGEST — 2026-10-11T14:54:12Z

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
| XRPUSDT | IDLE | 0.47 | 0.93 | 0.06 | -0.01 | 10026108.17 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.11 | -0.0 | 167905601.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.34 | 0.11 | 0.0 | 122721577.72 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.01 | 2.75 | 1.05 | -0.05 | 1076645.98 | 9.71 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 31.62 | 16.08 | 0.06 | 54224.63 | 20.97 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 11.9 | 7.06 | -0.0 | 28445.58 | 24.38 | skipped_fast |
| PYTHUSDT | IDLE | 1.36 | 2.56 | 1.04 | -0.01 | 730432.95 | 2.59 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.03 | 0.53 | -0.02 | 962985.28 | 2.86 | skipped_fast |
| CCUSDT | IDLE | 2.19 | 4.37 | 0.1 | 0.03 | 302531.38 | 9.61 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 10.01 | 2.02 | 0.33 | 406067.84 | 11.6 | skipped_fast |
| EDELUSDT | IDLE | 1.25 | 2.3 | 1.33 | 0.01 | 384789.57 | 15.52 | skipped_fast |
| RIZEUSDT | IDLE | 2.33 | 6.54 | 2.22 | -0.07 | 35577.68 | 40.26 | skipped_fast |
| BIOUSDT | IDLE | 1.89 | 3.78 | 0.03 | 0.04 | 72805.6 | 6.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.54 | 1.48 | -0.01 | 162803.77 | 39.66 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.27 | 0.0 | -0.0 | 57831.85 | 0.66 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 1.88 | 0.2 | -0.02 | 73538.69 | 5.5 | skipped_fast |
| TELUSDT | IDLE | 2.07 | 3.85 | 2.11 | -0.05 | 144389.11 | 29.13 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 2.08 | 0.15 | -0.01 | 245908.94 | 3.24 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.59 | 0.0 | 0.01 | 51973.26 | 7.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.74 | 0.05 | -0.01 | 31205.5 | 24.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
