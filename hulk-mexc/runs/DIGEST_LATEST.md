# Hulk DIGEST — 2026-08-22T08:32:31Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 19.14 | 10.85 | 0.02 | 29226383.49 | 26.11 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 23.87 | 11.38 | 0.11 | 223866038.54 | 3.32 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 15.8 | 10.5 | 0.02 | 1340589.01 | 6.43 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.31 | 24.54 | 12.82 | -0.1 | 682876.02 | 3.38 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.22 | 0.02 | 600980.42 | 10.5 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.05 | -0.05 | 253231.96 | 16.07 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.97 | 0.07 | 155778.04 | 9.71 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.08 | 11.25 | 3.52 | 0.17 | 820264.47 | 6.63 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 8.47 | 6.48 | 0.01 | 535778.04 | 26.11 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.39 | 0.02 | 194000.59 | 9.34 | n/a |
| KITEUSDT | IDLE | 3.82 | 9.68 | 4.29 | 0.06 | 73447.96 | 13.66 | no_map |
| EDELUSDT | IDLE | 2.3 | 4.52 | 3.68 | -0.03 | 86958.58 | 22.45 | no_map |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6716.59 | 21.15 | tvl≈2,562,763,298 |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11110.27 | 118.03 | no_map |
| TELUSDT | IDLE | 1.92 | 4.81 | 4.59 | 0.0 | 173523.2 | 36.26 | no_map |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.02 | 3212.56 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.9 | 0.0 | 52278.8 | 46.13 | no_map |
| RWAUSDT | IDLE | 1.74 | 3.29 | 1.2 | 0.04 | 58325.48 | 8.05 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
