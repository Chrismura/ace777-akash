# Hulk DIGEST — 2026-08-21T20:26:12Z

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
| PYTHUSDT | IDLE | 1.33 | 4.78 | 3.05 | 0.08 | 5510602.01 | 2.11 | skipped_fast |
| XRPUSDT | IDLE | 1.24 | 4.21 | 3.07 | 0.12 | 129098743.2 | 2.18 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.88 | 0.16 | 153453.49 | 12.23 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 10.86 | 5.43 | 0.11 | 478370.7 | 24.97 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 3.91 | 1.2 | 0.08 | 632355.42 | 6.5 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.89 | 0.06 | 802153.71 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.34 | 4.81 | 3.61 | 0.08 | 509834.05 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.1 | 3.92 | 1.92 | 0.06 | 366564.51 | 13.78 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.73 | 0.02 | 189622.35 | 3.16 | skipped_fast |
| EDELUSDT | IDLE | 2.71 | 4.77 | 4.33 | -0.05 | 80366.31 | 22.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.61 | 0.01 | 56231.62 | 29.91 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 11163.46 | 53.62 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.41 | 0.11 | 61009.5 | 12.11 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 3.39 | 1.64 | 0.01 | 183871.81 | 16.13 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 2.65 | 1.45 | 0.04 | 59970.61 | 29.73 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.03 | 54341.16 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 23.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
