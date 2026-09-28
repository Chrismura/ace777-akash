# Hulk DIGEST — 2026-09-28T19:29:31Z

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
| WUSDT | IDLE | 1.26 | 5.82 | 5.0 | -0.14 | 2496930.31 | 5.2 | skipped_fast |
| QNTUSDT | IDLE | 0.79 | 18.61 | 8.67 | 0.25 | 22227525.69 | 10.11 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 13.26 | 2.74 | 0.34 | 10928161.09 | 0.79 | skipped_fast |
| XRPUSDT | IDLE | 1.74 | 3.23 | 1.66 | -0.02 | 67068745.6 | 2.0 | skipped_fast |
| ETHUSDT | IDLE | 1.38 | 2.55 | 1.37 | -0.0 | 396782457.59 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.13 | 2.14 | 0.8 | -0.01 | 832007785.9 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 5.9 | 4.3 | -0.07 | 1327993.51 | 5.47 | skipped_fast |
| PYTHUSDT | IDLE | 1.54 | 3.93 | 1.91 | -0.07 | 1298354.12 | 3.78 | skipped_fast |
| TELUSDT | IDLE | 3.55 | 27.96 | 2.33 | 0.24 | 248765.55 | 52.84 | skipped_fast |
| RWAINCUSDT | IDLE | 3.5 | 8.99 | 3.32 | 0.04 | 16167.23 | 28.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.17 | 4.82 | 3.91 | -0.08 | 68900.94 | 16.12 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 6.35 | 4.05 | -0.11 | 100959.66 | 3.69 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 2.56 | 1.83 | -0.06 | 238449.65 | 13.53 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 6.47 | 0.09 | 0.02 | 55854.39 | 51.24 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 3.65 | 1.85 | -0.08 | 115317.35 | 3.42 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 3.22 | 2.01 | -0.07 | 59893.4 | 14.39 | skipped_fast |
| EDELUSDT | IDLE | 0.55 | 3.47 | 1.66 | 0.12 | 173279.12 | 24.04 | skipped_fast |
| FLUIDUSDT | IDLE | 1.41 | 3.66 | 0.0 | -0.05 | 3168.68 | 14.96 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.59 | 0.5 | -0.01 | 60043.0 | 14.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.44 | 0.78 | 0.62 | -0.02 | 34589.72 | 33.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
