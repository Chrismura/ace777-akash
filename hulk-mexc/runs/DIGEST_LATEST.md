# Hulk DIGEST — 2026-08-21T20:01:39Z

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
| PYTHUSDT | IDLE | 1.37 | 4.78 | 4.14 | 0.06 | 5455636.25 | 2.14 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.59 | 0.11 | 128848106.34 | 2.92 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.86 | 0.16 | 154322.86 | 13.98 | tvl≈2,358,074 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 10.86 | 8.84 | 0.07 | 481666.53 | 27.43 | n/a |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.66 | 0.07 | 635011.58 | 9.34 | no_map |
| HBARUSDT | IDLE | 1.81 | 3.23 | 3.13 | 0.05 | 793651.67 | 1.32 | empty_tvl |
| CHIPUSDT | IDLE | 1.37 | 4.81 | 4.41 | 0.08 | 514269.51 | 6.24 | no_map |
| WUSDT | IDLE | 2.21 | 3.92 | 3.28 | 0.04 | 365574.82 | 21.49 | tvl≈1,603,481,943 |
| BIOUSDT | IDLE | 2.66 | 5.33 | 4.66 | -0.01 | 189969.78 | 3.21 | n/a |
| EDELUSDT | IDLE | 2.42 | 4.29 | 3.68 | -0.04 | 79684.82 | 22.52 | no_map |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.54 | 0.02 | 56217.19 | 45.77 | no_map |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.44 | 0.1 | 61378.4 | 11.29 | no_map |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 91.28 | no_map |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2867.01 | 63.29 | no_map |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.59 | 0.01 | 183702.22 | 43.45 | no_map |
| QNTUSDT | IDLE | 1.48 | 2.65 | 2.09 | 0.04 | 59955.1 | 6.29 | n/a |
| RWAUSDT | IDLE | 0.61 | 1.08 | 0.99 | 0.04 | 54309.3 | 8.31 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.14 | 0.07 | 4276.39 | 22.48 | tvl≈2,554,565,268 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
