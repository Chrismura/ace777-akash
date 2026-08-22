# Hulk DIGEST — 2026-08-22T02:39:06Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 10.52 | 1.08 | 0.15 | 7149456.21 | 1.92 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.46 | 12.02 | 0.72 | 0.18 | 156481149.0 | 3.28 | skipped_fast |
| HBARUSDT | IDLE | 2.43 | 5.62 | 0.49 | 0.08 | 977601.66 | 1.24 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 9.63 | 1.45 | 0.11 | 542574.63 | 22.91 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.79 | 0.0 | 0.15 | 653835.99 | 5.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 5.26 | 0.48 | -0.01 | 459228.92 | 9.01 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.16 | 8.18 | 1.29 | 0.1 | 193746.57 | 2.97 | skipped_fast |
| WUSDT | IDLE | 1.94 | 5.62 | 0.09 | 0.1 | 411093.96 | 13.95 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 5.02 | 2.5 | -0.03 | 79767.34 | 33.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.23 | 0.1 | 61537.44 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 5.4 | 0.18 | 157849.3 | 10.44 | skipped_fast |
| QNTUSDT | IDLE | 2.35 | 5.48 | 0.43 | 0.08 | 172669.93 | 5.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.86 | 3.27 | 3.0 | 0.01 | 9350.76 | 37.95 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.15 | 0.12 | 62561.96 | 9.85 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.06 | 176358.57 | 51.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.08 | skipped_fast |
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
