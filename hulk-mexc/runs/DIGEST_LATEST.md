# Hulk DIGEST — 2026-08-21T22:35:49Z

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
| PYTHUSDT | IDLE | 1.37 | 5.17 | 0.57 | 0.11 | 5822451.72 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.59 | 5.91 | 0.35 | 0.14 | 134683256.0 | 4.17 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 6.74 | 0.0 | 0.14 | 659013.28 | 4.43 | skipped_fast |
| HBARUSDT | IDLE | 2.23 | 4.71 | 1.02 | 0.08 | 869022.56 | 6.35 | skipped_fast |
| WUSDT | IDLE | 2.47 | 5.3 | 0.47 | 0.08 | 370961.79 | 15.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 6.77 | 0.52 | 0.11 | 503147.31 | 7.39 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.45 | 0.06 | 533802.71 | 3.06 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.45 | 0.03 | 188350.86 | 6.24 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.08 | 0.18 | 155958.71 | 8.9 | skipped_fast |
| EDELUSDT | IDLE | 2.31 | 5.04 | 0.44 | -0.04 | 82569.32 | 43.91 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.07 | 2.43 | 0.02 | 10212.45 | 16.17 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.77 | 0.06 | 187069.32 | 15.54 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3825.97 | 63.67 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.2 | 0.11 | 61491.5 | 12.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.79 | 0.06 | 56357.6 | 45.14 | skipped_fast |
| QNTUSDT | IDLE | 2.03 | 4.06 | 0.0 | 0.06 | 73811.41 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.88 | 1.75 | 0.0 | 0.04 | 54182.94 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 20.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
