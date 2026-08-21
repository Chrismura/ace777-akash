# Hulk DIGEST — 2026-08-21T22:53:04Z

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
| PYTHUSDT | IDLE | 1.37 | 5.26 | 0.02 | 0.11 | 5898821.45 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 6.52 | 0.1 | 0.15 | 136248294.57 | 0.69 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 7.44 | 0.12 | 0.14 | 660638.22 | 9.7 | skipped_fast |
| HBARUSDT | IDLE | 2.16 | 4.73 | 0.03 | 0.08 | 876266.88 | 2.51 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 9.13 | 0.0 | 0.15 | 508168.53 | 34.52 | skipped_fast |
| WUSDT | IDLE | 2.63 | 6.48 | 0.13 | 0.09 | 371374.69 | 10.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.54 | 4.54 | 2.41 | 0.05 | 541641.42 | 12.33 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.92 | 0.04 | 187826.19 | 3.1 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.9 | 0.18 | 157342.35 | 13.73 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.22 | -0.03 | 82568.5 | 21.86 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.82 | 0.06 | 186810.14 | 20.7 | skipped_fast |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3896.16 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.9 | 0.11 | 61332.94 | 12.89 | skipped_fast |
| QNTUSDT | IDLE | 2.29 | 4.59 | 0.0 | 0.06 | 88189.79 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.94 | 0.06 | 56408.96 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.92 | 1.83 | 0.08 | 0.04 | 54071.09 | 16.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 14.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
