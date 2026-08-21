# Hulk DIGEST — 2026-08-21T23:25:09Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.4 | 0.12 | 6061938.51 | 2.02 | skipped_fast |
| XRPUSDT | IDLE | 1.93 | 8.23 | 0.26 | 0.16 | 140240429.69 | 4.76 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 11.25 | 1.15 | 0.14 | 512856.08 | 24.27 | skipped_fast |
| HBARUSDT | IDLE | 2.56 | 6.29 | 0.28 | 0.1 | 900196.4 | 1.24 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.06 | 0.13 | 644572.65 | 8.9 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.39 | 0.08 | 378003.37 | 11.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.34 | 0.05 | 548036.01 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.05 | 0.02 | 187688.33 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82561.65 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 9.82 | 3.53 | 0.1 | 59484.88 | 45.4 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.1 | 0.07 | 184987.45 | 20.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.75 | 0.19 | 157501.3 | 12.92 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.51 | 0.0 | 0.07 | 119224.33 | 1.5 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.09 | 61417.45 | 12.04 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54511.01 | 8.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
