# Hulk DIGEST — 2026-08-20T14:25:50Z

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
| XRPUSDT | IDLE | 1.68 | 8.64 | 0.54 | 0.22 | 71529242.04 | 2.42 | skipped_fast |
| CHIPUSDT | IDLE | 3.93 | 12.13 | 4.31 | 0.07 | 293479.42 | 3.36 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 4.1 | 3.18 | 0.13 | 882039.22 | 2.3 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 10.35 | 8.81 | 0.09 | 269544.45 | 14.3 | skipped_fast |
| BIOUSDT | IDLE | 2.06 | 11.94 | 9.95 | 0.16 | 279902.34 | 6.59 | skipped_fast |
| REDUSDT | IDLE | 1.31 | 10.55 | 9.15 | 0.19 | 200118.56 | 8.56 | skipped_fast |
| WUSDT | IDLE | 1.56 | 3.06 | 0.74 | 0.09 | 344777.08 | 13.52 | skipped_fast |
| CCUSDT | IDLE | 0.64 | 2.14 | 1.93 | 0.14 | 499902.1 | 4.85 | skipped_fast |
| QAITUSDT | IDLE | 2.57 | 6.03 | 4.38 | -0.0 | 8322.53 | 50.4 | skipped_fast |
| HBARUSDT | IDLE | 1.32 | 2.67 | 0.74 | 0.08 | 470863.9 | 1.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.16 | 8.15 | 1.85 | 0.13 | 64858.56 | 45.14 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 7.23 | 0.34 | 0.23 | 212481.15 | 11.47 | skipped_fast |
| RWAINCUSDT | IDLE | 0.97 | 1.88 | 0.45 | 0.01 | 7715.67 | 11.16 | skipped_fast |
| EDELUSDT | IDLE | 0.41 | 2.94 | 1.32 | 0.17 | 104980.44 | 22.3 | skipped_fast |
| KITEUSDT | IDLE | 0.67 | 1.21 | 0.83 | 0.04 | 59659.11 | 11.4 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 3.22 | 0.43 | 0.1 | 62641.81 | 9.64 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.21 | 0.6 | 0.02 | 52813.56 | 17.26 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.24 | 0.98 | 0.1 | 3409.47 | 19.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
