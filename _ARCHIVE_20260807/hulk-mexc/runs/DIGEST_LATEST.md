# Hulk DIGEST — 2026-07-28T21:05:07Z

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
| XRPUSDT | IDLE | 0.54 | 1.07 | 0.08 | -0.02 | 18266148.36 | 1.88 | skipped_fast |
| PYTHUSDT | IDLE | 1.46 | 3.47 | 2.13 | -0.07 | 363133.06 | 4.79 | skipped_fast |
| RIZEUSDT | IDLE | 2.98 | 5.54 | 2.75 | -0.03 | 36035.08 | 31.52 | skipped_fast |
| ZBCNUSDT | IDLE | 1.17 | 2.1 | 1.59 | -0.04 | 213495.3 | 22.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.44 | 2.74 | 0.89 | -0.05 | 84960.04 | 3.9 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.23 | 0.44 | -0.02 | 139424.91 | 8.39 | skipped_fast |
| BIOUSDT | IDLE | 1.33 | 2.8 | 2.14 | -0.08 | 65611.74 | 4.21 | skipped_fast |
| WUSDT | IDLE | 0.72 | 1.32 | 0.77 | -0.0 | 222031.69 | 13.35 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.68 | 0.82 | -0.05 | 33999.84 | 27.62 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 5.61 | 3.48 | -0.15 | 50133.78 | 48.43 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 1.58 | 0.6 | -0.02 | 59573.53 | 13.08 | skipped_fast |
| QAITUSDT | IDLE | 1.1 | 2.07 | 0.85 | -0.01 | 9167.6 | 37.15 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 1.07 | 0.51 | -0.04 | 60950.72 | 14.93 | skipped_fast |
| HBARUSDT | IDLE | 0.88 | 1.6 | 1.04 | -0.01 | 208957.64 | 1.46 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.62 | -0.03 | 68924.4 | 4.94 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.24 | 1.07 | -0.03 | 109457.2 | 34.05 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.78 | 0.69 | -0.01 | 52197.26 | 8.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 1.78 | 1.75 | -0.04 | 15987.05 | 21.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
