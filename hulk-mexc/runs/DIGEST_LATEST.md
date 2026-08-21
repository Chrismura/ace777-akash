# Hulk DIGEST — 2026-08-21T23:42:02Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.39 | 0.1 | 6147597.09 | 2.05 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.19 | 0.15 | 141146376.17 | 5.49 | n/a |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.63 | 0.13 | 513880.7 | 11.01 | n/a |
| HBARUSDT | IDLE | 2.62 | 6.36 | 1.08 | 0.09 | 909281.7 | 1.25 | empty_tvl |
| CCUSDT | IDLE | 1.9 | 7.42 | 0.95 | 0.13 | 645275.97 | 10.66 | no_map |
| WUSDT | IDLE | 2.78 | 6.91 | 1.91 | 0.08 | 380027.28 | 13.38 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.34 | 0.03 | 547503.79 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.02 | 186467.26 | 6.22 | n/a |
| EDELUSDT | IDLE | 2.52 | 5.5 | 0.43 | -0.02 | 82417.03 | 21.81 | no_map |
| RIZEUSDT | IDLE | 2.2 | 9.82 | 4.6 | 0.14 | 59280.31 | 46.13 | no_map |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.31 | 0.07 | 189913.04 | 20.53 | no_map |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10344.85 | 21.39 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.81 | 0.18 | 157696.88 | 20.19 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.08 | 145154.91 | 1.49 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.09 | 61470.17 | 9.25 | no_map |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.26 | tvl≈2,594,160,978 |
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
