# Hulk DIGEST — 2026-09-11T18:16:39Z

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
| ETHUSDT | IDLE | 3.25 | 7.02 | 4.71 | 0.03 | 630346640.2 | 0.51 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 6.32 | 5.28 | 0.0 | 52847956.68 | 2.21 | skipped_fast |
| BTCUSDT | IDLE | 2.15 | 3.79 | 3.38 | 0.0 | 550551256.1 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 110.08 | 13.2 | 0.86 | 187883.35 | 698.99 | skipped_fast |
| PYTHUSDT | IDLE | 3.09 | 5.7 | 4.82 | 0.0 | 395860.29 | 3.88 | skipped_fast |
| CCUSDT | IDLE | 2.87 | 5.15 | 3.88 | -0.0 | 461114.35 | 9.19 | skipped_fast |
| RWAINCUSDT | IDLE | 4.16 | 8.51 | 4.0 | 0.04 | 11164.91 | 5.41 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.34 | 10.12 | 5.36 | 0.01 | 149390.76 | 12.67 | skipped_fast |
| EDELUSDT | IDLE | 3.65 | 6.74 | 3.73 | -0.02 | 155570.3 | 46.06 | skipped_fast |
| WUSDT | IDLE | 2.86 | 5.63 | 2.89 | 0.01 | 193257.96 | 18.47 | skipped_fast |
| REDUSDT | IDLE | 3.13 | 6.07 | 1.24 | 0.05 | 60703.95 | 17.39 | skipped_fast |
| ZBCNUSDT | IDLE | 2.09 | 3.73 | 2.97 | -0.0 | 189165.67 | 22.25 | skipped_fast |
| BIOUSDT | IDLE | 2.35 | 4.18 | 3.47 | -0.0 | 82131.65 | 7.99 | skipped_fast |
| TELUSDT | IDLE | 3.46 | 6.91 | 4.74 | -0.01 | 96308.92 | 33.96 | skipped_fast |
| HBARUSDT | IDLE | 2.37 | 4.19 | 3.71 | -0.01 | 229820.7 | 1.35 | skipped_fast |
| KITEUSDT | IDLE | 1.7 | 3.06 | 2.23 | -0.02 | 59772.38 | 11.98 | skipped_fast |
| FLUIDUSDT | IDLE | 2.57 | 4.94 | 1.3 | 0.01 | 1302.75 | 20.85 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 2.97 | 2.73 | -0.02 | 40095.28 | 9.36 | skipped_fast |
| RWAUSDT | IDLE | 1.46 | 2.81 | 0.74 | 0.02 | 51606.61 | 29.81 | skipped_fast |
| MNSRYUSDT | IDLE | 1.29 | 2.27 | 2.04 | 0.0 | 37067.87 | 62.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
