# Hulk DIGEST — 2026-09-03T01:06:46Z

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
| ETHUSDT | IDLE | 0.67 | 1.23 | 0.73 | -0.01 | 348964013.02 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.64 | 1.19 | 0.6 | 0.01 | 35771598.1 | 0.74 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.7 | 0.42 | -0.0 | 496046664.69 | 0.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 3.55 | 2.81 | 0.05 | 1346000.19 | 1.76 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 3.89 | 2.24 | -0.04 | 921348.33 | 4.76 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 25.63 | 14.46 | 0.15 | 56051.21 | 157.37 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.52 | 2.21 | -0.05 | 414437.26 | 9.2 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 7.78 | 4.95 | -0.01 | 140346.25 | 26.44 | skipped_fast |
| BIOUSDT | IDLE | 2.22 | 4.26 | 1.26 | 0.01 | 70897.94 | 3.87 | skipped_fast |
| WUSDT | IDLE | 1.52 | 2.83 | 1.45 | 0.02 | 221866.19 | 17.46 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 4.69 | 3.74 | 0.11 | 141322.65 | 13.02 | skipped_fast |
| REDUSDT | IDLE | 1.84 | 3.65 | 0.25 | 0.04 | 113319.28 | 59.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.09 | 2.34 | 2.15 | -0.02 | 180520.55 | 18.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 5.45 | 0.0 | 0.13 | 12319.52 | 52.03 | skipped_fast |
| HBARUSDT | IDLE | 0.68 | 1.31 | 0.33 | 0.02 | 192899.62 | 2.68 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 1.7 | 0.46 | 0.01 | 60747.21 | 6.22 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.77 | 1.21 | 0.0 | 51457.11 | 22.98 | skipped_fast |
| TELUSDT | IDLE | 0.85 | 1.6 | 0.64 | 0.04 | 73908.09 | 46.78 | skipped_fast |
| FLUIDUSDT | IDLE | 0.09 | 0.18 | 0.0 | -0.02 | 2252.11 | 21.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.0 | 18777.29 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
