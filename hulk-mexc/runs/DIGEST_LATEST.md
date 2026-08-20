# Hulk DIGEST — 2026-08-20T07:22:46Z

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
| XRPUSDT | IDLE | 0.74 | 2.43 | 0.32 | 0.11 | 47237151.97 | 0.9 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 24.94 | 5.13 | 0.3 | 168405.45 | 26.9 | tvl≈1,819,284 |
| CHIPUSDT | IDLE | 1.77 | 7.39 | 4.32 | 0.12 | 227480.23 | 3.48 | no_map |
| CCUSDT | IDLE | 0.95 | 3.18 | 0.93 | 0.12 | 388892.8 | 7.95 | no_map |
| EDELUSDT | IDLE | 1.44 | 11.01 | 8.1 | 0.23 | 101572.56 | 22.0 | no_map |
| BIOUSDT | IDLE | 1.27 | 6.88 | 0.26 | 0.21 | 181267.54 | 3.33 | n/a |
| ZBCNUSDT | IDLE | 0.96 | 3.83 | 1.11 | 0.14 | 233035.75 | 14.47 | n/a |
| WUSDT | IDLE | 0.78 | 1.63 | 0.79 | 0.06 | 284493.53 | 16.31 | tvl≈1,460,644,153 |
| PYTHUSDT | IDLE | 0.49 | 1.47 | 0.54 | 0.1 | 306031.76 | 4.69 | tvl≈95,798,707 |
| HBARUSDT | IDLE | 1.25 | 2.35 | 0.95 | 0.05 | 370768.89 | 1.4 | empty_tvl |
| RIZEUSDT | IDLE | 2.08 | 13.97 | 7.51 | 0.14 | 62834.76 | 211.53 | no_map |
| KITEUSDT | IDLE | 0.86 | 1.51 | 1.35 | 0.05 | 59925.69 | 10.47 | no_map |
| QAITUSDT | IDLE | 1.26 | 3.52 | 1.42 | 0.05 | 10706.0 | 64.48 | no_map |
| RWAINCUSDT | IDLE | 0.69 | 1.88 | 1.57 | 0.04 | 17321.68 | 34.09 | no_map |
| TELUSDT | IDLE | 0.51 | 2.31 | 1.28 | 0.11 | 192285.76 | 68.13 | no_map |
| QNTUSDT | IDLE | 0.73 | 1.42 | 0.24 | 0.05 | 37111.76 | 11.8 | n/a |
| FLUIDUSDT | IDLE | 0.74 | 2.01 | 0.12 | 0.08 | 3551.44 | 22.09 | tvl≈2,489,705,199 |
| RWAUSDT | IDLE | 0.44 | 0.78 | 0.69 | 0.02 | 53648.65 | 17.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
