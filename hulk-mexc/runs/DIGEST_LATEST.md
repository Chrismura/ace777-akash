# Hulk DIGEST — 2026-08-19T10:01:29Z

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
| XRPUSDT | IDLE | 0.54 | 1.01 | 0.49 | 0.01 | 10387758.35 | 1.99 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.42 | 1.22 | 0.04 | 64868.28 | 7.98 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 3.42 | 2.34 | -0.13 | 145438.61 | 21.72 | skipped_fast |
| CHIPUSDT | IDLE | 0.69 | 2.04 | 1.35 | -0.11 | 164907.19 | 3.91 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.19 | 1.34 | -0.0 | 64940.94 | 14.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.86 | 1.48 | -0.05 | 28580.23 | 28.52 | skipped_fast |
| ZBCNUSDT | IDLE | 0.78 | 1.52 | 0.25 | 0.01 | 154930.99 | 15.13 | skipped_fast |
| CCUSDT | IDLE | 0.43 | 0.86 | 0.02 | -0.01 | 213662.38 | 9.96 | skipped_fast |
| PYTHUSDT | IDLE | 0.55 | 0.96 | 0.92 | 0.01 | 163581.39 | 2.59 | skipped_fast |
| WUSDT | IDLE | 0.89 | 1.66 | 0.82 | -0.01 | 102490.42 | 14.9 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 2.31 | 0.27 | -0.04 | 59280.41 | 66.89 | skipped_fast |
| QAITUSDT | IDLE | 0.75 | 4.96 | 0.85 | -0.15 | 12077.3 | 66.45 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 1.49 | 1.12 | -0.02 | 9998.44 | 112.59 | skipped_fast |
| HBARUSDT | IDLE | 0.5 | 0.91 | 0.54 | 0.03 | 126482.38 | 1.48 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.42 | 0.89 | 0.01 | 38385.12 | 7.08 | skipped_fast |
| TELUSDT | IDLE | 0.65 | 1.25 | 0.27 | 0.03 | 86977.98 | 41.27 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.06 | 0.44 | -0.01 | 52583.89 | 17.53 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.66 | 0.0 | -0.01 | 1163.31 | 45.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
