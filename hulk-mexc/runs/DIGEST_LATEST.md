# Hulk DIGEST — 2026-09-21T17:04:37Z

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
| XRPUSDT | IDLE | 1.3 | 2.54 | 1.31 | 0.06 | 82170160.21 | 2.01 | skipped_fast |
| ETHUSDT | IDLE | 1.06 | 2.05 | 0.47 | 0.04 | 650558843.77 | 1.56 | skipped_fast |
| BTCUSDT | IDLE | 0.95 | 1.84 | 0.43 | 0.06 | 931758049.71 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 4.13 | 1.82 | 0.04 | 1174797.98 | 1.09 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 4.56 | 2.77 | 0.06 | 687391.04 | 12.37 | skipped_fast |
| WUSDT | IDLE | 1.96 | 4.3 | 4.08 | 0.05 | 644079.38 | 4.31 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 3.47 | 1.56 | 0.07 | 574299.42 | 9.48 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 5.81 | 3.21 | 0.07 | 229013.05 | 21.91 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 15.36 | 3.94 | -0.12 | 56072.13 | 93.71 | skipped_fast |
| CHIPUSDT | IDLE | 1.3 | 6.16 | 5.43 | 0.09 | 143679.79 | 19.46 | skipped_fast |
| BIOUSDT | IDLE | 1.55 | 2.83 | 1.77 | 0.04 | 101908.34 | 10.39 | skipped_fast |
| EDELUSDT | IDLE | 0.62 | 6.22 | 0.68 | 0.4 | 254400.9 | 42.04 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 2.29 | 0.98 | 0.01 | 102986.72 | 16.3 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.12 | 1.64 | 0.04 | 74398.55 | 13.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 3.23 | 0.97 | 0.02 | 8070.54 | 5.72 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 4.49 | 0.67 | 0.07 | 100739.77 | 42.59 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 1.86 | 1.68 | 0.02 | 102415.06 | 7.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.2 | 2.6 | 0.3 | 0.1 | 11811.41 | 21.45 | skipped_fast |
| MNSRYUSDT | IDLE | 0.9 | 1.71 | 0.54 | 0.04 | 42874.86 | 18.01 | skipped_fast |
| RWAUSDT | IDLE | 0.74 | 1.39 | 0.65 | 0.02 | 56206.8 | 7.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
