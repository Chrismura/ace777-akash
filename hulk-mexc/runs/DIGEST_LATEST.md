# Hulk DIGEST — 2026-08-16T18:06:06Z

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
| XRPUSDT | IDLE | 0.22 | 0.39 | 0.38 | -0.0 | 5136357.37 | 1.0 | n/a |
| CHIPUSDT | IDLE | 1.98 | 10.74 | 7.8 | 0.13 | 283480.88 | 6.98 | no_map |
| CCUSDT | IDLE | 1.44 | 2.74 | 2.23 | -0.04 | 338930.43 | 8.39 | no_map |
| ZBCNUSDT | IDLE | 1.61 | 2.92 | 2.02 | -0.0 | 191607.57 | 3.83 | n/a |
| WUSDT | IDLE | 1.1 | 1.93 | 1.85 | 0.02 | 167286.97 | 15.21 | tvl≈1,362,509,768 |
| RIZEUSDT | IDLE | 1.8 | 3.43 | 1.11 | -0.02 | 49742.78 | 62.01 | no_map |
| EDELUSDT | IDLE | 1.27 | 2.4 | 0.91 | -0.01 | 60735.22 | 39.4 | no_map |
| QAITUSDT | IDLE | 1.56 | 4.87 | 1.28 | -0.04 | 2707.17 | 61.66 | no_map |
| PYTHUSDT | IDLE | 0.67 | 1.22 | 0.76 | -0.01 | 121604.14 | 2.54 | tvl≈88,941,988 |
| BIOUSDT | IDLE | 0.77 | 1.34 | 1.33 | -0.01 | 62504.83 | 4.07 | n/a |
| RWAINCUSDT | IDLE | 1.47 | 4.0 | 2.29 | 0.07 | 9960.01 | 73.72 | no_map |
| KITEUSDT | IDLE | 0.49 | 0.9 | 0.47 | -0.02 | 57317.76 | 11.65 | no_map |
| REDUSDT | IDLE | 0.14 | 1.18 | 1.09 | -0.04 | 88957.16 | 24.11 | tvl≈1,593,982 |
| TELUSDT | IDLE | 0.97 | 1.88 | 0.41 | -0.03 | 96830.58 | 48.09 | no_map |
| QNTUSDT | IDLE | 0.55 | 0.98 | 0.76 | -0.01 | 32438.66 | 3.5 | n/a |
| HBARUSDT | IDLE | 0.3 | 0.55 | 0.38 | -0.01 | 75695.02 | 1.53 | empty_tvl |
| RWAUSDT | IDLE | 0.42 | 0.79 | 0.35 | -0.0 | 52051.64 | 17.47 | no_map |
| FLUIDUSDT | IDLE | 0.49 | 0.92 | 0.4 | 0.02 | 229.44 | 20.99 | tvl≈2,305,667,636 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
