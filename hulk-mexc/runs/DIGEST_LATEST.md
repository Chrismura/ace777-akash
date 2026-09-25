# Hulk DIGEST — 2026-09-25T14:26:14Z

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
| XRPUSDT | IDLE | 2.72 | 5.7 | 3.64 | 0.04 | 112069137.52 | 2.55 | skipped_fast |
| ETHUSDT | IDLE | 1.47 | 2.63 | 2.06 | 0.0 | 397135824.55 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.37 | 2.46 | 1.88 | -0.01 | 761115372.19 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.73 | 4.19 | 1.06 | 0.07 | 1221649.33 | 1.39 | skipped_fast |
| HBARUSDT | IDLE | 2.49 | 4.48 | 3.35 | -0.0 | 1030250.56 | 2.14 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 6.44 | 1.12 | 0.13 | 778757.02 | 7.28 | skipped_fast |
| ZBCNUSDT | IDLE | 4.08 | 9.17 | 4.74 | 0.04 | 193904.68 | 12.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 32.62 | 23.32 | 0.53 | 127257.53 | 56.1 | skipped_fast |
| BIOUSDT | IDLE | 3.16 | 10.33 | 3.4 | 0.09 | 117480.68 | 9.12 | skipped_fast |
| WUSDT | IDLE | 2.14 | 3.97 | 2.09 | 0.02 | 379570.87 | 8.4 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 8.52 | 6.34 | 0.16 | 590874.76 | 6.37 | skipped_fast |
| REDUSDT | IDLE | 2.08 | 5.16 | 2.0 | 0.06 | 136142.09 | 14.12 | skipped_fast |
| KITEUSDT | IDLE | 2.09 | 3.8 | 2.54 | -0.03 | 73295.23 | 11.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 6.93 | 2.65 | 0.15 | 124079.63 | 22.42 | skipped_fast |
| EDELUSDT | IDLE | 0.5 | 5.36 | 2.67 | 0.08 | 220855.22 | 20.37 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.11 | 1.83 | -0.02 | 124418.59 | 42.18 | skipped_fast |
| RWAINCUSDT | IDLE | 0.81 | 3.53 | 2.22 | 0.05 | 23636.95 | 111.56 | skipped_fast |
| MNSRYUSDT | IDLE | 1.28 | 2.42 | 0.9 | 0.03 | 43153.73 | 20.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.39 | 2.49 | 1.97 | 0.03 | 915.96 | 20.28 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.73 | 0.0 | 58054.88 | 7.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
