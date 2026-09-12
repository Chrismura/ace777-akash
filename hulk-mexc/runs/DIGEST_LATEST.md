# Hulk DIGEST — 2026-09-12T03:18:04Z

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
| XRPUSDT | IDLE | 0.65 | 1.44 | 0.04 | 0.02 | 53096290.42 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.32 | 0.7 | 0.29 | 0.03 | 643280592.03 | 0.4 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.52 | 0.09 | 0.01 | 571341092.42 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 3.79 | 1.26 | 0.01 | 426003.42 | 7.07 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 3.43 | 0.12 | 0.02 | 409639.44 | 3.86 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 5.56 | 5.21 | -0.01 | 15073.58 | 5.61 | skipped_fast |
| EDELUSDT | IDLE | 1.74 | 4.8 | 2.77 | 0.04 | 165659.82 | 17.76 | skipped_fast |
| WUSDT | IDLE | 1.61 | 3.4 | 0.04 | 0.03 | 198327.34 | 8.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.84 | 5.4 | 1.83 | 0.01 | 121234.46 | 18.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 2.64 | 1.43 | -0.0 | 193156.51 | 14.01 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 4.58 | 0.58 | 0.09 | 64235.91 | 17.56 | skipped_fast |
| BIOUSDT | IDLE | 1.57 | 3.11 | 0.16 | 0.03 | 81929.42 | 7.84 | skipped_fast |
| KITEUSDT | IDLE | 0.73 | 1.34 | 0.83 | -0.01 | 59185.29 | 12.02 | skipped_fast |
| TELUSDT | IDLE | 1.5 | 3.13 | 2.8 | -0.03 | 101528.48 | 11.77 | skipped_fast |
| HBARUSDT | IDLE | 0.56 | 1.08 | 0.21 | -0.01 | 258802.15 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 2.21 | 0.11 | -0.0 | 46079.48 | 4.68 | skipped_fast |
| RIZEUSDT | IDLE | 0.05 | 3.37 | 0.89 | 0.67 | 206422.72 | 148.94 | skipped_fast |
| FLUIDUSDT | IDLE | 1.14 | 2.27 | 0.0 | 0.02 | 1933.19 | 22.0 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.75 | 0.07 | 0.03 | 53498.38 | 7.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.7 | 0.4 | 0.01 | 34060.39 | 9.73 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
