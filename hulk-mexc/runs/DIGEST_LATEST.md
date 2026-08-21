# Hulk DIGEST — 2026-08-21T21:09:51Z

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
| PYTHUSDT | IDLE | 1.22 | 4.51 | 1.99 | 0.08 | 5589557.78 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 3.73 | 2.44 | 0.1 | 128016289.45 | 1.45 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 8.19 | 5.65 | 0.08 | 480747.83 | 26.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 4.62 | 4.32 | 0.08 | 514063.72 | 12.49 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.41 | 0.1 | 642103.49 | 7.37 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.04 | 1.56 | 0.06 | 805734.22 | 1.3 | skipped_fast |
| WUSDT | IDLE | 2.0 | 3.83 | 1.11 | 0.06 | 368002.21 | 10.52 | skipped_fast |
| BIOUSDT | IDLE | 2.49 | 5.2 | 2.95 | 0.0 | 187814.47 | 3.17 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.49 | 0.16 | 153448.2 | 9.04 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.54 | 1.53 | 0.02 | 56221.93 | 29.91 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 4.12 | 3.41 | -0.06 | 82274.98 | 34.07 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10934.2 | 16.11 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.0 | 2.43 | 0.11 | 61185.71 | 13.96 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.22 | 0.02 | 180283.17 | 37.58 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 155.29 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.85 | 0.03 | 60124.11 | 4.7 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.82 | 0.03 | 53759.78 | 24.93 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 21.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
