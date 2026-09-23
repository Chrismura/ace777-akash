# Hulk DIGEST — 2026-09-23T14:19:45Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 10.92 | 8.18 | -0.06 | 1580727.37 | 11.14 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 6.42 | 5.23 | -0.03 | 120481609.68 | 2.63 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 9.65 | 7.69 | -0.07 | 1682638.96 | 8.85 | skipped_fast |
| ETHUSDT | IDLE | 1.83 | 3.21 | 3.01 | -0.03 | 463358571.53 | 2.56 | skipped_fast |
| BTCUSDT | IDLE | 1.07 | 1.86 | 1.81 | -0.02 | 843613556.61 | 0.64 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 10.17 | 7.82 | -0.04 | 403954.79 | 8.74 | skipped_fast |
| CCUSDT | IDLE | 3.04 | 6.34 | 4.9 | -0.08 | 434949.69 | 5.56 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 8.67 | 5.94 | -0.05 | 215756.59 | 20.74 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.9 | 7.52 | 5.77 | -0.01 | 124700.48 | 13.99 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 7.35 | 5.81 | -0.0 | 59101.24 | 14.24 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 5.8 | 5.45 | -0.02 | 242077.37 | 23.95 | skipped_fast |
| KITEUSDT | IDLE | 2.88 | 5.2 | 3.75 | 0.01 | 151742.61 | 8.25 | skipped_fast |
| EDELUSDT | IDLE | 1.61 | 6.0 | 4.23 | -0.11 | 219093.56 | 17.03 | skipped_fast |
| QNTUSDT | IDLE | 3.07 | 5.4 | 4.88 | -0.0 | 184357.97 | 12.51 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.88 | 8.15 | 7.32 | 0.02 | 156900.5 | 35.09 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.52 | 6.26 | 5.22 | -0.04 | 4195.18 | 60.61 | skipped_fast |
| RIZEUSDT | IDLE | 0.31 | 4.86 | 2.36 | 0.61 | 62525.32 | 71.24 | skipped_fast |
| RWAINCUSDT | IDLE | 0.59 | 1.36 | 0.48 | 0.03 | 19681.11 | 75.63 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 1.91 | 1.66 | -0.01 | 54566.93 | 36.59 | skipped_fast |
| MNSRYUSDT | IDLE | 1.11 | 1.99 | 1.47 | -0.01 | 40788.34 | 59.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
