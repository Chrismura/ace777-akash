# Hulk DIGEST — 2026-09-17T18:17:16Z

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
| XRPUSDT | IDLE | 1.26 | 2.29 | 1.52 | 0.02 | 50064315.79 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 2.02 | 0.8 | 0.02 | 373467717.74 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.38 | 0.44 | 0.01 | 498640781.84 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.3 | 6.58 | 0.45 | 0.09 | 619079.2 | 5.25 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 3.22 | 2.85 | 0.09 | 633217.23 | 10.97 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 10.8 | 6.98 | -0.09 | 190003.53 | 41.77 | skipped_fast |
| RIZEUSDT | IDLE | 2.77 | 19.9 | 3.59 | -0.07 | 46051.27 | 67.97 | skipped_fast |
| WUSDT | IDLE | 2.04 | 6.09 | 0.75 | 0.1 | 251220.4 | 14.38 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 7.14 | 5.22 | 0.03 | 141324.86 | 15.8 | skipped_fast |
| ZBCNUSDT | IDLE | 2.31 | 4.32 | 2.04 | 0.02 | 189728.96 | 22.7 | skipped_fast |
| HBARUSDT | IDLE | 1.84 | 3.5 | 1.17 | 0.04 | 549888.52 | 1.32 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.79 | 2.05 | 0.01 | 64475.13 | 0.77 | skipped_fast |
| RWAINCUSDT | IDLE | 1.9 | 3.46 | 2.25 | 0.01 | 21976.63 | 29.42 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 3.14 | 0.57 | 0.03 | 61494.11 | 13.29 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 2.21 | 1.1 | 0.02 | 71261.99 | 7.94 | skipped_fast |
| TELUSDT | IDLE | 1.87 | 3.41 | 2.22 | 0.02 | 88172.52 | 41.29 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.74 | 0.78 | 0.02 | 37201.05 | 4.89 | skipped_fast |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.03 | 192.45 | 21.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.55 | 1.02 | 0.53 | 0.01 | 42004.9 | 4.19 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.13 | 0.15 | 0.0 | 58335.29 | 29.85 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
