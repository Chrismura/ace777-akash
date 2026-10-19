# Hulk DIGEST — 2026-10-19T21:04:30Z

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
| XRPUSDT | IDLE | 0.45 | 0.85 | 0.28 | 0.03 | 23757591.3 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.43 | 0.82 | 0.22 | 0.02 | 141016550.1 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.25 | 0.48 | 0.12 | 0.01 | 348034542.86 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.48 | 4.45 | 3.42 | 0.01 | 850249.86 | 2.76 | tvl≈164,136,048 |
| WUSDT | IDLE | 2.6 | 4.69 | 3.4 | 0.03 | 693293.97 | 13.78 | tvl≈1,555,685,839 |
| QNTUSDT | IDLE | 0.91 | 2.32 | 1.28 | 0.05 | 730378.19 | 1.03 | n/a |
| CCUSDT | IDLE | 0.74 | 1.53 | 0.5 | 0.06 | 416173.2 | 7.69 | no_map |
| EDELUSDT | IDLE | 1.64 | 2.9 | 2.52 | 0.03 | 206819.77 | 15.0 | no_map |
| ZBCNUSDT | IDLE | 0.73 | 2.44 | 2.38 | 0.01 | 251561.4 | 9.21 | n/a |
| CHIPUSDT | IDLE | 1.48 | 3.3 | 1.68 | 0.06 | 78920.92 | 12.04 | no_map |
| KITEUSDT | IDLE | 1.45 | 3.65 | 1.62 | 0.09 | 68195.46 | 10.64 | no_map |
| HBARUSDT | IDLE | 0.74 | 1.35 | 0.87 | -0.01 | 514977.25 | 7.3 | empty_tvl |
| REDUSDT | IDLE | 1.33 | 2.43 | 1.5 | 0.02 | 58249.58 | 8.06 | tvl≈3,443,960 |
| BIOUSDT | IDLE | 1.13 | 2.07 | 1.27 | 0.02 | 69404.37 | 4.28 | n/a |
| RWAINCUSDT | IDLE | 1.02 | 2.01 | 1.92 | 0.04 | 78973.34 | 5.16 | no_map |
| RIZEUSDT | IDLE | 1.02 | 3.65 | 0.53 | -0.05 | 53303.83 | 50.68 | no_map |
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
