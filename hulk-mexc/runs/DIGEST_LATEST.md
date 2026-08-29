# Hulk DIGEST — 2026-08-29T08:10:44Z

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
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.73 | 12.93 | 7.28 | 0.03 | 1247497.31 | 2.43 | skipped_fast |
| XRPUSDT | IDLE | 0.66 | 1.17 | 1.03 | -0.03 | 43063920.57 | 2.9 | skipped_fast |
| PYTHUSDT | IDLE | 1.7 | 2.98 | 2.81 | -0.04 | 500834.33 | 4.29 | skipped_fast |
| WUSDT | IDLE | 1.24 | 2.18 | 2.05 | -0.03 | 209588.98 | 15.37 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 2.85 | 2.09 | -0.01 | 69218.65 | 11.84 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.52 | 0.44 | -0.01 | 213355.31 | 5.39 | skipped_fast |
| REDUSDT | IDLE | 1.45 | 2.82 | 0.77 | 0.01 | 60872.51 | 14.65 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.32 | 1.28 | -0.04 | 461316.28 | 1.34 | skipped_fast |
| ZBCNUSDT | IDLE | 0.52 | 1.4 | 0.44 | -0.06 | 180642.66 | 8.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.56 | 3.21 | 1.49 | -0.05 | 29586.82 | 58.36 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 1.34 | 1.18 | -0.04 | 81721.75 | 3.62 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 1.66 | 1.63 | 0.01 | 3548.47 | 88.35 | skipped_fast |
| TELUSDT | IDLE | 0.79 | 1.44 | 0.96 | -0.05 | 79738.52 | 34.38 | skipped_fast |
| QAITUSDT | IDLE | 0.24 | 2.07 | 1.47 | -0.03 | 84066.77 | 181.39 | skipped_fast |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
