# Hulk DIGEST — 2026-08-21T23:27:01Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.42 | 0.11 | 6069118.15 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.93 | 8.23 | 0.42 | 0.15 | 140223380.34 | 2.04 | skipped_fast |
| HBARUSDT | IDLE | 2.57 | 6.29 | 0.35 | 0.09 | 900386.74 | 1.24 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 11.25 | 1.07 | 0.14 | 512882.66 | 33.28 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 0.96 | 0.13 | 643415.32 | 4.44 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.36 | 0.08 | 378031.95 | 11.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 1.0 | 0.04 | 547976.22 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.8 | 0.02 | 187657.47 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82503.49 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.16 | 9.82 | 3.3 | 0.15 | 58921.26 | 45.4 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.21 | 0.07 | 184977.7 | 20.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.83 | 0.18 | 157552.08 | 7.27 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.63 | 0.01 | 0.07 | 119338.92 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.11 | 0.09 | 61385.5 | 12.98 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54452.98 | 40.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
