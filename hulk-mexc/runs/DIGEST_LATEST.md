# Hulk DIGEST — 2026-10-11T13:16:20Z

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
| XRPUSDT | IDLE | 0.35 | 0.66 | 0.23 | -0.01 | 10135272.59 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.16 | 0.0 | 178413738.14 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.34 | 0.19 | 0.0 | 123302321.38 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.89 | 2.42 | 0.95 | 0.01 | 1137736.94 | 5.72 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 31.62 | 16.77 | 0.05 | 56477.96 | 20.84 | skipped_fast |
| QNTUSDT | IDLE | 1.9 | 3.75 | 0.3 | -0.03 | 1042625.15 | 1.23 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.53 | 1.81 | -0.02 | 710971.96 | 2.61 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 3.5 | 2.52 | 0.0 | 371233.72 | 5.17 | skipped_fast |
| CCUSDT | IDLE | 1.86 | 3.66 | 0.41 | 0.03 | 289438.38 | 8.1 | skipped_fast |
| CHIPUSDT | IDLE | 0.88 | 8.41 | 1.93 | 0.3 | 373326.46 | 16.33 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.5 | 6.22 | 5.41 | -0.07 | 145251.36 | 23.58 | skipped_fast |
| RIZEUSDT | IDLE | 2.37 | 6.58 | 2.78 | -0.07 | 35356.05 | 36.21 | skipped_fast |
| BIOUSDT | IDLE | 1.58 | 2.99 | 1.1 | 0.03 | 78124.05 | 6.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.31 | 0.25 | 0.0 | 159353.14 | 18.73 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 2.2 | 1.09 | -0.01 | 58195.25 | 15.42 | skipped_fast |
| RWAINCUSDT | IDLE | 0.93 | 1.67 | 1.3 | -0.03 | 19109.27 | 5.05 | skipped_fast |
| KITEUSDT | IDLE | 0.68 | 1.24 | 0.75 | -0.03 | 74742.14 | 8.73 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.65 | 0.52 | -0.01 | 225446.53 | 3.27 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.87 | 0.08 | -0.0 | 52600.2 | 15.75 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.73 | 0.11 | -0.01 | 32206.9 | 41.06 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
