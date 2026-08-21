# Hulk DIGEST — 2026-08-21T20:41:25Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.31 | 4.78 | 2.58 | 0.08 | 5544476.38 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.25 | 0.11 | 128965110.63 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.26 | 0.17 | 153489.44 | 11.31 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.77 | 0.12 | 478659.98 | 36.57 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.91 | 0.21 | 0.09 | 639161.54 | 10.12 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.86 | 0.06 | 809778.58 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 4.81 | 3.01 | 0.09 | 514491.87 | 3.08 | skipped_fast |
| WUSDT | IDLE | 2.07 | 3.92 | 1.51 | 0.06 | 367723.17 | 13.72 | skipped_fast |
| BIOUSDT | IDLE | 2.54 | 5.33 | 2.94 | 0.01 | 189212.0 | 3.16 | skipped_fast |
| EDELUSDT | IDLE | 2.77 | 5.01 | 3.9 | -0.05 | 81394.04 | 56.21 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10892.53 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.66 | 0.02 | 56280.58 | 47.09 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.49 | 0.11 | 60914.26 | 12.11 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.0 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 181841.86 | 26.83 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.74 | 0.04 | 59908.54 | 6.26 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53889.66 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 23.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
