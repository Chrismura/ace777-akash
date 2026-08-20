# Hulk DIGEST — 2026-08-20T03:20:24Z

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
| XRPUSDT | IDLE | 1.47 | 4.46 | 3.86 | 0.09 | 45591111.91 | 0.92 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.42 | 22.95 | 12.55 | 0.07 | 56231.56 | 195.75 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 4.08 | 2.19 | 0.1 | 376631.3 | 9.01 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.93 | 2.56 | 0.06 | 269294.48 | 10.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 5.71 | 0.55 | 0.12 | 208435.41 | 13.78 | skipped_fast |
| PYTHUSDT | IDLE | 0.79 | 2.41 | 0.65 | 0.1 | 305671.55 | 2.35 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 6.6 | 2.17 | 0.1 | 102308.6 | 13.17 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 5.48 | 1.11 | 0.15 | 165227.36 | 3.5 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 3.06 | 2.93 | 0.12 | 229313.87 | 23.78 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.16 | 1.91 | 0.04 | 356585.71 | 2.84 | skipped_fast |
| QAITUSDT | IDLE | 1.26 | 3.23 | 2.45 | 0.01 | 10680.55 | 65.07 | skipped_fast |
| KITEUSDT | IDLE | 0.55 | 1.09 | 0.37 | 0.06 | 59479.55 | 14.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.83 | 0.9 | 0.04 | 17163.5 | 39.49 | skipped_fast |
| EDELUSDT | IDLE | 0.4 | 2.02 | 1.76 | 0.19 | 83743.0 | 55.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.49 | 3.84 | 3.7 | 0.06 | 3462.78 | 17.81 | skipped_fast |
| TELUSDT | IDLE | 0.54 | 2.37 | 2.08 | 0.1 | 189341.25 | 24.97 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.5 | 1.03 | 0.04 | 37460.54 | 6.8 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.69 | 0.43 | 0.01 | 53436.33 | 8.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
