# Hulk DIGEST — 2026-10-23T12:47:41Z

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
| XRPUSDT | IDLE | 0.64 | 1.13 | 1.01 | -0.01 | 26116586.04 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.89 | 0.46 | -0.0 | 225354554.63 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.29 | 0.55 | 0.17 | 0.0 | 324907700.49 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.73 | 6.04 | 4.1 | -0.07 | 1042178.25 | 0.55 | skipped_fast |
| WUSDT | IDLE | 2.92 | 5.22 | 4.2 | -0.0 | 619503.39 | 14.96 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 3.42 | 2.54 | -0.04 | 695345.79 | 2.79 | skipped_fast |
| ZBCNUSDT | IDLE | 3.12 | 6.58 | 1.0 | -0.01 | 165119.83 | 20.38 | skipped_fast |
| EDELUSDT | IDLE | 1.71 | 3.16 | 1.67 | -0.03 | 403910.97 | 18.86 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 4.76 | 3.3 | 0.02 | 124501.37 | 17.81 | skipped_fast |
| RIZEUSDT | IDLE | 2.45 | 10.85 | 6.39 | -0.08 | 48790.0 | 65.48 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.92 | 0.22 | 0.01 | 193875.38 | 7.69 | skipped_fast |
| HBARUSDT | IDLE | 1.34 | 2.46 | 1.5 | -0.02 | 334484.03 | 7.54 | skipped_fast |
| RWAINCUSDT | IDLE | 1.19 | 2.24 | 0.99 | 0.01 | 51532.09 | 27.66 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 1.66 | 1.41 | -0.02 | 76949.73 | 16.44 | skipped_fast |
| KITEUSDT | IDLE | 0.87 | 1.62 | 0.85 | 0.0 | 57435.55 | 13.26 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 1.43 | 0.79 | -0.0 | 60059.07 | 4.18 | skipped_fast |
| LAUSDT | IDLE | 2.03 | 3.88 | 1.23 | 0.02 | 55403.83 | 26.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.84 | 3.21 | 3.11 | -0.05 | 9529.1 | 21.32 | skipped_fast |
| WAXLUSDT | IDLE | 1.74 | 3.15 | 2.26 | -0.02 | 56661.98 | 41.96 | skipped_fast |
| IOTAUSDT | IDLE | 0.57 | 1.07 | 0.53 | -0.0 | 66240.92 | 17.81 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.71 | 0.16 | 0.0 | 51432.48 | 15.72 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.25 | 0.88 | -0.01 | 36960.2 | 64.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
