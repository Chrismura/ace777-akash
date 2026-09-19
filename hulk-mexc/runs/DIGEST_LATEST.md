# Hulk DIGEST — 2026-09-19T09:58:06Z

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
| XRPUSDT | IDLE | 1.05 | 2.18 | 1.76 | 0.06 | 67880092.61 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.95 | 1.8 | 0.66 | 0.05 | 572291656.39 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.74 | 0.22 | 0.04 | 625147712.94 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.64 | 4.8 | 3.23 | -0.01 | 708162.83 | 3.33 | skipped_fast |
| WUSDT | IDLE | 1.01 | 3.15 | 0.35 | 0.07 | 977793.05 | 8.2 | skipped_fast |
| EDELUSDT | IDLE | 2.38 | 13.4 | 9.74 | -0.12 | 189168.06 | 19.49 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 3.18 | 2.2 | 0.0 | 418640.27 | 9.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 5.83 | 4.04 | 0.03 | 145353.75 | 19.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 16.29 | 9.29 | -0.06 | 39526.59 | 93.83 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 2.11 | 0.4 | 0.03 | 617056.81 | 1.26 | skipped_fast |
| KITEUSDT | IDLE | 2.05 | 4.06 | 0.24 | 0.06 | 70969.41 | 12.01 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 6.49 | 2.81 | 0.06 | 128896.64 | 7.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 2.36 | 0.45 | 0.02 | 186775.66 | 17.47 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.5 | 0.58 | 0.01 | 79751.83 | 7.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.72 | 1.44 | 0.0 | 0.04 | 5047.22 | 5.66 | skipped_fast |
| QNTUSDT | IDLE | 1.16 | 2.3 | 0.11 | 0.03 | 75332.59 | 4.66 | skipped_fast |
| TELUSDT | IDLE | 0.9 | 2.97 | 2.01 | 0.04 | 126169.95 | 44.77 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.64 | 0.66 | 0.0 | 56982.47 | 29.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.57 | 2.64 | 0.32 | 0.18 | 10160.89 | 20.59 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.55 | 0.17 | 0.04 | 40129.53 | 2.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
