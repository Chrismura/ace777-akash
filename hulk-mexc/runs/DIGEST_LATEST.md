# Hulk DIGEST — 2026-08-21T23:27:46Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.65 | 0.11 | 6071113.4 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.64 | 0.15 | 140249877.76 | 3.41 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.29 | 0.47 | 0.09 | 901218.55 | 3.74 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 11.25 | 1.14 | 0.14 | 512908.86 | 34.25 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.85 | 0.13 | 643415.32 | 7.11 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.31 | 0.08 | 378090.76 | 12.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.22 | 0.04 | 547965.52 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.74 | 0.02 | 187624.72 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82465.48 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.16 | 9.82 | 3.3 | 0.15 | 58921.26 | 23.57 | skipped_fast |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.21 | 0.07 | 185437.79 | 15.4 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.11 | 0.18 | 157552.08 | 11.35 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10164.7 | 32.38 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 5.63 | 0.04 | 0.07 | 119420.78 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.09 | 61385.5 | 12.98 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54467.25 | 40.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
