# Hulk DIGEST — 2026-09-06T02:30:32Z

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
| XRPUSDT | IDLE | 0.74 | 1.41 | 0.44 | 0.01 | 23928195.77 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.33 | 0.3 | 0.02 | 194401745.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.23 | 0.43 | 0.17 | 0.01 | 372309310.08 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.09 | 3.73 | 2.96 | 0.02 | 409331.83 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 4.43 | 2.31 | 0.05 | 424161.69 | 1.69 | skipped_fast |
| RWAINCUSDT | IDLE | 2.89 | 5.2 | 3.9 | -0.0 | 8379.45 | 27.05 | skipped_fast |
| CCUSDT | IDLE | 1.33 | 2.52 | 0.87 | 0.03 | 290399.02 | 8.15 | skipped_fast |
| WUSDT | IDLE | 1.91 | 3.59 | 1.57 | 0.04 | 171819.69 | 18.79 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 2.5 | 2.2 | -0.01 | 224628.84 | 5.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.41 | 9.29 | 2.44 | -0.07 | 125003.84 | 56.57 | skipped_fast |
| REDUSDT | IDLE | 1.3 | 2.28 | 2.2 | 0.01 | 59545.56 | 8.73 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.98 | 0.11 | 0.04 | 368289.57 | 1.23 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 2.27 | 0.33 | -0.05 | 64700.35 | 12.48 | skipped_fast |
| RWAUSDT | IDLE | 2.23 | 3.91 | 3.63 | 0.03 | 53562.32 | 28.37 | skipped_fast |
| BIOUSDT | IDLE | 0.64 | 1.22 | 0.46 | 0.02 | 96059.06 | 7.15 | skipped_fast |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.76 | 0.02 | 116192.39 | 28.24 | skipped_fast |
| TELUSDT | IDLE | 1.74 | 3.28 | 1.27 | 0.0 | 72971.57 | 29.2 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.62 | 0.69 | 0.03 | 36831.3 | 4.55 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 2.11 | 0.0 | 0.03 | 390.92 | 21.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.97 | 0.16 | 0.01 | 38962.66 | 44.77 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
