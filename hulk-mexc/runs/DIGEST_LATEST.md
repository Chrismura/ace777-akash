# Hulk DIGEST — 2026-08-21T22:45:54Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.37 | 0.11 | 5864050.8 | 4.1 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.65 | 6.41 | 0.1 | 0.15 | 135586447.67 | 2.07 | n/a |
| CCUSDT | IDLE | 1.88 | 7.44 | 0.16 | 0.15 | 659986.71 | 6.18 | no_map |
| HBARUSDT | IDLE | 2.18 | 4.71 | 0.29 | 0.08 | 872692.07 | 1.26 | empty_tvl |
| ZBCNUSDT | IDLE | 1.89 | 8.12 | 0.14 | 0.13 | 507630.95 | 29.04 | n/a |
| WUSDT | IDLE | 2.55 | 5.94 | 0.14 | 0.09 | 371161.28 | 13.27 | tvl≈1,602,784,605 |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.05 | 0.05 | 533567.54 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.11 | 0.03 | 188065.37 | 3.11 | n/a |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.39 | 0.17 | 156286.13 | 10.57 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.03 | 82554.21 | 21.83 | no_map |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | no_map |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.05 | 186816.65 | 5.17 | no_map |
| QAITUSDT | IDLE | 2.34 | 4.38 | 1.94 | -0.02 | 3835.98 | 67.45 | no_map |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.21 | 0.11 | 61433.88 | 12.02 | no_map |
| QNTUSDT | IDLE | 2.15 | 4.29 | 0.0 | 0.06 | 81848.7 | 1.51 | n/a |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.83 | 0.06 | 56395.39 | 46.99 | no_map |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
