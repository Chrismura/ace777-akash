# Hulk DIGEST — 2026-08-29T02:08:38Z

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
| XRPUSDT | IDLE | 0.72 | 1.42 | 0.19 | -0.04 | 48987861.92 | 2.88 | skipped_fast |
| CHIPUSDT | IDLE | 1.09 | 6.52 | 2.41 | 0.02 | 1191857.21 | 2.4 | skipped_fast |
| QAITUSDT | IDLE | 2.08 | 27.55 | 20.0 | -0.02 | 82499.69 | 71.94 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.06 | 0.65 | -0.03 | 589837.51 | 2.1 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 6.84 | 6.26 | -0.08 | 34966.5 | 55.32 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.88 | 1.3 | -0.03 | 267321.68 | 10.84 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.79 | 1.6 | -0.04 | 469383.25 | 1.32 | skipped_fast |
| KITEUSDT | IDLE | 1.48 | 2.67 | 1.91 | -0.02 | 78998.07 | 10.26 | skipped_fast |
| WUSDT | IDLE | 0.8 | 1.54 | 0.35 | -0.05 | 219054.89 | 13.11 | skipped_fast |
| EDELUSDT | IDLE | 1.0 | 4.26 | 0.76 | -0.11 | 92867.16 | 19.14 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.76 | 0.9 | -0.08 | 171716.15 | 10.25 | skipped_fast |
| REDUSDT | IDLE | 0.78 | 1.76 | 1.5 | -0.05 | 62007.21 | 12.15 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.3 | 0.32 | -0.04 | 85432.85 | 3.59 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 2.28 | 0.0 | -0.02 | 3438.94 | 103.91 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.12 | 0.45 | -0.06 | 99513.59 | 50.66 | skipped_fast |
| QNTUSDT | IDLE | 0.38 | 0.74 | 0.08 | -0.03 | 41935.15 | 6.53 | skipped_fast |
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
