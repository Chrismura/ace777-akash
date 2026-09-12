# Hulk DIGEST — 2026-09-12T12:32:41Z

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
| XRPUSDT | IDLE | 0.44 | 0.85 | 0.23 | 0.04 | 45425999.14 | 1.46 | skipped_fast |
| ETHUSDT | IDLE | 0.36 | 0.7 | 0.14 | 0.04 | 582172396.42 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.09 | 0.16 | 0.09 | 0.01 | 517846330.6 | 0.0 | skipped_fast |
| ZBCNUSDT | IDLE | 3.77 | 9.06 | 4.63 | 0.01 | 237504.62 | 21.58 | skipped_fast |
| RWAINCUSDT | IDLE | 3.44 | 6.94 | 2.55 | 0.04 | 16683.57 | 21.21 | skipped_fast |
| PYTHUSDT | IDLE | 1.66 | 3.19 | 0.93 | 0.05 | 403662.12 | 1.88 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 3.66 | 2.33 | 0.08 | 169569.12 | 26.47 | skipped_fast |
| CCUSDT | IDLE | 0.62 | 1.09 | 1.03 | 0.02 | 317442.65 | 9.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.62 | 4.04 | 0.35 | 0.06 | 85043.74 | 20.51 | skipped_fast |
| WUSDT | IDLE | 0.74 | 1.34 | 0.93 | 0.05 | 185547.39 | 11.25 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 2.09 | 0.19 | 0.05 | 76800.96 | 3.87 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 2.6 | 0.76 | 0.07 | 64236.39 | 20.17 | skipped_fast |
| RIZEUSDT | IDLE | 0.13 | 7.88 | 2.57 | 0.88 | 176546.85 | 46.48 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 1.67 | 0.0 | -0.01 | 61310.93 | 10.29 | skipped_fast |
| HBARUSDT | IDLE | 0.38 | 0.74 | 0.16 | 0.01 | 239142.21 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.05 | 2.96 | 1.64 | -0.02 | 100847.37 | 23.87 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 1.54 | 0.39 | 0.01 | 41969.4 | 9.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.64 | 1.24 | 0.32 | 0.01 | 26218.38 | 36.16 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.74 | 0.29 | 0.03 | 55366.81 | 22.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.05 | 1339.83 | 20.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
