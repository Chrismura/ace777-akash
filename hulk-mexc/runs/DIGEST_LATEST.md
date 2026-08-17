# Hulk DIGEST — 2026-08-17T05:10:27Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.83 | 1.62 | 0.28 | 0.0 | 8427408.37 | 1.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 25.44 | 18.03 | 0.06 | 44115.34 | 58.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.67 | 7.11 | 0.54 | 0.07 | 296499.69 | 3.42 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.71 | 1.63 | -0.02 | 281453.3 | 10.54 | skipped_fast |
| PYTHUSDT | IDLE | 1.28 | 2.54 | 0.08 | -0.01 | 159172.58 | 2.55 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 2.95 | 2.6 | -0.04 | 58873.44 | 15.34 | skipped_fast |
| WUSDT | IDLE | 1.08 | 1.89 | 1.8 | 0.02 | 187061.22 | 11.79 | skipped_fast |
| KITEUSDT | IDLE | 1.43 | 2.62 | 1.65 | -0.0 | 54348.46 | 13.84 | skipped_fast |
| EDELUSDT | IDLE | 1.73 | 3.17 | 1.92 | 0.03 | 55264.14 | 52.08 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 1.48 | 0.8 | -0.0 | 199780.74 | 17.85 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.83 | 0.25 | -0.0 | 65367.89 | 8.18 | skipped_fast |
| RWAINCUSDT | IDLE | 0.56 | 1.02 | 0.68 | 0.01 | 3256.94 | 28.34 | skipped_fast |
| QNTUSDT | IDLE | 1.51 | 2.65 | 2.47 | -0.03 | 34191.79 | 10.79 | skipped_fast |
| HBARUSDT | IDLE | 0.58 | 1.15 | 0.03 | -0.0 | 88542.05 | 1.54 | skipped_fast |
| QAITUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 2142.08 | 61.3 | skipped_fast |
| TELUSDT | IDLE | 0.78 | 1.44 | 0.74 | 0.0 | 89661.99 | 47.64 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.88 | 0.09 | 0.01 | 49785.37 | 17.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.51 | 0.15 | 0.01 | 411.11 | 23.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
