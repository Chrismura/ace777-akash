# Hulk DIGEST — 2026-09-13T16:40:05Z

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
| ETHUSDT | IDLE | 0.88 | 1.74 | 0.12 | -0.01 | 250811026.51 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.65 | 0.49 | -0.02 | 15047895.2 | 2.97 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 1.0 | 0.04 | -0.0 | 292973191.4 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.42 | 4.76 | 0.5 | 0.02 | 433286.91 | 1.8 | skipped_fast |
| CHIPUSDT | IDLE | 2.12 | 6.9 | 6.13 | -0.12 | 88776.14 | 11.55 | skipped_fast |
| WUSDT | IDLE | 1.49 | 2.92 | 0.39 | 0.02 | 252667.7 | 13.91 | skipped_fast |
| EDELUSDT | IDLE | 1.85 | 7.67 | 0.77 | 0.09 | 200851.37 | 77.88 | skipped_fast |
| ZBCNUSDT | IDLE | 1.53 | 2.96 | 0.63 | -0.02 | 205797.64 | 21.76 | skipped_fast |
| CCUSDT | IDLE | 0.83 | 1.6 | 0.34 | -0.03 | 294858.51 | 9.44 | skipped_fast |
| REDUSDT | IDLE | 1.66 | 2.93 | 2.57 | -0.0 | 60795.18 | 18.43 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.38 | 2.33 | 0.01 | 63484.27 | 12.15 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.03 | 1.05 | -0.01 | 70078.75 | 3.93 | skipped_fast |
| RIZEUSDT | IDLE | 0.77 | 12.36 | 4.11 | -0.09 | 87276.38 | 85.69 | skipped_fast |
| RWAINCUSDT | IDLE | 0.87 | 1.65 | 0.56 | -0.02 | 6655.69 | 5.6 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.11 | 1.12 | 0.01 | 186724.06 | 1.32 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.96 | 0.37 | -0.0 | 54064.47 | 29.7 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 1.46 | 0.46 | 0.0 | 37234.15 | 4.67 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.65 | 0.44 | -0.05 | 85309.11 | 50.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.63 | 1.11 | 1.05 | -0.01 | 1479.56 | 22.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.04 | -0.0 | 32152.31 | 13.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
