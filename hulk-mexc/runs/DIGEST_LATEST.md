# Hulk DIGEST — 2026-09-23T13:18:54Z

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
| XRPUSDT | IDLE | 2.38 | 4.29 | 3.47 | 0.01 | 121754907.75 | 2.56 | n/a |
| PYTHUSDT | IDLE | 1.11 | 4.33 | 2.23 | 0.05 | 1965112.78 | 7.47 | tvl≈150,879,290 |
| HBARUSDT | IDLE | 2.92 | 5.17 | 4.47 | -0.02 | 1716421.34 | 3.19 | empty_tvl |
| ETHUSDT | IDLE | 0.88 | 1.58 | 1.26 | -0.01 | 422702693.71 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.65 | 1.17 | 0.91 | -0.01 | 837616409.43 | 0.0 | no_map |
| WUSDT | IDLE | 1.75 | 3.15 | 2.34 | 0.02 | 386679.66 | 5.78 | tvl≈1,769,454,895 |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 10.33 | 8.68 | 0.04 | 158081.91 | 58.0 | no_map |
| ZBCNUSDT | IDLE | 1.8 | 4.16 | 3.39 | 0.02 | 239076.48 | 23.26 | n/a |
| CCUSDT | IDLE | 0.93 | 1.68 | 1.23 | -0.04 | 417755.63 | 8.93 | no_map |
| CHIPUSDT | IDLE | 1.59 | 3.05 | 0.89 | -0.02 | 190668.16 | 13.1 | no_map |
| KITEUSDT | IDLE | 1.62 | 3.03 | 1.46 | 0.02 | 150497.87 | 10.25 | no_map |
| EDELUSDT | IDLE | 1.02 | 3.78 | 3.58 | -0.11 | 231545.3 | 40.55 | no_map |
| BIOUSDT | IDLE | 1.39 | 2.5 | 1.91 | 0.02 | 120285.97 | 10.09 | n/a |
| QNTUSDT | IDLE | 2.16 | 3.88 | 2.96 | -0.0 | 191071.11 | 2.72 | n/a |
| REDUSDT | IDLE | 1.5 | 2.67 | 2.17 | 0.03 | 60040.52 | 9.98 | tvl≈2,919,731 |
| RWAINCUSDT | IDLE | 0.98 | 2.23 | 1.22 | 0.03 | 19233.12 | 5.38 | no_map |
| RIZEUSDT | IDLE | 0.23 | 3.97 | 2.55 | 0.54 | 64721.97 | 32.35 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 1.85 | 1.82 | 0.0 | 4410.07 | 21.98 | tvl≈2,635,539,142 |
| RWAUSDT | IDLE | 0.42 | 0.73 | 0.72 | 0.0 | 54266.38 | 14.5 | no_map |
| MNSRYUSDT | IDLE | 0.72 | 1.27 | 1.14 | -0.01 | 40726.11 | 71.02 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
