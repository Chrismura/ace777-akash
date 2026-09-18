# Hulk DIGEST — 2026-09-18T09:27:53Z

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
| ETHUSDT | IDLE | 1.05 | 2.05 | 0.31 | 0.03 | 365380788.91 | 0.04 | no_map |
| XRPUSDT | IDLE | 1.04 | 2.01 | 0.44 | 0.02 | 40628255.2 | 2.25 | n/a |
| BTCUSDT | IDLE | 0.84 | 1.63 | 0.3 | 0.02 | 553056791.67 | 0.0 | no_map |
| CCUSDT | IDLE | 1.74 | 5.8 | 1.43 | 0.09 | 656092.85 | 10.78 | no_map |
| PYTHUSDT | IDLE | 0.78 | 2.59 | 0.33 | 0.12 | 629080.08 | 4.94 | tvl≈135,621,931 |
| WUSDT | IDLE | 1.25 | 3.66 | 0.67 | 0.1 | 383823.66 | 9.76 | tvl≈1,552,339,763 |
| CHIPUSDT | IDLE | 1.41 | 6.85 | 2.02 | 0.12 | 152657.62 | 15.99 | no_map |
| BIOUSDT | IDLE | 1.83 | 4.06 | 0.7 | 0.07 | 79459.65 | 3.71 | n/a |
| KITEUSDT | IDLE | 1.91 | 3.58 | 1.62 | 0.03 | 73785.87 | 11.91 | no_map |
| ZBCNUSDT | IDLE | 1.03 | 2.04 | 0.12 | 0.04 | 249866.32 | 22.18 | n/a |
| REDUSDT | IDLE | 1.7 | 3.52 | 0.2 | 0.06 | 67996.2 | 16.48 | tvl≈2,500,114 |
| HBARUSDT | IDLE | 1.13 | 2.22 | 0.24 | 0.05 | 455559.89 | 1.29 | empty_tvl |
| TELUSDT | IDLE | 2.99 | 6.01 | 0.73 | 0.04 | 82977.97 | 39.87 | no_map |
| RWAINCUSDT | IDLE | 1.71 | 3.4 | 0.18 | -0.01 | 10570.29 | 23.54 | no_map |
| EDELUSDT | IDLE | 0.44 | 4.61 | 0.55 | -0.06 | 263031.3 | 33.94 | no_map |
| QNTUSDT | IDLE | 1.02 | 1.79 | 1.69 | 0.01 | 45580.63 | 9.64 | n/a |
| RIZEUSDT | IDLE | 0.26 | 3.41 | 1.33 | 0.07 | 54670.24 | 106.25 | no_map |
| MNSRYUSDT | IDLE | 0.5 | 0.98 | 0.16 | 0.03 | 43117.45 | 4.09 | no_map |
| RWAUSDT | IDLE | 0.54 | 1.04 | 0.29 | 0.01 | 57497.39 | 29.54 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 148.34 | 20.86 | tvl≈2,620,474,605 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
