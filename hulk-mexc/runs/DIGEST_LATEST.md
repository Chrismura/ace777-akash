# Hulk DIGEST — 2026-08-22T09:26:44Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.26 | 0.05 | 40488973.71 | 3.99 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.84 | 23.87 | 11.15 | 0.11 | 219519595.04 | 7.95 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 15.8 | 9.76 | 0.04 | 1300762.84 | 6.39 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 23.96 | 11.79 | -0.08 | 667486.24 | 3.35 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.42 | 0.05 | 595065.27 | 14.56 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.71 | -0.02 | 237876.37 | 6.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.73 | 0.06 | 154687.36 | 9.71 | skipped_fast |
| CCUSDT | IDLE | 2.22 | 11.25 | 7.12 | 0.13 | 795410.28 | 6.02 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.62 | -0.01 | 463971.79 | 20.19 | skipped_fast |
| KITEUSDT | IDLE | 4.27 | 9.68 | 4.41 | 0.05 | 73123.49 | 12.76 | skipped_fast |
| EDELUSDT | IDLE | 2.54 | 4.52 | 3.78 | -0.03 | 79353.72 | 22.47 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.69 | 6.02 | -0.02 | 171134.92 | 21.0 | skipped_fast |
| RWAINCUSDT | IDLE | 2.4 | 4.36 | 2.93 | 0.01 | 11509.42 | 69.8 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.36 | 1.75 | -0.02 | 50332.64 | 46.77 | skipped_fast |
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
