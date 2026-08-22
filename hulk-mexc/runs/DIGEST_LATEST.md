# Hulk DIGEST — 2026-08-22T15:40:15Z

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
| PYTHUSDT | IDLE | 1.57 | 7.62 | 1.15 | 0.05 | 51500605.57 | 7.88 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.05 | 0.02 | 215865099.68 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 5.65 | 3.17 | 0.07 | 794608.01 | 3.43 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.38 | -0.02 | 1156752.12 | 5.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.63 | 3.51 | 2.23 | -0.09 | 605205.93 | 3.4 | skipped_fast |
| WUSDT | IDLE | 0.78 | 3.17 | 1.61 | -0.02 | 554241.21 | 13.87 | skipped_fast |
| KITEUSDT | IDLE | 2.76 | 6.37 | 2.06 | 0.03 | 85319.61 | 8.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.83 | -0.05 | 319874.22 | 16.97 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 4.98 | -0.07 | 221022.65 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.05 | 79024.76 | 22.78 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 5.18 | -0.1 | 144752.3 | 23.07 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.22 | 0.03 | 56479.2 | 23.62 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.22 | -0.02 | 185198.12 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.63 | -0.01 | 140391.84 | 48.04 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.57 | 0.02 | 57394.29 | 16.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
