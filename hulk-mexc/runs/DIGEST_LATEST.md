# Hulk DIGEST — 2026-08-18T01:08:52Z

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
| XRPUSDT | IDLE | 0.3 | 0.54 | 0.35 | 0.0 | 11898675.94 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.22 | 5.74 | 3.93 | -0.0 | 338348.31 | 7.25 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.78 | 0.32 | -0.05 | 273907.52 | 11.03 | skipped_fast |
| EDELUSDT | IDLE | 1.52 | 2.77 | 1.79 | -0.0 | 65960.86 | 26.11 | skipped_fast |
| PYTHUSDT | IDLE | 0.86 | 1.56 | 1.08 | -0.01 | 144403.14 | 2.59 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 7.23 | 5.72 | 0.05 | 88138.35 | 47.1 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 5.85 | 2.59 | -0.05 | 131739.47 | 64.63 | skipped_fast |
| ZBCNUSDT | IDLE | 0.56 | 1.01 | 0.7 | 0.0 | 228251.55 | 12.69 | skipped_fast |
| WUSDT | IDLE | 0.9 | 1.62 | 1.26 | -0.04 | 133921.54 | 8.52 | skipped_fast |
| QAITUSDT | IDLE | 1.89 | 3.62 | 1.08 | -0.04 | 4076.43 | 60.02 | skipped_fast |
| BIOUSDT | IDLE | 0.61 | 1.06 | 1.05 | 0.02 | 81356.57 | 4.07 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.79 | 0.34 | 0.01 | 57225.43 | 26.38 | skipped_fast |
| KITEUSDT | IDLE | 0.71 | 1.28 | 0.98 | -0.01 | 60134.5 | 14.11 | skipped_fast |
| RWAINCUSDT | IDLE | 0.41 | 0.76 | 0.41 | -0.03 | 1057.17 | 58.58 | skipped_fast |
| HBARUSDT | IDLE | 0.32 | 0.62 | 0.14 | 0.02 | 121968.05 | 1.51 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.06 | 0.7 | 0.01 | 34980.64 | 7.03 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.24 | 1.12 | -0.03 | 751.16 | 21.69 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.61 | 0.17 | 0.01 | 49538.79 | 25.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
