# Hulk DIGEST — 2026-08-21T20:42:20Z

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
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.54 | 0.08 | 5544420.77 | 2.1 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.34 | 0.1 | 128914126.29 | 2.91 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.31 | 0.17 | 152987.35 | 11.31 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.77 | 0.12 | 478612.44 | 31.57 | n/a |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.23 | 0.09 | 641225.62 | 9.21 | no_map |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.86 | 0.05 | 809878.52 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.32 | 4.81 | 2.98 | 0.09 | 514458.61 | 3.07 | no_map |
| WUSDT | IDLE | 2.08 | 3.92 | 1.56 | 0.06 | 367575.21 | 19.01 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.54 | 5.33 | 2.94 | 0.0 | 189199.33 | 3.16 | n/a |
| EDELUSDT | IDLE | 2.77 | 5.01 | 3.9 | -0.05 | 81419.12 | 67.49 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10892.53 | 26.77 | no_map |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.66 | 0.02 | 56268.08 | 47.09 | no_map |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.39 | 0.11 | 60917.75 | 13.96 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.01 | 2767.35 | 67.05 | no_map |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 181519.32 | 26.83 | no_map |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.68 | 0.04 | 59885.73 | 9.39 | n/a |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53899.79 | 8.31 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 20.09 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
