# Hulk DIGEST — 2026-10-18T00:24:24Z

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
| ETHUSDT | IDLE | 1.46 | 2.79 | 0.89 | -0.01 | 89076213.08 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.44 | 2.74 | 0.87 | -0.01 | 17102176.44 | 1.54 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 9.68 | 5.99 | -0.08 | 1055400.06 | 2.52 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 1.06 | 0.23 | -0.0 | 169122232.19 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.89 | 5.68 | 2.82 | -0.04 | 1002602.87 | 16.6 | skipped_fast |
| QNTUSDT | IDLE | 2.83 | 5.23 | 2.84 | -0.03 | 600211.27 | 1.54 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 9.07 | 6.82 | -0.09 | 162502.74 | 116.3 | skipped_fast |
| CCUSDT | IDLE | 1.51 | 2.74 | 1.84 | -0.0 | 260458.16 | 5.81 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 4.41 | 1.3 | -0.03 | 71655.57 | 8.22 | skipped_fast |
| CHIPUSDT | IDLE | 2.06 | 5.85 | 2.39 | -0.07 | 84290.79 | 13.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 2.79 | 1.26 | -0.03 | 186492.49 | 15.33 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 3.41 | 1.89 | -0.05 | 61229.8 | 9.37 | skipped_fast |
| HBARUSDT | IDLE | 2.02 | 4.01 | 0.19 | 0.03 | 264611.79 | 5.83 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 3.83 | 1.85 | -0.04 | 69508.39 | 18.95 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 3.53 | 2.48 | 0.05 | 20760.5 | 10.6 | skipped_fast |
| TELUSDT | IDLE | 2.03 | 3.59 | 3.11 | -0.06 | 102320.15 | 24.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.22 | 2.28 | 1.08 | -0.02 | 50452.14 | 58.86 | skipped_fast |
| RWAUSDT | IDLE | 1.34 | 2.52 | 1.03 | -0.01 | 51506.56 | 16.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.42 | 2.69 | 0.97 | -0.01 | 1804.21 | 20.17 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.58 | 0.55 | -0.0 | 30851.6 | 8.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
