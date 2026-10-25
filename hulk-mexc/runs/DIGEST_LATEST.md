# Hulk DIGEST — 2026-10-25T12:02:43Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.72 | 1.36 | 0.47 | -0.01 | 129799196.34 | 0.47 | skipped_fast |
| XRPUSDT | IDLE | 0.65 | 1.23 | 0.43 | 0.01 | 22570609.95 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.76 | 0.19 | -0.0 | 202609544.09 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.04 | 3.71 | 2.49 | -0.04 | 805084.8 | 16.7 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.08 | 520241.97 | 23.69 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 3.1 | 0.45 | 0.02 | 512342.4 | 4.21 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 10.5 | 7.14 | -0.02 | 17169.64 | 21.15 | skipped_fast |
| REDUSDT | IDLE | 2.43 | 4.25 | 4.08 | -0.04 | 68499.59 | 9.85 | skipped_fast |
| QNTUSDT | IDLE | 2.13 | 4.04 | 1.53 | 0.02 | 406527.54 | 0.55 | skipped_fast |
| CHIPUSDT | IDLE | 1.39 | 4.41 | 0.2 | 0.06 | 92782.03 | 17.71 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.74 | 0.11 | -0.01 | 191797.37 | 7.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.48 | 2.78 | 1.14 | -0.02 | 57553.92 | 16.4 | skipped_fast |
| ZBCNUSDT | IDLE | 0.74 | 1.73 | 0.73 | 0.01 | 225457.77 | 17.12 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.55 | 0.93 | -0.04 | 65202.88 | 8.95 | skipped_fast |
| KITEUSDT | IDLE | 0.96 | 1.83 | 0.66 | -0.05 | 59117.51 | 11.66 | skipped_fast |
| LAUSDT | IDLE | 1.46 | 6.45 | 4.55 | -0.09 | 77059.55 | 21.15 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.79 | 1.11 | 0.0 | 196516.53 | 14.31 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.14 | 0.8 | -0.03 | 40645.54 | 64.89 | skipped_fast |
| WAXLUSDT | IDLE | 1.32 | 2.56 | 0.52 | -0.04 | 52861.9 | 35.22 | skipped_fast |
| IOTAUSDT | IDLE | 1.27 | 2.35 | 1.22 | -0.02 | 65215.83 | 53.48 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.19 | 1.02 | -0.0 | 51978.1 | 15.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.72 | -0.01 | 38096.35 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
