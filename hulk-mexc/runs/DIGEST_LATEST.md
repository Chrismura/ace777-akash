# Hulk DIGEST — 2026-09-06T06:30:00Z

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
| ETHUSDT | IDLE | 0.74 | 1.38 | 0.68 | 0.02 | 213411240.94 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.75 | 1.37 | 0.85 | 0.01 | 24793570.99 | 2.11 | n/a |
| BTCUSDT | IDLE | 0.22 | 0.39 | 0.33 | 0.0 | 383603369.03 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.92 | 5.29 | 3.71 | 0.03 | 431805.84 | 1.82 | tvl≈122,790,024 |
| CHIPUSDT | IDLE | 2.66 | 5.64 | 4.82 | 0.02 | 395079.44 | 5.2 | no_map |
| RWAINCUSDT | IDLE | 2.97 | 5.37 | 3.85 | -0.0 | 9304.2 | 37.75 | no_map |
| RIZEUSDT | IDLE | 1.73 | 11.06 | 5.42 | 0.09 | 115995.72 | 56.07 | no_map |
| CCUSDT | IDLE | 1.16 | 2.12 | 1.31 | 0.02 | 302959.9 | 6.37 | no_map |
| ZBCNUSDT | IDLE | 1.48 | 2.9 | 0.37 | 0.0 | 220339.51 | 21.82 | n/a |
| WUSDT | IDLE | 1.39 | 2.52 | 1.75 | 0.02 | 172824.73 | 10.91 | tvl≈1,663,803,237 |
| EDELUSDT | IDLE | 1.72 | 3.33 | 0.74 | 0.02 | 107156.01 | 27.95 | no_map |
| KITEUSDT | IDLE | 1.65 | 3.06 | 1.62 | -0.02 | 64507.04 | 10.1 | no_map |
| HBARUSDT | IDLE | 1.18 | 2.17 | 1.26 | 0.02 | 449102.31 | 1.23 | empty_tvl |
| REDUSDT | IDLE | 1.45 | 2.67 | 1.52 | 0.0 | 57920.65 | 10.24 | tvl≈2,345,447 |
| BIOUSDT | IDLE | 0.88 | 1.55 | 1.45 | 0.02 | 97542.34 | 3.59 | n/a |
| QNTUSDT | IDLE | 1.62 | 3.09 | 0.97 | 0.04 | 37645.6 | 3.01 | n/a |
| MNSRYUSDT | IDLE | 1.38 | 2.64 | 0.79 | 0.02 | 40764.87 | 8.05 | no_map |
| FLUIDUSDT | IDLE | 1.18 | 2.33 | 0.14 | 0.04 | 380.96 | 21.99 | tvl≈2,661,977,389 |
| RWAUSDT | IDLE | 0.77 | 1.35 | 1.26 | 0.03 | 53038.21 | 14.2 | no_map |
| TELUSDT | IDLE | 0.81 | 1.59 | 0.23 | 0.01 | 73259.88 | 40.66 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
