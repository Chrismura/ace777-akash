# Hulk DIGEST — 2026-09-13T08:39:20Z

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
| XRPUSDT | IDLE | 0.91 | 1.59 | 1.52 | -0.01 | 13053753.23 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.08 | 1.03 | -0.01 | 194415586.25 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.59 | 0.58 | -0.01 | 282423575.32 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.9 | 30.17 | 14.19 | 0.18 | 101521.27 | 13.56 | skipped_fast |
| PYTHUSDT | IDLE | 1.99 | 3.48 | 3.32 | 0.02 | 460188.12 | 1.86 | skipped_fast |
| CCUSDT | IDLE | 2.35 | 4.15 | 3.68 | -0.03 | 273707.81 | 10.47 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 3.99 | 2.12 | 0.02 | 62306.22 | 11.98 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 5.68 | 5.31 | -0.0 | 36572.77 | 9.41 | skipped_fast |
| REDUSDT | IDLE | 1.86 | 3.26 | 3.08 | 0.03 | 55510.57 | 16.83 | skipped_fast |
| WUSDT | IDLE | 0.97 | 1.69 | 1.66 | 0.02 | 232099.67 | 10.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 3.25 | 3.12 | -0.04 | 77713.66 | 12.9 | skipped_fast |
| TELUSDT | IDLE | 2.87 | 5.03 | 4.79 | -0.07 | 88847.55 | 25.43 | skipped_fast |
| ZBCNUSDT | IDLE | 0.7 | 1.97 | 1.65 | -0.01 | 234665.36 | 3.38 | skipped_fast |
| EDELUSDT | IDLE | 1.04 | 2.55 | 2.09 | 0.07 | 173364.68 | 24.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.47 | 2.57 | 2.51 | -0.02 | 10144.49 | 5.59 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 1.69 | 1.62 | 0.0 | 70706.35 | 7.86 | skipped_fast |
| FLUIDUSDT | IDLE | 2.2 | 4.0 | 2.71 | 0.01 | 1217.06 | 42.63 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.24 | 1.08 | 0.01 | 151090.54 | 1.33 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.05 | 1.03 | -0.01 | 56104.85 | 7.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.36 | 0.11 | 0.01 | 33937.67 | 26.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
