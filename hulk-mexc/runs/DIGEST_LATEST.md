# Hulk DIGEST — 2026-08-20T15:25:57Z

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
| XRPUSDT | IDLE | 2.09 | 10.2 | 2.28 | 0.18 | 77330579.3 | 2.43 | skipped_fast |
| PYTHUSDT | IDLE | 1.3 | 4.1 | 2.09 | 0.11 | 998938.07 | 2.27 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.69 | 12.72 | 8.64 | 0.05 | 264023.99 | 41.18 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.74 | 11.92 | 0.16 | 0.1 | 280715.08 | 16.13 | skipped_fast |
| REDUSDT | IDLE | 1.74 | 12.24 | 10.65 | 0.14 | 200804.94 | 7.71 | skipped_fast |
| BIOUSDT | IDLE | 1.76 | 9.09 | 7.94 | 0.08 | 259145.15 | 6.61 | skipped_fast |
| CCUSDT | IDLE | 1.01 | 3.09 | 2.97 | 0.11 | 490557.55 | 5.89 | skipped_fast |
| WUSDT | IDLE | 1.57 | 3.06 | 0.47 | 0.06 | 342432.6 | 15.74 | skipped_fast |
| HBARUSDT | IDLE | 1.42 | 2.67 | 1.14 | 0.06 | 455239.93 | 1.37 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.05 | 8.84 | 1.01 | 0.21 | 218552.88 | 33.92 | skipped_fast |
| RIZEUSDT | IDLE | 1.11 | 7.91 | 1.11 | 0.14 | 64397.47 | 44.83 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.14 | 0.68 | 0.03 | 59361.16 | 15.39 | skipped_fast |
| RWAINCUSDT | IDLE | 1.54 | 2.95 | 0.83 | 0.01 | 7440.24 | 55.49 | skipped_fast |
| EDELUSDT | IDLE | 0.45 | 2.94 | 0.11 | 0.17 | 102444.51 | 22.05 | skipped_fast |
| QAITUSDT | IDLE | 1.0 | 2.01 | 0.0 | 0.04 | 7616.06 | 54.26 | skipped_fast |
| QNTUSDT | IDLE | 0.98 | 2.09 | 1.02 | 0.07 | 62893.86 | 4.84 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.68 | 0.01 | 52692.44 | 17.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.69 | 1.24 | 0.98 | 0.06 | 3398.29 | 21.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
