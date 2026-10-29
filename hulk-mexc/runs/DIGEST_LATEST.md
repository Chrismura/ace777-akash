# Hulk DIGEST — 2026-10-29T17:51:37Z

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
| ETHUSDT | IDLE | 1.55 | 2.84 | 1.75 | -0.0 | 277541860.37 | 0.09 | no_map |
| XRPUSDT | IDLE | 1.4 | 2.5 | 1.97 | -0.02 | 26311118.14 | 2.32 | n/a |
| BTCUSDT | IDLE | 1.37 | 2.53 | 1.4 | 0.0 | 398319130.71 | 0.0 | no_map |
| CCUSDT | IDLE | 2.78 | 6.2 | 3.28 | 0.02 | 390550.01 | 8.86 | no_map |
| WUSDT | IDLE | 1.98 | 3.53 | 2.93 | -0.04 | 403875.39 | 8.17 | tvl≈1,524,705,634 |
| HBARUSDT | IDLE | 1.9 | 3.38 | 2.84 | -0.02 | 464455.89 | 8.15 | empty_tvl |
| ZBCNUSDT | IDLE | 1.22 | 2.33 | 0.77 | 0.01 | 230202.11 | 11.59 | n/a |
| REDUSDT | IDLE | 1.66 | 3.05 | 1.74 | -0.01 | 63628.15 | 14.66 | tvl≈3,793,287 |
| RIZEUSDT | IDLE | 0.84 | 1.55 | 0.9 | -0.02 | 67315.48 | 65.54 | no_map |
| PYTHUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| BIOUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
