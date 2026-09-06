# Hulk DIGEST — 2026-09-06T07:30:07Z

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
| XRPUSDT | IDLE | 0.91 | 1.65 | 1.1 | 0.01 | 25755971.12 | 2.12 | n/a |
| ETHUSDT | IDLE | 0.88 | 1.61 | 1.06 | 0.02 | 226787219.96 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.33 | 0.0 | 387311515.2 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.95 | 5.29 | 4.11 | 0.02 | 416804.79 | 3.65 | tvl≈122,790,024 |
| CHIPUSDT | IDLE | 2.31 | 4.92 | 3.99 | -0.02 | 406650.19 | 1.73 | no_map |
| ZBCNUSDT | IDLE | 1.52 | 3.0 | 0.28 | -0.0 | 225882.43 | 13.82 | n/a |
| CCUSDT | IDLE | 1.06 | 1.91 | 1.38 | 0.01 | 302495.89 | 6.39 | no_map |
| RIZEUSDT | IDLE | 1.38 | 7.54 | 6.59 | 0.01 | 98348.38 | 28.41 | no_map |
| WUSDT | IDLE | 1.41 | 2.57 | 1.68 | 0.01 | 172025.57 | 13.91 | tvl≈1,664,853,708 |
| RWAINCUSDT | IDLE | 2.33 | 4.51 | 0.99 | 0.03 | 9383.1 | 47.36 | no_map |
| BIOUSDT | IDLE | 1.53 | 2.76 | 2.02 | 0.01 | 97043.26 | 3.61 | n/a |
| HBARUSDT | IDLE | 1.18 | 2.1 | 1.73 | 0.01 | 439794.92 | 1.24 | empty_tvl |
| KITEUSDT | IDLE | 1.5 | 2.72 | 1.92 | -0.03 | 64406.13 | 12.47 | no_map |
| EDELUSDT | IDLE | 1.33 | 2.46 | 1.29 | 0.01 | 73697.31 | 18.69 | no_map |
| REDUSDT | IDLE | 0.98 | 1.85 | 0.7 | 0.0 | 62458.88 | 10.27 | tvl≈2,345,447 |
| QNTUSDT | IDLE | 1.68 | 3.09 | 1.86 | 0.03 | 39022.41 | 6.07 | n/a |
| MNSRYUSDT | IDLE | 1.37 | 2.57 | 1.16 | 0.01 | 41338.12 | 22.93 | no_map |
| TELUSDT | IDLE | 0.7 | 1.29 | 0.75 | 0.0 | 72440.53 | 46.76 | no_map |
| RWAUSDT | IDLE | 0.49 | 0.85 | 0.85 | 0.02 | 52537.16 | 21.38 | no_map |
| FLUIDUSDT | IDLE | 0.47 | 0.91 | 0.14 | 0.03 | 358.09 | 21.31 | tvl≈2,663,697,145 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
