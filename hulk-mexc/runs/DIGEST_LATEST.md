# Hulk DIGEST — 2026-08-17T15:11:59Z

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
| XRPUSDT | IDLE | 0.47 | 0.93 | 0.01 | 0.0 | 12247159.32 | 0.99 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 26.76 | 15.64 | 0.18 | 70541.85 | 35.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.7 | 7.6 | 4.91 | 0.02 | 342351.23 | 3.33 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 3.54 | 3.34 | -0.05 | 262750.01 | 8.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.17 | 4.25 | 0.61 | 0.01 | 172825.64 | 25.86 | skipped_fast |
| REDUSDT | IDLE | 2.33 | 4.16 | 3.27 | -0.05 | 57088.85 | 16.86 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.97 | 0.86 | 0.07 | 61142.61 | 49.44 | skipped_fast |
| TELUSDT | IDLE | 2.73 | 4.86 | 4.02 | -0.03 | 107021.8 | 63.85 | skipped_fast |
| WUSDT | IDLE | 0.67 | 1.21 | 0.8 | -0.04 | 162450.35 | 16.75 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.67 | 1.0 | -0.01 | 74059.47 | 8.12 | skipped_fast |
| PYTHUSDT | IDLE | 0.54 | 0.98 | 0.71 | -0.01 | 150421.23 | 5.13 | skipped_fast |
| QAITUSDT | IDLE | 1.45 | 2.53 | 2.47 | -0.0 | 744.69 | 61.3 | skipped_fast |
| KITEUSDT | IDLE | 0.72 | 1.3 | 0.96 | -0.02 | 53408.88 | 16.17 | skipped_fast |
| QNTUSDT | IDLE | 1.98 | 3.77 | 1.33 | -0.01 | 35773.07 | 8.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.1 | 1.92 | 1.88 | -0.0 | 1860.75 | 58.04 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.48 | 0.62 | 0.01 | 123833.73 | 1.52 | skipped_fast |
| FLUIDUSDT | IDLE | 1.11 | 2.23 | 0.0 | 0.0 | 869.84 | 19.65 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.7 | 0.17 | 0.01 | 49823.18 | 8.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
