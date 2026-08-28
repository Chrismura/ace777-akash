# Hulk DIGEST — 2026-08-28T05:06:51Z

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
| PYTHUSDT | IDLE | 1.56 | 3.65 | 3.0 | 0.02 | 20149180.58 | 2.06 | tvl≈110,870,887 |
| XRPUSDT | IDLE | 2.12 | 3.73 | 3.44 | 0.01 | 57229338.6 | 1.41 | n/a |
| CCUSDT | IDLE | 2.14 | 3.96 | 2.14 | -0.02 | 472003.6 | 9.76 | no_map |
| WUSDT | IDLE | 2.56 | 4.51 | 4.11 | 0.0 | 201236.4 | 11.68 | tvl≈1,565,826,878 |
| BIOUSDT | IDLE | 2.93 | 5.18 | 4.55 | 0.0 | 95011.76 | 7.02 | n/a |
| ZBCNUSDT | IDLE | 1.4 | 4.42 | 3.26 | 0.05 | 246019.22 | 15.81 | n/a |
| REDUSDT | IDLE | 1.91 | 3.56 | 1.79 | 0.02 | 82495.9 | 12.69 | tvl≈2,051,381 |
| KITEUSDT | IDLE | 1.77 | 3.15 | 2.65 | 0.01 | 78379.72 | 8.62 | no_map |
| HBARUSDT | IDLE | 1.83 | 3.24 | 2.82 | 0.0 | 332438.39 | 2.58 | empty_tvl |
| QAITUSDT | IDLE | 0.38 | 18.58 | 13.16 | -0.21 | 61337.7 | 65.05 | no_map |
| RIZEUSDT | IDLE | 0.94 | 11.77 | 2.6 | -0.18 | 118976.65 | 53.43 | no_map |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
