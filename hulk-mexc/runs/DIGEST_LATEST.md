# Hulk DIGEST — 2026-08-22T02:55:13Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.62 | 11.02 | 0.49 | 0.16 | 7329059.7 | 3.79 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.53 | 13.33 | 0.28 | 0.2 | 158868477.91 | 4.51 | skipped_fast |
| HBARUSDT | IDLE | 2.57 | 6.7 | 0.02 | 0.1 | 989820.32 | 1.22 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 9.53 | 0.04 | 0.18 | 662598.53 | 7.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 9.63 | 2.72 | 0.1 | 541306.86 | 26.6 | skipped_fast |
| CHIPUSDT | IDLE | 2.52 | 5.8 | 0.21 | -0.01 | 451341.55 | 2.98 | skipped_fast |
| BIOUSDT | IDLE | 3.21 | 8.18 | 2.17 | 0.08 | 194233.53 | 3.0 | skipped_fast |
| WUSDT | IDLE | 2.05 | 6.23 | 0.22 | 0.11 | 415570.79 | 12.91 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 5.02 | 2.39 | -0.03 | 79904.1 | 22.25 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.44 | 0.1 | 61384.36 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.94 | 0.2 | 157853.05 | 10.4 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9385.21 | 5.43 | skipped_fast |
| QNTUSDT | IDLE | 2.33 | 5.48 | 0.12 | 0.09 | 172672.29 | 4.46 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.25 | 0.12 | 62421.7 | 11.66 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 0.97 | 0.06 | 173942.5 | 61.98 | skipped_fast |
| RWAUSDT | IDLE | 1.67 | 3.33 | 0.08 | 0.05 | 56200.68 | 24.26 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 43.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
