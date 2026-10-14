# Hulk DIGEST — 2026-10-14T22:28:40Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.01 | 8.93 | 1.85 | 0.1 | 2055981.86 | 1.17 | skipped_fast |
| WUSDT | IDLE | 1.3 | 4.66 | 2.84 | -0.11 | 2368472.15 | 8.49 | skipped_fast |
| ETHUSDT | IDLE | 1.12 | 2.01 | 1.54 | -0.04 | 233304559.03 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.87 | 1.65 | 0.56 | -0.03 | 46687452.55 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.68 | 0.53 | -0.02 | 445461790.88 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.2 | 4.0 | 2.66 | -0.04 | 1082282.94 | 1.96 | skipped_fast |
| CCUSDT | IDLE | 1.84 | 3.74 | 3.53 | -0.08 | 401944.91 | 8.68 | skipped_fast |
| RWAINCUSDT | IDLE | 3.4 | 8.46 | 2.24 | -0.03 | 26539.13 | 10.16 | skipped_fast |
| ZBCNUSDT | IDLE | 2.14 | 3.89 | 2.62 | -0.03 | 204887.15 | 2.74 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 4.34 | 2.67 | -0.03 | 174671.84 | 15.04 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 5.27 | 4.2 | -0.01 | 86699.64 | 10.23 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.29 | 0.65 | -0.03 | 531936.57 | 3.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.31 | 3.72 | 3.51 | -0.08 | 101543.78 | 13.39 | skipped_fast |
| BIOUSDT | IDLE | 1.47 | 2.71 | 1.56 | -0.04 | 66716.21 | 3.77 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 4.58 | 4.27 | -0.03 | 100616.12 | 28.58 | skipped_fast |
| REDUSDT | IDLE | 1.2 | 2.29 | 0.73 | 0.01 | 61946.28 | 8.28 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 3.64 | 1.96 | -0.01 | 49837.8 | 61.89 | skipped_fast |
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
