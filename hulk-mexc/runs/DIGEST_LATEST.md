# Hulk DIGEST — 2026-08-28T02:07:08Z

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
| PYTHUSDT | IDLE | 1.56 | 3.89 | 1.42 | 0.02 | 22771578.43 | 2.03 | tvl≈109,767,013 |
| XRPUSDT | IDLE | 1.19 | 2.11 | 1.75 | 0.02 | 53653008.24 | 2.07 | n/a |
| QAITUSDT | IDLE | 1.03 | 49.9 | 31.75 | -0.2 | 59623.07 | 65.18 | no_map |
| CHIPUSDT | IDLE | 1.15 | 6.73 | 0.2 | 0.15 | 799360.18 | 2.44 | no_map |
| CCUSDT | IDLE | 1.82 | 3.43 | 1.35 | -0.02 | 458035.93 | 7.91 | no_map |
| RWAINCUSDT | IDLE | 2.3 | 8.19 | 4.04 | -0.02 | 22382.43 | 10.69 | no_map |
| KITEUSDT | IDLE | 2.38 | 4.64 | 0.84 | 0.02 | 74609.53 | 19.19 | no_map |
| REDUSDT | IDLE | 1.83 | 3.65 | 0.04 | 0.04 | 81369.29 | 11.57 | tvl≈2,008,376 |
| WUSDT | IDLE | 1.33 | 2.45 | 1.42 | 0.02 | 183052.03 | 12.39 | tvl≈1,590,823,184 |
| BIOUSDT | IDLE | 1.43 | 2.54 | 2.14 | 0.03 | 97857.4 | 10.27 | n/a |
| ZBCNUSDT | IDLE | 0.82 | 2.75 | 1.77 | 0.08 | 237402.08 | 22.62 | n/a |
| RIZEUSDT | IDLE | 0.74 | 9.33 | 1.56 | -0.16 | 112984.7 | 50.82 | no_map |
| HBARUSDT | IDLE | 0.8 | 1.4 | 1.27 | 0.01 | 328999.21 | 1.27 | empty_tvl |
| TELUSDT | IDLE | 1.32 | 2.49 | 1.91 | 0.03 | 122217.02 | 36.93 | no_map |
| EDELUSDT | IDLE | 0.43 | 3.18 | 2.58 | 0.11 | 29168.14 | 68.2 | no_map |
| QNTUSDT | IDLE | 0.68 | 1.19 | 1.13 | -0.01 | 44152.93 | 6.36 | n/a |
| RWAUSDT | IDLE | 0.61 | 1.17 | 0.33 | 0.01 | 54276.73 | 8.27 | no_map |
| FLUIDUSDT | IDLE | 0.35 | 1.1 | 0.12 | -0.0 | 8387.32 | 21.06 | tvl≈2,619,418,206 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
