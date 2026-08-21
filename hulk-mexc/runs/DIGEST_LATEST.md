# Hulk DIGEST — 2026-08-21T23:10:37Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.4 | 0.12 | 5991807.91 | 2.02 | skipped_fast |
| XRPUSDT | IDLE | 1.75 | 6.77 | 0.33 | 0.15 | 138505616.7 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.9 | 0.13 | 666456.69 | 8.88 | skipped_fast |
| HBARUSDT | IDLE | 2.39 | 5.24 | 0.08 | 0.09 | 890331.28 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 10.14 | 0.31 | 0.15 | 511402.69 | 30.51 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.4 | 0.08 | 374871.8 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 0.91 | 0.05 | 544757.36 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.31 | 5.04 | 1.41 | 0.02 | 187393.65 | 3.12 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82514.69 | 21.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10220.57 | 16.16 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.33 | 0.18 | 157388.3 | 18.69 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.31 | 0.07 | 184994.27 | 46.36 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.01 | 0.07 | 105778.29 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.14 | 0.09 | 61564.03 | 11.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 6.21 | 0.47 | 0.09 | 57925.66 | 67.49 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.25 | 0.04 | 54402.8 | 8.2 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 21.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
