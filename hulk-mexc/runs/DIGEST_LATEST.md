# Hulk DIGEST — 2026-08-21T22:57:48Z

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
| PYTHUSDT | IDLE | 1.51 | 5.77 | 0.12 | 0.12 | 5922228.25 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 6.54 | 0.2 | 0.15 | 137015471.94 | 4.14 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.47 | 0.23 | 0.14 | 661735.31 | 7.94 | skipped_fast |
| HBARUSDT | IDLE | 2.22 | 5.03 | 0.13 | 0.09 | 877556.52 | 1.26 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 9.94 | 0.0 | 0.16 | 508299.21 | 13.33 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.91 | 0.18 | 0.09 | 372963.74 | 14.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.11 | 0.05 | 542911.37 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.8 | 0.03 | 187767.77 | 3.1 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.53 | 0.19 | 157223.11 | 19.32 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.03 | 82553.51 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10217.99 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.05 | 186688.27 | 10.36 | skipped_fast |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3896.16 | 63.29 | skipped_fast |
| QNTUSDT | IDLE | 2.46 | 4.91 | 0.0 | 0.07 | 88622.33 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 1.07 | 0.1 | 61317.15 | 10.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 2.01 | 0.06 | 56402.51 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.92 | 0.08 | 0.04 | 54116.09 | 24.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
