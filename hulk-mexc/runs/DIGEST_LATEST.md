# Hulk DIGEST — 2026-08-26T03:10:43Z

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
| PYTHUSDT | IDLE | 2.59 | 5.41 | 1.0 | -0.0 | 2133150.16 | 5.8 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.94 | 76.3 | 38.46 | 0.1 | 57431.55 | 29.29 | skipped_fast |
| XRPUSDT | IDLE | 1.01 | 2.06 | 0.77 | -0.06 | 63976235.24 | 0.69 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.58 | 2.07 | -0.05 | 528622.03 | 9.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.71 | 0.49 | 0.01 | 403454.98 | 6.11 | skipped_fast |
| WUSDT | IDLE | 1.55 | 3.09 | 0.34 | -0.02 | 297088.06 | 9.46 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.84 | 0.43 | -0.05 | 687894.56 | 2.55 | skipped_fast |
| REDUSDT | IDLE | 1.92 | 4.97 | 1.87 | 0.01 | 81030.86 | 11.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.47 | 2.81 | 0.92 | -0.01 | 162781.19 | 13.16 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 3.57 | 1.01 | -0.04 | 60459.09 | 9.75 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 1.76 | 0.88 | -0.02 | 94252.1 | 3.43 | skipped_fast |
| EDELUSDT | IDLE | 0.53 | 7.59 | 5.46 | 0.06 | 155612.52 | 80.04 | skipped_fast |
| QAITUSDT | IDLE | 1.17 | 3.05 | 1.48 | 0.03 | 12825.21 | 30.02 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 1.62 | 1.25 | -0.02 | 2581.87 | 95.94 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 2.12 | 0.0 | -0.03 | 96239.42 | 38.39 | skipped_fast |
| QNTUSDT | IDLE | 0.54 | 1.05 | 0.22 | -0.03 | 134031.53 | 1.57 | skipped_fast |
| RWAUSDT | IDLE | 0.86 | 1.5 | 1.47 | -0.05 | 55699.02 | 24.91 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.85 | 0.0 | -0.03 | 289.45 | 22.0 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
