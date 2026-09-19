# Hulk DIGEST — 2026-09-19T08:01:29Z

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
| XRPUSDT | IDLE | 1.07 | 2.18 | 1.98 | 0.06 | 69831813.48 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.47 | 0.89 | 0.33 | 0.06 | 596358548.24 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 0.32 | 0.59 | 0.32 | 0.04 | 672452414.05 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.71 | 4.8 | 4.18 | -0.01 | 699459.11 | 1.68 | skipped_fast |
| WUSDT | IDLE | 1.11 | 3.23 | 2.09 | 0.05 | 968180.11 | 8.34 | skipped_fast |
| CCUSDT | IDLE | 2.21 | 3.87 | 3.64 | -0.01 | 457281.49 | 9.12 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 7.21 | 5.38 | 0.05 | 149606.24 | 22.21 | skipped_fast |
| EDELUSDT | IDLE | 1.73 | 7.59 | 5.69 | -0.08 | 189306.52 | 42.16 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.04 | 2.0 | 0.02 | 625726.48 | 1.28 | skipped_fast |
| RIZEUSDT | IDLE | 2.02 | 16.62 | 10.2 | -0.07 | 41846.36 | 101.01 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 2.73 | 2.22 | 0.01 | 82478.65 | 11.16 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 3.22 | 0.45 | 0.06 | 70086.13 | 12.09 | skipped_fast |
| REDUSDT | IDLE | 0.89 | 4.53 | 2.38 | 0.07 | 117606.13 | 6.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 1.95 | 0.41 | 0.02 | 190681.76 | 26.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.62 | 1.21 | 0.17 | 0.04 | 5360.43 | 28.38 | skipped_fast |
| TELUSDT | IDLE | 0.73 | 3.03 | 2.01 | 0.09 | 132078.36 | 38.39 | skipped_fast |
| QNTUSDT | IDLE | 0.73 | 1.38 | 0.47 | 0.01 | 74519.79 | 6.29 | skipped_fast |
| RWAUSDT | IDLE | 0.92 | 1.71 | 0.88 | 0.0 | 56146.45 | 29.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.56 | 2.29 | 1.86 | 0.16 | 5401.67 | 21.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.55 | 0.29 | 0.04 | 40728.91 | 22.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
