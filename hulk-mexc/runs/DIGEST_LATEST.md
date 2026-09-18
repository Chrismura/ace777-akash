# Hulk DIGEST — 2026-09-18T11:27:37Z

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
| XRPUSDT | IDLE | 1.01 | 1.81 | 1.41 | 0.02 | 41504354.96 | 2.27 | skipped_fast |
| ETHUSDT | IDLE | 0.86 | 1.63 | 0.61 | 0.03 | 387047311.99 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.37 | 0.5 | 0.02 | 571970680.79 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 6.0 | 4.86 | 0.06 | 655309.58 | 13.99 | skipped_fast |
| PYTHUSDT | IDLE | 1.59 | 4.64 | 4.3 | 0.08 | 659770.03 | 1.72 | skipped_fast |
| WUSDT | IDLE | 1.15 | 3.24 | 2.14 | 0.1 | 411075.7 | 9.84 | skipped_fast |
| BIOUSDT | IDLE | 2.18 | 5.52 | 3.94 | 0.06 | 84787.43 | 7.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 6.69 | 5.71 | 0.1 | 158897.11 | 11.89 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 2.84 | 1.61 | 0.03 | 487544.92 | 1.3 | skipped_fast |
| TELUSDT | IDLE | 3.03 | 6.08 | 1.25 | 0.04 | 88516.54 | 13.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.11 | 2.22 | 0.03 | 0.04 | 266697.48 | 29.92 | skipped_fast |
| REDUSDT | IDLE | 1.66 | 3.98 | 1.75 | 0.03 | 64371.93 | 10.0 | skipped_fast |
| EDELUSDT | IDLE | 0.58 | 5.86 | 2.04 | -0.03 | 262987.03 | 50.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.67 | 3.28 | 0.41 | -0.01 | 10661.57 | 23.6 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.24 | 0.83 | 0.05 | 75032.69 | 10.0 | skipped_fast |
| FLUIDUSDT | IDLE | 2.5 | 4.83 | 1.19 | 0.05 | 217.96 | 22.65 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.11 | 1.01 | 0.02 | 44415.83 | 4.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.19 | 2.55 | 0.9 | 0.16 | 53154.64 | 91.04 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.97 | 0.44 | 0.02 | 58370.31 | 36.94 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.66 | 0.04 | 0.03 | 42588.65 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
