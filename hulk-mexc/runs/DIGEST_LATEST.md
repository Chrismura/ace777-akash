# Hulk DIGEST — 2026-08-22T12:30:40Z

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
| XRPUSDT | IDLE | 2.47 | 14.26 | 6.5 | 0.11 | 215884216.82 | 3.29 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 7.83 | 1.48 | 0.06 | 51606440.17 | 9.86 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 4.63 | 1.92 | 0.03 | 1260599.46 | 5.12 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.75 | 0.14 | 776024.76 | 8.35 | skipped_fast |
| WUSDT | IDLE | 1.54 | 6.27 | 3.29 | 0.02 | 577699.2 | 11.6 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.6 | -0.02 | 351383.75 | 29.17 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.16 | -0.09 | 605470.73 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.63 | 6.37 | 0.04 | 0.05 | 83477.9 | 11.41 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 3.89 | 2.43 | -0.02 | 78104.53 | 22.55 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 5.65 | 0.91 | -0.01 | 241989.21 | 3.17 | skipped_fast |
| QAITUSDT | IDLE | 2.25 | 4.16 | 2.33 | -0.01 | 2396.75 | 43.59 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.08 | 0.01 | 153304.18 | 11.55 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.93 | -0.03 | 163634.1 | 47.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.42 | 0.0 | 188104.22 | 4.66 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.27 | -0.03 | 47940.51 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.12 | 0.02 | 57782.62 | 8.12 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 21.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
