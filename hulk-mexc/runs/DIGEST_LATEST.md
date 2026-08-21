# Hulk DIGEST — 2026-08-21T23:49:44Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.57 | 0.1 | 6187019.51 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.27 | 0.15 | 141807124.57 | 0.69 | n/a |
| ZBCNUSDT | IDLE | 2.87 | 11.25 | 2.22 | 0.13 | 514244.78 | 19.73 | n/a |
| HBARUSDT | IDLE | 2.61 | 6.36 | 0.95 | 0.09 | 906943.91 | 1.25 | empty_tvl |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.1 | 0.13 | 644766.93 | 8.89 | no_map |
| WUSDT | IDLE | 2.78 | 6.91 | 1.95 | 0.08 | 378269.81 | 16.48 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.31 | 0.03 | 546893.91 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.11 | 0.02 | 186647.37 | 3.11 | n/a |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.3 | 0.0 | 80173.07 | 22.0 | no_map |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.89 | 0.12 | 58842.58 | 46.13 | no_map |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.31 | 0.07 | 190428.81 | 25.66 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.89 | 0.18 | 157885.68 | 13.75 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.04 | 0.08 | 148493.19 | 1.49 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10306.4 | 53.56 | no_map |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.93 | 0.1 | 61358.81 | 37.12 | no_map |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.03 | 54543.66 | 16.37 | no_map |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 19.83 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
