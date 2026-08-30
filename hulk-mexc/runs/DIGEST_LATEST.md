# Hulk DIGEST — 2026-08-30T11:13:44Z

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
| XRPUSDT | IDLE | 0.83 | 1.53 | 0.93 | 0.0 | 16715153.26 | 2.88 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 3.98 | 2.6 | -0.04 | 605565.11 | 2.52 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.88 | 0.66 | 0.04 | 210671.72 | 21.21 | skipped_fast |
| PYTHUSDT | IDLE | 1.27 | 2.42 | 0.82 | 0.01 | 330617.72 | 2.11 | skipped_fast |
| ZBCNUSDT | IDLE | 1.88 | 3.58 | 1.25 | 0.0 | 156888.37 | 15.91 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.41 | 1.17 | 0.05 | 296498.08 | 8.45 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.59 | 1.55 | -0.01 | 67877.65 | 3.67 | skipped_fast |
| KITEUSDT | IDLE | 0.94 | 2.13 | 1.6 | -0.0 | 70489.64 | 10.92 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 1.6 | 0.77 | -0.04 | 64897.22 | 14.62 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 4.47 | 2.27 | -0.05 | 47019.01 | 61.55 | skipped_fast |
| RWAINCUSDT | IDLE | 0.82 | 1.59 | 0.39 | -0.01 | 1437.3 | 5.62 | skipped_fast |
| EDELUSDT | IDLE | 0.24 | 4.36 | 0.92 | 0.16 | 120583.19 | 33.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.3 | 0.34 | 0.03 | 3393.64 | 21.71 | skipped_fast |
| HBARUSDT | IDLE | 0.28 | 0.53 | 0.19 | 0.0 | 141293.48 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 0.62 | 1.13 | 0.71 | -0.03 | 73199.9 | 17.79 | skipped_fast |
| QNTUSDT | IDLE | 0.49 | 0.96 | 0.1 | 0.01 | 36787.76 | 3.24 | skipped_fast |
| RWAUSDT | IDLE | 0.26 | 0.49 | 0.24 | 0.01 | 52235.02 | 8.17 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
