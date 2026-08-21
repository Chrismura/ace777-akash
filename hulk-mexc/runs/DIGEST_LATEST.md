# Hulk DIGEST — 2026-08-21T21:19:03Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.96 | 0.09 | 5614409.55 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 2.09 | 0.1 | 128569278.35 | 2.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.92 | 5.61 | 4.62 | 0.06 | 515564.65 | 6.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.2 | 0.1 | 483799.48 | 29.79 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.14 | 0.59 | 0.09 | 644468.78 | 6.45 | skipped_fast |
| HBARUSDT | IDLE | 1.58 | 3.04 | 0.84 | 0.07 | 809421.81 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.97 | 3.83 | 0.79 | 0.06 | 366795.86 | 9.44 | skipped_fast |
| BIOUSDT | IDLE | 2.45 | 5.2 | 2.46 | 0.0 | 187207.3 | 6.29 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.43 | 0.16 | 153624.51 | 22.19 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10270.17 | 10.76 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.32 | 0.02 | 56190.47 | 45.77 | skipped_fast |
| EDELUSDT | IDLE | 2.05 | 4.12 | 2.75 | -0.04 | 82591.66 | 78.78 | skipped_fast |
| QAITUSDT | IDLE | 2.5 | 4.38 | 4.2 | -0.04 | 3753.25 | 115.79 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 4.0 | 1.95 | 0.11 | 61008.58 | 13.91 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.22 | 0.01 | 179213.43 | 16.06 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.03 | 61249.82 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.17 | 1.07 | 0.03 | 53814.32 | 16.61 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 21.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
