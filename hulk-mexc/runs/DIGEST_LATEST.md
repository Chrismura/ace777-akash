# Hulk DIGEST — 2026-09-01T18:27:33Z

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
| XRPUSDT | IDLE | 1.36 | 2.38 | 2.33 | -0.02 | 31455522.45 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 1.13 | 2.01 | 1.72 | -0.02 | 300825084.45 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.99 | 1.72 | 1.68 | -0.02 | 520523091.77 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.89 | 11.76 | 5.55 | 0.09 | 512641.21 | 4.75 | skipped_fast |
| PYTHUSDT | IDLE | 1.83 | 3.29 | 2.5 | 0.03 | 652186.52 | 2.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.54 | 6.34 | 4.87 | 0.01 | 211691.22 | 22.69 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 4.19 | 2.95 | -0.03 | 424402.64 | 9.6 | skipped_fast |
| WUSDT | IDLE | 2.43 | 4.64 | 1.42 | 0.06 | 301149.76 | 13.47 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 7.18 | 5.23 | -0.08 | 44858.77 | 64.47 | skipped_fast |
| REDUSDT | IDLE | 2.32 | 5.3 | 0.66 | 0.07 | 75284.47 | 20.32 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 3.97 | 2.18 | 0.03 | 69409.78 | 13.17 | skipped_fast |
| BIOUSDT | IDLE | 1.61 | 2.86 | 2.4 | -0.03 | 68992.65 | 3.9 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 5.12 | 3.76 | -0.06 | 171989.17 | 26.63 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.86 | 2.31 | -0.03 | 6350.44 | 23.65 | skipped_fast |
| HBARUSDT | IDLE | 1.22 | 2.13 | 2.08 | 0.01 | 238562.8 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 2.92 | 1.18 | 0.04 | 46524.92 | 1.57 | skipped_fast |
| TELUSDT | IDLE | 1.68 | 3.0 | 2.39 | -0.01 | 97141.92 | 47.7 | skipped_fast |
| FLUIDUSDT | IDLE | 1.5 | 2.61 | 2.55 | -0.01 | 155.07 | 22.46 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.23 | 0.91 | -0.02 | 59871.69 | 15.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.63 | 1.13 | 0.82 | -0.01 | 32295.15 | 42.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
