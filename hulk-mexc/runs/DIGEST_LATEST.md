# Hulk DIGEST — 2026-08-30T12:12:56Z

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
| XRPUSDT | IDLE | 0.7 | 1.38 | 0.19 | 0.01 | 17130557.35 | 2.14 | skipped_fast |
| CHIPUSDT | IDLE | 3.35 | 6.51 | 1.32 | 0.02 | 598899.66 | 19.47 | skipped_fast |
| WUSDT | IDLE | 2.02 | 3.88 | 1.13 | 0.04 | 209413.75 | 13.87 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 2.76 | 0.04 | 0.02 | 335022.01 | 4.17 | skipped_fast |
| ZBCNUSDT | IDLE | 1.9 | 3.58 | 1.48 | -0.0 | 156190.82 | 0.51 | skipped_fast |
| CCUSDT | IDLE | 0.67 | 1.2 | 0.95 | 0.04 | 300726.9 | 8.45 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.56 | 0.76 | 0.0 | 68250.13 | 3.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.08 | 4.33 | 1.98 | -0.05 | 46905.27 | 61.55 | skipped_fast |
| KITEUSDT | IDLE | 0.71 | 1.59 | 1.27 | 0.0 | 69661.47 | 11.73 | skipped_fast |
| EDELUSDT | IDLE | 0.21 | 3.63 | 1.84 | 0.14 | 120713.43 | 16.99 | skipped_fast |
| REDUSDT | IDLE | 0.65 | 1.28 | 0.16 | -0.03 | 62961.03 | 13.67 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 2.35 | 1.7 | -0.04 | 77570.56 | 11.95 | skipped_fast |
| RWAINCUSDT | IDLE | 0.76 | 1.48 | 0.28 | -0.01 | 1538.7 | 101.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.3 | 0.34 | 0.03 | 3257.71 | 21.55 | skipped_fast |
| HBARUSDT | IDLE | 0.4 | 0.79 | 0.0 | 0.01 | 140671.75 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.62 | 1.23 | 0.05 | 0.02 | 38380.86 | 6.46 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.57 | 0.08 | 0.01 | 52653.03 | 16.3 | skipped_fast |
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
