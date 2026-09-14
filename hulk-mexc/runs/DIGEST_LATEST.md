# Hulk DIGEST — 2026-09-14T12:34:30Z

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
| XRPUSDT | IDLE | 1.06 | 2.06 | 0.45 | 0.04 | 36188958.14 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.16 | 0.69 | 0.01 | 313028943.68 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.09 | 0.4 | 0.02 | 408581258.58 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.35 | 5.94 | 5.03 | 0.02 | 515944.9 | 1.8 | skipped_fast |
| WUSDT | IDLE | 1.69 | 2.99 | 2.59 | 0.0 | 231242.64 | 9.04 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 6.96 | 0.96 | 0.18 | 239281.22 | 27.62 | skipped_fast |
| REDUSDT | IDLE | 1.75 | 4.33 | 0.37 | 0.06 | 163349.44 | 15.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.74 | 5.38 | 0.63 | -0.07 | 105202.69 | 16.45 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 1.85 | 0.11 | 0.01 | 233508.96 | 9.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.9 | 0.89 | 0.0 | 210134.77 | 44.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.49 | 2.83 | 0.97 | 0.04 | 8654.89 | 5.46 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.89 | 0.77 | 0.01 | 75856.79 | 3.89 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.13 | 0.75 | -0.02 | 61443.36 | 10.29 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 9.88 | 4.23 | 0.23 | 72659.51 | 95.48 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.87 | 0.05 | 0.03 | 285763.21 | 1.29 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.38 | 1.6 | 0.0 | 90430.59 | 37.57 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.06 | 1.64 | 0.01 | 800.11 | 17.5 | skipped_fast |
| QNTUSDT | IDLE | 0.66 | 1.31 | 0.0 | 0.01 | 38634.15 | 6.22 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.46 | 0.31 | -0.0 | 29166.15 | 5.59 | skipped_fast |
| RWAUSDT | IDLE | 0.17 | 0.3 | 0.22 | 0.0 | 53718.8 | 14.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
