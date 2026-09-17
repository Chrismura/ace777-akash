# Hulk DIGEST — 2026-09-17T21:04:50Z

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
| ETHUSDT | IDLE | 0.73 | 1.31 | 1.03 | 0.02 | 306145606.45 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.7 | 1.26 | 0.9 | -0.0 | 39155454.37 | 2.31 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.63 | 0.55 | 0.0 | 437362229.14 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.61 | 40.67 | 25.55 | -0.29 | 260914.78 | 31.81 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 3.34 | 2.2 | 0.04 | 565403.39 | 9.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 3.44 | 3.06 | 0.06 | 548555.27 | 1.8 | skipped_fast |
| WUSDT | IDLE | 1.87 | 6.12 | 2.07 | 0.11 | 324823.32 | 13.14 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.24 | 1.49 | 0.03 | 552436.54 | 1.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.48 | 4.75 | 3.22 | 0.05 | 144607.27 | 18.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.06 | 1.92 | 1.37 | 0.01 | 200478.1 | 19.33 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.61 | 2.19 | 0.01 | 65666.12 | 16.18 | skipped_fast |
| RIZEUSDT | IDLE | 1.37 | 9.66 | 3.27 | -0.09 | 45641.32 | 74.06 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.6 | 1.41 | 0.01 | 69125.04 | 11.95 | skipped_fast |
| KITEUSDT | IDLE | 0.87 | 1.63 | 0.76 | 0.04 | 62235.31 | 12.37 | skipped_fast |
| TELUSDT | IDLE | 2.13 | 3.77 | 3.3 | -0.01 | 76105.67 | 55.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.61 | 1.07 | 1.06 | 0.02 | 22656.9 | 29.63 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.03 | 146.13 | 21.84 | skipped_fast |
| QNTUSDT | IDLE | 0.61 | 1.08 | 0.92 | 0.01 | 40259.36 | 3.27 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.75 | 0.22 | 0.0 | 57266.81 | 29.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.04 | 0.02 | 42651.76 | 4.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
