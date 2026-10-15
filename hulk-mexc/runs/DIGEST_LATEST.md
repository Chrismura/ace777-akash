# Hulk DIGEST — 2026-10-15T06:35:07Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.0 | 9.59 | 1.27 | 0.1 | 2645080.35 | 3.42 | skipped_fast |
| WUSDT | IDLE | 2.41 | 8.91 | 4.27 | -0.07 | 2631021.64 | 16.63 | skipped_fast |
| ETHUSDT | IDLE | 2.24 | 4.59 | 2.63 | -0.06 | 328520631.77 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.04 | 3.8 | 1.89 | -0.04 | 60800293.52 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 1.09 | 2.01 | 1.11 | -0.03 | 541169041.75 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.46 | 7.37 | 5.23 | -0.09 | 1181146.52 | 1.03 | skipped_fast |
| CCUSDT | IDLE | 2.2 | 7.02 | 6.52 | -0.12 | 465491.88 | 5.56 | skipped_fast |
| HBARUSDT | IDLE | 2.44 | 5.21 | 3.47 | -0.06 | 636799.81 | 3.68 | skipped_fast |
| CHIPUSDT | IDLE | 2.01 | 13.34 | 11.44 | -0.2 | 119321.07 | 13.37 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 8.8 | 6.53 | -0.11 | 85250.0 | 8.13 | skipped_fast |
| EDELUSDT | IDLE | 2.46 | 5.46 | 4.43 | -0.06 | 198033.73 | 15.78 | skipped_fast |
| RIZEUSDT | IDLE | 2.39 | 16.47 | 7.08 | -0.03 | 63494.1 | 45.94 | skipped_fast |
| REDUSDT | IDLE | 2.18 | 4.29 | 0.48 | 0.02 | 66513.63 | 8.17 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 6.38 | 5.16 | -0.12 | 82146.22 | 11.73 | skipped_fast |
| ZBCNUSDT | IDLE | 1.2 | 3.17 | 1.4 | -0.06 | 219040.86 | 18.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.56 | 3.3 | 2.3 | 0.0 | 26440.14 | 30.66 | skipped_fast |
| FLUIDUSDT | IDLE | 2.12 | 6.25 | 4.9 | -0.05 | 22890.42 | 31.87 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.3 | 2.11 | -0.04 | 99507.34 | 46.57 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.62 | 1.03 | -0.04 | 54759.05 | 24.14 | skipped_fast |
| MNSRYUSDT | IDLE | 0.9 | 1.58 | 1.41 | -0.02 | 32009.06 | 39.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
