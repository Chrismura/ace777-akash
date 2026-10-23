# Hulk DIGEST — 2026-10-23T10:46:26Z

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
| XRPUSDT | IDLE | 0.58 | 1.04 | 0.77 | -0.01 | 25827561.39 | 1.51 | n/a |
| ETHUSDT | IDLE | 0.49 | 0.89 | 0.54 | -0.0 | 227704823.63 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.27 | 0.5 | 0.31 | -0.0 | 338739906.84 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.85 | 6.37 | 3.87 | -0.06 | 1007873.92 | 4.37 | n/a |
| WUSDT | IDLE | 2.59 | 4.54 | 4.21 | -0.02 | 608790.5 | 8.99 | tvl≈1,549,124,835 |
| PYTHUSDT | IDLE | 1.97 | 3.51 | 2.86 | -0.05 | 670017.94 | 1.4 | tvl≈162,477,830 |
| ZBCNUSDT | IDLE | 3.59 | 8.19 | 3.27 | -0.03 | 171611.75 | 22.33 | n/a |
| EDELUSDT | IDLE | 1.91 | 3.48 | 2.22 | -0.06 | 402909.47 | 15.78 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.71 | 11.83 | 8.28 | -0.1 | 45171.88 | 34.88 | no_map |
| CHIPUSDT | IDLE | 1.89 | 3.57 | 2.95 | 0.03 | 124930.36 | 19.98 | no_map |
| HBARUSDT | IDLE | 1.93 | 3.44 | 2.83 | -0.02 | 326496.55 | 6.3 | empty_tvl |
| CCUSDT | IDLE | 0.91 | 1.65 | 1.11 | -0.01 | 194515.53 | 3.89 | no_map |
| REDUSDT | IDLE | 1.16 | 2.04 | 1.93 | -0.01 | 82666.49 | 9.32 | tvl≈3,537,570 |
| KITEUSDT | IDLE | 1.04 | 2.05 | 0.21 | 0.01 | 57175.21 | 9.04 | no_map |
| RWAINCUSDT | IDLE | 1.21 | 2.3 | 0.82 | 0.03 | 51509.1 | 33.15 | no_map |
| BIOUSDT | IDLE | 0.76 | 1.39 | 0.83 | 0.0 | 59369.21 | 4.18 | n/a |
| LAUSDT | IDLE | 1.27 | 2.5 | 0.27 | 0.01 | 53929.55 | 23.24 | no_map |
| FLUIDUSDT | IDLE | 1.38 | 2.45 | 2.09 | -0.04 | 9530.15 | 21.21 | tvl≈2,209,600,881 |
| RWAUSDT | IDLE | 0.76 | 1.43 | 0.63 | 0.0 | 51952.71 | 15.75 | no_map |
| IOTAUSDT | IDLE | 0.65 | 1.23 | 0.51 | -0.0 | 65811.67 | 22.24 | no_map |
| MNSRYUSDT | IDLE | 0.33 | 0.65 | 0.13 | -0.0 | 37790.13 | 65.78 | no_map |
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
