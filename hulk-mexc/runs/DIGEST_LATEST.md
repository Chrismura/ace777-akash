# Hulk DIGEST — 2026-08-22T12:02:22Z

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
| PYTHUSDT | IDLE | 1.73 | 7.83 | 4.84 | 0.01 | 51606666.12 | 4.08 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 14.26 | 8.55 | 0.1 | 215634909.92 | 1.34 | skipped_fast |
| HBARUSDT | IDLE | 1.28 | 4.63 | 2.89 | 0.02 | 1254017.1 | 3.88 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 8.38 | 4.84 | 0.13 | 781428.11 | 5.97 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.74 | 0.02 | 580242.31 | 12.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.28 | 5.77 | 5.1 | -0.04 | 381000.61 | 59.34 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 4.16 | 0.76 | -0.09 | 617227.81 | 3.33 | skipped_fast |
| KITEUSDT | IDLE | 2.61 | 6.24 | 0.53 | 0.04 | 82195.92 | 11.45 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.31 | -0.04 | 78203.95 | 11.4 | skipped_fast |
| BIOUSDT | IDLE | 0.8 | 5.65 | 2.11 | -0.03 | 240945.74 | 6.41 | skipped_fast |
| TELUSDT | IDLE | 2.2 | 5.61 | 4.5 | -0.03 | 167513.67 | 10.7 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | 0.0 | 2397.64 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 2.97 | 0.02 | 154122.24 | 9.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.56 | 0.01 | 188356.43 | 1.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 1.91 | 0.95 | -0.04 | 48587.83 | 46.44 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.02 | 57852.81 | 8.15 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 21.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
