# Hulk DIGEST — 2026-08-16T21:08:50Z

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
| XRPUSDT | IDLE | 0.32 | 0.58 | 0.41 | -0.0 | 5863581.9 | 2.0 | skipped_fast |
| RIZEUSDT | IDLE | 3.07 | 6.05 | 0.6 | 0.02 | 36713.43 | 60.13 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 5.71 | 1.62 | 0.09 | 275344.17 | 6.86 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 2.03 | 1.58 | -0.03 | 336751.73 | 7.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.62 | 2.89 | 2.29 | -0.0 | 193383.02 | 11.52 | skipped_fast |
| WUSDT | IDLE | 1.49 | 2.62 | 2.34 | 0.01 | 177863.28 | 16.54 | skipped_fast |
| PYTHUSDT | IDLE | 1.5 | 2.66 | 2.24 | -0.02 | 134011.0 | 2.58 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.64 | 2.57 | -0.02 | 65597.67 | 4.13 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 2.67 | 1.43 | 0.03 | 60184.33 | 52.63 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 1.45 | 1.42 | -0.03 | 56527.68 | 13.9 | skipped_fast |
| QAITUSDT | IDLE | 1.23 | 3.47 | 2.01 | -0.04 | 2388.15 | 61.48 | skipped_fast |
| REDUSDT | IDLE | 0.3 | 1.7 | 1.31 | -0.24 | 74053.22 | 14.99 | skipped_fast |
| RWAINCUSDT | IDLE | 1.04 | 2.96 | 0.0 | 0.09 | 9918.52 | 62.13 | skipped_fast |
| HBARUSDT | IDLE | 0.4 | 0.69 | 0.67 | -0.01 | 96756.88 | 1.54 | skipped_fast |
| TELUSDT | IDLE | 0.67 | 1.18 | 1.03 | -0.02 | 93532.35 | 41.41 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.05 | 1.04 | -0.02 | 32120.57 | 7.04 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.61 | 0.17 | 0.0 | 51576.37 | 17.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 0.62 | 0.11 | 0.02 | 219.43 | 21.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
