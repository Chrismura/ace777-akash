# Hulk DIGEST — 2026-08-21T22:05:35Z

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
| PYTHUSDT | IDLE | 1.25 | 4.74 | 0.27 | 0.1 | 5699369.52 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.21 | 4.21 | 0.03 | 0.13 | 129946559.22 | 2.11 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.71 | 0.49 | 0.08 | 840831.06 | 3.79 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 4.04 | 0.0 | 0.11 | 636311.46 | 8.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.05 | 0.06 | 531263.04 | 6.15 | skipped_fast |
| WUSDT | IDLE | 2.27 | 4.52 | 0.1 | 0.07 | 368446.48 | 9.31 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 6.22 | 0.15 | 0.12 | 495169.32 | 15.3 | skipped_fast |
| BIOUSDT | IDLE | 2.25 | 5.01 | 0.71 | 0.04 | 185396.88 | 6.2 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.65 | 0.18 | 153844.91 | 8.95 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.45 | 1.44 | 0.05 | 186587.81 | 20.8 | skipped_fast |
| EDELUSDT | IDLE | 1.88 | 4.12 | 0.22 | -0.03 | 82453.02 | 33.17 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 4.07 | 0.9 | 0.02 | 10204.87 | 58.74 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.97 | 0.11 | 61292.18 | 10.14 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.83 | 0.06 | 56422.9 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 2.49 | 0.0 | 0.05 | 62373.35 | 3.08 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.67 | 0.41 | 0.04 | 54092.51 | 16.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
