# Hulk DIGEST — 2026-08-22T12:44:20Z

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
| XRPUSDT | IDLE | 2.49 | 14.26 | 7.13 | 0.1 | 216220181.56 | 0.66 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 7.83 | 1.18 | 0.05 | 51599790.14 | 1.97 | skipped_fast |
| HBARUSDT | IDLE | 1.26 | 4.63 | 2.21 | 0.02 | 1250951.99 | 6.42 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 8.38 | 3.37 | 0.14 | 778142.06 | 5.05 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.55 | 0.0 | 575640.79 | 12.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.19 | 5.77 | 3.41 | -0.01 | 335446.72 | 20.94 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.62 | -0.1 | 603369.43 | 6.72 | skipped_fast |
| KITEUSDT | IDLE | 2.68 | 6.37 | 0.74 | 0.03 | 84971.35 | 22.11 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 3.89 | 2.43 | -0.02 | 78229.78 | 22.57 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.74 | -0.05 | 238437.77 | 3.23 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2395.57 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.56 | 0.01 | 152883.19 | 12.48 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.61 | 3.83 | -0.03 | 163215.99 | 37.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.58 | -0.01 | 187692.99 | 1.56 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 2.03 | 0.0 | 0.0 | 46794.11 | 46.02 | skipped_fast |
| RWAUSDT | IDLE | 0.99 | 1.8 | 1.2 | 0.02 | 57834.61 | 8.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.04 | 5072.55 | 22.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
