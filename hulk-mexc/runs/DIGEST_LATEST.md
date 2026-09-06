# Hulk DIGEST — 2026-09-06T11:45:37Z

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
| ETHUSDT | IDLE | 0.64 | 1.21 | 0.44 | 0.02 | 231851787.1 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.62 | 1.19 | 0.36 | 0.01 | 25504176.22 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 0.28 | 0.54 | 0.08 | 0.0 | 404224134.09 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 7.32 | 3.2 | 0.06 | 412579.66 | 1.68 | skipped_fast |
| RWAINCUSDT | IDLE | 3.52 | 7.89 | 2.1 | 0.05 | 7825.85 | 46.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.18 | 2.33 | 0.25 | 0.03 | 448860.07 | 1.8 | skipped_fast |
| WUSDT | IDLE | 2.12 | 4.21 | 0.17 | 0.04 | 196342.02 | 13.48 | skipped_fast |
| RIZEUSDT | IDLE | 2.05 | 11.34 | 8.96 | 0.01 | 90409.4 | 65.17 | skipped_fast |
| REDUSDT | IDLE | 2.39 | 4.59 | 1.33 | 0.02 | 61345.55 | 11.62 | skipped_fast |
| CCUSDT | IDLE | 1.1 | 2.07 | 0.83 | 0.01 | 317578.37 | 9.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 2.76 | 1.44 | 0.0 | 203330.07 | 21.67 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 2.63 | 2.02 | -0.0 | 69002.62 | 46.62 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.75 | 0.43 | 0.02 | 93827.81 | 3.59 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 1.84 | 1.69 | -0.04 | 65114.04 | 10.23 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.37 | 0.23 | 0.02 | 419809.03 | 1.23 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 2.56 | 1.98 | 0.03 | 40160.59 | 4.57 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 1.65 | 1.1 | 0.01 | 70436.93 | 46.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.61 | 1.15 | 0.45 | 0.02 | 42711.13 | 2.68 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.0 | 0.85 | 0.0 | 53255.84 | 14.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 21.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
