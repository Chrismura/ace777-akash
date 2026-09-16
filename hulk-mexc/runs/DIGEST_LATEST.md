# Hulk DIGEST — 2026-09-16T15:13:54Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 1.09 | 2.96 | 2.2 | -0.09 | 81903107.12 | 2.36 | skipped_fast |
| ETHUSDT | IDLE | 1.14 | 2.06 | 1.44 | -0.01 | 424515917.97 | 0.54 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.13 | 0.73 | -0.0 | 565162099.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.77 | 3.21 | 2.26 | -0.02 | 668029.76 | 1.92 | skipped_fast |
| CCUSDT | IDLE | 1.86 | 3.55 | 1.12 | -0.03 | 452491.24 | 6.59 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 5.94 | 5.17 | -0.05 | 64960.9 | 18.93 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.92 | 7.82 | 5.95 | -0.04 | 98773.13 | 16.58 | skipped_fast |
| EDELUSDT | IDLE | 0.71 | 10.01 | 8.57 | 0.3 | 414322.65 | 3.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.54 | 24.15 | 18.76 | 0.37 | 58378.15 | 90.76 | skipped_fast |
| HBARUSDT | IDLE | 1.65 | 3.34 | 2.53 | -0.06 | 352263.09 | 1.38 | skipped_fast |
| WUSDT | IDLE | 1.04 | 2.33 | 1.17 | -0.07 | 220601.98 | 15.82 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 2.84 | 2.32 | -0.02 | 80467.6 | 12.29 | skipped_fast |
| KITEUSDT | IDLE | 1.54 | 2.92 | 1.65 | -0.04 | 59595.32 | 10.16 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 2.59 | 1.42 | -0.01 | 195441.29 | 23.4 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 5.6 | 4.01 | -0.07 | 123157.18 | 35.37 | skipped_fast |
| RWAINCUSDT | IDLE | 1.27 | 2.31 | 1.51 | -0.03 | 13229.5 | 53.36 | skipped_fast |
| QNTUSDT | IDLE | 1.09 | 2.02 | 1.07 | -0.05 | 42765.86 | 5.04 | skipped_fast |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
