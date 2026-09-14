# Hulk DIGEST — 2026-09-14T17:43:01Z

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
| XRPUSDT | IDLE | 1.66 | 3.32 | 0.0 | 0.05 | 47988024.15 | 2.1 | skipped_fast |
| ETHUSDT | IDLE | 1.03 | 1.99 | 0.49 | 0.01 | 350284354.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.98 | 1.94 | 0.2 | 0.02 | 487323450.21 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.98 | 3.95 | 0.04 | 0.01 | 468212.71 | 3.54 | skipped_fast |
| REDUSDT | IDLE | 2.49 | 8.59 | 6.19 | 0.06 | 182456.98 | 16.6 | skipped_fast |
| EDELUSDT | IDLE | 1.53 | 6.1 | 4.82 | 0.09 | 262853.57 | 27.8 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 19.21 | 11.57 | 0.05 | 69723.05 | 103.92 | skipped_fast |
| CHIPUSDT | IDLE | 2.16 | 4.25 | 2.28 | -0.04 | 88527.29 | 19.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 2.8 | 1.02 | -0.0 | 206247.21 | 16.79 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 2.13 | 0.68 | 0.01 | 287575.29 | 19.62 | skipped_fast |
| WUSDT | IDLE | 1.26 | 2.43 | 0.56 | -0.01 | 223565.84 | 13.03 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.26 | 0.7 | 0.0 | 86154.02 | 3.9 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.84 | 1.03 | 0.04 | 10451.59 | 5.47 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.17 | 0.65 | -0.01 | 61407.29 | 14.12 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.27 | 0.72 | 0.02 | 291967.24 | 1.29 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 1.77 | 0.74 | -0.01 | 40985.96 | 6.21 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.95 | 0.68 | 0.01 | 90695.44 | 62.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.9 | 1.79 | 0.0 | 0.02 | 676.15 | 21.79 | skipped_fast |
| MNSRYUSDT | IDLE | 0.52 | 1.01 | 0.18 | 0.0 | 28938.84 | 31.91 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.22 | 0.0 | 55134.82 | 29.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
