# Hulk DIGEST — 2026-09-25T16:45:00Z

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
| XRPUSDT | IDLE | 2.63 | 4.74 | 3.51 | 0.03 | 118193483.68 | 2.54 | skipped_fast |
| ETHUSDT | IDLE | 1.51 | 2.74 | 1.86 | -0.0 | 373394210.63 | 0.07 | skipped_fast |
| BTCUSDT | IDLE | 1.34 | 2.46 | 1.52 | -0.01 | 744065938.21 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.34 | 6.36 | 1.79 | 0.06 | 1224506.63 | 2.74 | skipped_fast |
| HBARUSDT | IDLE | 2.44 | 4.46 | 2.81 | 0.01 | 957173.49 | 1.06 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 6.13 | 1.69 | 0.1 | 751532.25 | 9.63 | skipped_fast |
| BIOUSDT | IDLE | 3.29 | 9.8 | 3.11 | 0.05 | 116231.33 | 9.1 | skipped_fast |
| ZBCNUSDT | IDLE | 2.96 | 7.26 | 1.11 | 0.06 | 207658.46 | 0.45 | skipped_fast |
| WUSDT | IDLE | 2.07 | 3.97 | 1.17 | 0.02 | 377217.51 | 3.32 | skipped_fast |
| CHIPUSDT | IDLE | 2.01 | 6.19 | 2.65 | 0.07 | 170439.09 | 14.34 | skipped_fast |
| KITEUSDT | IDLE | 2.49 | 4.62 | 2.43 | -0.02 | 74753.21 | 10.76 | skipped_fast |
| QNTUSDT | IDLE | 1.02 | 7.35 | 0.39 | 0.17 | 633840.27 | 10.17 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 17.0 | 14.51 | 0.48 | 132241.33 | 47.79 | skipped_fast |
| REDUSDT | IDLE | 1.9 | 4.89 | 0.0 | 0.09 | 135751.56 | 19.97 | skipped_fast |
| EDELUSDT | IDLE | 0.51 | 5.36 | 0.76 | 0.07 | 220071.3 | 6.66 | skipped_fast |
| TELUSDT | IDLE | 1.84 | 3.3 | 2.49 | 0.01 | 116902.33 | 30.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.84 | 3.47 | 1.38 | 0.02 | 3204.08 | 21.59 | skipped_fast |
| RWAINCUSDT | IDLE | 0.49 | 1.79 | 0.55 | -0.05 | 19530.33 | 30.55 | skipped_fast |
| MNSRYUSDT | IDLE | 0.94 | 1.76 | 0.82 | 0.02 | 41992.37 | 19.15 | skipped_fast |
| RWAUSDT | IDLE | 0.75 | 1.32 | 1.23 | -0.01 | 57807.8 | 7.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
