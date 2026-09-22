# Hulk DIGEST — 2026-09-22T15:12:12Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 20.05 | 11.51 | -0.0 | 1472290.77 | 3.06 | skipped_fast |
| XRPUSDT | IDLE | 2.58 | 4.93 | 1.5 | 0.05 | 114962765.45 | 1.91 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.73 | 0.78 | -0.0 | 527201948.73 | 0.26 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.14 | 0.34 | 0.0 | 929369025.22 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.59 | 5.39 | 0.62 | 0.06 | 1212032.17 | 2.05 | skipped_fast |
| CCUSDT | IDLE | 2.24 | 3.99 | 3.33 | -0.01 | 497949.59 | 8.64 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 9.22 | 4.26 | 0.1 | 259707.47 | 17.93 | skipped_fast |
| RIZEUSDT | IDLE | 2.06 | 24.12 | 8.29 | -0.21 | 41703.33 | 41.26 | skipped_fast |
| QNTUSDT | IDLE | 3.33 | 10.62 | 3.12 | 0.07 | 184084.22 | 6.91 | skipped_fast |
| WUSDT | IDLE | 1.5 | 2.89 | 0.68 | 0.0 | 382280.46 | 5.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.41 | 4.48 | 2.27 | -0.03 | 146827.29 | 19.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 2.28 | 1.77 | -0.02 | 262371.74 | 23.87 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 2.78 | 0.89 | -0.01 | 114983.77 | 6.92 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 5.46 | 0.04 | 0.14 | 114551.52 | 20.34 | skipped_fast |
| REDUSDT | IDLE | 1.28 | 2.45 | 0.69 | 0.01 | 66736.62 | 13.47 | skipped_fast |
| TELUSDT | IDLE | 2.29 | 4.52 | 0.36 | 0.05 | 104675.22 | 47.56 | skipped_fast |
| RWAINCUSDT | IDLE | 0.88 | 1.61 | 1.04 | 0.03 | 26762.05 | 5.51 | skipped_fast |
| FLUIDUSDT | IDLE | 1.14 | 2.07 | 1.37 | 0.01 | 8990.81 | 22.0 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.95 | 0.22 | -0.0 | 54585.38 | 36.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.11 | 0.21 | 0.05 | -0.0 | 40082.24 | 6.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
