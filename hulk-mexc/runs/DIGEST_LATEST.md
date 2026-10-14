# Hulk DIGEST — 2026-10-14T20:27:17Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.56 | 8.82 | 0.73 | 0.08 | 1905919.57 | 9.42 | tvl≈178,515,229 |
| WUSDT | IDLE | 1.01 | 4.46 | 1.71 | -0.1 | 2556083.96 | 8.47 | miss:timeout |
| XRPUSDT | IDLE | 0.83 | 1.49 | 1.09 | -0.03 | 44995573.67 | 2.26 | n/a |
| ETHUSDT | IDLE | 0.74 | 1.33 | 0.95 | -0.03 | 203119536.65 | 0.25 | no_map |
| BTCUSDT | IDLE | 0.35 | 0.68 | 0.15 | -0.01 | 434321757.04 | 0.0 | no_map |
| ZBCNUSDT | IDLE | 2.9 | 5.26 | 3.55 | -0.04 | 195949.11 | 13.63 | n/a |
| CCUSDT | IDLE | 1.39 | 3.38 | 2.69 | -0.09 | 412697.22 | 7.74 | no_map |
| REDUSDT | IDLE | 2.25 | 4.43 | 0.42 | 0.02 | 61982.41 | 8.27 | tvl≈3,885,465 |
| KITEUSDT | IDLE | 1.85 | 5.27 | 4.17 | -0.01 | 86473.86 | 10.23 | no_map |
| HBARUSDT | IDLE | 1.22 | 2.29 | 1.01 | -0.04 | 526375.75 | 3.56 | empty_tvl |
| BIOUSDT | IDLE | 1.5 | 2.71 | 1.9 | -0.05 | 65782.5 | 3.79 | n/a |
| RIZEUSDT | IDLE | 0.5 | 2.68 | 1.09 | -0.0 | 49015.88 | 61.33 | no_map |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
