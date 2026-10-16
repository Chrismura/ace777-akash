# Hulk DIGEST — 2026-10-16T10:58:29Z

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
| WUSDT | IDLE | 2.48 | 6.02 | 5.01 | 0.02 | 1842078.51 | 17.01 | skipped_fast |
| PYTHUSDT | IDLE | 0.89 | 5.01 | 4.03 | 0.06 | 3814159.44 | 1.09 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.14 | 0.12 | 0.04 | 227886669.04 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.52 | 1.01 | 0.16 | 0.03 | 30622364.49 | 2.23 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.7 | 0.2 | 0.02 | 396751846.53 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.96 | 5.23 | 4.57 | -0.02 | 432550.43 | 9.64 | skipped_fast |
| QNTUSDT | IDLE | 0.94 | 2.74 | 0.4 | 0.06 | 1171048.81 | 4.29 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 9.55 | 6.28 | -0.02 | 68712.88 | 61.89 | skipped_fast |
| RWAINCUSDT | IDLE | 2.89 | 5.35 | 4.07 | 0.03 | 24941.24 | 4.99 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 5.24 | 0.92 | -0.01 | 216542.89 | 16.53 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.9 | 0.27 | 0.05 | 213655.35 | 13.56 | skipped_fast |
| CHIPUSDT | IDLE | 0.81 | 4.12 | 3.13 | 0.11 | 194182.61 | 12.12 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 2.32 | 0.75 | 0.03 | 69792.14 | 8.95 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 2.99 | 0.75 | 0.01 | 88567.18 | 13.97 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.67 | 0.65 | 0.06 | 69656.62 | 3.85 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 2.05 | 0.87 | 0.06 | 255863.9 | 4.64 | skipped_fast |
| FLUIDUSDT | IDLE | 2.08 | 3.64 | 3.51 | -0.03 | 8114.06 | 21.2 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 2.94 | 2.09 | 0.05 | 95331.41 | 28.03 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.03 | 0.16 | 0.02 | 51804.31 | 15.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.33 | 0.14 | 0.01 | 39248.95 | 15.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
