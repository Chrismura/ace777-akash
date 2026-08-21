# Hulk DIGEST — 2026-08-21T23:31:15Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.73 | 0.11 | 6088923.7 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.49 | 0.15 | 140506961.95 | 2.73 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 11.25 | 1.2 | 0.13 | 512878.21 | 18.13 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.29 | 0.51 | 0.09 | 903078.28 | 1.25 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.03 | 0.13 | 645367.12 | 8.01 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.91 | 1.09 | 0.08 | 379019.4 | 10.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.28 | 0.04 | 550041.47 | 6.16 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.04 | 0.55 | 0.03 | 187056.73 | 3.09 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.54 | -0.03 | 82472.47 | 21.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 9.82 | 3.53 | 0.13 | 58882.97 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.69 | 6.62 | 0.05 | 0.07 | 186589.31 | 20.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.01 | 10152.37 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.18 | 0.18 | 157785.4 | 19.48 | skipped_fast |
| QNTUSDT | IDLE | 2.58 | 5.67 | 0.0 | 0.07 | 120135.78 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.11 | 0.09 | 61394.87 | 11.12 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54537.64 | 24.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 23.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
