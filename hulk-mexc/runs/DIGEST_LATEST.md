# Hulk DIGEST — 2026-08-21T20:54:06Z

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
| PYTHUSDT | IDLE | 1.3 | 4.78 | 2.23 | 0.09 | 5562993.38 | 4.19 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.47 | 0.1 | 128388490.94 | 0.73 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.76 | 0.17 | 153002.79 | 26.02 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.46 | 0.12 | 478946.07 | 23.98 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.28 | 0.1 | 642151.31 | 8.28 | skipped_fast |
| HBARUSDT | IDLE | 1.71 | 3.23 | 1.72 | 0.06 | 808694.39 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.64 | 0.08 | 514559.04 | 6.19 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.92 | 0.91 | 0.07 | 368106.98 | 13.63 | skipped_fast |
| BIOUSDT | IDLE | 2.51 | 5.33 | 2.48 | 0.01 | 188264.14 | 3.15 | skipped_fast |
| EDELUSDT | IDLE | 2.92 | 5.73 | 4.88 | -0.06 | 82483.19 | 56.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.42 | 0.02 | 56238.74 | 46.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10901.49 | 32.26 | skipped_fast |
| KITEUSDT | IDLE | 1.23 | 4.0 | 2.04 | 0.11 | 61268.84 | 13.91 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.53 | 0.01 | 181285.0 | 42.94 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60252.75 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 190.78 | skipped_fast |
| RWAUSDT | IDLE | 0.7 | 1.25 | 0.99 | 0.03 | 53958.55 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
