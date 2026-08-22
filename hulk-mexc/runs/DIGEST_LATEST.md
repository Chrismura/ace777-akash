# Hulk DIGEST — 2026-08-22T16:23:06Z

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
| PYTHUSDT | IDLE | 1.47 | 7.24 | 0.33 | 0.06 | 51442509.91 | 5.86 | skipped_fast |
| XRPUSDT | IDLE | 1.35 | 7.64 | 4.37 | 0.05 | 215643319.84 | 3.42 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.09 | -0.0 | 1139963.22 | 5.17 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.31 | 0.1 | 768239.85 | 7.69 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.56 | -0.09 | 627855.85 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.97 | -0.01 | 544679.19 | 9.53 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 1.97 | -0.04 | 316082.94 | 24.18 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.35 | -0.07 | 219576.04 | 3.3 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.45 | 0.03 | 85436.15 | 11.57 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 2.52 | 2.35 | -0.03 | 74831.11 | 22.88 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.81 | -0.12 | 133769.29 | 27.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.08 | 0.03 | 56572.2 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.13 | -0.02 | 184423.12 | 7.88 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 8652.8 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.26 | 0.0 | 137743.23 | 15.94 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.02 | 56363.47 | 8.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 21.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
