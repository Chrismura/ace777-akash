# Hulk DIGEST — 2026-08-16T18:18:48Z

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
| XRPUSDT | IDLE | 0.32 | 0.58 | 0.46 | -0.0 | 5227271.61 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.97 | 10.74 | 7.51 | 0.14 | 282976.92 | 3.48 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.74 | 2.19 | -0.04 | 333732.04 | 7.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 2.92 | 2.54 | -0.01 | 192782.54 | 14.11 | skipped_fast |
| WUSDT | IDLE | 1.17 | 2.06 | 1.8 | 0.02 | 168524.42 | 10.52 | skipped_fast |
| RIZEUSDT | IDLE | 1.8 | 3.43 | 1.11 | -0.03 | 42503.83 | 62.01 | skipped_fast |
| QAITUSDT | IDLE | 1.64 | 4.87 | 2.98 | -0.06 | 2708.91 | 61.86 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.84 | 1.65 | -0.02 | 62581.13 | 4.08 | skipped_fast |
| PYTHUSDT | IDLE | 0.69 | 1.22 | 1.03 | -0.01 | 123500.9 | 2.55 | skipped_fast |
| EDELUSDT | IDLE | 1.34 | 2.4 | 1.83 | -0.03 | 60779.83 | 52.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.44 | 4.0 | 1.62 | 0.07 | 9965.81 | 73.72 | skipped_fast |
| KITEUSDT | IDLE | 0.5 | 0.9 | 0.63 | -0.02 | 57258.53 | 15.91 | skipped_fast |
| REDUSDT | IDLE | 0.14 | 1.18 | 1.02 | -0.04 | 88877.51 | 14.92 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 1.88 | 0.48 | -0.03 | 96472.63 | 48.13 | skipped_fast |
| QNTUSDT | IDLE | 0.56 | 0.98 | 0.89 | -0.01 | 32574.67 | 3.51 | skipped_fast |
| HBARUSDT | IDLE | 0.31 | 0.55 | 0.43 | -0.01 | 75623.81 | 1.53 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.79 | 0.26 | -0.0 | 52288.92 | 17.47 | skipped_fast |
| FLUIDUSDT | IDLE | 0.49 | 0.92 | 0.4 | 0.02 | 219.43 | 21.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
