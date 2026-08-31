# Hulk DIGEST — 2026-08-31T02:15:45Z

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
| XRPUSDT | IDLE | 2.8 | 5.09 | 3.45 | -0.03 | 33809913.17 | 1.48 | n/a |
| ETHUSDT | IDLE | 2.36 | 4.32 | 2.7 | -0.01 | 377278396.65 | 0.12 | no_map |
| BTCUSDT | IDLE | 1.25 | 2.34 | 1.02 | -0.0 | 379654894.39 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.96 | 5.84 | 4.45 | -0.02 | 494716.83 | 2.14 | tvl≈109,675,290 |
| CHIPUSDT | IDLE | 2.07 | 6.38 | 3.46 | -0.04 | 524340.11 | 2.6 | no_map |
| WUSDT | IDLE | 3.35 | 6.33 | 3.39 | 0.0 | 238540.47 | 12.04 | tvl≈1,502,119,397 |
| BIOUSDT | IDLE | 3.37 | 6.22 | 3.63 | -0.05 | 88700.33 | 3.8 | n/a |
| EDELUSDT | IDLE | 2.89 | 6.32 | 4.18 | 0.05 | 82170.79 | 16.75 | no_map |
| CCUSDT | IDLE | 2.31 | 4.26 | 2.45 | -0.02 | 225803.49 | 6.88 | no_map |
| KITEUSDT | IDLE | 2.66 | 7.34 | 4.08 | -0.07 | 91116.0 | 9.19 | no_map |
| ZBCNUSDT | IDLE | 1.89 | 4.62 | 3.05 | -0.05 | 218803.13 | 13.83 | n/a |
| REDUSDT | IDLE | 2.37 | 4.49 | 1.65 | -0.0 | 62741.05 | 20.24 | tvl≈2,002,827 |
| RIZEUSDT | IDLE | 2.62 | 4.92 | 2.12 | -0.03 | 39670.78 | 50.64 | no_map |
| FLUIDUSDT | IDLE | 3.47 | 6.19 | 4.98 | -0.02 | 3849.88 | 21.82 | tvl≈2,605,552,080 |
| TELUSDT | IDLE | 2.75 | 4.91 | 3.94 | -0.0 | 82764.1 | 35.63 | no_map |
| HBARUSDT | IDLE | 1.76 | 3.19 | 2.19 | -0.02 | 214856.39 | 1.36 | empty_tvl |
| RWAINCUSDT | IDLE | 1.46 | 2.55 | 2.49 | 0.0 | 2191.44 | 90.34 | no_map |
| QNTUSDT | IDLE | 1.52 | 2.79 | 1.73 | -0.02 | 37800.78 | 9.97 | n/a |
| RWAUSDT | IDLE | 0.79 | 1.39 | 1.21 | 0.0 | 53009.91 | 24.4 | no_map |
| MNSRYUSDT | IDLE | 1.02 | 1.85 | 1.2 | -0.0 | 31881.22 | 60.93 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
