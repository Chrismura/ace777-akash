# Hulk DIGEST — 2026-10-17T18:20:52Z

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
| XRPUSDT | IDLE | 0.69 | 1.3 | 0.57 | -0.01 | 17193769.7 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.23 | 0.48 | 0.0 | 87339676.83 | 0.04 | skipped_fast |
| WUSDT | IDLE | 2.53 | 7.26 | 4.33 | -0.02 | 1200249.64 | 13.68 | skipped_fast |
| PYTHUSDT | IDLE | 2.82 | 7.06 | 3.09 | -0.01 | 1071483.05 | 1.21 | skipped_fast |
| BTCUSDT | IDLE | 0.26 | 0.51 | 0.09 | 0.0 | 181385188.64 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.12 | 3.97 | 1.74 | -0.01 | 534344.53 | 0.5 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.56 | 1.67 | -0.01 | 254644.49 | 7.71 | skipped_fast |
| CHIPUSDT | IDLE | 2.01 | 3.65 | 2.41 | -0.03 | 87102.76 | 15.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.34 | 1.72 | -0.03 | 195607.48 | 16.04 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.55 | 1.55 | -0.05 | 154914.7 | 38.45 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.62 | 1.18 | -0.02 | 69104.41 | 8.21 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.71 | 1.12 | -0.01 | 64427.95 | 10.97 | skipped_fast |
| FLUIDUSDT | IDLE | 2.68 | 4.89 | 3.2 | 0.04 | 3656.49 | 21.47 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 4.34 | 0.52 | 0.05 | 24932.91 | 5.23 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 1.78 | 0.83 | -0.03 | 59860.0 | 7.85 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 1.8 | 0.88 | -0.03 | 49445.62 | 61.51 | skipped_fast |
| HBARUSDT | IDLE | 1.04 | 1.97 | 0.74 | 0.0 | 150143.49 | 1.2 | skipped_fast |
| TELUSDT | IDLE | 1.19 | 2.11 | 1.83 | -0.06 | 84993.47 | 24.05 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.04 | 0.71 | 0.0 | 50732.82 | 15.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.54 | 1.05 | 0.18 | 0.01 | 29347.05 | 15.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
