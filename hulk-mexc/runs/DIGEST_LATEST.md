# Hulk DIGEST — 2026-08-28T22:08:14Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 1.23 | 2.24 | 1.45 | -0.06 | 52502819.57 | 2.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 8.41 | 7.23 | 0.03 | 1092823.09 | 4.96 | skipped_fast |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 33.89 | 22.97 | -0.16 | 80122.42 | 55.74 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 2.56 | 1.18 | -0.05 | 702254.69 | 2.14 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.23 | 13.86 | 9.91 | -0.13 | 90414.58 | 28.92 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 6.27 | 5.39 | -0.09 | 186519.25 | 31.31 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.8 | 0.68 | -0.02 | 342980.68 | 9.08 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 5.16 | 0.72 | -0.01 | 63369.8 | 22.22 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 3.61 | 0.73 | -0.01 | 79766.17 | 8.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 4.97 | 2.26 | 0.02 | 36753.41 | 35.78 | skipped_fast |
| WUSDT | IDLE | 0.81 | 1.76 | 1.15 | -0.07 | 205725.39 | 5.51 | skipped_fast |
| RWAINCUSDT | IDLE | 2.45 | 4.28 | 4.1 | -0.04 | 10141.46 | 105.0 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.82 | 1.26 | -0.04 | 453826.43 | 1.32 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.97 | 0.86 | -0.06 | 91427.87 | 7.22 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 2.93 | 2.62 | -0.09 | 97776.71 | 40.15 | skipped_fast |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
