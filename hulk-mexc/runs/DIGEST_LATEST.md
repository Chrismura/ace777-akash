# Hulk DIGEST — 2026-09-17T07:15:37Z

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
| ETHUSDT | IDLE | 0.8 | 1.56 | 0.23 | 0.02 | 390696651.51 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.58 | 1.11 | 0.34 | 0.01 | 55026595.94 | 2.3 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.78 | 0.18 | 0.01 | 503492357.97 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.06 | 3.9 | 1.53 | 0.02 | 530331.91 | 3.69 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.69 | 10.83 | 6.58 | -0.06 | 221875.95 | 48.23 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 3.66 | 0.19 | 0.09 | 585121.1 | 7.04 | skipped_fast |
| ZBCNUSDT | IDLE | 2.25 | 4.35 | 1.0 | 0.02 | 171844.13 | 2.86 | skipped_fast |
| WUSDT | IDLE | 1.23 | 2.35 | 0.76 | 0.03 | 225783.26 | 14.11 | skipped_fast |
| RIZEUSDT | IDLE | 1.29 | 13.22 | 8.44 | -0.09 | 61549.16 | 109.4 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.74 | 0.44 | 0.08 | 67090.39 | 11.96 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 3.14 | 0.67 | -0.01 | 74858.48 | 16.26 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.21 | 1.15 | -0.01 | 61403.97 | 1.53 | skipped_fast |
| BIOUSDT | IDLE | 0.66 | 1.24 | 0.51 | 0.02 | 71657.53 | 11.87 | skipped_fast |
| HBARUSDT | IDLE | 0.64 | 1.21 | 0.51 | -0.01 | 314966.29 | 1.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.74 | 1.4 | 0.52 | -0.01 | 16245.55 | 23.2 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 1.53 | 1.03 | -0.03 | 115072.98 | 41.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.22 | 0.17 | 0.01 | 36099.45 | 9.82 | skipped_fast |
| QNTUSDT | IDLE | 0.49 | 0.91 | 0.41 | 0.01 | 36357.61 | 8.24 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.98 | 0.3 | 0.02 | 56260.16 | 29.9 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1571.52 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
