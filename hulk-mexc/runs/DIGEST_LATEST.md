# Hulk DIGEST — 2026-09-11T00:15:32Z

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
| XRPUSDT | IDLE | 1.2 | 2.22 | 1.17 | -0.04 | 42422890.43 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 0.84 | 1.55 | 0.92 | -0.01 | 423933330.75 | 0.49 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.11 | 0.67 | -0.02 | 547199104.66 | 0.06 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 10.01 | 7.88 | -0.09 | 100056.77 | 15.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 2.94 | 2.3 | -0.01 | 431054.28 | 1.95 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 2.52 | 1.32 | -0.06 | 477268.95 | 7.1 | skipped_fast |
| ZBCNUSDT | IDLE | 2.27 | 4.05 | 3.3 | -0.02 | 204521.43 | 22.41 | skipped_fast |
| RIZEUSDT | IDLE | 0.61 | 34.58 | 3.79 | -0.43 | 136763.45 | 96.79 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 5.04 | 4.62 | -0.03 | 235885.41 | 18.62 | skipped_fast |
| BIOUSDT | IDLE | 1.64 | 2.97 | 2.01 | -0.04 | 77822.0 | 8.05 | skipped_fast |
| WUSDT | IDLE | 1.18 | 2.17 | 1.23 | -0.05 | 169596.32 | 15.71 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.62 | 2.19 | -0.05 | 56847.65 | 12.02 | skipped_fast |
| REDUSDT | IDLE | 0.69 | 1.33 | 0.74 | -0.07 | 66896.53 | 18.99 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 2.5 | 1.88 | -0.01 | 86017.59 | 5.64 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 2.98 | 2.27 | -0.04 | 36714.09 | 13.96 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.67 | 0.95 | -0.02 | 193336.66 | 1.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.84 | 3.26 | 2.78 | -0.06 | 2252.37 | 21.5 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.24 | 0.28 | 0.01 | 4454.55 | 61.4 | skipped_fast |
| RWAUSDT | IDLE | 0.79 | 1.38 | 1.28 | -0.03 | 50766.08 | 15.3 | skipped_fast |
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
