# Hulk DIGEST — 2026-08-22T00:47:03Z

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
| PYTHUSDT | IDLE | 2.0 | 7.38 | 0.58 | 0.12 | 6468474.46 | 2.01 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 2.11 | 8.72 | 2.36 | 0.15 | 147424230.75 | 3.46 | n/a |
| HBARUSDT | IDLE | 2.82 | 6.36 | 1.91 | 0.07 | 941063.54 | 1.26 | empty_tvl |
| ZBCNUSDT | IDLE | 2.92 | 11.25 | 3.57 | 0.11 | 543446.43 | 36.08 | n/a |
| CCUSDT | IDLE | 1.96 | 7.42 | 1.42 | 0.14 | 640957.94 | 6.25 | no_map |
| WUSDT | IDLE | 2.73 | 6.91 | 0.85 | 0.09 | 388772.56 | 16.3 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.52 | 0.03 | 548392.9 | 3.06 | no_map |
| BIOUSDT | IDLE | 2.51 | 5.62 | 0.52 | 0.03 | 186334.47 | 3.08 | n/a |
| EDELUSDT | IDLE | 2.56 | 5.5 | 0.98 | -0.01 | 79902.16 | 21.91 | no_map |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 2.5 | 0.13 | 60107.04 | 45.1 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 15.91 | no_map |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.61 | 0.07 | 184163.26 | 25.75 | no_map |
| QNTUSDT | IDLE | 2.57 | 5.42 | 1.51 | 0.06 | 170545.08 | 4.55 | n/a |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.03 | 9754.98 | 32.35 | no_map |
| REDUSDT | IDLE | 0.85 | 7.82 | 0.23 | 0.26 | 158788.72 | 58.79 | tvl≈2,226,572 |
| KITEUSDT | IDLE | 1.07 | 3.12 | 0.38 | 0.1 | 61051.49 | 11.96 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 54862.96 | 16.43 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.68 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
