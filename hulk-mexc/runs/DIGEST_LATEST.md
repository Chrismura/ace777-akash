# Hulk DIGEST — 2026-08-22T02:58:49Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.63 | 11.02 | 0.91 | 0.14 | 7376923.8 | 3.81 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.54 | 13.33 | 0.38 | 0.2 | 159417420.13 | 3.87 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.73 | 0.11 | 0.1 | 990304.48 | 1.22 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.12 | 9.96 | 0.05 | 0.18 | 663857.49 | 7.56 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.81 | 0.11 | 541431.04 | 18.37 | skipped_fast |
| CHIPUSDT | IDLE | 2.58 | 5.95 | 0.09 | -0.0 | 450493.77 | 2.97 | skipped_fast |
| BIOUSDT | IDLE | 3.2 | 8.18 | 2.08 | 0.08 | 194352.92 | 3.0 | skipped_fast |
| WUSDT | IDLE | 2.05 | 6.33 | 0.03 | 0.12 | 415845.51 | 12.85 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 5.02 | 2.28 | -0.03 | 79879.02 | 33.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.37 | 0.1 | 61397.04 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.55 | 0.2 | 158017.19 | 18.33 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9385.21 | 10.86 | skipped_fast |
| QNTUSDT | IDLE | 2.33 | 5.48 | 0.15 | 0.09 | 172647.06 | 4.46 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.1 | 0.12 | 62385.0 | 11.63 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.28 | 0.06 | 173469.4 | 56.83 | skipped_fast |
| RWAUSDT | IDLE | 1.68 | 3.33 | 0.24 | 0.05 | 56261.79 | 24.26 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
