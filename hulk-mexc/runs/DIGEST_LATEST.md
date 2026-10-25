# Hulk DIGEST — 2026-10-25T09:00:40Z

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
| XRPUSDT | IDLE | 0.99 | 1.75 | 1.51 | 0.01 | 25264052.17 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.9 | 1.58 | 1.45 | -0.01 | 128003813.93 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.78 | 0.74 | -0.0 | 208348373.43 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.83 | 3.22 | 2.92 | -0.06 | 787180.51 | 14.23 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 3.26 | 2.84 | -0.0 | 494525.02 | 2.86 | skipped_fast |
| EDELUSDT | IDLE | 0.94 | 2.18 | 1.87 | -0.07 | 564518.68 | 20.12 | skipped_fast |
| KITEUSDT | IDLE | 1.99 | 3.47 | 3.34 | -0.06 | 58652.9 | 19.95 | skipped_fast |
| QNTUSDT | IDLE | 1.77 | 3.12 | 2.86 | 0.01 | 373473.95 | 2.21 | skipped_fast |
| BIOUSDT | IDLE | 1.83 | 3.21 | 3.02 | -0.04 | 65217.23 | 9.03 | skipped_fast |
| RWAINCUSDT | IDLE | 1.85 | 3.39 | 2.1 | -0.01 | 57085.65 | 5.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 4.54 | 4.06 | 0.03 | 88203.03 | 18.37 | skipped_fast |
| CCUSDT | IDLE | 1.22 | 2.13 | 2.03 | -0.04 | 199879.05 | 10.05 | skipped_fast |
| REDUSDT | IDLE | 1.73 | 4.1 | 3.78 | -0.04 | 80977.69 | 46.83 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 1.73 | 1.56 | 0.01 | 231726.45 | 14.93 | skipped_fast |
| HBARUSDT | IDLE | 1.13 | 1.98 | 1.82 | 0.01 | 216055.28 | 14.25 | skipped_fast |
| FLUIDUSDT | IDLE | 1.66 | 2.89 | 2.8 | -0.05 | 7691.86 | 21.18 | skipped_fast |
| RIZEUSDT | IDLE | 0.24 | 0.65 | 0.39 | -0.04 | 41408.1 | 64.7 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.52 | 0.63 | 0.0 | 52000.94 | 39.48 | skipped_fast |
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
