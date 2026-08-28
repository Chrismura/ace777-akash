# Hulk DIGEST — 2026-08-28T11:07:23Z

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
| XRPUSDT | IDLE | 1.1 | 2.15 | 0.36 | -0.0 | 48904052.56 | 1.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.77 | 3.19 | 2.31 | -0.02 | 1318900.75 | 2.07 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.17 | 10.9 | 1.17 | 0.15 | 768159.33 | 18.63 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 5.77 | 5.05 | -0.05 | 81412.61 | 14.17 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.55 | 0.8 | -0.03 | 430349.22 | 9.74 | skipped_fast |
| KITEUSDT | IDLE | 2.4 | 4.27 | 3.58 | -0.02 | 76316.92 | 10.27 | skipped_fast |
| WUSDT | IDLE | 0.92 | 1.84 | 0.0 | -0.02 | 190077.45 | 12.61 | skipped_fast |
| RIZEUSDT | IDLE | 0.83 | 9.5 | 5.69 | -0.22 | 114306.63 | 56.03 | skipped_fast |
| ZBCNUSDT | IDLE | 0.56 | 1.53 | 0.16 | 0.0 | 233867.7 | 10.03 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 2.02 | 0.49 | 0.0 | 84331.9 | 3.49 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.58 | 0.42 | -0.0 | 323465.47 | 1.28 | skipped_fast |
| EDELUSDT | IDLE | 0.51 | 2.43 | 1.19 | 0.04 | 52537.18 | 34.39 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 2.54 | 1.88 | -0.01 | 134220.35 | 16.46 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 3.17 | 0.0 | -0.02 | 19840.28 | 118.79 | skipped_fast |
| QAITUSDT | IDLE | 0.35 | 4.58 | 1.39 | -0.17 | 45340.73 | 152.67 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.16 | 0.0 | 0.0 | 39747.59 | 3.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.21 | 1.06 | 0.01 | 2618.7 | 22.02 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.66 | 0.58 | 0.01 | 53444.98 | 16.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
