# Hulk DIGEST — 2026-09-14T18:43:36Z

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
| XRPUSDT | IDLE | 2.48 | 6.15 | 0.35 | 0.07 | 55855551.36 | 0.68 | skipped_fast |
| BTCUSDT | IDLE | 1.15 | 2.28 | 0.12 | 0.02 | 514138834.56 | 0.04 | skipped_fast |
| ETHUSDT | IDLE | 1.12 | 2.21 | 0.14 | 0.01 | 369147828.92 | 0.12 | skipped_fast |
| PYTHUSDT | IDLE | 2.3 | 4.48 | 0.74 | -0.01 | 455223.22 | 1.77 | skipped_fast |
| REDUSDT | IDLE | 2.44 | 8.59 | 4.97 | 0.07 | 184646.6 | 17.07 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 6.39 | 4.03 | 0.1 | 267152.68 | 27.47 | skipped_fast |
| BIOUSDT | IDLE | 2.22 | 4.32 | 0.8 | 0.02 | 89646.44 | 7.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.77 | 3.54 | 0.01 | 0.01 | 208263.9 | 24.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 4.25 | 1.89 | -0.03 | 90108.16 | 21.32 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.26 | 0.03 | -0.01 | 212899.38 | 11.86 | skipped_fast |
| CCUSDT | IDLE | 1.08 | 2.14 | 0.17 | 0.01 | 293258.56 | 9.25 | skipped_fast |
| HBARUSDT | IDLE | 1.57 | 3.08 | 0.38 | 0.02 | 317654.55 | 2.55 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 2.84 | 1.03 | 0.04 | 10093.3 | 5.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.97 | 10.72 | 8.83 | -0.03 | 55232.37 | 97.56 | skipped_fast |
| KITEUSDT | IDLE | 1.08 | 2.06 | 0.67 | -0.01 | 61622.97 | 10.37 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 1.97 | 1.16 | -0.02 | 41640.42 | 7.79 | skipped_fast |
| FLUIDUSDT | IDLE | 1.28 | 2.54 | 0.09 | 0.03 | 1029.98 | 21.58 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 1.95 | 0.06 | 0.01 | 92234.53 | 37.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.8 | 1.58 | 0.1 | 0.01 | 29509.51 | 53.86 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.3 | 0.0 | 55078.13 | 29.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
