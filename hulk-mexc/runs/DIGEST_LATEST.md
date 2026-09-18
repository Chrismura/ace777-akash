# Hulk DIGEST — 2026-09-18T08:27:57Z

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
| XRPUSDT | IDLE | 1.18 | 2.34 | 0.2 | 0.03 | 39998870.84 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 0.93 | 1.82 | 0.25 | 0.02 | 334974573.01 | 0.16 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.4 | 0.04 | 0.02 | 531351075.81 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 46.36 | 22.15 | 0.07 | 54871.98 | 106.25 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 5.8 | 0.6 | 0.11 | 662720.93 | 8.94 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 5.5 | 1.43 | 0.11 | 604835.27 | 5.0 | skipped_fast |
| WUSDT | IDLE | 1.26 | 3.66 | 0.84 | 0.11 | 367789.86 | 10.76 | skipped_fast |
| KITEUSDT | IDLE | 2.22 | 4.19 | 1.64 | 0.02 | 73624.48 | 11.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.42 | 6.29 | 4.41 | 0.14 | 188222.77 | 18.87 | skipped_fast |
| HBARUSDT | IDLE | 1.2 | 2.22 | 1.22 | 0.04 | 576205.16 | 1.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 3.14 | 0.28 | 0.03 | 250481.4 | 31.16 | skipped_fast |
| BIOUSDT | IDLE | 1.98 | 3.93 | 0.19 | 0.05 | 77486.98 | 7.5 | skipped_fast |
| EDELUSDT | IDLE | 0.78 | 7.93 | 2.12 | -0.08 | 260587.35 | 38.99 | skipped_fast |
| REDUSDT | IDLE | 1.22 | 2.35 | 0.57 | 0.05 | 67784.63 | 9.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.09 | 2.19 | 0.0 | -0.03 | 16065.28 | 5.92 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.12 | 0.9 | 0.03 | 45079.91 | 7.98 | skipped_fast |
| MNSRYUSDT | IDLE | 1.11 | 2.2 | 0.15 | 0.03 | 43087.64 | 4.09 | skipped_fast |
| TELUSDT | IDLE | 0.73 | 1.33 | 0.83 | -0.0 | 72541.64 | 41.72 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.04 | 0.37 | 0.02 | 58139.61 | 44.35 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 148.34 | 21.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
