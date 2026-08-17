# Hulk DIGEST — 2026-08-17T19:08:13Z

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
| XRPUSDT | IDLE | 0.56 | 1.01 | 0.72 | 0.0 | 12797171.93 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 9.58 | 8.15 | -0.01 | 350049.68 | 3.54 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 6.28 | 5.91 | 0.01 | 65790.81 | 52.42 | skipped_fast |
| ZBCNUSDT | IDLE | 2.44 | 4.83 | 0.34 | 0.02 | 197704.56 | 11.88 | skipped_fast |
| REDUSDT | IDLE | 2.83 | 5.41 | 1.63 | -0.01 | 58418.87 | 15.16 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 3.16 | 2.71 | -0.05 | 231254.85 | 6.62 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 11.55 | 7.13 | 0.15 | 86290.9 | 47.09 | skipped_fast |
| QAITUSDT | IDLE | 2.72 | 5.09 | 2.34 | -0.02 | 1007.97 | 94.79 | skipped_fast |
| PYTHUSDT | IDLE | 1.06 | 1.92 | 1.33 | -0.01 | 162982.59 | 2.58 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.49 | 1.75 | 0.01 | 82268.88 | 4.05 | skipped_fast |
| WUSDT | IDLE | 0.97 | 1.69 | 1.64 | -0.03 | 150152.35 | 12.09 | skipped_fast |
| TELUSDT | IDLE | 1.89 | 3.44 | 2.22 | -0.03 | 119473.0 | 56.7 | skipped_fast |
| FLUIDUSDT | IDLE | 2.07 | 3.61 | 3.49 | -0.03 | 751.15 | 24.14 | skipped_fast |
| KITEUSDT | IDLE | 0.54 | 1.02 | 0.42 | -0.02 | 60300.19 | 16.19 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.19 | 0.78 | 0.01 | 144344.91 | 1.52 | skipped_fast |
| RWAINCUSDT | IDLE | 0.3 | 0.52 | 0.52 | -0.03 | 1225.45 | 63.97 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.51 | 0.76 | 0.0 | 37394.89 | 8.73 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.69 | 0.52 | 0.01 | 49369.71 | 8.65 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
