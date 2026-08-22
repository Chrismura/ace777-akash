# Hulk DIGEST — 2026-08-22T00:12:05Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.84 | 0.1 | 6294801.8 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.08 | 8.23 | 2.98 | 0.13 | 143349874.61 | 4.19 | skipped_fast |
| HBARUSDT | IDLE | 2.83 | 6.36 | 2.08 | 0.07 | 912763.02 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 3.09 | 0.11 | 515606.32 | 24.27 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 7.42 | 1.9 | 0.12 | 645320.26 | 8.97 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.1 | 0.08 | 381099.66 | 5.11 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.88 | 0.04 | 545112.8 | 6.14 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.51 | 0.02 | 187161.11 | 3.12 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 5.5 | 1.52 | 0.0 | 79899.2 | 11.02 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.45 | 0.13 | 59052.45 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.88 | 6.89 | 1.23 | 0.05 | 190400.92 | 36.24 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 4.91 | 2.82 | 0.19 | 157609.7 | 12.15 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.93 | 0.09 | 61472.58 | 11.1 | skipped_fast |
| QNTUSDT | IDLE | 2.63 | 5.42 | 2.45 | 0.05 | 166920.91 | 113.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.32 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54694.34 | 32.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
