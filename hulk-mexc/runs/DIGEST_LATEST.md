# Hulk DIGEST — 2026-09-20T08:01:15Z

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
| XRPUSDT | IDLE | 0.66 | 1.27 | 0.39 | -0.02 | 54259352.2 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.03 | 0.58 | -0.02 | 260566738.11 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.6 | 0.39 | -0.01 | 503678669.76 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.53 | 4.54 | 3.46 | 0.01 | 513232.58 | 6.37 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 1.93 | 1.62 | -0.02 | 693524.75 | 1.72 | skipped_fast |
| HBARUSDT | IDLE | 1.92 | 3.67 | 1.16 | 0.04 | 768381.14 | 1.23 | skipped_fast |
| REDUSDT | IDLE | 2.67 | 5.23 | 0.77 | 0.04 | 89523.83 | 0.65 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 2.88 | 2.65 | -0.05 | 350295.78 | 6.74 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 7.45 | 3.38 | -0.07 | 34920.76 | 50.58 | skipped_fast |
| ZBCNUSDT | IDLE | 0.92 | 3.32 | 1.15 | 0.05 | 224503.65 | 16.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 3.11 | 1.91 | -0.08 | 103959.35 | 16.78 | skipped_fast |
| EDELUSDT | IDLE | 1.2 | 3.83 | 1.06 | -0.09 | 80842.42 | 30.55 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.78 | 1.72 | 0.0 | 89194.49 | 11.13 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 2.16 | 0.37 | -0.01 | 74804.65 | 14.0 | skipped_fast |
| RWAINCUSDT | IDLE | 0.83 | 1.85 | 1.35 | -0.04 | 10049.32 | 23.78 | skipped_fast |
| QNTUSDT | IDLE | 1.27 | 2.22 | 2.1 | 0.0 | 57052.54 | 9.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.34 | 2.37 | 2.07 | -0.01 | 8031.79 | 21.89 | skipped_fast |
| TELUSDT | IDLE | 0.79 | 1.65 | 1.02 | -0.06 | 103813.95 | 54.83 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.12 | 0.66 | -0.01 | 52412.15 | 29.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.75 | 0.56 | -0.01 | 33118.37 | 19.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
