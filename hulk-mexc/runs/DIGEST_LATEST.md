# Hulk DIGEST — 2026-10-16T16:01:08Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.82 | 8.1 | 6.77 | -0.11 | 2665202.51 | 2.32 | skipped_fast |
| WUSDT | IDLE | 2.66 | 4.67 | 4.32 | -0.04 | 1672255.65 | 20.84 | skipped_fast |
| XRPUSDT | IDLE | 2.0 | 3.5 | 3.29 | -0.02 | 23255076.45 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 1.47 | 2.56 | 2.49 | -0.0 | 204951787.69 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.11 | 1.94 | 1.89 | -0.01 | 352672434.87 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.39 | 6.02 | 5.11 | -0.03 | 970098.07 | 2.48 | skipped_fast |
| CCUSDT | IDLE | 2.3 | 4.1 | 3.37 | -0.07 | 395445.18 | 10.69 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 10.33 | 7.73 | -0.11 | 25938.03 | 5.37 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.67 | 8.03 | 7.31 | -0.02 | 153689.32 | 8.66 | skipped_fast |
| ZBCNUSDT | IDLE | 2.37 | 4.16 | 3.9 | -0.02 | 193523.99 | 23.13 | skipped_fast |
| RIZEUSDT | IDLE | 2.65 | 6.13 | 1.35 | 0.02 | 52467.96 | 28.7 | skipped_fast |
| KITEUSDT | IDLE | 2.35 | 4.2 | 3.39 | -0.04 | 58520.94 | 12.47 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 3.97 | 3.74 | -0.02 | 60413.08 | 11.9 | skipped_fast |
| REDUSDT | IDLE | 2.06 | 3.99 | 3.83 | -0.09 | 96581.66 | 14.88 | skipped_fast |
| EDELUSDT | IDLE | 1.19 | 2.91 | 2.11 | -0.05 | 213952.98 | 3.32 | skipped_fast |
| HBARUSDT | IDLE | 2.13 | 3.75 | 3.41 | 0.01 | 305735.69 | 8.32 | skipped_fast |
| TELUSDT | IDLE | 1.16 | 2.03 | 1.88 | 0.01 | 89899.58 | 28.15 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.35 | 1.17 | 0.01 | 52252.81 | 7.9 | skipped_fast |
| FLUIDUSDT | IDLE | 0.84 | 1.61 | 0.49 | -0.03 | 6222.33 | 39.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.45 | 0.32 | -0.0 | 37417.77 | 21.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
