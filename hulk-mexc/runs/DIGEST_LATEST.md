# Hulk DIGEST — 2026-10-17T11:58:28Z

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
| WUSDT | IDLE | 2.71 | 5.53 | 4.48 | -0.0 | 1316557.97 | 15.81 | skipped_fast |
| XRPUSDT | IDLE | 0.37 | 0.67 | 0.43 | -0.03 | 21062604.38 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.31 | 0.57 | 0.3 | -0.02 | 131395680.66 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.25 | 0.21 | -0.01 | 262185220.09 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.77 | 1.83 | 0.62 | -0.06 | 1357942.9 | 9.44 | skipped_fast |
| ZBCNUSDT | IDLE | 2.45 | 5.48 | 2.09 | -0.05 | 224615.24 | 35.46 | skipped_fast |
| KITEUSDT | IDLE | 2.44 | 4.28 | 4.01 | -0.02 | 56112.55 | 19.77 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.57 | 1.03 | -0.0 | 299221.98 | 9.65 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 2.56 | 2.46 | -0.05 | 156053.65 | 17.29 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.57 | 0.63 | -0.03 | 576454.16 | 1.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 3.18 | 2.91 | -0.08 | 100217.31 | 15.43 | skipped_fast |
| RWAINCUSDT | IDLE | 1.19 | 4.84 | 1.26 | -0.06 | 22924.2 | 10.63 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.54 | 1.16 | -0.05 | 66562.09 | 4.03 | skipped_fast |
| REDUSDT | IDLE | 0.86 | 1.75 | 1.53 | -0.07 | 75054.77 | 17.0 | skipped_fast |
| RIZEUSDT | IDLE | 0.84 | 1.67 | 0.27 | 0.01 | 44640.26 | 33.73 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.14 | 1.03 | -0.04 | 197730.06 | 7.21 | skipped_fast |
| RWAUSDT | IDLE | 1.21 | 2.35 | 0.4 | -0.01 | 52497.55 | 23.89 | skipped_fast |
| FLUIDUSDT | IDLE | 1.34 | 2.7 | 0.0 | 0.05 | 3788.43 | 21.72 | skipped_fast |
| TELUSDT | IDLE | 0.85 | 1.48 | 1.46 | -0.06 | 86524.05 | 17.78 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.23 | 0.07 | -0.0 | 27836.59 | 7.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
