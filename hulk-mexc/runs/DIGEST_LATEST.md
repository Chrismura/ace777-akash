# Hulk DIGEST — 2026-09-07T05:34:15Z

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
| XRPUSDT | IDLE | 1.14 | 2.12 | 1.1 | -0.0 | 29693573.63 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.71 | 0.93 | 0.0 | 297498172.64 | 0.16 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.09 | 0.71 | 0.0 | 395048184.01 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.77 | 4.96 | 3.93 | -0.0 | 588612.61 | 1.81 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.93 | 6.01 | 5.63 | -0.05 | 435879.42 | 14.23 | skipped_fast |
| EDELUSDT | IDLE | 3.95 | 7.34 | 3.69 | 0.0 | 68898.22 | 37.42 | skipped_fast |
| WUSDT | IDLE | 1.54 | 2.87 | 1.41 | 0.04 | 412775.94 | 9.59 | skipped_fast |
| CCUSDT | IDLE | 1.52 | 2.82 | 1.46 | 0.01 | 390759.86 | 9.04 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 2.8 | 1.54 | -0.02 | 76348.42 | 3.65 | skipped_fast |
| RWAINCUSDT | IDLE | 1.58 | 6.24 | 2.66 | 0.12 | 6193.22 | 23.96 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 2.08 | 1.2 | -0.0 | 411058.67 | 1.23 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 2.24 | 1.5 | -0.03 | 56153.54 | 8.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.15 | 8.69 | 1.93 | -0.17 | 71018.57 | 62.31 | skipped_fast |
| ZBCNUSDT | IDLE | 0.89 | 1.67 | 0.74 | -0.01 | 135723.1 | 17.74 | skipped_fast |
| REDUSDT | IDLE | 1.11 | 2.06 | 1.11 | 0.0 | 66454.36 | 10.23 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.21 | 1.02 | 0.01 | 98011.99 | 40.26 | skipped_fast |
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
