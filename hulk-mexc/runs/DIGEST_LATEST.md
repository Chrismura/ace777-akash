# Hulk DIGEST — 2026-08-21T20:11:23Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.28 | 0.08 | 5475999.53 | 4.23 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.42 | 0.11 | 129106128.44 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 13.23 | 0.17 | 154079.06 | 16.34 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 10.86 | 6.55 | 0.11 | 477979.23 | 33.86 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.8 | 0.07 | 632493.13 | 7.47 | skipped_fast |
| HBARUSDT | IDLE | 1.76 | 3.23 | 2.46 | 0.05 | 795729.7 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.43 | 0.09 | 512991.6 | 6.18 | skipped_fast |
| WUSDT | IDLE | 2.13 | 3.92 | 2.3 | 0.06 | 367011.44 | 12.77 | skipped_fast |
| BIOUSDT | IDLE | 2.58 | 5.33 | 3.56 | 0.01 | 189888.06 | 3.18 | skipped_fast |
| EDELUSDT | IDLE | 2.51 | 4.41 | 4.12 | -0.05 | 80185.16 | 11.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.54 | 0.01 | 56230.16 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.04 | 11178.26 | 42.87 | skipped_fast |
| KITEUSDT | IDLE | 1.26 | 4.0 | 2.77 | 0.1 | 61296.03 | 14.01 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.02 | 2816.78 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 3.39 | 2.17 | 0.01 | 183538.98 | 37.85 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.68 | 0.04 | 59886.35 | 6.25 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.16 | 0.82 | 0.04 | 54334.44 | 8.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
