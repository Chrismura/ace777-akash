# Hulk DIGEST — 2026-09-11T18:21:35Z

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
| ETHUSDT | IDLE | 3.23 | 7.02 | 4.51 | 0.04 | 631656096.58 | 0.51 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.2 | 6.32 | 5.04 | 0.01 | 53080575.37 | 2.2 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 110.08 | 11.7 | 0.98 | 188000.18 | 112.61 | skipped_fast |
| BTCUSDT | IDLE | 2.14 | 3.79 | 3.27 | 0.0 | 552614973.27 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.06 | 5.7 | 4.5 | 0.01 | 399584.51 | 1.93 | skipped_fast |
| CCUSDT | IDLE | 2.84 | 5.15 | 3.53 | 0.0 | 461887.34 | 8.14 | skipped_fast |
| RWAINCUSDT | IDLE | 4.16 | 8.51 | 4.0 | 0.04 | 11185.18 | 5.41 | skipped_fast |
| EDELUSDT | IDLE | 3.66 | 6.74 | 3.91 | -0.02 | 155687.02 | 18.47 | skipped_fast |
| CHIPUSDT | IDLE | 3.29 | 10.12 | 4.2 | 0.02 | 149539.21 | 16.66 | skipped_fast |
| WUSDT | IDLE | 2.85 | 5.63 | 2.73 | 0.02 | 193475.06 | 8.18 | skipped_fast |
| REDUSDT | IDLE | 3.09 | 6.07 | 0.71 | 0.06 | 60648.58 | 10.23 | skipped_fast |
| ZBCNUSDT | IDLE | 2.08 | 3.73 | 2.81 | -0.0 | 189293.59 | 24.44 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 4.18 | 3.12 | 0.0 | 82299.32 | 7.96 | skipped_fast |
| TELUSDT | IDLE | 3.46 | 6.91 | 4.69 | -0.01 | 96260.55 | 50.89 | skipped_fast |
| HBARUSDT | IDLE | 2.36 | 4.19 | 3.57 | -0.01 | 229878.6 | 1.35 | skipped_fast |
| KITEUSDT | IDLE | 1.69 | 3.06 | 2.07 | -0.02 | 59772.37 | 11.96 | skipped_fast |
| FLUIDUSDT | IDLE | 2.57 | 4.94 | 1.3 | 0.01 | 1302.75 | 21.69 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 2.97 | 2.79 | -0.02 | 40151.22 | 6.25 | skipped_fast |
| RWAUSDT | IDLE | 1.46 | 2.81 | 0.67 | 0.02 | 51719.65 | 14.89 | skipped_fast |
| MNSRYUSDT | IDLE | 1.27 | 2.27 | 1.77 | 0.0 | 37024.63 | 45.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
