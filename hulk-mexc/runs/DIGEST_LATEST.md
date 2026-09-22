# Hulk DIGEST — 2026-09-22T23:16:00Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.88 | 3.48 | 1.89 | 0.01 | 107539284.18 | 1.9 | skipped_fast |
| PYTHUSDT | IDLE | 0.77 | 3.74 | 0.72 | 0.06 | 1678738.63 | 2.98 | skipped_fast |
| HBARUSDT | IDLE | 2.03 | 5.15 | 0.85 | 0.07 | 1684405.3 | 1.0 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.4 | 0.29 | -0.01 | 423895111.79 | 0.54 | skipped_fast |
| BTCUSDT | IDLE | 0.4 | 0.76 | 0.33 | -0.0 | 905083512.81 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.55 | 42.49 | 7.33 | 0.14 | 50780.22 | 82.83 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.63 | 9.03 | 5.71 | 0.01 | 20205.35 | 21.45 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.86 | 0.0 | -0.03 | 485223.83 | 7.81 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.23 | 0.25 | 0.03 | 325236.46 | 8.18 | skipped_fast |
| EDELUSDT | IDLE | 1.75 | 7.91 | 4.57 | -0.0 | 242287.25 | 49.74 | skipped_fast |
| CHIPUSDT | IDLE | 2.17 | 4.55 | 0.26 | -0.0 | 136684.66 | 17.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.28 | 1.94 | -0.03 | 214531.39 | 17.46 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.78 | 0.07 | 0.03 | 135849.36 | 10.02 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 2.11 | 0.06 | 0.06 | 63660.17 | 13.12 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 4.82 | 1.35 | 0.1 | 210920.24 | 4.05 | skipped_fast |
| KITEUSDT | IDLE | 0.62 | 2.75 | 0.62 | 0.17 | 113364.39 | 10.03 | skipped_fast |
| TELUSDT | IDLE | 1.33 | 5.51 | 0.75 | 0.11 | 101589.84 | 43.45 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.51 | 0.36 | -0.0 | 53064.76 | 7.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.44 | 0.86 | 0.13 | 0.02 | 5956.82 | 21.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.06 | -0.01 | 39952.4 | 9.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
