# Hulk DIGEST — 2026-10-26T14:22:39Z

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
| ETHUSDT | IDLE | 0.97 | 1.84 | 0.63 | -0.0 | 123846737.13 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.72 | 1.36 | 0.49 | -0.0 | 289347234.34 | 0.0 | no_map |
| XRPUSDT | IDLE | 0.74 | 1.46 | 0.12 | 0.0 | 21604517.97 | 2.31 | n/a |
| QNTUSDT | IDLE | 2.42 | 12.76 | 2.38 | 0.18 | 1457882.45 | 15.12 | n/a |
| PYTHUSDT | IDLE | 1.57 | 3.05 | 0.65 | 0.07 | 921305.33 | 6.58 | tvl≈167,023,667 |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.62 | 10.88 | 1.24 | 0.12 | 153849.53 | 12.17 | no_map |
| WUSDT | IDLE | 1.41 | 2.8 | 0.17 | 0.02 | 502161.7 | 15.84 | tvl≈1,524,147,089 |
| ZBCNUSDT | IDLE | 1.88 | 4.35 | 3.13 | -0.04 | 216698.84 | 35.03 | n/a |
| CCUSDT | IDLE | 0.98 | 1.75 | 1.37 | -0.0 | 190148.08 | 9.96 | no_map |
| REDUSDT | IDLE | 1.44 | 2.68 | 1.32 | 0.03 | 61638.34 | 16.35 | tvl≈3,686,953 |
| RIZEUSDT | IDLE | 1.81 | 3.33 | 2.0 | -0.0 | 34188.36 | 62.78 | no_map |
| RWAINCUSDT | IDLE | 1.25 | 2.42 | 0.52 | -0.05 | 67019.56 | 17.36 | no_map |
| EDELUSDT | IDLE | 1.0 | 2.24 | 1.17 | 0.09 | 131422.75 | 37.39 | no_map |
| KITEUSDT | IDLE | 1.0 | 1.97 | 0.25 | 0.02 | 53532.27 | 9.68 | no_map |
| BIOUSDT | IDLE | 1.0 | 1.96 | 0.22 | 0.0 | 59771.16 | 13.42 | n/a |
| HBARUSDT | IDLE | 0.75 | 1.42 | 0.56 | 0.01 | 200218.77 | 6.45 | empty_tvl |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.72 | -0.01 | 54076.21 | 24.01 | no_map |
| FLUIDUSDT | IDLE | 0.78 | 1.39 | 1.32 | -0.01 | 2162.6 | 42.19 | tvl≈2,182,061,749 |
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
