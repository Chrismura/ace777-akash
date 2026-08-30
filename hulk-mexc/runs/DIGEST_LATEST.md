# Hulk DIGEST — 2026-08-30T13:13:48Z

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
| XRPUSDT | IDLE | 0.76 | 1.48 | 0.28 | 0.01 | 17949726.84 | 2.14 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.11 | 0.21 | 0.01 | 238839117.76 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.46 | 0.86 | 0.38 | 0.01 | 149654149.94 | 0.04 | skipped_fast |
| CHIPUSDT | IDLE | 3.44 | 6.51 | 2.49 | 0.02 | 583044.69 | 2.46 | skipped_fast |
| PYTHUSDT | IDLE | 1.83 | 3.62 | 0.27 | 0.02 | 346097.61 | 2.07 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.77 | 0.65 | 0.04 | 208060.32 | 13.79 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.62 | 0.58 | 0.04 | 287127.61 | 5.88 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 2.62 | 1.03 | 0.01 | 153872.82 | 11.78 | skipped_fast |
| REDUSDT | IDLE | 1.28 | 2.53 | 0.18 | -0.0 | 61424.68 | 11.72 | skipped_fast |
| BIOUSDT | IDLE | 0.69 | 1.36 | 0.15 | 0.01 | 70054.83 | 3.63 | skipped_fast |
| EDELUSDT | IDLE | 0.41 | 7.09 | 0.89 | 0.17 | 115498.82 | 48.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 3.44 | 1.1 | -0.04 | 46789.32 | 34.05 | skipped_fast |
| KITEUSDT | IDLE | 0.6 | 1.33 | 1.23 | -0.01 | 69250.72 | 10.19 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 1.48 | 1.23 | -0.02 | 770.1 | 68.07 | skipped_fast |
| TELUSDT | IDLE | 1.24 | 2.35 | 0.82 | -0.03 | 77837.99 | 35.57 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 1.06 | 0.2 | 0.01 | 147367.73 | 1.33 | skipped_fast |
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
