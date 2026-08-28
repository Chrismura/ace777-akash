# Hulk DIGEST — 2026-08-28T02:05:43Z

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
| PYTHUSDT | IDLE | 1.57 | 3.89 | 1.62 | 0.02 | 22800306.03 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.19 | 2.11 | 1.84 | 0.02 | 53641431.95 | 2.07 | skipped_fast |
| QAITUSDT | IDLE | 1.03 | 49.9 | 31.75 | -0.2 | 59623.07 | 65.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.15 | 6.73 | 0.12 | 0.14 | 799247.01 | 4.89 | skipped_fast |
| CCUSDT | IDLE | 1.83 | 3.43 | 1.48 | -0.02 | 458813.06 | 10.58 | skipped_fast |
| KITEUSDT | IDLE | 2.43 | 4.64 | 1.47 | 0.02 | 74610.0 | 9.28 | skipped_fast |
| RWAINCUSDT | IDLE | 2.3 | 8.19 | 4.04 | -0.02 | 22382.43 | 21.37 | skipped_fast |
| REDUSDT | IDLE | 1.84 | 3.65 | 0.14 | 0.04 | 81372.13 | 12.48 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.45 | 1.53 | 0.01 | 182182.47 | 15.5 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 2.54 | 2.11 | 0.03 | 97722.05 | 6.84 | skipped_fast |
| ZBCNUSDT | IDLE | 0.82 | 2.75 | 1.82 | 0.08 | 237600.57 | 25.35 | skipped_fast |
| RIZEUSDT | IDLE | 0.74 | 9.33 | 1.58 | -0.16 | 112970.84 | 42.67 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.4 | 1.33 | 0.01 | 328491.01 | 1.27 | skipped_fast |
| TELUSDT | IDLE | 1.31 | 2.49 | 1.76 | 0.03 | 122259.45 | 36.77 | skipped_fast |
| EDELUSDT | IDLE | 0.44 | 3.18 | 2.83 | 0.12 | 29093.17 | 102.21 | skipped_fast |
| QNTUSDT | IDLE | 0.68 | 1.19 | 1.08 | -0.01 | 44156.91 | 4.77 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.17 | 0.25 | 0.02 | 54285.52 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.35 | 1.1 | 0.12 | -0.0 | 8387.32 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
