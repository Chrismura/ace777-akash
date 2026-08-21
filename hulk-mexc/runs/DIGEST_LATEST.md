# Hulk DIGEST — 2026-08-21T22:55:10Z

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
| PYTHUSDT | IDLE | 1.45 | 5.54 | 0.04 | 0.11 | 5909439.94 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 6.54 | 0.14 | 0.15 | 136778914.83 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 7.44 | 0.02 | 0.15 | 660279.86 | 7.92 | skipped_fast |
| HBARUSDT | IDLE | 2.16 | 4.74 | 0.0 | 0.08 | 876693.55 | 2.52 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.2 | 9.48 | 0.0 | 0.15 | 508355.89 | 14.82 | skipped_fast |
| WUSDT | IDLE | 2.65 | 6.77 | 0.0 | 0.09 | 372259.45 | 6.07 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 4.54 | 2.29 | 0.05 | 541743.12 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.83 | 0.03 | 187756.25 | 6.22 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.71 | 0.19 | 157347.08 | 12.07 | skipped_fast |
| EDELUSDT | IDLE | 2.3 | 5.04 | 0.33 | -0.03 | 82593.53 | 21.86 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10244.46 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.06 | 186746.48 | 20.7 | skipped_fast |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3896.16 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.98 | 0.11 | 61288.72 | 9.21 | skipped_fast |
| QNTUSDT | IDLE | 2.39 | 4.78 | 0.0 | 0.07 | 88316.45 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.94 | 0.06 | 56408.54 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.92 | 0.16 | 0.04 | 54125.53 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 4.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
