# Hulk DIGEST — 2026-10-14T02:11:35Z

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
| WUSDT | IDLE | 1.17 | 6.8 | 6.14 | -0.16 | 4019441.49 | 7.81 | skipped_fast |
| PYTHUSDT | IDLE | 1.12 | 3.72 | 1.13 | -0.03 | 1923058.58 | 2.51 | skipped_fast |
| XRPUSDT | IDLE | 0.59 | 1.08 | 0.69 | 0.01 | 29413204.81 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 0.49 | 0.9 | 0.55 | 0.02 | 164192543.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.67 | 0.44 | 0.01 | 358669138.96 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 0.99 | 3.62 | 0.9 | -0.05 | 1745758.42 | 2.33 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 3.34 | 3.06 | 0.02 | 585520.89 | 5.64 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 6.02 | 5.63 | -0.03 | 31766.8 | 5.13 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.57 | 1.64 | 0.04 | 222354.74 | 26.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 3.19 | 2.22 | -0.01 | 97075.09 | 10.49 | skipped_fast |
| ZBCNUSDT | IDLE | 1.04 | 2.0 | 0.51 | -0.01 | 216877.08 | 11.85 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 2.54 | 0.89 | 0.03 | 118806.64 | 9.55 | skipped_fast |
| KITEUSDT | IDLE | 1.51 | 2.85 | 1.13 | 0.06 | 57886.9 | 10.76 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 4.26 | 2.73 | 0.0 | 52640.87 | 48.67 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.63 | 1.11 | 0.02 | 71128.8 | 3.61 | skipped_fast |
| FLUIDUSDT | IDLE | 2.11 | 4.24 | 0.0 | 0.08 | 19545.86 | 21.46 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.43 | 0.86 | 0.0 | 245000.08 | 3.43 | skipped_fast |
| TELUSDT | IDLE | 1.41 | 2.77 | 0.33 | 0.05 | 116893.26 | 27.54 | skipped_fast |
| RWAUSDT | IDLE | 0.16 | 0.31 | 0.08 | 0.01 | 51847.33 | 7.73 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.39 | 0.1 | 0.0 | 37802.42 | 5.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
