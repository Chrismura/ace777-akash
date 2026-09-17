# Hulk DIGEST — 2026-09-17T03:03:04Z

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
| XRPUSDT | IDLE | 1.24 | 2.36 | 0.76 | 0.01 | 56948176.59 | 2.31 | skipped_fast |
| ETHUSDT | IDLE | 1.22 | 2.35 | 0.57 | 0.01 | 380736875.05 | 0.37 | skipped_fast |
| BTCUSDT | IDLE | 0.78 | 1.49 | 0.48 | 0.01 | 518053168.51 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.18 | 7.73 | 5.71 | 0.06 | 561401.44 | 8.25 | skipped_fast |
| PYTHUSDT | IDLE | 2.5 | 4.91 | 0.66 | 0.01 | 427493.69 | 3.71 | skipped_fast |
| WUSDT | IDLE | 2.78 | 5.27 | 2.16 | 0.01 | 225905.75 | 12.02 | skipped_fast |
| CHIPUSDT | IDLE | 3.14 | 7.1 | 3.38 | -0.03 | 81847.41 | 19.27 | skipped_fast |
| RWAINCUSDT | IDLE | 3.15 | 5.77 | 3.54 | -0.03 | 21137.2 | 5.83 | skipped_fast |
| REDUSDT | IDLE | 2.16 | 4.49 | 1.17 | 0.01 | 63968.47 | 16.7 | skipped_fast |
| BIOUSDT | IDLE | 1.93 | 3.74 | 0.75 | 0.02 | 78240.11 | 11.86 | skipped_fast |
| EDELUSDT | IDLE | 0.89 | 3.78 | 3.16 | 0.03 | 266985.08 | 19.18 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.54 | 0.27 | 0.03 | 162754.4 | 16.54 | skipped_fast |
| RIZEUSDT | IDLE | 0.82 | 10.2 | 7.8 | 0.18 | 63455.1 | 44.09 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 4.0 | 3.0 | 0.05 | 66622.75 | 13.34 | skipped_fast |
| HBARUSDT | IDLE | 1.17 | 2.27 | 0.44 | -0.01 | 303005.5 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 1.88 | 1.3 | -0.02 | 115421.28 | 41.61 | skipped_fast |
| QNTUSDT | IDLE | 0.73 | 1.32 | 0.98 | -0.0 | 37556.34 | 6.59 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 0.98 | 0.75 | 0.01 | 55361.4 | 15.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.97 | 0.21 | 0.0 | 33754.09 | 26.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1573.23 | 22.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
