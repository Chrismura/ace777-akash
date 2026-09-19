# Hulk DIGEST — 2026-09-19T23:02:44Z

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
| XRPUSDT | IDLE | 1.43 | 2.66 | 1.38 | 0.01 | 58422095.24 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.11 | 0.62 | 0.0 | 246572207.71 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.77 | 0.34 | 0.0 | 446456202.14 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.37 | 2.57 | 1.08 | 0.01 | 642562.12 | 1.65 | skipped_fast |
| WUSDT | IDLE | 1.74 | 3.28 | 1.36 | 0.01 | 542979.31 | 5.46 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 3.14 | 2.59 | -0.02 | 333948.87 | 10.08 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 2.88 | 1.36 | 0.02 | 628445.66 | 1.23 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 6.05 | 3.11 | -0.08 | 139791.43 | 14.58 | skipped_fast |
| ZBCNUSDT | IDLE | 1.05 | 4.16 | 1.44 | 0.11 | 221725.59 | 11.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.49 | 0.41 | -0.02 | 130818.84 | 16.02 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.46 | 0.85 | 0.03 | 88534.13 | 3.56 | skipped_fast |
| RWAINCUSDT | IDLE | 1.96 | 4.31 | 3.62 | -0.04 | 6959.75 | 77.04 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 2.31 | 0.97 | 0.03 | 77028.47 | 13.96 | skipped_fast |
| REDUSDT | IDLE | 0.43 | 2.03 | 0.13 | 0.03 | 136606.02 | 2.0 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.53 | 1.35 | 0.04 | 59259.38 | 4.57 | skipped_fast |
| TELUSDT | IDLE | 1.27 | 2.69 | 2.36 | -0.09 | 104554.91 | 26.83 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.48 | 1.24 | 0.01 | 53151.05 | 14.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.54 | 0.81 | 0.04 | 9383.62 | 21.06 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 3.49 | 1.7 | 0.02 | 38212.63 | 229.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.63 | 0.05 | -0.01 | 34579.13 | 49.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
