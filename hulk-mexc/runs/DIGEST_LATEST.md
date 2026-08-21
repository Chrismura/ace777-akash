# Hulk DIGEST — 2026-08-21T21:58:50Z

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
| PYTHUSDT | IDLE | 1.22 | 4.74 | 0.29 | 0.1 | 5687654.89 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.56 | 0.12 | 129724849.88 | 2.13 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 4.71 | 0.64 | 0.08 | 834185.03 | 1.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.87 | 5.61 | 3.49 | 0.05 | 527069.91 | 3.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.91 | 8.19 | 2.48 | 0.11 | 493192.51 | 22.8 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 3.92 | 0.05 | 0.11 | 635855.71 | 8.2 | skipped_fast |
| WUSDT | IDLE | 2.1 | 4.19 | 0.1 | 0.07 | 367632.47 | 17.65 | skipped_fast |
| BIOUSDT | IDLE | 2.36 | 5.2 | 1.11 | 0.03 | 186124.8 | 6.21 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.38 | 0.19 | 153851.78 | 8.92 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 4.12 | 0.77 | -0.04 | 83297.29 | 22.3 | skipped_fast |
| TELUSDT | IDLE | 2.55 | 6.45 | 1.28 | 0.05 | 191579.08 | 31.19 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.9 | 0.03 | 10238.87 | 53.39 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.08 | 0.11 | 61243.53 | 11.01 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 11.42 | 1.98 | 0.04 | 56508.15 | 222.15 | skipped_fast |
| QNTUSDT | IDLE | 1.34 | 2.65 | 0.17 | 0.05 | 62420.8 | 3.08 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.33 | 0.08 | 0.04 | 54127.3 | 8.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
