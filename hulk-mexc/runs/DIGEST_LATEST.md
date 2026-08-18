# Hulk DIGEST — 2026-08-18T10:24:58Z

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
| XRPUSDT | IDLE | 0.46 | 0.84 | 0.55 | -0.0 | 11823534.52 | 1.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 11.21 | 8.4 | -0.03 | 81234.87 | 39.19 | skipped_fast |
| RWAINCUSDT | IDLE | 4.34 | 8.85 | 4.96 | -0.02 | 2589.12 | 29.46 | skipped_fast |
| REDUSDT | IDLE | 2.13 | 18.49 | 11.07 | 0.23 | 84325.28 | 14.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.06 | 8.07 | 2.0 | -0.05 | 276726.56 | 3.46 | skipped_fast |
| KITEUSDT | IDLE | 2.86 | 5.03 | 4.56 | -0.02 | 61589.73 | 14.33 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.53 | 1.91 | -0.04 | 289416.11 | 5.48 | skipped_fast |
| QAITUSDT | IDLE | 1.64 | 10.79 | 8.14 | -0.04 | 11368.62 | 60.02 | skipped_fast |
| PYTHUSDT | IDLE | 0.82 | 1.51 | 0.84 | -0.03 | 198394.26 | 5.28 | skipped_fast |
| ZBCNUSDT | IDLE | 0.69 | 1.32 | 0.37 | -0.01 | 211310.8 | 15.93 | skipped_fast |
| WUSDT | IDLE | 0.67 | 1.19 | 1.04 | -0.03 | 152718.18 | 14.79 | skipped_fast |
| BIOUSDT | IDLE | 0.72 | 1.29 | 1.02 | -0.02 | 76213.41 | 4.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.28 | 2.04 | 0.0 | -0.18 | 55599.46 | 27.27 | skipped_fast |
| TELUSDT | IDLE | 0.89 | 1.94 | 0.07 | -0.02 | 136112.34 | 14.12 | skipped_fast |
| HBARUSDT | IDLE | 0.41 | 0.78 | 0.26 | 0.0 | 122709.44 | 1.52 | skipped_fast |
| QNTUSDT | IDLE | 0.46 | 0.83 | 0.66 | 0.0 | 36661.03 | 7.16 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.78 | 0.78 | -0.01 | 50162.0 | 17.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.22 | 0.39 | 0.38 | -0.04 | 217.91 | 22.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
