# Hulk DIGEST — 2026-09-19T02:00:36Z

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
| XRPUSDT | IDLE | 0.92 | 2.02 | 0.67 | 0.08 | 68637138.12 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.42 | 1.02 | 0.06 | 657208803.45 | 0.23 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.09 | 0.56 | 0.06 | 788762737.92 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.94 | 3.26 | 1.52 | 0.1 | 938404.21 | 6.38 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 19.02 | 15.35 | 0.05 | 90439.78 | 14.63 | skipped_fast |
| PYTHUSDT | IDLE | 1.14 | 2.16 | 0.85 | 0.05 | 778657.24 | 9.92 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 2.54 | 0.96 | 0.06 | 672747.22 | 12.56 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 2.02 | 0.78 | 0.05 | 701689.58 | 2.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.98 | 5.69 | 2.87 | 0.1 | 162700.01 | 15.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.33 | 1.47 | 0.03 | 235750.76 | 21.49 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.52 | 11.02 | 6.46 | 0.12 | 126795.57 | 43.93 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.36 | 0.21 | 0.04 | 78417.87 | 13.31 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.85 | 0.65 | 0.07 | 86909.0 | 14.63 | skipped_fast |
| RWAINCUSDT | IDLE | 0.03 | 0.06 | 0.06 | 0.04 | 6732.04 | 5.75 | skipped_fast |
| RIZEUSDT | IDLE | 0.16 | 2.77 | 0.0 | -0.08 | 56072.54 | 70.35 | skipped_fast |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
