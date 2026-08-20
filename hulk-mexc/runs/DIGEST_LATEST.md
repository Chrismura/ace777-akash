# Hulk DIGEST — 2026-08-20T04:12:32Z

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
| XRPUSDT | IDLE | 0.83 | 2.58 | 1.8 | 0.1 | 45930160.44 | 0.91 | n/a |
| RIZEUSDT | IDLE | 3.22 | 22.95 | 2.9 | 0.2 | 58006.19 | 172.25 | no_map |
| CCUSDT | IDLE | 1.26 | 4.08 | 2.07 | 0.11 | 382122.46 | 8.0 | no_map |
| EDELUSDT | IDLE | 1.44 | 11.14 | 7.19 | 0.23 | 98942.23 | 10.9 | no_map |
| CHIPUSDT | IDLE | 1.57 | 5.71 | 0.96 | 0.12 | 207536.56 | 6.9 | no_map |
| WUSDT | IDLE | 1.34 | 2.93 | 2.36 | 0.06 | 271921.64 | 12.84 | tvl≈1,458,413,855 |
| BIOUSDT | IDLE | 1.22 | 5.81 | 0.86 | 0.16 | 168162.03 | 3.46 | n/a |
| ZBCNUSDT | IDLE | 1.0 | 3.98 | 2.72 | 0.13 | 238715.57 | 26.56 | n/a |
| REDUSDT | IDLE | 1.42 | 6.6 | 0.7 | 0.12 | 102402.51 | 12.93 | tvl≈1,730,214 |
| PYTHUSDT | IDLE | 0.77 | 2.41 | 0.21 | 0.1 | 291007.9 | 9.36 | tvl≈95,074,651 |
| HBARUSDT | IDLE | 0.9 | 1.71 | 0.6 | 0.05 | 351397.72 | 1.41 | empty_tvl |
| QAITUSDT | IDLE | 1.19 | 3.23 | 1.06 | 0.05 | 10308.39 | 30.48 | no_map |
| RWAINCUSDT | IDLE | 0.64 | 1.71 | 1.68 | 0.04 | 17311.81 | 5.69 | no_map |
| KITEUSDT | IDLE | 0.58 | 1.15 | 0.41 | 0.06 | 59075.88 | 20.84 | no_map |
| FLUIDUSDT | IDLE | 1.72 | 4.41 | 4.22 | 0.05 | 3480.84 | 22.34 | tvl≈2,491,470,505 |
| TELUSDT | IDLE | 0.53 | 2.37 | 1.59 | 0.11 | 190365.18 | 37.2 | no_map |
| QNTUSDT | IDLE | 0.68 | 1.31 | 0.27 | 0.05 | 36683.37 | 6.76 | n/a |
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
