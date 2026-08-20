# Hulk DIGEST — 2026-08-20T23:28:40Z

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
| XRPUSDT | IDLE | 1.45 | 8.05 | 3.42 | 0.15 | 101685221.93 | 1.57 | n/a |
| PYTHUSDT | IDLE | 1.0 | 2.0 | 0.05 | 0.05 | 1372028.09 | 2.26 | tvl≈99,839,273 |
| CCUSDT | IDLE | 2.16 | 3.9 | 2.83 | 0.0 | 479463.49 | 7.04 | no_map |
| CHIPUSDT | IDLE | 2.3 | 7.54 | 0.13 | 0.12 | 289942.51 | 6.39 | no_map |
| ZBCNUSDT | IDLE | 1.97 | 6.08 | 1.43 | 0.03 | 274092.63 | 16.18 | n/a |
| RIZEUSDT | IDLE | 1.73 | 9.79 | 8.92 | -0.03 | 49088.5 | 48.44 | no_map |
| QAITUSDT | IDLE | 2.51 | 6.4 | 1.2 | -0.0 | 6012.14 | 66.45 | no_map |
| WUSDT | IDLE | 1.01 | 1.99 | 0.2 | 0.04 | 257626.31 | 11.07 | tvl≈1,504,277,482 |
| HBARUSDT | IDLE | 1.32 | 2.61 | 0.22 | 0.04 | 428442.4 | 1.36 | empty_tvl |
| BIOUSDT | IDLE | 0.65 | 3.42 | 0.57 | 0.14 | 229969.27 | 3.17 | n/a |
| RWAINCUSDT | IDLE | 2.14 | 4.08 | 1.31 | 0.02 | 7379.22 | 71.02 | no_map |
| KITEUSDT | IDLE | 1.3 | 2.59 | 0.01 | 0.03 | 62432.99 | 15.08 | no_map |
| TELUSDT | IDLE | 1.41 | 7.03 | 5.58 | 0.13 | 183723.02 | 10.95 | no_map |
| REDUSDT | IDLE | 0.34 | 2.17 | 1.29 | 0.1 | 184682.9 | 14.36 | tvl≈1,896,648 |
| EDELUSDT | IDLE | 0.84 | 2.49 | 0.11 | 0.05 | 88590.98 | 31.76 | no_map |
| QNTUSDT | IDLE | 0.78 | 1.74 | 0.03 | 0.06 | 64137.24 | 4.81 | n/a |
| FLUIDUSDT | IDLE | 0.49 | 0.95 | 0.94 | 0.06 | 1433.85 | 19.19 | tvl≈2,527,496,827 |
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
