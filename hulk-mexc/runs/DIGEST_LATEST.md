# Hulk DIGEST — 2026-08-22T12:28:17Z

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.61 | 0.11 | 215821785.58 | 2.63 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 7.83 | 1.92 | 0.05 | 51603745.3 | 1.98 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 4.63 | 2.1 | 0.03 | 1260439.02 | 7.69 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 8.38 | 2.89 | 0.14 | 773751.1 | 9.21 | skipped_fast |
| WUSDT | IDLE | 1.54 | 6.27 | 3.28 | 0.02 | 577642.29 | 14.74 | skipped_fast |
| ZBCNUSDT | IDLE | 2.18 | 5.77 | 3.29 | -0.02 | 370978.58 | 19.42 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.16 | -0.09 | 606329.6 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.58 | 6.24 | 0.06 | 0.05 | 83490.27 | 11.41 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.02 | 78154.47 | 33.88 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 5.65 | 0.97 | -0.02 | 242005.5 | 3.17 | skipped_fast |
| QAITUSDT | IDLE | 2.25 | 4.16 | 2.33 | -0.01 | 2396.75 | 43.59 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.51 | 0.02 | 153255.56 | 11.45 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.88 | -0.03 | 163880.76 | 47.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 3.47 | 1.06 | 0.01 | 188107.87 | 7.75 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.27 | -0.03 | 47956.82 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.99 | 1.8 | 1.2 | 0.02 | 57781.87 | 8.13 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 21.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
