# Hulk DIGEST — 2026-08-21T20:05:22Z

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
| PYTHUSDT | IDLE | 1.35 | 4.78 | 3.48 | 0.07 | 5463642.78 | 2.12 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.34 | 0.11 | 128897899.91 | 0.73 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.39 | 0.16 | 154371.84 | 18.02 | tvl≈2,358,074 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.54 | 10.86 | 7.73 | 0.08 | 481462.47 | 22.0 | n/a |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.75 | 0.07 | 635296.75 | 8.4 | no_map |
| HBARUSDT | IDLE | 1.78 | 3.23 | 2.73 | 0.05 | 793930.99 | 2.62 | empty_tvl |
| CHIPUSDT | IDLE | 1.36 | 4.81 | 4.21 | 0.08 | 513774.3 | 3.11 | no_map |
| WUSDT | IDLE | 2.16 | 3.92 | 2.63 | 0.05 | 366531.04 | 10.68 | tvl≈1,603,481,943 |
| BIOUSDT | IDLE | 2.59 | 5.33 | 3.65 | 0.0 | 189902.29 | 6.36 | n/a |
| EDELUSDT | IDLE | 2.41 | 4.29 | 3.58 | -0.04 | 79714.87 | 22.47 | no_map |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.61 | 0.01 | 56211.1 | 45.77 | no_map |
| RWAINCUSDT | IDLE | 2.26 | 4.3 | 1.53 | 0.04 | 11069.14 | 86.07 | no_map |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.85 | 0.1 | 61265.94 | 19.64 | no_map |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2867.01 | 63.29 | no_map |
| TELUSDT | IDLE | 1.44 | 3.39 | 2.38 | 0.01 | 183593.23 | 37.97 | no_map |
| QNTUSDT | IDLE | 1.44 | 2.65 | 1.58 | 0.04 | 59930.17 | 6.25 | n/a |
| RWAUSDT | IDLE | 0.64 | 1.16 | 0.82 | 0.04 | 54336.82 | 8.3 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.63 | tvl≈2,554,565,268 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
