# Hulk DIGEST — 2026-08-31T11:16:43Z

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
| XRPUSDT | IDLE | 0.9 | 1.76 | 0.22 | -0.01 | 39631811.59 | 1.45 | skipped_fast |
| BTCUSDT | IDLE | 0.62 | 1.2 | 0.24 | 0.01 | 525147241.8 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.53 | 1.06 | 0.06 | -0.0 | 441146245.75 | 0.61 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 7.0 | 2.48 | 0.03 | 600928.0 | 2.45 | skipped_fast |
| PYTHUSDT | IDLE | 0.94 | 2.26 | 1.06 | -0.0 | 520367.2 | 2.11 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 2.46 | 0.94 | 0.01 | 242845.04 | 8.34 | skipped_fast |
| REDUSDT | IDLE | 1.92 | 3.44 | 2.61 | -0.0 | 70272.11 | 11.93 | skipped_fast |
| WUSDT | IDLE | 1.13 | 2.11 | 1.3 | -0.01 | 233969.02 | 15.03 | skipped_fast |
| ZBCNUSDT | IDLE | 0.81 | 2.68 | 0.23 | -0.07 | 235484.35 | 9.96 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 2.51 | 1.64 | -0.05 | 97148.48 | 9.91 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.51 | 1.38 | -0.03 | 85996.01 | 3.78 | skipped_fast |
| EDELUSDT | IDLE | 0.46 | 3.03 | 0.74 | 0.02 | 120529.15 | 24.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.22 | 2.42 | 0.18 | -0.0 | 33470.69 | 61.55 | skipped_fast |
| TELUSDT | IDLE | 1.99 | 3.87 | 0.69 | 0.03 | 95056.15 | 40.4 | skipped_fast |
| RWAUSDT | IDLE | 1.76 | 3.5 | 0.08 | 0.04 | 54239.14 | 15.72 | skipped_fast |
| QNTUSDT | IDLE | 1.58 | 2.93 | 1.55 | -0.0 | 38399.58 | 6.5 | skipped_fast |
| RWAINCUSDT | IDLE | 1.35 | 2.35 | 2.29 | -0.02 | 2855.92 | 119.49 | skipped_fast |
| HBARUSDT | IDLE | 0.38 | 0.73 | 0.24 | -0.01 | 241750.26 | 1.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.15 | 0.16 | 0.01 | 1733.99 | 22.36 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.59 | 0.37 | -0.01 | 28881.71 | 31.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
