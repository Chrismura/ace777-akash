# Hulk DIGEST — 2026-08-21T23:17:28Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.46 | 0.12 | 6023214.57 | 6.08 | skipped_fast |
| XRPUSDT | IDLE | 1.76 | 6.77 | 0.48 | 0.14 | 138622948.25 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 2.48 | 5.82 | 0.04 | 0.1 | 892948.74 | 2.49 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 7.42 | 1.29 | 0.13 | 654646.51 | 4.46 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 10.14 | 0.08 | 0.14 | 511451.3 | 12.82 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.48 | 0.08 | 377022.63 | 12.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.16 | 0.05 | 547425.54 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.2 | 0.02 | 187901.83 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.52 | 5.5 | 0.43 | -0.03 | 82514.65 | 10.91 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 9.82 | 0.49 | 0.14 | 59493.27 | 44.02 | skipped_fast |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 26.99 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.96 | 0.18 | 157440.51 | 10.52 | skipped_fast |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.31 | 0.07 | 184960.33 | 51.41 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 2.51 | 5.22 | 0.04 | 0.07 | 118535.7 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 3.12 | 1.34 | 0.09 | 61591.72 | 12.07 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.33 | 0.04 | 54450.95 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 2.35 | 0.18 | 0.1 | 4226.13 | 20.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
