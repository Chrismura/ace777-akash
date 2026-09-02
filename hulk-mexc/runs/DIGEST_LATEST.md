# Hulk DIGEST — 2026-09-02T11:40:19Z

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
| XRPUSDT | IDLE | 1.78 | 3.25 | 2.1 | -0.04 | 40306178.46 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 1.67 | 3.04 | 1.96 | -0.03 | 407600100.77 | 1.18 | skipped_fast |
| BTCUSDT | IDLE | 1.07 | 1.94 | 1.32 | -0.02 | 528373673.85 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 8.6 | 5.52 | 0.13 | 981258.37 | 4.53 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 5.35 | 3.5 | 0.07 | 869676.74 | 9.21 | skipped_fast |
| WUSDT | IDLE | 2.37 | 4.28 | 3.03 | -0.01 | 407916.64 | 12.61 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.69 | 14.74 | 7.54 | 0.03 | 171177.29 | 33.25 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.6 | 1.79 | -0.06 | 355678.19 | 9.79 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.62 | 8.17 | 0.9 | 0.09 | 10833.75 | 21.29 | skipped_fast |
| QNTUSDT | IDLE | 3.17 | 6.19 | 4.45 | 0.04 | 70645.11 | 4.68 | skipped_fast |
| RIZEUSDT | IDLE | 2.1 | 7.95 | 6.51 | -0.12 | 40350.52 | 82.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 2.04 | 1.56 | -0.03 | 234475.37 | 20.4 | skipped_fast |
| BIOUSDT | IDLE | 1.54 | 2.8 | 1.83 | -0.04 | 76445.65 | 3.97 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 4.2 | 2.93 | 0.11 | 82721.7 | 9.74 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 2.39 | 0.37 | 0.03 | 152910.31 | 9.78 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 1.99 | 1.21 | -0.02 | 242924.47 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.02 | 2.34 | -0.03 | 85631.04 | 47.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.52 | 1.49 | -0.04 | 328.21 | 18.91 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.77 | 0.54 | -0.0 | 50572.6 | 7.7 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.75 | 0.62 | -0.02 | 36128.79 | 22.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
