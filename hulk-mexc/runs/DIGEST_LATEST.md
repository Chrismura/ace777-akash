# Hulk DIGEST — 2026-08-30T02:11:40Z

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
| XRPUSDT | IDLE | 0.41 | 0.76 | 0.44 | 0.01 | 16490186.7 | 1.44 | n/a |
| RIZEUSDT | IDLE | 2.78 | 8.3 | 4.91 | -0.01 | 42414.54 | 58.23 | no_map |
| PYTHUSDT | IDLE | 0.88 | 1.55 | 1.34 | 0.0 | 317525.51 | 2.1 | tvl≈108,869,783 |
| ZBCNUSDT | IDLE | 1.39 | 2.57 | 1.45 | -0.03 | 201929.53 | 10.0 | n/a |
| CCUSDT | IDLE | 0.8 | 1.62 | 0.32 | 0.07 | 243039.8 | 10.05 | no_map |
| WUSDT | IDLE | 0.52 | 0.98 | 0.41 | -0.0 | 177835.19 | 6.58 | tvl≈1,545,716,193 |
| BIOUSDT | IDLE | 0.92 | 1.76 | 0.54 | -0.01 | 66846.26 | 3.62 | n/a |
| REDUSDT | IDLE | 0.84 | 1.52 | 1.06 | 0.02 | 76469.08 | 11.91 | tvl≈2,028,643 |
| HBARUSDT | IDLE | 0.35 | 0.61 | 0.54 | -0.0 | 131974.26 | 1.33 | empty_tvl |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
