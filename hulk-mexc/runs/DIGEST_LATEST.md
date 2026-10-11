# Hulk DIGEST — 2026-10-11T08:38:19Z

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
| XRPUSDT | IDLE | 0.51 | 0.96 | 0.46 | -0.01 | 10078235.41 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.51 | 0.4 | 0.0 | 168776632.2 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.51 | 0.16 | 0.0 | 135661486.23 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.53 | 4.74 | 1.79 | 0.04 | 1236044.91 | 7.44 | skipped_fast |
| PYTHUSDT | IDLE | 3.0 | 5.54 | 3.07 | -0.02 | 723557.4 | 2.57 | skipped_fast |
| QNTUSDT | IDLE | 0.84 | 1.64 | 0.63 | -0.05 | 1275821.27 | 1.68 | skipped_fast |
| EDELUSDT | IDLE | 2.47 | 4.54 | 2.61 | -0.04 | 364926.83 | 12.92 | skipped_fast |
| CHIPUSDT | IDLE | 1.27 | 11.69 | 6.07 | 0.22 | 315860.13 | 17.04 | skipped_fast |
| BIOUSDT | IDLE | 2.55 | 5.01 | 0.57 | 0.03 | 78254.75 | 6.69 | skipped_fast |
| CCUSDT | IDLE | 1.55 | 3.11 | 0.0 | -0.0 | 228486.56 | 6.6 | skipped_fast |
| RIZEUSDT | IDLE | 2.17 | 4.09 | 2.55 | -0.04 | 32528.7 | 33.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.1 | 1.97 | 1.58 | -0.01 | 149519.81 | 16.41 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 2.61 | 0.46 | 0.0 | 57742.11 | 14.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.4 | 2.46 | 2.21 | -0.02 | 19401.81 | 45.06 | skipped_fast |
| KITEUSDT | IDLE | 0.92 | 1.74 | 0.7 | 0.01 | 74732.69 | 12.67 | skipped_fast |
| FLUIDUSDT | IDLE | 2.29 | 4.57 | 0.0 | 0.02 | 9481.28 | 21.34 | skipped_fast |
| TELUSDT | IDLE | 1.67 | 3.04 | 2.06 | -0.05 | 136087.47 | 28.45 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.48 | 0.42 | -0.01 | 277505.3 | 3.26 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.71 | -0.01 | 53206.36 | 15.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.59 | 1.03 | 1.01 | -0.02 | 34249.01 | 28.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
