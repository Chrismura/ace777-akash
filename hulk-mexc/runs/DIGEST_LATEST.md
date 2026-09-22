# Hulk DIGEST — 2026-09-22T14:06:14Z

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
| XRPUSDT | IDLE | 2.54 | 4.93 | 1.01 | 0.06 | 113139842.11 | 1.27 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 20.05 | 6.15 | 0.07 | 1037145.44 | 50.57 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.21 | 0.42 | 0.01 | 537550234.3 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.47 | 0.89 | 0.29 | 0.01 | 954841587.27 | 0.12 | skipped_fast |
| HBARUSDT | IDLE | 2.38 | 4.83 | 0.39 | 0.07 | 1194796.54 | 1.03 | skipped_fast |
| CCUSDT | IDLE | 1.97 | 3.68 | 1.73 | 0.03 | 539084.56 | 6.8 | skipped_fast |
| EDELUSDT | IDLE | 2.2 | 9.22 | 5.44 | 0.11 | 253650.45 | 6.03 | skipped_fast |
| QNTUSDT | IDLE | 3.49 | 11.12 | 3.35 | 0.07 | 179736.97 | 8.32 | skipped_fast |
| RIZEUSDT | IDLE | 2.02 | 24.12 | 5.21 | -0.18 | 49206.63 | 64.79 | skipped_fast |
| WUSDT | IDLE | 1.5 | 2.89 | 0.67 | 0.0 | 373612.76 | 5.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.43 | 4.42 | 2.88 | -0.02 | 159740.27 | 17.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.53 | 2.87 | 1.23 | -0.01 | 265661.96 | 6.88 | skipped_fast |
| KITEUSDT | IDLE | 1.78 | 6.66 | 1.84 | 0.12 | 116018.69 | 8.27 | skipped_fast |
| REDUSDT | IDLE | 2.02 | 3.74 | 2.01 | 0.01 | 67102.84 | 14.17 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.78 | 0.24 | 0.01 | 117520.33 | 6.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.18 | 2.18 | 1.21 | 0.04 | 27012.0 | 5.53 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 4.24 | 0.24 | 0.03 | 110095.7 | 35.95 | skipped_fast |
| FLUIDUSDT | IDLE | 1.07 | 2.07 | 0.5 | 0.02 | 8561.79 | 21.95 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.95 | 0.36 | -0.0 | 55067.59 | 14.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.4 | 0.05 | 0.0 | 40058.04 | 6.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
