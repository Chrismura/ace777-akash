# Hulk DIGEST — 2026-08-19T12:12:05Z

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
| XRPUSDT | IDLE | 0.34 | 0.63 | 0.31 | 0.01 | 10296531.57 | 1.99 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 12.24 | 6.97 | 0.04 | 12357.32 | 28.68 | skipped_fast |
| CHIPUSDT | IDLE | 2.59 | 6.29 | 0.59 | -0.05 | 166086.79 | 3.72 | skipped_fast |
| QAITUSDT | IDLE | 3.66 | 6.87 | 3.04 | -0.15 | 13033.95 | 65.85 | skipped_fast |
| PYTHUSDT | IDLE | 1.4 | 2.5 | 1.97 | 0.0 | 177586.46 | 5.23 | skipped_fast |
| BIOUSDT | IDLE | 1.7 | 3.38 | 0.19 | 0.05 | 64465.88 | 7.79 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.67 | 0.63 | -0.02 | 220110.35 | 9.94 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 2.94 | 0.22 | 0.01 | 56598.26 | 14.05 | skipped_fast |
| REDUSDT | IDLE | 0.96 | 2.98 | 2.03 | -0.11 | 130997.91 | 12.54 | skipped_fast |
| EDELUSDT | IDLE | 1.28 | 2.31 | 1.72 | -0.03 | 59165.44 | 26.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.5 | 3.82 | 2.42 | -0.08 | 28609.61 | 50.0 | skipped_fast |
| ZBCNUSDT | IDLE | 0.63 | 1.23 | 0.24 | 0.01 | 161642.73 | 14.46 | skipped_fast |
| WUSDT | IDLE | 0.68 | 1.28 | 0.5 | -0.0 | 99851.68 | 14.79 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 1.88 | 1.57 | 0.02 | 86806.86 | 48.66 | skipped_fast |
| HBARUSDT | IDLE | 0.38 | 0.74 | 0.18 | 0.03 | 149303.02 | 1.48 | skipped_fast |
| QNTUSDT | IDLE | 0.66 | 1.19 | 0.9 | 0.01 | 37378.89 | 3.54 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.17 | -0.01 | 52373.74 | 17.51 | skipped_fast |
| FLUIDUSDT | IDLE | 0.49 | 0.99 | 0.0 | -0.01 | 1261.45 | 22.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
