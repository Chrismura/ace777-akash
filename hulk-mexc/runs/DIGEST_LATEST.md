# Hulk DIGEST — 2026-08-22T08:12:39Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.13 | 19.14 | 8.56 | 0.01 | 26296224.24 | 3.92 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 23.87 | 8.8 | 0.16 | 224772331.29 | 1.94 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.37 | 0.04 | 1357192.49 | 5.08 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.09 | -0.08 | 684522.25 | 6.61 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.67 | 0.05 | 609866.26 | 13.42 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 29.98 | 8.78 | -0.03 | 247350.4 | 3.16 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.45 | 0.06 | 154585.14 | 9.64 | skipped_fast |
| CCUSDT | IDLE | 2.04 | 11.25 | 2.05 | 0.2 | 818905.51 | 7.33 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 8.47 | 5.9 | 0.03 | 537351.7 | 30.45 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.36 | 0.03 | 194127.31 | 7.69 | skipped_fast |
| KITEUSDT | IDLE | 3.8 | 9.68 | 3.81 | 0.07 | 72935.0 | 10.85 | skipped_fast |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 18.81 | skipped_fast |
| EDELUSDT | IDLE | 2.27 | 4.52 | 3.24 | -0.03 | 86973.81 | 44.54 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11216.08 | 112.81 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.9 | -0.01 | 173695.04 | 46.21 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.85 | 0.0 | 52290.89 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 1.71 | 3.29 | 0.8 | 0.05 | 58243.41 | 16.09 | skipped_fast |
| QAITUSDT | IDLE | 0.99 | 1.92 | 0.35 | 0.01 | 3170.95 | 67.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
