# Hulk DIGEST — 2026-08-22T16:35:00Z

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
| PYTHUSDT | IDLE | 1.64 | 8.12 | 0.02 | 0.07 | 51435559.85 | 11.58 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.64 | 4.03 | 0.05 | 215166217.92 | 2.72 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.56 | 0.07 | 763812.6 | 6.84 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.1 | -0.01 | 1126612.5 | 6.46 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.66 | -0.1 | 627235.32 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.81 | -0.01 | 543931.8 | 6.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.49 | 1.08 | -0.03 | 315741.35 | 0.51 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.13 | -0.06 | 219809.41 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.93 | 4.35 | 2.08 | 0.02 | 85150.2 | 13.46 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.03 | 74851.1 | 22.83 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.04 | -0.15 | 133348.01 | 21.9 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.29 | 0.12 | 49535.11 | 30.31 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2317.66 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.31 | -0.02 | 183288.75 | 7.9 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8171.79 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.37 | 2.31 | 0.0 | 136852.43 | 75.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 21.64 | skipped_fast |
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
