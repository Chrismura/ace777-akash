# Hulk DIGEST — 2026-08-30T17:21:44Z

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
| ETHUSDT | IDLE | 1.6 | 3.05 | 1.04 | 0.02 | 210725191.18 | 0.88 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 2.44 | 0.57 | 0.02 | 20349093.84 | 2.12 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.58 | 0.51 | 0.01 | 274863155.26 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.88 | 7.33 | 5.75 | -0.02 | 512038.69 | 5.0 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 9.26 | 5.42 | -0.06 | 195933.18 | 24.66 | skipped_fast |
| PYTHUSDT | IDLE | 3.03 | 5.66 | 2.65 | 0.03 | 391528.56 | 2.05 | skipped_fast |
| WUSDT | IDLE | 1.56 | 3.02 | 0.61 | 0.05 | 222396.29 | 10.47 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 5.99 | 3.47 | 0.07 | 72603.7 | 25.12 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.62 | 1.29 | 0.01 | 255979.32 | 10.15 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.02 | 1.42 | 0.02 | 62191.86 | 22.68 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.65 | 0.51 | -0.0 | 79450.57 | 3.63 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 1.67 | 1.4 | -0.02 | 61060.23 | 10.18 | skipped_fast |
| RIZEUSDT | IDLE | 1.27 | 4.02 | 3.51 | -0.08 | 37412.51 | 62.12 | skipped_fast |
| TELUSDT | IDLE | 2.19 | 4.37 | 0.06 | 0.01 | 83600.11 | 40.29 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.63 | 0.0 | 0.02 | 1921.2 | 120.81 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.21 | 0.15 | 0.0 | 131484.98 | 1.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.0 | 32254.68 | 2.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 22.23 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.97 | 0.34 | 0.01 | 38455.89 | 4.84 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 52762.86 | 24.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
