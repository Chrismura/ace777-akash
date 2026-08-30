# Hulk DIGEST — 2026-08-30T14:06:55Z

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
| XRPUSDT | IDLE | 1.04 | 2.02 | 0.44 | 0.01 | 18726168.01 | 1.42 | n/a |
| BTCUSDT | IDLE | 0.64 | 1.27 | 0.09 | 0.02 | 249512775.88 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.54 | 1.06 | 0.18 | 0.02 | 156811300.07 | 0.08 | no_map |
| PYTHUSDT | IDLE | 3.88 | 7.51 | 1.63 | 0.04 | 412100.28 | 2.02 | tvl≈107,930,951 |
| ZBCNUSDT | IDLE | 2.61 | 4.6 | 4.08 | -0.02 | 151525.87 | 12.14 | n/a |
| WUSDT | IDLE | 1.86 | 3.68 | 0.25 | 0.04 | 206418.68 | 11.62 | tvl≈1,550,358,630 |
| CCUSDT | IDLE | 0.89 | 1.62 | 1.12 | 0.03 | 283915.58 | 7.6 | no_map |
| REDUSDT | IDLE | 1.23 | 2.39 | 0.48 | 0.01 | 60523.97 | 11.74 | tvl≈2,031,180 |
| BIOUSDT | IDLE | 0.7 | 1.36 | 0.25 | -0.0 | 71477.75 | 3.64 | n/a |
| RIZEUSDT | IDLE | 0.77 | 2.75 | 1.27 | -0.06 | 46205.11 | 61.0 | no_map |
| HBARUSDT | IDLE | 0.64 | 1.23 | 0.3 | 0.01 | 141922.71 | 1.32 | empty_tvl |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
