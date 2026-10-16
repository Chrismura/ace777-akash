# Hulk DIGEST — 2026-10-16T11:43:40Z

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
| PYTHUSDT | IDLE | 1.36 | 7.67 | 6.06 | 0.03 | 3889750.56 | 5.59 | tvl≈206,072,259 |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.53 | 6.05 | 5.65 | 0.02 | 1809610.33 | 15.08 | tvl≈1,652,485,183 |
| ETHUSDT | IDLE | 1.1 | 2.12 | 0.57 | 0.05 | 239979325.49 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.81 | 1.58 | 0.33 | 0.03 | 31310841.83 | 1.48 | n/a |
| BTCUSDT | IDLE | 0.68 | 1.33 | 0.23 | 0.02 | 410429439.6 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.35 | 3.89 | 0.97 | 0.06 | 1219869.7 | 1.9 | n/a |
| CCUSDT | IDLE | 2.98 | 5.23 | 4.82 | -0.03 | 428970.79 | 3.86 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 9.55 | 5.54 | -0.02 | 68415.88 | 61.51 | no_map |
| RWAINCUSDT | IDLE | 2.96 | 5.35 | 3.83 | -0.01 | 24763.91 | 14.94 | no_map |
| EDELUSDT | IDLE | 1.97 | 5.31 | 0.26 | -0.0 | 215671.42 | 19.7 | no_map |
| ZBCNUSDT | IDLE | 1.48 | 2.98 | 1.52 | 0.04 | 215928.25 | 26.11 | n/a |
| CHIPUSDT | IDLE | 0.75 | 3.82 | 3.03 | 0.12 | 187060.38 | 10.1 | no_map |
| REDUSDT | IDLE | 1.27 | 4.07 | 0.95 | 0.0 | 88261.14 | 9.25 | tvl≈3,681,377 |
| KITEUSDT | IDLE | 1.42 | 2.74 | 0.63 | 0.03 | 70164.08 | 11.31 | no_map |
| BIOUSDT | IDLE | 0.92 | 1.79 | 0.34 | 0.06 | 69509.34 | 7.67 | n/a |
| HBARUSDT | IDLE | 0.86 | 1.81 | 0.1 | 0.07 | 268837.9 | 5.74 | empty_tvl |
| FLUIDUSDT | IDLE | 1.97 | 3.64 | 1.96 | -0.01 | 8041.97 | 21.4 | tvl≈2,265,195,612 |
| TELUSDT | IDLE | 0.91 | 2.15 | 0.06 | 0.06 | 93933.57 | 5.54 | no_map |
| RWAUSDT | IDLE | 0.4 | 0.79 | 0.08 | 0.02 | 51295.42 | 31.52 | no_map |
| MNSRYUSDT | IDLE | 0.12 | 0.21 | 0.16 | 0.01 | 39020.08 | 21.19 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
