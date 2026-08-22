# Hulk DIGEST — 2026-08-22T15:28:07Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.56 | 0.04 | 51497827.12 | 7.91 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.49 | 5.71 | 0.02 | 214851544.87 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.34 | 5.65 | 3.57 | 0.09 | 797527.97 | 7.77 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 3.03 | 2.79 | -0.02 | 1163929.37 | 6.57 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.59 | -0.09 | 606300.95 | 3.41 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 2.04 | -0.03 | 554415.17 | 12.85 | skipped_fast |
| KITEUSDT | IDLE | 2.79 | 6.37 | 2.61 | 0.02 | 85198.46 | 12.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 3.49 | 2.45 | -0.06 | 324515.24 | 24.3 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.85 | -0.06 | 221632.62 | 3.31 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.05 | -0.06 | 147911.25 | 19.35 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.44 | 0.03 | 56420.14 | 23.62 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.0 | 9835.08 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.58 | -0.01 | 140445.06 | 42.71 | skipped_fast |
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
