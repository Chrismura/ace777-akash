# Hulk DIGEST — 2026-09-28T05:16:51Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.97 | 8.07 | 0.03 | 5102202.39 | 14.41 | skipped_fast |
| QNTUSDT | IDLE | 1.02 | 32.28 | 19.92 | 0.37 | 15859064.07 | 4.29 | skipped_fast |
| PYTHUSDT | IDLE | 2.3 | 4.72 | 4.24 | -0.03 | 2034168.32 | 3.69 | skipped_fast |
| XRPUSDT | IDLE | 1.92 | 3.38 | 3.09 | -0.02 | 50101255.7 | 6.73 | skipped_fast |
| ETHUSDT | IDLE | 1.3 | 2.32 | 1.91 | -0.02 | 264855720.23 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.2 | 2.11 | 1.92 | -0.01 | 522645683.06 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.81 | 6.41 | 4.53 | 0.02 | 792123.57 | 7.21 | skipped_fast |
| HBARUSDT | IDLE | 2.04 | 3.74 | 2.32 | 0.03 | 1082901.64 | 2.1 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 7.32 | 6.51 | -0.04 | 88735.29 | 6.61 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 7.47 | 6.28 | -0.04 | 106188.12 | 9.7 | skipped_fast |
| REDUSDT | IDLE | 2.51 | 5.3 | 4.17 | -0.05 | 65804.67 | 8.53 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 6.25 | 4.89 | -0.07 | 88390.37 | 15.59 | skipped_fast |
| RIZEUSDT | IDLE | 2.18 | 13.55 | 5.97 | -0.19 | 64851.93 | 63.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.53 | 2.74 | 2.18 | -0.03 | 246962.42 | 13.29 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 5.92 | 5.59 | -0.02 | 3561.6 | 16.8 | skipped_fast |
| EDELUSDT | IDLE | 1.22 | 6.77 | 2.24 | -0.1 | 172005.64 | 35.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.48 | 5.04 | 0.0 | 0.25 | 31652.11 | 66.16 | skipped_fast |
| TELUSDT | IDLE | 0.79 | 1.74 | 1.45 | 0.06 | 172304.14 | 32.66 | skipped_fast |
| MNSRYUSDT | IDLE | 1.09 | 1.98 | 1.34 | -0.0 | 38896.31 | 35.89 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.79 | 0.35 | 0.01 | 60325.94 | 64.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
