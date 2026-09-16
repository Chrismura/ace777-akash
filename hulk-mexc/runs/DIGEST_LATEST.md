# Hulk DIGEST — 2026-09-16T07:12:39Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 0.81 | 2.92 | 1.49 | -0.08 | 96376049.09 | 1.55 | n/a |
| ETHUSDT | IDLE | 0.51 | 0.94 | 0.48 | -0.03 | 486115218.66 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.43 | 0.82 | 0.31 | -0.02 | 613287086.34 | 0.0 | no_map |
| EDELUSDT | IDLE | 1.44 | 21.93 | 10.91 | 0.45 | 435307.51 | 7.53 | no_map |
| PYTHUSDT | IDLE | 2.01 | 3.73 | 1.88 | -0.03 | 668083.34 | 3.76 | tvl≈119,616,356 |
| RIZEUSDT | IDLE | 2.51 | 29.97 | 2.36 | 0.43 | 42930.45 | 100.5 | no_map |
| CCUSDT | IDLE | 1.13 | 2.05 | 1.41 | -0.04 | 405611.97 | 9.89 | no_map |
| REDUSDT | IDLE | 1.99 | 4.36 | 2.41 | -0.01 | 69289.06 | 13.58 | tvl≈2,392,981 |
| WUSDT | IDLE | 1.03 | 2.06 | 1.45 | -0.08 | 204514.47 | 7.79 | tvl≈1,401,950,706 |
| BIOUSDT | IDLE | 1.53 | 2.83 | 1.47 | -0.03 | 79572.1 | 8.08 | n/a |
| KITEUSDT | IDLE | 1.48 | 2.71 | 1.67 | -0.06 | 61048.87 | 13.92 | no_map |
| CHIPUSDT | IDLE | 1.09 | 3.55 | 2.78 | -0.09 | 114105.52 | 21.53 | no_map |
| ZBCNUSDT | IDLE | 0.66 | 2.34 | 0.52 | -0.04 | 234613.59 | 29.16 | n/a |
| HBARUSDT | IDLE | 0.72 | 1.46 | 0.35 | -0.03 | 464615.31 | 1.34 | empty_tvl |
| RWAINCUSDT | IDLE | 0.61 | 1.09 | 0.91 | -0.03 | 13019.77 | 5.74 | no_map |
| TELUSDT | IDLE | 1.12 | 2.54 | 0.4 | -0.06 | 104913.15 | 26.9 | no_map |
| QNTUSDT | IDLE | 1.21 | 2.18 | 1.56 | -0.05 | 43583.87 | 9.99 | n/a |
| FLUIDUSDT | IDLE | 0.26 | 0.45 | 0.45 | -0.06 | 1334.58 | 21.84 | tvl≈2,626,002,646 |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
