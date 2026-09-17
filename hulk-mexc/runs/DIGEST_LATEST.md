# Hulk DIGEST — 2026-09-17T09:15:43Z

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
| ETHUSDT | IDLE | 0.62 | 1.2 | 0.28 | 0.02 | 370624275.17 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 0.56 | 1.11 | 0.1 | 0.02 | 55528048.96 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.69 | 0.03 | 0.01 | 477294373.26 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.05 | 3.9 | 1.29 | 0.04 | 532757.21 | 5.52 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 5.57 | 0.0 | 0.12 | 628528.66 | 8.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.7 | 7.63 | 0.1 | 0.07 | 142370.86 | 12.81 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 9.16 | 5.76 | -0.06 | 212945.79 | 64.33 | skipped_fast |
| ZBCNUSDT | IDLE | 0.91 | 1.7 | 0.8 | 0.03 | 169563.22 | 24.69 | skipped_fast |
| WUSDT | IDLE | 0.58 | 1.15 | 0.12 | 0.05 | 225493.39 | 16.14 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 3.32 | 2.56 | 0.07 | 67852.65 | 12.2 | skipped_fast |
| RWAINCUSDT | IDLE | 1.47 | 2.57 | 2.44 | -0.0 | 17643.94 | 46.65 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.21 | 0.2 | -0.0 | 430874.97 | 1.35 | skipped_fast |
| RIZEUSDT | IDLE | 0.82 | 8.9 | 3.8 | -0.14 | 60563.25 | 73.07 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 1.7 | 0.01 | 0.02 | 61363.97 | 6.06 | skipped_fast |
| BIOUSDT | IDLE | 0.59 | 1.16 | 0.2 | 0.03 | 69891.1 | 3.95 | skipped_fast |
| RWAUSDT | IDLE | 1.69 | 3.31 | 0.52 | 0.02 | 59045.69 | 52.45 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 2.45 | 0.45 | 0.03 | 34851.57 | 1.62 | skipped_fast |
| TELUSDT | IDLE | 0.62 | 1.19 | 0.35 | -0.02 | 113371.66 | 41.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.96 | 0.07 | 0.01 | 37421.57 | 2.8 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.0 | 1541.55 | 21.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
