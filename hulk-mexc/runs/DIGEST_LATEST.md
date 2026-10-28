# Hulk DIGEST — 2026-10-28T07:30:07Z

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
| XRPUSDT | IDLE | 0.87 | 1.53 | 1.45 | 0.02 | 19565537.22 | 2.26 | skipped_fast |
| ETHUSDT | IDLE | 0.44 | 0.78 | 0.62 | 0.02 | 242442159.09 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.44 | 0.33 | 0.02 | 295332769.8 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 2.87 | 2.58 | -0.02 | 365644.48 | 4.16 | skipped_fast |
| WUSDT | IDLE | 0.69 | 1.32 | 1.21 | 0.02 | 616047.38 | 18.01 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 3.51 | 2.42 | -0.04 | 206122.43 | 18.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.01 | 4.04 | 3.36 | -0.08 | 57475.82 | 27.27 | skipped_fast |
| RIZEUSDT | IDLE | 2.44 | 4.52 | 2.46 | 0.03 | 36185.05 | 61.36 | skipped_fast |
| CCUSDT | IDLE | 1.05 | 1.86 | 1.61 | 0.01 | 239538.38 | 10.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.01 | 1.73 | 0.07 | 119184.95 | 12.83 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.79 | 1.64 | -0.01 | 372711.67 | 6.58 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 1.55 | 1.53 | 0.02 | 82043.52 | 8.84 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 1.75 | 1.55 | 0.03 | 60344.18 | 13.72 | skipped_fast |
| REDUSDT | IDLE | 0.82 | 1.64 | 1.33 | 0.04 | 58072.76 | 14.39 | skipped_fast |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
