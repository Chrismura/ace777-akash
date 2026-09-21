# Hulk DIGEST — 2026-09-21T18:07:20Z

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
| XRPUSDT | IDLE | 1.23 | 2.54 | 0.35 | 0.07 | 84650180.15 | 2.66 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 2.05 | 0.77 | 0.05 | 663108605.54 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 0.95 | 1.84 | 0.42 | 0.06 | 928535743.9 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.69 | 3.95 | 2.42 | 0.06 | 1144378.21 | 3.29 | skipped_fast |
| PYTHUSDT | IDLE | 2.35 | 5.49 | 4.15 | 0.04 | 681041.35 | 7.85 | skipped_fast |
| WUSDT | IDLE | 2.08 | 4.58 | 3.05 | 0.04 | 627818.62 | 8.53 | skipped_fast |
| CCUSDT | IDLE | 1.21 | 3.06 | 2.02 | 0.08 | 568925.96 | 6.93 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 5.81 | 1.68 | 0.1 | 226492.4 | 21.08 | skipped_fast |
| BIOUSDT | IDLE | 1.74 | 3.2 | 1.87 | 0.04 | 101484.44 | 6.95 | skipped_fast |
| EDELUSDT | IDLE | 0.89 | 7.08 | 1.63 | 0.33 | 250793.91 | 29.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.22 | 5.87 | 4.71 | 0.04 | 142319.47 | 15.37 | skipped_fast |
| REDUSDT | IDLE | 1.59 | 2.87 | 2.06 | -0.0 | 103816.15 | 15.89 | skipped_fast |
| KITEUSDT | IDLE | 1.64 | 2.95 | 2.26 | 0.04 | 74793.11 | 12.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.49 | 2.81 | 1.08 | 0.02 | 11080.39 | 11.51 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 5.31 | 0.42 | 0.09 | 100050.25 | 24.08 | skipped_fast |
| QNTUSDT | IDLE | 1.67 | 2.97 | 2.5 | 0.03 | 112116.63 | 7.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.62 | 4.98 | 0.48 | -0.11 | 48842.75 | 32.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.26 | 2.6 | 1.28 | 0.06 | 9946.59 | 21.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.9 | 1.71 | 0.58 | 0.03 | 42554.06 | 15.44 | skipped_fast |
| RWAUSDT | IDLE | 0.75 | 1.39 | 0.72 | 0.02 | 56236.71 | 7.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
