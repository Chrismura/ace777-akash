# Hulk DIGEST — 2026-09-22T14:11:49Z

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
| XRPUSDT | IDLE | 2.56 | 4.93 | 1.21 | 0.06 | 113374623.62 | 2.54 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 20.05 | 7.35 | 0.06 | 1130615.24 | 30.72 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.21 | 0.38 | 0.01 | 539311929.71 | 0.44 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.89 | 0.15 | 0.01 | 955322794.23 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.37 | 4.85 | 0.04 | 0.07 | 1196670.77 | 6.16 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 3.68 | 2.05 | 0.02 | 541578.78 | 5.97 | skipped_fast |
| QNTUSDT | IDLE | 3.45 | 11.12 | 2.53 | 0.08 | 179911.14 | 12.37 | skipped_fast |
| EDELUSDT | IDLE | 2.22 | 9.22 | 5.9 | 0.11 | 253339.76 | 84.52 | skipped_fast |
| WUSDT | IDLE | 1.51 | 2.89 | 0.8 | 0.0 | 371975.8 | 5.02 | skipped_fast |
| CHIPUSDT | IDLE | 2.43 | 4.42 | 2.95 | -0.01 | 159623.08 | 17.33 | skipped_fast |
| RIZEUSDT | IDLE | 2.05 | 24.12 | 7.68 | -0.2 | 49417.37 | 122.76 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 6.66 | 2.28 | 0.11 | 115851.41 | 8.28 | skipped_fast |
| ZBCNUSDT | IDLE | 1.53 | 2.87 | 1.2 | -0.01 | 265997.28 | 28.99 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 3.74 | 2.27 | 0.01 | 67161.04 | 13.52 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.78 | 0.27 | 0.0 | 117055.26 | 6.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.15 | 2.18 | 0.82 | 0.04 | 27035.28 | 27.59 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 4.24 | 0.18 | 0.04 | 109399.74 | 29.95 | skipped_fast |
| FLUIDUSDT | IDLE | 1.04 | 2.07 | 0.13 | 0.03 | 8841.72 | 19.73 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.95 | 0.58 | -0.0 | 55083.81 | 43.73 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.4 | 0.08 | 0.0 | 40007.27 | 6.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
