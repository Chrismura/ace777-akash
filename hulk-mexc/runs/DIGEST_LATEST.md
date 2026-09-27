# Hulk DIGEST — 2026-09-27T20:12:36Z

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
| PYTHUSDT | IDLE | 1.53 | 4.98 | 0.85 | 0.09 | 2241958.84 | 4.66 | skipped_fast |
| WUSDT | IDLE | 1.31 | 8.22 | 0.49 | 0.22 | 4407572.58 | 8.27 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 16.37 | 2.96 | 0.56 | 6563756.06 | 8.53 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 2.11 | 0.43 | 0.01 | 41813110.39 | 1.95 | skipped_fast |
| ETHUSDT | IDLE | 0.34 | 0.65 | 0.16 | 0.0 | 201111837.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.6 | 0.06 | 0.01 | 435438935.3 | 0.0 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 42.2 | 17.2 | 0.15 | 28415.53 | 50.78 | skipped_fast |
| CCUSDT | IDLE | 2.67 | 5.22 | 0.81 | 0.02 | 609899.78 | 7.98 | skipped_fast |
| RIZEUSDT | IDLE | 2.3 | 15.37 | 12.58 | -0.16 | 47171.51 | 41.27 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 2.7 | 0.09 | 0.03 | 729135.87 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 10.45 | 8.55 | -0.14 | 138006.01 | 69.44 | skipped_fast |
| KITEUSDT | IDLE | 1.98 | 4.47 | 0.99 | 0.03 | 140106.62 | 9.18 | skipped_fast |
| REDUSDT | IDLE | 1.69 | 3.22 | 1.09 | 0.02 | 65466.85 | 12.81 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 2.35 | 0.35 | 0.01 | 201203.05 | 27.68 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.8 | 0.13 | -0.01 | 88488.16 | 9.4 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 2.45 | 0.42 | -0.04 | 99908.08 | 16.86 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 3.83 | 2.85 | 0.13 | 166193.95 | 21.72 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 2.5 | 0.9 | 0.04 | 2321.19 | 22.22 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.64 | 0.49 | 0.01 | 57426.89 | 7.07 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.39 | 0.14 | 0.01 | 40107.6 | 17.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
