# Hulk DIGEST — 2026-10-12T02:58:48Z

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
| WUSDT | IDLE | 2.68 | 48.74 | 2.9 | 0.62 | 6816158.88 | 12.59 | skipped_fast |
| ETHUSDT | IDLE | 0.99 | 1.89 | 0.58 | 0.01 | 202806503.23 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.07 | 0.42 | 0.01 | 17858166.61 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.89 | 0.21 | 0.01 | 166919092.4 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.88 | 5.76 | 0.04 | 0.03 | 918249.44 | 12.28 | skipped_fast |
| CHIPUSDT | IDLE | 2.02 | 6.69 | 5.98 | -0.03 | 240138.54 | 15.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.23 | 4.42 | 0.21 | 0.04 | 242954.02 | 5.89 | skipped_fast |
| QNTUSDT | IDLE | 1.28 | 2.28 | 1.87 | 0.0 | 706496.16 | 0.42 | skipped_fast |
| EDELUSDT | IDLE | 1.65 | 3.14 | 1.07 | -0.01 | 334056.96 | 23.81 | skipped_fast |
| CCUSDT | IDLE | 1.26 | 2.67 | 0.45 | 0.06 | 384351.44 | 8.7 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.26 | 0.22 | 0.01 | 63203.62 | 10.11 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.86 | 0.1 | 0.03 | 97556.99 | 6.65 | skipped_fast |
| RWAINCUSDT | IDLE | 1.08 | 2.88 | 2.21 | -0.02 | 25163.32 | 5.02 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 1.99 | 0.76 | 0.01 | 54786.25 | 7.29 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.78 | 0.7 | 0.02 | 302042.2 | 4.26 | skipped_fast |
| RIZEUSDT | IDLE | 0.61 | 3.69 | 2.63 | 0.05 | 37011.71 | 17.97 | skipped_fast |
| TELUSDT | IDLE | 1.27 | 2.48 | 0.35 | -0.01 | 170391.24 | 28.86 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 3.75 | 1.9 | 0.06 | 67201.47 | 21.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.78 | 0.2 | 0.0 | 34874.67 | 5.46 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.54 | 0.23 | 0.02 | 52846.26 | 7.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
