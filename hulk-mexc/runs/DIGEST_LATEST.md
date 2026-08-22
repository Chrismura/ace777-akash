# Hulk DIGEST — 2026-08-22T04:16:23Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 13.13 | 0.33 | 0.2 | 10416398.28 | 9.17 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 12.22 | 0.75 | 0.21 | 167400763.94 | 2.52 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.11 | 11.56 | 0.46 | 0.21 | 724551.26 | 11.37 | skipped_fast |
| HBARUSDT | IDLE | 2.15 | 6.49 | 0.0 | 0.12 | 1005392.49 | 1.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.84 | 5.36 | 2.15 | 0.0 | 446472.4 | 6.01 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.23 | 0.07 | 199930.88 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.97 | 7.18 | 0.74 | 0.14 | 430867.46 | 9.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.29 | 0.11 | 535392.12 | 22.34 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.98 | 0.1 | 59148.03 | 11.97 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.58 | -0.05 | 80357.11 | 11.25 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.39 | 0.2 | 160319.33 | 19.12 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.55 | 0.8 | 0.13 | 67627.04 | 13.31 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 3.6 | 2.74 | 0.01 | 9442.75 | 59.44 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.47 | 0.09 | 178549.39 | 4.44 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.32 | 0.06 | 56353.86 | 8.02 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.4 | 0.61 | 0.07 | 173867.66 | 35.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
