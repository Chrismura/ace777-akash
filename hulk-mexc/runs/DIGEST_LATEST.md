# Hulk DIGEST — 2026-09-27T09:06:44Z

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
| WUSDT | IDLE | 2.18 | 12.47 | 2.44 | 0.19 | 2220196.99 | 8.58 | skipped_fast |
| PYTHUSDT | IDLE | 2.28 | 9.68 | 4.67 | 0.12 | 1919828.01 | 8.28 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 15.7 | 7.53 | 0.73 | 5003380.46 | 8.93 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 2.43 | 0.73 | -0.01 | 41636003.28 | 1.31 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.3 | 0.55 | 0.01 | 150759815.22 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.66 | 0.21 | 0.01 | 375033299.22 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 16.11 | 11.57 | -0.01 | 50667.36 | 61.87 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 3.18 | 1.1 | 0.01 | 623013.03 | 10.27 | skipped_fast |
| HBARUSDT | IDLE | 1.9 | 3.64 | 1.02 | 0.01 | 618000.21 | 2.11 | skipped_fast |
| REDUSDT | IDLE | 2.8 | 5.15 | 3.02 | 0.01 | 63108.26 | 15.65 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 5.38 | 4.2 | -0.05 | 146037.41 | 59.49 | skipped_fast |
| ZBCNUSDT | IDLE | 1.58 | 2.93 | 1.51 | 0.0 | 221806.51 | 19.89 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 3.17 | 0.84 | -0.02 | 101371.26 | 6.26 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 3.85 | 0.44 | 0.01 | 116720.12 | 14.11 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 3.96 | 2.18 | 0.12 | 168135.64 | 9.88 | skipped_fast |
| RWAINCUSDT | IDLE | 1.24 | 4.77 | 1.16 | 0.05 | 8754.66 | 74.84 | skipped_fast |
| TELUSDT | IDLE | 1.21 | 4.06 | 2.17 | 0.08 | 128412.12 | 39.92 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.72 | 0.14 | 0.05 | 58138.98 | 7.05 | skipped_fast |
| MNSRYUSDT | IDLE | 1.05 | 2.07 | 0.26 | 0.01 | 39342.98 | 40.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 2.05 | 0.0 | 0.03 | 909.03 | 21.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
