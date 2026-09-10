# Hulk DIGEST — 2026-09-10T10:18:32Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.08 | 209.6 | 53.36 | -0.55 | 86104.52 | 501.18 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.33 | 1.11 | -0.03 | 41088082.63 | 2.18 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.82 | 0.61 | -0.01 | 330387990.61 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.79 | 0.72 | -0.01 | 516645109.07 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 3.38 | 2.84 | -0.05 | 998785.15 | 1.94 | skipped_fast |
| CCUSDT | IDLE | 2.29 | 4.0 | 3.83 | -0.05 | 665989.59 | 6.91 | skipped_fast |
| KITEUSDT | IDLE | 3.06 | 6.55 | 4.33 | -0.05 | 57483.84 | 12.02 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 5.35 | 2.75 | 0.08 | 240615.21 | 17.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.81 | 3.24 | 2.49 | 0.02 | 160450.8 | 13.98 | skipped_fast |
| WUSDT | IDLE | 1.43 | 3.38 | 2.16 | -0.05 | 229700.0 | 12.44 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 3.08 | 1.97 | -0.06 | 65168.03 | 8.9 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 2.35 | 1.48 | -0.06 | 99256.52 | 3.94 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.67 | 1.57 | -0.04 | 377394.11 | 1.32 | skipped_fast |
| CHIPUSDT | IDLE | 0.69 | 3.96 | 2.7 | -0.18 | 103038.72 | 16.57 | skipped_fast |
| RWAINCUSDT | IDLE | 1.29 | 2.27 | 2.11 | -0.02 | 5918.39 | 28.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.27 | 2.61 | 2.55 | -0.08 | 1430.23 | 21.43 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.27 | 1.09 | -0.02 | 38678.83 | 3.01 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 1.96 | 0.66 | 0.01 | 85650.62 | 66.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.34 | -0.02 | 25263.05 | 4.14 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.15 | -0.03 | 53783.4 | 14.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
