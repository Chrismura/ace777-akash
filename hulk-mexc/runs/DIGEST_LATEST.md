# Hulk DIGEST — 2026-09-01T06:23:01Z

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
| XRPUSDT | IDLE | 1.03 | 1.96 | 0.66 | 0.02 | 28822570.35 | 2.16 | skipped_fast |
| BTCUSDT | IDLE | 0.67 | 1.28 | 0.39 | 0.01 | 572739023.77 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.21 | 0.37 | 0.02 | 290553268.25 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.47 | 3.58 | 2.31 | 0.06 | 485285.5 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.95 | 4.81 | 0.9 | -0.0 | 379173.82 | 7.59 | skipped_fast |
| CCUSDT | IDLE | 1.63 | 3.15 | 0.69 | 0.04 | 389521.89 | 8.93 | skipped_fast |
| WUSDT | IDLE | 1.84 | 3.58 | 0.7 | 0.02 | 206670.8 | 13.58 | skipped_fast |
| RWAINCUSDT | IDLE | 2.51 | 4.39 | 4.21 | -0.04 | 4366.54 | 23.65 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 2.7 | 1.67 | 0.05 | 193446.99 | 15.56 | skipped_fast |
| EDELUSDT | IDLE | 0.89 | 5.54 | 2.37 | -0.04 | 137491.39 | 8.66 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.26 | 1.28 | -0.04 | 58302.75 | 12.18 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.16 | 0.84 | -0.03 | 68412.16 | 9.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.35 | 4.77 | 0.27 | -0.04 | 36229.89 | 60.69 | skipped_fast |
| BIOUSDT | IDLE | 0.71 | 1.33 | 0.6 | -0.01 | 64430.41 | 3.77 | skipped_fast |
| RWAUSDT | IDLE | 1.78 | 6.31 | 2.61 | 0.12 | 62100.18 | 14.51 | skipped_fast |
| HBARUSDT | IDLE | 1.11 | 2.14 | 0.5 | 0.01 | 237078.85 | 2.67 | skipped_fast |
| TELUSDT | IDLE | 1.64 | 3.07 | 1.43 | 0.02 | 93411.34 | 34.82 | skipped_fast |
| QNTUSDT | IDLE | 0.49 | 0.92 | 0.39 | 0.0 | 49882.64 | 4.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.85 | 0.71 | 0.0 | 28055.91 | 25.69 | skipped_fast |
| FLUIDUSDT | IDLE | 0.46 | 0.85 | 0.53 | 0.01 | 1149.26 | 21.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
