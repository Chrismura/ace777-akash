# Hulk DIGEST — 2026-08-22T15:48:09Z

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
| PYTHUSDT | IDLE | 1.58 | 7.62 | 1.42 | 0.04 | 51492545.66 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 5.98 | 0.02 | 216106396.87 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.74 | 0.08 | 789794.21 | 9.43 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.4 | -0.02 | 1153998.65 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.29 | -0.09 | 603608.31 | 3.4 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.76 | -0.02 | 554309.48 | 7.48 | skipped_fast |
| KITEUSDT | IDLE | 2.75 | 6.37 | 1.88 | 0.03 | 85498.04 | 14.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.33 | 3.49 | 2.21 | -0.06 | 320779.29 | 27.85 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.92 | -0.07 | 219622.7 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.03 | 76106.27 | 22.78 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.6 | -0.15 | 135090.69 | 12.85 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.15 | 0.03 | 56473.15 | 45.5 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.25 | -0.02 | 184230.5 | 3.16 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 53.68 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.52 | -0.01 | 140541.16 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 20.23 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 57382.44 | 8.11 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
