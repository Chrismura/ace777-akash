# Hulk DIGEST — 2026-09-10T21:14:58Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.9 | 1.71 | 0.54 | -0.0 | 443614308.21 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.88 | 1.66 | 0.67 | -0.03 | 44150763.4 | 1.48 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.93 | 0.35 | -0.01 | 541703140.27 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.36 | 0.34 | -0.04 | 692966.88 | 3.84 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.7 | 1.39 | -0.05 | 512362.92 | 5.04 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.13 | 8.58 | 1.15 | -0.09 | 90205.86 | 16.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 3.52 | 2.24 | -0.0 | 200726.11 | 6.55 | skipped_fast |
| WUSDT | IDLE | 1.61 | 3.07 | 0.97 | -0.04 | 189335.64 | 8.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.51 | 28.21 | 4.58 | -0.5 | 126244.98 | 91.98 | skipped_fast |
| EDELUSDT | IDLE | 0.8 | 4.65 | 1.87 | 0.09 | 262913.69 | 36.23 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 2.7 | 1.84 | -0.06 | 79688.96 | 3.99 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.54 | 1.55 | -0.04 | 57342.22 | 12.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.38 | 1.88 | -0.02 | 4956.12 | 22.54 | skipped_fast |
| REDUSDT | IDLE | 0.66 | 1.48 | 0.36 | -0.06 | 67579.49 | 18.93 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.73 | 0.07 | -0.02 | 244094.33 | 1.32 | skipped_fast |
| QNTUSDT | IDLE | 1.14 | 2.03 | 1.69 | -0.02 | 36787.92 | 4.59 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 1.92 | 0.67 | -0.02 | 83675.55 | 39.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 1.84 | 1.81 | -0.06 | 1786.37 | 22.22 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.76 | 0.45 | -0.03 | 51539.69 | 15.17 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.62 | 0.0 | -0.02 | 32273.51 | 5.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
