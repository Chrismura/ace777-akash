# Hulk DIGEST — 2026-09-22T18:14:15Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.76 | 17.48 | 8.93 | 0.05 | 1600127.16 | 4.47 | skipped_fast |
| XRPUSDT | IDLE | 2.1 | 3.98 | 1.44 | 0.04 | 116644779.91 | 1.27 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.73 | 0.37 | 0.0 | 467005037.34 | 0.69 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.42 | 0.12 | 0.01 | 929227587.04 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.03 | 4.42 | 2.84 | 0.05 | 1447161.63 | 1.04 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 18.96 | 10.39 | 0.01 | 289217.65 | 76.19 | skipped_fast |
| CCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 6.3 | 5.72 | -0.03 | 483783.77 | 8.02 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.97 | 35.18 | 9.14 | -0.17 | 44150.74 | 110.39 | skipped_fast |
| WUSDT | IDLE | 2.02 | 3.87 | 1.07 | 0.02 | 367603.39 | 10.8 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 4.6 | 2.22 | -0.03 | 243068.7 | 26.04 | skipped_fast |
| BIOUSDT | IDLE | 2.36 | 4.57 | 1.04 | 0.02 | 136526.76 | 3.4 | skipped_fast |
| CHIPUSDT | IDLE | 2.41 | 4.48 | 2.29 | 0.01 | 140566.44 | 19.58 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 6.06 | 0.33 | 0.17 | 116250.15 | 7.94 | skipped_fast |
| REDUSDT | IDLE | 1.79 | 3.56 | 0.2 | 0.05 | 66042.96 | 7.58 | skipped_fast |
| TELUSDT | IDLE | 2.68 | 7.85 | 0.0 | 0.06 | 105067.9 | 45.17 | skipped_fast |
| QNTUSDT | IDLE | 1.65 | 5.05 | 2.97 | 0.09 | 178393.26 | 1.38 | skipped_fast |
| RWAINCUSDT | IDLE | 0.5 | 1.0 | 0.0 | 0.05 | 20725.34 | 5.51 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.32 | 0.07 | 0.0 | 55000.83 | 7.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.67 | 1.25 | 0.63 | 0.02 | 7749.3 | 20.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.01 | -0.0 | 40412.28 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
