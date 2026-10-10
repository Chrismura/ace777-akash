# Hulk DIGEST — 2026-10-10T20:58:04Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 8.29 | 5.81 | 0.03 | 1252147.7 | 6.16 | skipped_fast |
| ETHUSDT | IDLE | 0.31 | 0.58 | 0.32 | 0.01 | 102104424.5 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.26 | 0.51 | 0.06 | 0.01 | 13230082.45 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.24 | 0.13 | 0.01 | 170387161.26 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 4.33 | 3.49 | -0.01 | 1227030.58 | 2.91 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.65 | 31.32 | 0.93 | 0.32 | 196020.9 | 10.43 | skipped_fast |
| PYTHUSDT | IDLE | 1.16 | 2.26 | 0.44 | -0.02 | 783638.96 | 1.26 | skipped_fast |
| EDELUSDT | IDLE | 1.81 | 3.92 | 0.97 | -0.03 | 224196.25 | 5.14 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.54 | 1.46 | -0.01 | 299814.54 | 6.71 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 3.13 | 0.37 | 0.06 | 87955.44 | 3.38 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 3.41 | 3.06 | 0.07 | 71479.86 | 8.59 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 4.24 | 2.18 | -0.04 | 9632.44 | 78.9 | skipped_fast |
| ZBCNUSDT | IDLE | 0.64 | 1.21 | 0.45 | 0.02 | 203920.92 | 23.02 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 2.28 | 1.88 | -0.02 | 36696.16 | 50.45 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 3.63 | 0.49 | -0.0 | 135379.82 | 27.53 | skipped_fast |
| REDUSDT | IDLE | 0.64 | 1.18 | 0.65 | 0.03 | 54159.11 | 15.92 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.16 | 0.55 | 0.02 | 316063.34 | 4.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.29 | 2.45 | 0.87 | 0.0 | 8531.47 | 26.88 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.79 | 0.7 | 0.01 | 53941.46 | 7.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.78 | 0.16 | 0.0 | 37108.02 | 65.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
