# Hulk DIGEST — 2026-10-19T11:57:35Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.01 | 1.83 | 1.25 | 0.01 | 33025698.44 | 2.3 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.39 | 0.97 | 0.0 | 150029028.31 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.24 | 0.91 | 0.0 | 334493499.55 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 4.32 | 3.76 | -0.07 | 1004613.25 | 1.36 | skipped_fast |
| WUSDT | IDLE | 1.55 | 2.79 | 2.06 | -0.05 | 524252.03 | 14.95 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 2.97 | 2.6 | -0.06 | 713487.4 | 2.41 | skipped_fast |
| EDELUSDT | IDLE | 2.24 | 4.55 | 2.8 | 0.02 | 238760.75 | 18.49 | skipped_fast |
| KITEUSDT | IDLE | 2.28 | 4.38 | 1.25 | 0.03 | 63045.73 | 11.02 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.58 | 0.4 | 0.02 | 328326.91 | 6.78 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.1 | 3.03 | 0.0 | 87080.3 | 9.55 | skipped_fast |
| RWAINCUSDT | IDLE | 1.62 | 4.95 | 1.71 | -0.0 | 88756.19 | 21.11 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.54 | 2.01 | -0.02 | 72639.0 | 4.28 | skipped_fast |
| ZBCNUSDT | IDLE | 0.53 | 1.99 | 0.22 | 0.02 | 280147.04 | 13.03 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 2.28 | 1.65 | -0.01 | 77055.69 | 7.37 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 4.84 | 3.6 | -0.05 | 60081.84 | 50.8 | skipped_fast |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
