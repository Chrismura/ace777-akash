# Hulk DIGEST — 2026-10-08T10:14:27Z

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
| WUSDT | IDLE | 2.07 | 16.56 | 13.51 | 0.15 | 3783452.33 | 14.38 | tvl≈1,933,634,391 |
| QNTUSDT | IDLE | 1.59 | 3.08 | 1.88 | -0.02 | 2496242.78 | 3.73 | n/a |
| XRPUSDT | IDLE | 0.84 | 1.63 | 0.3 | -0.03 | 39889160.12 | 2.12 | n/a |
| BTCUSDT | IDLE | 0.48 | 0.92 | 0.24 | -0.01 | 559487141.73 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.46 | 0.84 | 0.49 | -0.01 | 380851785.8 | 0.04 | no_map |
| PYTHUSDT | IDLE | 2.09 | 4.39 | 0.76 | 0.05 | 609384.49 | 1.32 | tvl≈164,223,628 |
| EDELUSDT | IDLE | 1.81 | 15.13 | 4.42 | -0.12 | 375762.2 | 14.04 | no_map |
| CCUSDT | IDLE | 2.09 | 4.11 | 0.47 | 0.02 | 404794.82 | 5.84 | no_map |
| HBARUSDT | IDLE | 2.55 | 4.96 | 0.96 | 0.01 | 490197.68 | 8.35 | empty_tvl |
| CHIPUSDT | IDLE | 1.91 | 6.69 | 6.07 | 0.04 | 146563.14 | 13.69 | no_map |
| ZBCNUSDT | IDLE | 1.58 | 3.16 | 0.47 | -0.03 | 283774.11 | 16.35 | n/a |
| REDUSDT | IDLE | 2.14 | 4.14 | 0.91 | 0.02 | 56720.67 | 9.15 | tvl≈3,767,370 |
| KITEUSDT | IDLE | 1.91 | 3.74 | 0.5 | 0.0 | 64551.84 | 8.81 | no_map |
| RIZEUSDT | IDLE | 1.59 | 10.23 | 2.02 | -0.01 | 52228.24 | 34.42 | no_map |
| BIOUSDT | IDLE | 1.62 | 3.33 | 1.43 | 0.03 | 69010.79 | 6.75 | n/a |
| RWAINCUSDT | IDLE | 1.55 | 7.69 | 2.1 | -0.12 | 46623.77 | 65.05 | no_map |
| TELUSDT | IDLE | 1.08 | 1.96 | 1.31 | -0.06 | 126046.34 | 36.0 | no_map |
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
