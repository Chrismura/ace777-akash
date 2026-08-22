# Hulk DIGEST — 2026-08-22T15:11:02Z

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
| PYTHUSDT | IDLE | 1.6 | 7.62 | 2.12 | 0.03 | 51476475.06 | 1.99 | tvl≈110,752,782 |
| XRPUSDT | IDLE | 1.36 | 7.49 | 6.07 | 0.02 | 214568536.35 | 2.09 | n/a |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.71 | 0.11 | 801547.15 | 6.0 | no_map |
| HBARUSDT | IDLE | 0.81 | 2.85 | 2.4 | -0.02 | 1172934.4 | 5.24 | empty_tvl |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.86 | -0.11 | 614774.38 | 3.41 | no_map |
| WUSDT | IDLE | 0.79 | 3.17 | 2.01 | -0.02 | 562398.99 | 8.57 | tvl≈1,572,799,710 |
| KITEUSDT | IDLE | 2.78 | 6.37 | 2.36 | 0.03 | 85039.11 | 10.79 | no_map |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.55 | -0.07 | 324952.87 | 21.01 | n/a |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.17 | -0.06 | 225127.26 | 3.32 | n/a |
| REDUSDT | IDLE | 0.49 | 5.19 | 4.94 | -0.04 | 150655.3 | 11.05 | tvl≈2,031,082 |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.05 | 79080.44 | 34.19 | no_map |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | no_map |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.37 | 0.04 | 46508.31 | 43.92 | no_map |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9931.39 | 75.23 | no_map |
| TELUSDT | IDLE | 1.08 | 2.75 | 1.1 | 0.01 | 140821.69 | 53.16 | no_map |
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
