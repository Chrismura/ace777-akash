# Hulk DIGEST — 2026-08-29T08:06:40Z

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
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 12.93 | 7.8 | 0.02 | 1244487.56 | 2.45 | skipped_fast |
| XRPUSDT | IDLE | 0.65 | 1.17 | 0.9 | -0.03 | 43098573.57 | 2.9 | skipped_fast |
| PYTHUSDT | IDLE | 1.7 | 2.98 | 2.84 | -0.04 | 501450.99 | 2.15 | skipped_fast |
| WUSDT | IDLE | 1.24 | 2.18 | 2.02 | -0.03 | 209753.41 | 12.07 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 2.85 | 2.09 | -0.01 | 69147.96 | 11.84 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.52 | 0.39 | -0.01 | 213234.78 | 5.39 | skipped_fast |
| REDUSDT | IDLE | 1.45 | 2.82 | 0.71 | 0.01 | 60900.85 | 10.07 | skipped_fast |
| EDELUSDT | IDLE | 1.01 | 3.69 | 3.37 | -0.11 | 90067.25 | 19.38 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.32 | 1.24 | -0.04 | 461312.52 | 1.34 | skipped_fast |
| ZBCNUSDT | IDLE | 0.52 | 1.4 | 0.48 | -0.06 | 180355.89 | 12.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.55 | 3.21 | 1.34 | -0.05 | 29598.85 | 58.36 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 1.34 | 1.22 | -0.04 | 81802.68 | 3.63 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 1.66 | 1.63 | 0.01 | 3548.47 | 88.35 | skipped_fast |
| QAITUSDT | IDLE | 0.24 | 2.07 | 1.47 | -0.03 | 84066.77 | 66.99 | skipped_fast |
| TELUSDT | IDLE | 0.82 | 1.44 | 1.3 | -0.05 | 80341.74 | 45.85 | skipped_fast |
| QNTUSDT | IDLE | 0.59 | 1.03 | 1.02 | -0.03 | 40682.24 | 4.92 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.16 | 0.41 | 0.01 | 55517.37 | 16.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.25 | 0.44 | 0.44 | -0.05 | 3704.21 | 21.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
