# Hulk DIGEST — 2026-08-31T14:17:20Z

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
| XRPUSDT | IDLE | 1.07 | 1.91 | 1.49 | -0.03 | 40580076.36 | 2.2 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.43 | 1.15 | -0.01 | 550674060.93 | 0.18 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.1 | 0.92 | -0.01 | 445483385.01 | 0.16 | skipped_fast |
| CHIPUSDT | IDLE | 2.39 | 6.29 | 5.25 | -0.06 | 556828.06 | 2.52 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.74 | 2.11 | -0.05 | 447589.06 | 2.13 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.36 | 2.72 | -0.04 | 233024.45 | 9.87 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 2.98 | 2.87 | -0.01 | 243867.69 | 5.13 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.61 | 2.43 | -0.05 | 83053.57 | 3.83 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 2.91 | 2.82 | -0.03 | 70746.45 | 21.54 | skipped_fast |
| ZBCNUSDT | IDLE | 0.88 | 2.11 | 0.68 | -0.05 | 230613.0 | 9.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.88 | 3.35 | 2.69 | -0.03 | 2116.72 | 34.54 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.92 | 2.38 | -0.07 | 100308.74 | 10.95 | skipped_fast |
| RWAUSDT | IDLE | 2.23 | 4.35 | 0.7 | 0.04 | 54442.62 | 7.78 | skipped_fast |
| EDELUSDT | IDLE | 0.56 | 3.51 | 1.78 | 0.02 | 123019.1 | 24.66 | skipped_fast |
| QNTUSDT | IDLE | 2.12 | 3.9 | 2.3 | -0.01 | 49418.42 | 6.54 | skipped_fast |
| HBARUSDT | IDLE | 1.1 | 1.98 | 1.5 | -0.02 | 261611.59 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 1.88 | 3.33 | 2.93 | -0.01 | 90537.6 | 35.57 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 1.99 | 0.68 | -0.01 | 34115.28 | 61.74 | skipped_fast |
| FLUIDUSDT | IDLE | 0.78 | 1.54 | 0.13 | 0.01 | 2017.96 | 19.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.04 | -0.02 | 25386.88 | 4.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
