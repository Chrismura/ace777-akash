# Hulk DIGEST — 2026-08-19T04:10:38Z

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
| XRPUSDT | IDLE | 0.36 | 0.66 | 0.38 | 0.01 | 10296080.38 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 5.6 | 3.56 | -0.08 | 186993.53 | 3.85 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.25 | 1.14 | 0.03 | 177852.55 | 5.14 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.56 | 2.05 | -0.02 | 216244.39 | 5.57 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 5.65 | 5.35 | -0.01 | 166760.63 | 15.72 | skipped_fast |
| ZBCNUSDT | IDLE | 0.87 | 1.58 | 1.01 | 0.0 | 157688.71 | 20.49 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.96 | 0.24 | 0.03 | 63159.19 | 4.02 | skipped_fast |
| WUSDT | IDLE | 0.62 | 1.12 | 0.74 | -0.01 | 125809.68 | 12.42 | skipped_fast |
| EDELUSDT | IDLE | 0.77 | 2.29 | 1.19 | -0.03 | 73532.02 | 26.67 | skipped_fast |
| KITEUSDT | IDLE | 0.74 | 1.29 | 1.22 | -0.03 | 65525.45 | 14.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.5 | 3.92 | 2.31 | -0.05 | 27807.65 | 169.91 | skipped_fast |
| QAITUSDT | IDLE | 0.48 | 3.72 | 3.58 | -0.18 | 12357.27 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.49 | 0.41 | -0.0 | 10867.32 | 94.62 | skipped_fast |
| HBARUSDT | IDLE | 0.56 | 1.12 | 0.03 | 0.04 | 112263.38 | 1.48 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 1.88 | 0.96 | 0.04 | 84105.58 | 48.29 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 1.4 | 0.14 | 0.01 | 37874.67 | 5.32 | skipped_fast |
| RWAUSDT | IDLE | 0.24 | 0.44 | 0.26 | -0.01 | 51352.36 | 8.72 | skipped_fast |
| FLUIDUSDT | IDLE | 0.48 | 0.84 | 0.83 | -0.01 | 187.94 | 22.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
