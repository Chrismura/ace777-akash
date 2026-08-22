# Hulk DIGEST — 2026-08-22T12:47:22Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.81 | 0.09 | 216162625.78 | 1.32 | n/a |
| PYTHUSDT | IDLE | 1.62 | 7.83 | 1.18 | 0.05 | 51599539.25 | 1.97 | tvl≈110,752,782 |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.25 | 0.01 | 1253644.62 | 6.43 | empty_tvl |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.02 | 0.13 | 778395.47 | 8.47 | no_map |
| WUSDT | IDLE | 1.56 | 6.27 | 3.82 | -0.0 | 575475.05 | 10.59 | tvl≈1,571,378,489 |
| ZBCNUSDT | IDLE | 2.19 | 5.77 | 3.41 | 0.0 | 335398.54 | 13.79 | n/a |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 1.98 | -0.11 | 606458.2 | 3.37 | no_map |
| KITEUSDT | IDLE | 2.7 | 6.37 | 1.15 | 0.04 | 84944.98 | 11.53 | no_map |
| EDELUSDT | IDLE | 2.13 | 3.89 | 2.43 | -0.02 | 78204.74 | 22.57 | no_map |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.67 | -0.05 | 238169.9 | 3.23 | n/a |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2395.57 | 67.45 | no_map |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.58 | 0.01 | 152850.38 | 19.62 | tvl≈2,031,082 |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.93 | -0.03 | 163279.99 | 63.76 | no_map |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | no_map |
| RIZEUSDT | IDLE | 0.5 | 2.03 | 0.56 | -0.0 | 46806.5 | 46.13 | no_map |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
