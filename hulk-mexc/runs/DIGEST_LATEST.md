# Hulk DIGEST — 2026-09-10T03:15:03Z

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
| XRPUSDT | IDLE | 0.79 | 1.53 | 0.33 | -0.01 | 43606390.39 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.43 | 0.15 | -0.01 | 390836501.0 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.96 | 0.19 | -0.0 | 542939783.94 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.2 | 3.27 | 1.16 | -0.02 | 1010146.94 | 1.92 | skipped_fast |
| EDELUSDT | IDLE | 4.12 | 16.05 | 4.04 | 0.06 | 236574.3 | 26.8 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 2.75 | 1.2 | -0.04 | 647728.68 | 4.8 | skipped_fast |
| REDUSDT | IDLE | 2.88 | 5.33 | 2.84 | 0.0 | 64270.94 | 10.21 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.66 | 1.73 | -0.02 | 207583.56 | 8.09 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 4.2 | 1.77 | -0.06 | 101931.18 | 3.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.07 | 5.72 | 4.85 | -0.08 | 123338.16 | 14.25 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 2.93 | 1.51 | -0.01 | 57080.64 | 12.42 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 1.85 | 0.87 | 0.02 | 185795.24 | 10.41 | skipped_fast |
| RWAINCUSDT | IDLE | 1.79 | 3.14 | 2.87 | -0.02 | 5889.78 | 39.63 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.77 | 0.17 | -0.02 | 443885.27 | 1.3 | skipped_fast |
| RIZEUSDT | IDLE | 0.63 | 7.7 | 0.48 | 0.05 | 60118.59 | 91.37 | skipped_fast |
| TELUSDT | IDLE | 1.21 | 2.31 | 0.77 | 0.01 | 97102.44 | 38.88 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 2.02 | 0.8 | -0.0 | 45740.23 | 4.47 | skipped_fast |
| FLUIDUSDT | IDLE | 1.27 | 2.41 | 2.35 | -0.07 | 1439.18 | 19.43 | skipped_fast |
| MNSRYUSDT | IDLE | 1.33 | 2.4 | 1.79 | -0.02 | 28175.67 | 60.79 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.5 | 0.96 | -0.03 | 54591.38 | 14.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
