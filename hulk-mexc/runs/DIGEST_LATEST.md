# Hulk DIGEST — 2026-09-11T17:20:29Z

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
| XRPUSDT | IDLE | 4.28 | 8.82 | 4.3 | 0.01 | 52822046.71 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 4.17 | 9.44 | 3.24 | 0.05 | 621586802.26 | 0.04 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 112.99 | 21.7 | 0.81 | 182400.22 | 102.04 | skipped_fast |
| BTCUSDT | IDLE | 2.65 | 4.93 | 2.5 | 0.01 | 549805272.97 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 4.16 | 8.17 | 3.16 | 0.02 | 396448.93 | 1.91 | skipped_fast |
| CCUSDT | IDLE | 3.4 | 6.23 | 3.81 | -0.01 | 480207.57 | 8.15 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.1 | 8.47 | 1.48 | 0.03 | 191582.4 | 6.07 | skipped_fast |
| RWAINCUSDT | IDLE | 4.17 | 8.51 | 4.21 | 0.03 | 10557.85 | 5.42 | skipped_fast |
| EDELUSDT | IDLE | 3.85 | 7.04 | 4.36 | -0.02 | 155431.64 | 37.24 | skipped_fast |
| CHIPUSDT | IDLE | 3.27 | 10.12 | 3.84 | 0.03 | 148942.87 | 18.68 | skipped_fast |
| REDUSDT | IDLE | 3.81 | 7.49 | 0.89 | 0.04 | 61342.38 | 12.67 | skipped_fast |
| BIOUSDT | IDLE | 3.37 | 6.44 | 2.01 | 0.0 | 80138.42 | 7.87 | skipped_fast |
| TELUSDT | IDLE | 4.27 | 8.79 | 4.04 | 0.0 | 99630.34 | 22.46 | skipped_fast |
| ZBCNUSDT | IDLE | 2.43 | 4.45 | 2.67 | 0.0 | 189197.63 | 4.87 | skipped_fast |
| HBARUSDT | IDLE | 2.5 | 4.64 | 2.4 | -0.0 | 233054.89 | 1.33 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 3.28 | 2.42 | -0.01 | 59889.21 | 12.92 | skipped_fast |
| FLUIDUSDT | IDLE | 2.47 | 4.94 | 0.0 | 0.03 | 1301.56 | 22.28 | skipped_fast |
| QNTUSDT | IDLE | 1.83 | 3.37 | 1.97 | -0.02 | 40287.99 | 7.73 | skipped_fast |
| RWAUSDT | IDLE | 1.64 | 3.2 | 0.52 | 0.02 | 52036.18 | 22.3 | skipped_fast |
| MNSRYUSDT | IDLE | 1.65 | 3.1 | 1.34 | 0.01 | 37205.46 | 40.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
