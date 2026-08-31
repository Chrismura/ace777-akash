# Hulk DIGEST — 2026-08-31T05:08:49Z

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
| XRPUSDT | IDLE | 1.26 | 2.34 | 1.19 | -0.03 | 35416753.76 | 2.95 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.6 | 0.82 | -0.02 | 386590561.97 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.01 | 0.71 | -0.01 | 406607881.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.81 | 4.25 | 2.61 | -0.03 | 555082.51 | 2.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 3.27 | 0.84 | -0.04 | 493457.11 | 2.58 | skipped_fast |
| WUSDT | IDLE | 2.37 | 4.76 | 0.44 | 0.02 | 224182.15 | 13.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.77 | 5.3 | 4.22 | -0.09 | 228982.01 | 27.9 | skipped_fast |
| CCUSDT | IDLE | 1.75 | 3.45 | 0.36 | -0.01 | 204452.98 | 6.74 | skipped_fast |
| KITEUSDT | IDLE | 1.93 | 5.78 | 0.0 | -0.04 | 90223.54 | 13.0 | skipped_fast |
| EDELUSDT | IDLE | 2.22 | 4.27 | 2.78 | 0.05 | 90215.1 | 50.42 | skipped_fast |
| REDUSDT | IDLE | 1.8 | 3.32 | 1.93 | -0.02 | 61835.08 | 12.92 | skipped_fast |
| BIOUSDT | IDLE | 1.1 | 2.15 | 0.45 | -0.04 | 86986.39 | 7.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.97 | 2.89 | -0.01 | 2255.56 | 96.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 2.01 | 1.9 | -0.04 | 37417.87 | 60.75 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.41 | 0.49 | -0.01 | 208853.32 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 0.65 | 1.24 | 0.35 | -0.02 | 40599.58 | 4.97 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.81 | 0.4 | 0.02 | 52766.21 | 16.23 | skipped_fast |
| TELUSDT | IDLE | 0.56 | 1.02 | 0.65 | -0.01 | 83463.19 | 71.43 | skipped_fast |
| FLUIDUSDT | IDLE | 0.46 | 0.91 | 0.0 | -0.02 | 3849.88 | 21.4 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.68 | 0.4 | -0.01 | 30098.04 | 59.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
