# Hulk DIGEST — 2026-09-06T06:31:12Z

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
| ETHUSDT | IDLE | 0.74 | 1.38 | 0.69 | 0.02 | 213392081.44 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.75 | 1.37 | 0.9 | 0.01 | 24785073.19 | 2.82 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.39 | 0.36 | 0.0 | 383293539.62 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.93 | 5.29 | 3.76 | 0.03 | 431821.8 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 2.64 | 5.64 | 4.45 | 0.01 | 395011.44 | 15.54 | skipped_fast |
| RWAINCUSDT | IDLE | 2.97 | 5.37 | 3.85 | -0.0 | 9304.2 | 37.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.73 | 11.06 | 5.45 | 0.08 | 115960.89 | 52.05 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.12 | 1.26 | 0.02 | 302914.06 | 5.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 2.9 | 0.42 | -0.0 | 220777.55 | 29.28 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.52 | 1.81 | 0.02 | 172850.36 | 10.91 | skipped_fast |
| EDELUSDT | IDLE | 1.71 | 3.33 | 0.65 | -0.32 | 97474.98 | 27.89 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 3.06 | 1.61 | -0.02 | 64567.91 | 10.1 | skipped_fast |
| HBARUSDT | IDLE | 1.18 | 2.17 | 1.28 | 0.02 | 449102.2 | 1.23 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 2.67 | 1.42 | 0.01 | 57876.83 | 11.81 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.55 | 1.45 | 0.01 | 97316.27 | 3.59 | skipped_fast |
| QNTUSDT | IDLE | 1.62 | 3.09 | 0.94 | 0.04 | 37662.77 | 1.5 | skipped_fast |
| MNSRYUSDT | IDLE | 1.38 | 2.64 | 0.76 | 0.02 | 40802.24 | 8.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.33 | 0.14 | 0.04 | 380.96 | 21.99 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.35 | 1.26 | 0.03 | 53088.59 | 14.2 | skipped_fast |
| TELUSDT | IDLE | 0.8 | 1.59 | 0.06 | 0.01 | 73380.1 | 34.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
