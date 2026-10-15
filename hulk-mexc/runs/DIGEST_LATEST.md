# Hulk DIGEST — 2026-10-15T09:38:25Z

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
| PYTHUSDT | IDLE | 2.56 | 8.03 | 3.05 | 0.06 | 2811138.22 | 4.64 | skipped_fast |
| WUSDT | IDLE | 2.46 | 7.02 | 6.05 | -0.1 | 2793204.4 | 17.28 | skipped_fast |
| XRPUSDT | IDLE | 1.41 | 2.73 | 0.57 | -0.03 | 60820340.85 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.94 | 1.9 | 0.66 | -0.05 | 353554233.58 | 0.42 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.5 | 0.49 | -0.02 | 541489879.59 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 5.01 | 1.01 | -0.05 | 1167533.97 | 3.5 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 4.69 | 4.48 | -0.13 | 449489.25 | 0.94 | skipped_fast |
| EDELUSDT | IDLE | 2.41 | 7.65 | 5.97 | -0.11 | 219153.7 | 16.34 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.82 | 1.37 | -0.05 | 563802.14 | 4.9 | skipped_fast |
| RIZEUSDT | IDLE | 1.78 | 11.92 | 7.7 | -0.03 | 65379.84 | 58.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 7.22 | 6.67 | -0.21 | 122637.55 | 11.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 3.08 | 0.46 | -0.05 | 219637.8 | 24.07 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 3.98 | 1.86 | -0.09 | 84566.01 | 8.04 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 2.38 | 2.32 | 0.0 | 69286.91 | 9.0 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 3.01 | 2.59 | -0.13 | 68011.93 | 10.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.05 | 2.27 | 1.21 | 0.01 | 27044.35 | 20.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.99 | 5.96 | 4.11 | -0.02 | 20393.8 | 21.5 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 1.77 | 1.22 | -0.05 | 100036.8 | 46.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.59 | 1.04 | 1.0 | -0.02 | 31312.83 | 2.86 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.73 | 0.64 | -0.04 | 55378.61 | 16.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
