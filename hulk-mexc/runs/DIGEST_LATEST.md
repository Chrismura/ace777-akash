# Hulk DIGEST — 2026-09-11T13:18:46Z

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
| XRPUSDT | IDLE | 2.15 | 4.17 | 0.89 | 0.0 | 41460601.49 | 2.94 | n/a |
| ETHUSDT | IDLE | 1.66 | 3.23 | 0.62 | 0.03 | 470919513.06 | 0.84 | no_map |
| BTCUSDT | IDLE | 1.39 | 2.69 | 0.61 | 0.01 | 508409908.31 | 0.0 | no_map |
| CCUSDT | IDLE | 2.72 | 5.13 | 2.08 | -0.03 | 436838.95 | 11.27 | no_map |
| PYTHUSDT | IDLE | 2.31 | 4.62 | 0.0 | 0.02 | 366305.99 | 1.91 | tvl≈114,862,105 |
| RIZEUSDT | IDLE | 1.2 | 24.77 | 6.46 | 0.17 | 113988.92 | 78.74 | no_map |
| WUSDT | IDLE | 2.01 | 3.91 | 0.76 | 0.0 | 126702.8 | 1.05 | tvl≈1,457,783,021 |
| CHIPUSDT | IDLE | 1.84 | 5.71 | 2.01 | -0.02 | 131119.21 | 15.12 | no_map |
| BIOUSDT | IDLE | 2.02 | 3.9 | 0.95 | 0.0 | 77758.58 | 7.97 | n/a |
| ZBCNUSDT | IDLE | 1.67 | 3.3 | 0.28 | 0.02 | 169631.8 | 15.64 | n/a |
| KITEUSDT | IDLE | 1.89 | 3.5 | 1.83 | 0.01 | 59196.21 | 11.98 | no_map |
| REDUSDT | IDLE | 1.87 | 3.52 | 1.43 | -0.01 | 59557.25 | 10.75 | tvl≈2,196,779 |
| RWAINCUSDT | IDLE | 2.03 | 3.55 | 3.43 | 0.0 | 4943.37 | 67.38 | no_map |
| EDELUSDT | IDLE | 0.61 | 2.87 | 0.93 | -0.05 | 196067.74 | 18.76 | no_map |
| HBARUSDT | IDLE | 1.68 | 3.26 | 0.65 | 0.0 | 184582.75 | 1.33 | empty_tvl |
| TELUSDT | IDLE | 1.7 | 3.22 | 1.25 | -0.01 | 97365.4 | 34.48 | no_map |
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
