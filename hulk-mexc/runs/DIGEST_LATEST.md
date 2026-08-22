# Hulk DIGEST — 2026-08-22T17:13:27Z

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
| PYTHUSDT | IDLE | 1.73 | 8.48 | 0.57 | 0.1 | 49181196.41 | 1.9 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.83 | 0.05 | 213964603.26 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.14 | -0.0 | 1106474.81 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 4.25 | 0.39 | 0.11 | 772190.41 | 2.51 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.0 | -0.1 | 631197.55 | 3.36 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.39 | -0.01 | 535693.36 | 10.54 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.77 | -0.08 | 226253.22 | 6.69 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 3.45 | 0.97 | -0.01 | 309996.15 | 32.15 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 3.0 | 2.91 | -0.03 | 74832.58 | 34.5 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 3.22 | 0.77 | 0.04 | 87674.18 | 13.27 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.19 | -0.13 | 122284.56 | 13.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.44 | 0.05 | 46183.84 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.97 | -0.01 | 181168.47 | 3.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 86.25 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.89 | -0.0 | 136294.19 | 53.53 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.16 | 0.02 | 56105.82 | 8.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
