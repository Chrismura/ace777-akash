# Hulk DIGEST — 2026-09-02T23:00:53Z

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
| XRPUSDT | IDLE | 0.77 | 1.42 | 0.83 | 0.0 | 35695303.82 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.88 | 0.84 | -0.01 | 348858989.48 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.64 | 0.62 | -0.0 | 502134812.71 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.84 | 2.73 | 2.45 | 0.1 | 1338703.6 | 3.51 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 4.71 | 0.75 | -0.03 | 966206.9 | 2.36 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 27.69 | 12.36 | 0.14 | 53050.47 | 61.74 | skipped_fast |
| ZBCNUSDT | IDLE | 2.83 | 6.79 | 0.75 | -0.01 | 177076.15 | 19.97 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 2.1 | 1.06 | -0.03 | 425954.66 | 3.64 | skipped_fast |
| WUSDT | IDLE | 1.84 | 3.39 | 1.92 | 0.01 | 239460.87 | 13.42 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 7.31 | 2.72 | 0.15 | 140720.5 | 11.27 | skipped_fast |
| BIOUSDT | IDLE | 1.92 | 3.59 | 1.65 | 0.0 | 69172.47 | 7.82 | skipped_fast |
| EDELUSDT | IDLE | 1.13 | 5.84 | 4.28 | 0.08 | 156045.7 | 25.87 | skipped_fast |
| RWAINCUSDT | IDLE | 2.08 | 6.05 | 0.53 | 0.11 | 11472.57 | 31.85 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 1.85 | 1.14 | 0.0 | 112026.57 | 7.84 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 3.44 | 3.06 | -0.0 | 61390.08 | 7.83 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.19 | 1.39 | 0.03 | 75401.28 | 23.46 | skipped_fast |
| RWAUSDT | IDLE | 1.04 | 1.93 | 0.98 | 0.01 | 52148.94 | 7.63 | skipped_fast |
| HBARUSDT | IDLE | 0.31 | 0.58 | 0.24 | 0.0 | 183194.98 | 1.35 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.81 | 0.0 | -0.01 | 2360.61 | 20.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.0 | 22591.42 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
