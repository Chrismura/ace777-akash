# Hulk DIGEST — 2026-08-21T04:29:58Z

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
| PYTHUSDT | IDLE | 2.11 | 4.63 | 1.11 | 0.07 | 1953523.33 | 2.19 | skipped_fast |
| XRPUSDT | IDLE | 1.0 | 5.29 | 1.67 | 0.18 | 114518286.17 | 0.77 | skipped_fast |
| CHIPUSDT | IDLE | 2.14 | 12.78 | 4.58 | 0.14 | 441034.67 | 9.06 | skipped_fast |
| CCUSDT | IDLE | 1.87 | 3.7 | 0.25 | 0.01 | 473204.82 | 8.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.89 | 5.53 | 3.54 | 0.04 | 300106.1 | 42.13 | skipped_fast |
| EDELUSDT | IDLE | 2.77 | 5.22 | 2.11 | 0.01 | 77344.19 | 21.55 | skipped_fast |
| HBARUSDT | IDLE | 1.7 | 3.31 | 0.65 | 0.06 | 491729.81 | 4.0 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 4.71 | 1.7 | 0.08 | 224034.98 | 6.41 | skipped_fast |
| WUSDT | IDLE | 1.02 | 1.88 | 1.01 | 0.06 | 267596.81 | 7.74 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 4.77 | 3.57 | 0.02 | 182488.5 | 21.13 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 3.77 | 0.0 | 0.05 | 8554.58 | 76.42 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.97 | 0.37 | 0.04 | 61971.1 | 15.02 | skipped_fast |
| QAITUSDT | IDLE | 1.0 | 2.55 | 0.47 | -0.02 | 6718.75 | 67.45 | skipped_fast |
| TELUSDT | IDLE | 0.69 | 3.43 | 2.68 | 0.13 | 200634.11 | 49.46 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 1.48 | 1.31 | 0.04 | 64805.34 | 3.25 | skipped_fast |
| RIZEUSDT | IDLE | 1.11 | 5.34 | 2.03 | -0.12 | 39558.44 | 207.08 | skipped_fast |
| FLUIDUSDT | IDLE | 1.03 | 2.26 | 0.8 | 0.09 | 2600.53 | 22.29 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.77 | 0.51 | 0.01 | 54563.84 | 8.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
