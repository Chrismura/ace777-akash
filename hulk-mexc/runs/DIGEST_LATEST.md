# Hulk DIGEST — 2026-10-13T14:02:30Z

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
| WUSDT | IDLE | 1.54 | 12.3 | 10.81 | -0.31 | 6137855.88 | 15.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.34 | 4.45 | 3.61 | -0.06 | 2436776.98 | 2.45 | skipped_fast |
| XRPUSDT | IDLE | 0.95 | 1.8 | 0.7 | -0.02 | 38891089.55 | 2.93 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.43 | 0.81 | -0.01 | 235247603.17 | 1.2 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 12.37 | 9.02 | -0.11 | 1152182.1 | 5.36 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.71 | 0.52 | 0.0 | 382192981.55 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.86 | 8.95 | 2.87 | 0.03 | 561172.22 | 8.62 | skipped_fast |
| EDELUSDT | IDLE | 3.48 | 6.69 | 1.84 | -0.06 | 334334.76 | 32.27 | skipped_fast |
| RWAINCUSDT | IDLE | 3.03 | 5.4 | 4.36 | -0.02 | 33075.99 | 4.96 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.17 | 10.38 | 5.46 | -0.11 | 64489.39 | 88.02 | skipped_fast |
| REDUSDT | IDLE | 1.82 | 6.14 | 4.71 | -0.06 | 201627.64 | 7.23 | skipped_fast |
| ZBCNUSDT | IDLE | 1.91 | 3.45 | 2.53 | -0.05 | 247845.55 | 17.12 | skipped_fast |
| CHIPUSDT | IDLE | 2.02 | 4.4 | 2.97 | -0.06 | 128176.2 | 12.01 | skipped_fast |
| HBARUSDT | IDLE | 1.92 | 3.63 | 1.37 | -0.05 | 394559.72 | 5.69 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 3.07 | 1.69 | -0.06 | 75651.12 | 7.3 | skipped_fast |
| KITEUSDT | IDLE | 0.96 | 1.93 | 1.32 | -0.01 | 63181.62 | 11.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.45 | 2.88 | 2.61 | 0.02 | 12535.37 | 21.04 | skipped_fast |
| TELUSDT | IDLE | 0.75 | 1.45 | 0.29 | -0.01 | 105041.11 | 45.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.16 | 0.79 | -0.02 | 37782.86 | 8.36 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.23 | 0.0 | 53456.45 | 15.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
