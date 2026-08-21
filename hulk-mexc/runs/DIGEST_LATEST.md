# Hulk DIGEST — 2026-08-21T21:01:06Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.7 | 0.09 | 5574319.44 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.18 | 3.73 | 2.81 | 0.11 | 128230508.66 | 2.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 8.19 | 6.1 | 0.08 | 480212.62 | 55.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.62 | 3.7 | 0.08 | 514576.95 | 3.09 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 3.14 | 0.06 | 0.1 | 642073.82 | 5.52 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.04 | 1.51 | 0.06 | 809396.42 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.83 | 0.86 | 0.07 | 368150.99 | 14.68 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.2 | 2.7 | 0.01 | 187919.48 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.68 | 0.17 | 152916.34 | 19.55 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.54 | 1.68 | 0.01 | 56230.07 | 45.77 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.12 | 2.97 | -0.06 | 82463.33 | 45.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 32.12 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.0 | 2.24 | 0.11 | 61228.61 | 9.29 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 181293.38 | 37.56 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.04 | 60175.42 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 171.08 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.08 | 0.74 | 0.03 | 53858.13 | 24.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
