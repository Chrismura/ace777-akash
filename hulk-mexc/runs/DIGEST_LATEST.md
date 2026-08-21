# Hulk DIGEST — 2026-08-21T21:10:28Z

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
| PYTHUSDT | IDLE | 1.22 | 4.51 | 2.01 | 0.08 | 5590763.09 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 3.73 | 2.43 | 0.1 | 127935377.01 | 0.73 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 8.19 | 5.62 | 0.08 | 480876.42 | 25.04 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 5.61 | 5.13 | 0.07 | 514134.4 | 18.81 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.39 | 0.1 | 642122.43 | 7.37 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.04 | 1.55 | 0.06 | 805756.69 | 1.3 | skipped_fast |
| WUSDT | IDLE | 2.0 | 3.83 | 1.11 | 0.06 | 368032.84 | 10.52 | skipped_fast |
| BIOUSDT | IDLE | 2.5 | 5.2 | 3.1 | 0.0 | 187814.47 | 3.17 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.53 | 0.16 | 153508.21 | 9.04 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.12 | 3.19 | -0.06 | 82274.97 | 22.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.54 | 1.53 | 0.01 | 56231.85 | 29.91 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10934.2 | 26.8 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.0 | 2.43 | 0.11 | 61221.05 | 13.96 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 180299.01 | 37.58 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.85 | 0.03 | 60114.85 | 7.82 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 167.13 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.82 | 0.03 | 53721.81 | 16.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 21.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
