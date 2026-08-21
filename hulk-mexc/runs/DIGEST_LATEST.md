# Hulk DIGEST — 2026-08-21T22:06:17Z

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
| PYTHUSDT | IDLE | 1.25 | 4.74 | 0.27 | 0.1 | 5700159.62 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 4.77 | 0.18 | 0.13 | 130103068.83 | 1.4 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 4.71 | 0.35 | 0.08 | 841085.06 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 4.04 | 0.02 | 0.11 | 636338.27 | 6.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.05 | 0.06 | 531230.26 | 6.15 | skipped_fast |
| WUSDT | IDLE | 2.27 | 4.52 | 0.12 | 0.07 | 367800.64 | 12.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 6.22 | 0.17 | 0.12 | 495318.7 | 11.84 | skipped_fast |
| BIOUSDT | IDLE | 2.26 | 5.01 | 0.74 | 0.04 | 185426.55 | 6.2 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.71 | 0.18 | 154711.07 | 0.81 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 4.12 | 0.77 | -0.03 | 82478.06 | 22.12 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.45 | 1.44 | 0.05 | 186626.21 | 25.99 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 4.07 | 0.9 | 0.02 | 10204.87 | 58.74 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 3.58 | 0.97 | 0.11 | 61286.78 | 11.98 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.76 | 0.06 | 56421.93 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 1.25 | 2.49 | 0.06 | 0.05 | 62381.13 | 7.7 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.67 | 0.41 | 0.04 | 54106.8 | 8.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 37.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
