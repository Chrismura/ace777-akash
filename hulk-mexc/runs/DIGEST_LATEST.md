# Hulk DIGEST — 2026-10-17T21:02:27Z

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
| XRPUSDT | IDLE | 0.62 | 1.23 | 0.05 | -0.0 | 13332887.02 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.49 | 0.97 | 0.02 | 0.0 | 77583192.43 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.29 | 0.57 | 0.02 | -0.0 | 169495670.12 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.9 | 5.01 | 0.37 | -0.02 | 988771.7 | 1.2 | tvl≈179,398,395 |
| WUSDT | IDLE | 1.78 | 5.3 | 1.81 | -0.03 | 1024320.68 | 17.14 | tvl≈1,591,901,445 |
| QNTUSDT | IDLE | 1.46 | 2.79 | 0.85 | -0.02 | 521635.66 | 0.5 | n/a |
| ZBCNUSDT | IDLE | 1.76 | 3.49 | 0.17 | -0.01 | 195809.17 | 20.21 | n/a |
| CCUSDT | IDLE | 1.06 | 2.02 | 0.64 | 0.02 | 259349.62 | 10.51 | no_map |
| EDELUSDT | IDLE | 1.22 | 2.19 | 1.7 | -0.04 | 151065.61 | 7.04 | no_map |
| HBARUSDT | IDLE | 2.21 | 4.36 | 0.35 | 0.03 | 201569.63 | 1.17 | empty_tvl |
| BIOUSDT | IDLE | 1.34 | 2.62 | 0.41 | -0.02 | 71683.86 | 4.08 | n/a |
| RIZEUSDT | IDLE | 1.47 | 2.8 | 0.92 | -0.02 | 50339.71 | 58.86 | no_map |
| CHIPUSDT | IDLE | 0.9 | 1.67 | 0.86 | -0.04 | 81319.58 | 15.91 | no_map |
| REDUSDT | IDLE | 0.98 | 1.91 | 0.35 | -0.02 | 59729.52 | 14.9 | tvl≈3,487,263 |
| KITEUSDT | IDLE | 0.88 | 1.68 | 0.88 | -0.02 | 65732.16 | 9.35 | no_map |
| RWAINCUSDT | IDLE | 0.89 | 3.31 | 0.1 | 0.07 | 20477.55 | 10.35 | no_map |
| TELUSDT | IDLE | 1.26 | 2.32 | 1.31 | -0.05 | 97874.17 | 18.12 | no_map |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.63 | 0.0 | 50909.22 | 15.87 | no_map |
| FLUIDUSDT | IDLE | 0.76 | 1.51 | 0.0 | 0.0 | 1570.34 | 21.33 | tvl≈2,233,513,283 |
| MNSRYUSDT | IDLE | 0.35 | 0.68 | 0.13 | 0.01 | 31422.27 | 5.63 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
