# Hulk DIGEST — 2026-09-11T12:16:09Z

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
| XRPUSDT | IDLE | 1.67 | 2.98 | 2.4 | -0.04 | 39598454.21 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.77 | 1.34 | 1.27 | -0.0 | 463279717.12 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.94 | 0.72 | -0.01 | 514085940.78 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.82 | 5.15 | 3.29 | -0.05 | 439188.41 | 9.34 | skipped_fast |
| PYTHUSDT | IDLE | 2.23 | 4.04 | 2.86 | -0.03 | 365375.34 | 1.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.22 | 24.77 | 8.86 | 0.19 | 128380.81 | 100.7 | skipped_fast |
| WUSDT | IDLE | 1.88 | 3.32 | 2.88 | -0.02 | 128593.33 | 11.75 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 2.95 | 0.43 | -0.01 | 190297.63 | 21.68 | skipped_fast |
| BIOUSDT | IDLE | 1.76 | 3.16 | 2.43 | -0.04 | 80065.74 | 8.17 | skipped_fast |
| QNTUSDT | IDLE | 2.93 | 5.13 | 4.86 | -0.04 | 41650.51 | 9.4 | skipped_fast |
| REDUSDT | IDLE | 1.7 | 3.09 | 2.06 | -0.03 | 59591.38 | 18.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.11 | 3.47 | 1.17 | -0.05 | 127797.83 | 15.32 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 2.48 | 1.67 | -0.02 | 57629.24 | 12.09 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 3.14 | 1.58 | 0.02 | 4233.78 | 22.09 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 2.87 | 2.05 | -0.07 | 197709.2 | 28.45 | skipped_fast |
| HBARUSDT | IDLE | 1.42 | 2.55 | 1.89 | -0.03 | 195841.53 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.17 | 1.43 | -0.04 | 100017.87 | 34.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.14 | 1.98 | 1.94 | -0.04 | 2304.28 | 22.16 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.46 | 0.15 | -0.01 | 49517.52 | 15.19 | skipped_fast |
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
