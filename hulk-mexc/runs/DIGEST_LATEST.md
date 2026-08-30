# Hulk DIGEST — 2026-08-30T19:13:37Z

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
| XRPUSDT | IDLE | 1.41 | 2.71 | 0.79 | 0.02 | 22260244.67 | 2.81 | skipped_fast |
| ETHUSDT | IDLE | 1.34 | 2.54 | 0.9 | 0.02 | 218554308.54 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.97 | 0.46 | 0.01 | 281419258.05 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 7.52 | 6.69 | -0.04 | 486716.15 | 2.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.98 | 6.39 | 3.52 | -0.04 | 200376.27 | 10.25 | skipped_fast |
| PYTHUSDT | IDLE | 1.84 | 3.62 | 0.42 | 0.04 | 409527.93 | 1.99 | skipped_fast |
| KITEUSDT | IDLE | 1.96 | 3.6 | 2.07 | -0.01 | 60996.93 | 8.67 | skipped_fast |
| WUSDT | IDLE | 1.13 | 2.08 | 1.14 | 0.03 | 224669.06 | 14.74 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 5.3 | 2.71 | -0.04 | 36494.85 | 34.15 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 4.54 | 0.0 | 0.08 | 74366.48 | 24.6 | skipped_fast |
| CCUSDT | IDLE | 0.54 | 0.99 | 0.54 | -0.0 | 246016.3 | 8.46 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 2.18 | 1.66 | 0.02 | 62048.72 | 14.57 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.94 | 0.4 | 0.01 | 81720.57 | 10.86 | skipped_fast |
| TELUSDT | IDLE | 2.22 | 4.41 | 0.17 | 0.0 | 87010.96 | 11.44 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.6 | 0.29 | 0.01 | 162719.25 | 1.32 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 2.24 | 0.0 | 0.01 | 1821.2 | 120.81 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.14 | 0.77 | 0.01 | 38435.31 | 4.86 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.22 | 0.08 | 0.02 | 53091.93 | 16.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 21.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.67 | 0.41 | 0.01 | 32115.41 | 9.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
