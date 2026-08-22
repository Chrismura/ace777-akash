# Hulk DIGEST — 2026-08-22T02:41:30Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 10.52 | 1.06 | 0.15 | 7165795.41 | 1.92 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 12.02 | 0.53 | 0.18 | 156693476.03 | 3.92 | n/a |
| HBARUSDT | IDLE | 2.42 | 5.62 | 0.26 | 0.09 | 978788.53 | 1.23 | empty_tvl |
| ZBCNUSDT | IDLE | 2.46 | 9.63 | 2.16 | 0.1 | 541572.5 | 20.63 | n/a |
| CCUSDT | IDLE | 1.77 | 6.79 | 0.09 | 0.14 | 654630.9 | 6.05 | no_map |
| CHIPUSDT | IDLE | 2.28 | 5.26 | 0.06 | -0.01 | 458933.35 | 3.0 | no_map |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.14 | 8.18 | 1.0 | 0.1 | 193260.08 | 5.91 | n/a |
| WUSDT | IDLE | 1.94 | 5.62 | 0.07 | 0.1 | 411281.98 | 13.95 | tvl≈1,646,654,250 |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.23 | 0.1 | 61314.5 | 28.82 | no_map |
| EDELUSDT | IDLE | 2.52 | 5.02 | 3.69 | -0.04 | 79867.38 | 78.61 | no_map |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.93 | 0.19 | 158117.13 | 16.79 | tvl≈2,314,909 |
| QNTUSDT | IDLE | 2.35 | 5.48 | 0.37 | 0.08 | 172677.21 | 7.45 | n/a |
| RWAINCUSDT | IDLE | 1.86 | 3.27 | 2.95 | 0.01 | 9365.53 | 37.95 | no_map |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.05 | 0.12 | 62453.87 | 10.74 | no_map |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | no_map |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.18 | 0.06 | 174221.92 | 46.57 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 14.03 | tvl≈2,599,456,799 |
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
