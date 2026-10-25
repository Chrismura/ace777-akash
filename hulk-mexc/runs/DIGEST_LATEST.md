# Hulk DIGEST — 2026-10-25T18:06:02Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.83 | 1.62 | 0.31 | 0.01 | 86806843.33 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.77 | 1.46 | 0.58 | 0.02 | 14724522.66 | 1.53 | n/a |
| BTCUSDT | IDLE | 0.44 | 0.85 | 0.17 | 0.01 | 146813476.54 | 0.0 | no_map |
| WUSDT | IDLE | 2.02 | 3.99 | 0.3 | -0.01 | 603284.05 | 15.58 | tvl≈1,514,831,420 |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.81 | 8.12 | 1.82 | 0.06 | 206887.63 | 50.15 | n/a |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.04 | 9.92 | 1.21 | 0.12 | 548370.03 | 11.65 | n/a |
| PYTHUSDT | IDLE | 2.29 | 4.57 | 0.07 | 0.07 | 432775.32 | 1.35 | tvl≈157,602,157 |
| EDELUSDT | IDLE | 2.33 | 4.66 | 0.0 | 0.02 | 398983.62 | 22.78 | no_map |
| CHIPUSDT | IDLE | 2.93 | 5.84 | 0.15 | 0.09 | 92393.12 | 21.74 | no_map |
| KITEUSDT | IDLE | 2.74 | 5.12 | 2.43 | 0.0 | 53417.89 | 13.27 | no_map |
| REDUSDT | IDLE | 2.13 | 4.24 | 0.12 | -0.0 | 63401.37 | 7.49 | tvl≈3,545,795 |
| CCUSDT | IDLE | 1.35 | 2.64 | 0.45 | 0.02 | 180206.44 | 8.76 | no_map |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.69 | 14.14 | 0.0 | 0.04 | 18749.01 | 21.28 | tvl≈2,183,782,030 |
| BIOUSDT | IDLE | 1.17 | 2.26 | 0.53 | 0.0 | 59448.95 | 4.44 | n/a |
| RIZEUSDT | IDLE | 1.28 | 2.61 | 1.4 | -0.01 | 44858.57 | 48.71 | no_map |
| RWAINCUSDT | IDLE | 0.99 | 1.72 | 1.69 | -0.03 | 59614.18 | 38.77 | no_map |
| HBARUSDT | IDLE | 1.09 | 2.14 | 0.24 | 0.02 | 141530.84 | 7.7 | empty_tvl |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
