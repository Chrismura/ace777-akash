# Hulk DIGEST — 2026-08-21T20:27:41Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 2.97 | 0.08 | 5515298.13 | 2.11 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.18 | 0.11 | 129090443.71 | 1.46 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.7 | 0.16 | 153418.26 | 19.48 | tvl≈2,358,074 |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.39 | 0.11 | 478304.57 | 21.47 | n/a |
| CCUSDT | IDLE | 1.46 | 3.91 | 1.27 | 0.08 | 632450.83 | 5.57 | no_map |
| HBARUSDT | IDLE | 1.73 | 3.23 | 2.04 | 0.05 | 800624.85 | 1.3 | empty_tvl |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.64 | 0.08 | 509766.58 | 6.19 | no_map |
| WUSDT | IDLE | 2.1 | 3.92 | 1.9 | 0.06 | 366490.47 | 13.78 | tvl≈1,588,156,646 |
| BIOUSDT | IDLE | 2.52 | 5.33 | 2.64 | 0.02 | 189662.42 | 3.15 | n/a |
| EDELUSDT | IDLE | 2.71 | 4.77 | 4.33 | -0.05 | 80341.3 | 34.03 | no_map |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.65 | 0.01 | 56219.52 | 45.77 | no_map |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10983.46 | 37.5 | no_map |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.6 | 0.1 | 60962.46 | 9.32 | no_map |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | no_map |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.69 | 0.01 | 183886.74 | 16.13 | no_map |
| QNTUSDT | IDLE | 1.48 | 2.65 | 2.03 | 0.03 | 59966.17 | 36.15 | n/a |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.03 | 54165.64 | 24.95 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.28 | tvl≈2,550,535,700 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
