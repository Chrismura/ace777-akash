# Hulk DIGEST — 2026-09-07T01:33:28Z

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
| XRPUSDT | IDLE | 0.86 | 1.53 | 1.33 | -0.01 | 25383426.35 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.47 | 0.83 | 0.0 | 280143689.08 | 0.16 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.12 | 0.76 | -0.0 | 369883555.81 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.08 | 5.95 | 1.42 | 0.02 | 590067.25 | 1.76 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 3.29 | 2.41 | -0.03 | 410099.31 | 1.72 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.21 | 13.68 | 1.53 | 0.16 | 5970.06 | 33.12 | skipped_fast |
| WUSDT | IDLE | 1.59 | 2.9 | 1.84 | 0.01 | 404654.41 | 7.75 | skipped_fast |
| CCUSDT | IDLE | 1.65 | 3.03 | 1.84 | -0.0 | 365216.35 | 9.07 | skipped_fast |
| ZBCNUSDT | IDLE | 1.85 | 3.35 | 2.28 | 0.0 | 139524.56 | 1.08 | skipped_fast |
| TELUSDT | IDLE | 3.11 | 5.56 | 4.45 | 0.02 | 95230.83 | 17.26 | skipped_fast |
| REDUSDT | IDLE | 1.88 | 3.31 | 3.06 | -0.02 | 67243.88 | 8.7 | skipped_fast |
| HBARUSDT | IDLE | 1.23 | 2.25 | 1.45 | 0.0 | 463879.85 | 1.23 | skipped_fast |
| BIOUSDT | IDLE | 1.5 | 2.69 | 2.11 | -0.02 | 89659.45 | 3.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.5 | 12.58 | 7.54 | -0.19 | 70140.62 | 128.46 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.25 | 1.04 | -0.01 | 57915.62 | 20.59 | skipped_fast |
| EDELUSDT | IDLE | 1.24 | 2.42 | 0.38 | 0.0 | 48708.54 | 66.07 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 2.02 | 0.94 | 0.01 | 38078.27 | 4.5 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.79 | 0.57 | -0.02 | 54171.01 | 14.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.65 | 1.3 | 0.0 | 0.03 | 309.53 | 21.87 | skipped_fast |
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
