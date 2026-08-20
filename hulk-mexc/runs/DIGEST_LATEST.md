# Hulk DIGEST — 2026-08-20T20:28:11Z

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
| XRPUSDT | IDLE | 1.93 | 10.14 | 7.99 | 0.15 | 106472441.72 | 1.62 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.51 | 1.64 | 0.06 | 1339631.42 | 2.28 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 11.37 | 6.0 | 0.05 | 293619.07 | 18.87 | skipped_fast |
| CCUSDT | IDLE | 2.18 | 3.84 | 3.41 | 0.0 | 478271.22 | 11.03 | skipped_fast |
| CHIPUSDT | IDLE | 2.34 | 6.82 | 3.92 | 0.07 | 293628.4 | 3.35 | skipped_fast |
| HBARUSDT | IDLE | 2.07 | 3.82 | 2.16 | 0.04 | 508407.74 | 1.37 | skipped_fast |
| WUSDT | IDLE | 1.51 | 2.76 | 1.68 | 0.05 | 310878.36 | 10.11 | skipped_fast |
| TELUSDT | IDLE | 2.39 | 12.91 | 6.53 | 0.17 | 189943.71 | 32.75 | skipped_fast |
| QAITUSDT | IDLE | 2.8 | 7.22 | 0.77 | 0.0 | 5838.81 | 66.45 | skipped_fast |
| KITEUSDT | IDLE | 1.96 | 3.55 | 2.52 | 0.02 | 64675.39 | 24.69 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 4.19 | 1.49 | 0.13 | 235063.38 | 3.22 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 5.19 | 0.21 | 0.1 | 91746.7 | 21.48 | skipped_fast |
| RIZEUSDT | IDLE | 1.11 | 5.83 | 3.67 | 0.05 | 48713.68 | 46.43 | skipped_fast |
| REDUSDT | IDLE | 0.36 | 2.55 | 0.09 | 0.11 | 187108.33 | 10.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.11 | 4.08 | 0.87 | 0.04 | 7126.06 | 126.48 | skipped_fast |
| QNTUSDT | IDLE | 1.98 | 4.04 | 3.34 | 0.06 | 63419.12 | 6.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.61 | 3.5 | 0.59 | 0.09 | 1890.82 | 22.48 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.91 | 0.77 | 0.02 | 54291.44 | 17.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
