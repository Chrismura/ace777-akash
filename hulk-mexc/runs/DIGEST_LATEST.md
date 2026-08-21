# Hulk DIGEST — 2026-08-21T22:14:10Z

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
| PYTHUSDT | IDLE | 1.35 | 5.17 | 0.12 | 0.11 | 5717368.52 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.53 | 5.44 | 0.82 | 0.14 | 131553930.67 | 6.31 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 6.42 | 0.01 | 0.14 | 644179.25 | 12.45 | skipped_fast |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.63 | 0.08 | 846333.49 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.44 | 5.24 | 0.0 | 0.08 | 369047.99 | 14.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.47 | 4.54 | 1.08 | 0.07 | 534581.67 | 3.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 6.5 | 0.11 | 0.11 | 498131.13 | 26.54 | skipped_fast |
| BIOUSDT | IDLE | 2.24 | 5.04 | 0.37 | 0.02 | 187667.99 | 3.09 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.08 | 0.19 | 155782.77 | 12.13 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.72 | 0.06 | 186822.98 | 20.7 | skipped_fast |
| EDELUSDT | IDLE | 1.86 | 4.12 | 0.0 | -0.03 | 82388.23 | 33.06 | skipped_fast |
| RWAINCUSDT | IDLE | 2.17 | 4.07 | 1.8 | 0.02 | 10212.63 | 37.4 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 3.58 | 0.45 | 0.12 | 61391.9 | 11.91 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.72 | 0.06 | 56399.58 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.05 | 65333.43 | 10.7 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.41 | 0.04 | 54366.81 | 8.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 16.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
