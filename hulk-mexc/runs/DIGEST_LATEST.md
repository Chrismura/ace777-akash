# Hulk DIGEST — 2026-09-02T02:29:49Z

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
| XRPUSDT | IDLE | 1.15 | 2.16 | 0.89 | -0.02 | 36925754.95 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.94 | 1.78 | 0.7 | -0.02 | 357999562.88 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.16 | 0.38 | -0.01 | 530220211.86 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.79 | 8.04 | 3.22 | 0.06 | 663697.33 | 3.81 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 7.22 | 4.4 | 0.13 | 807632.89 | 4.57 | skipped_fast |
| WUSDT | IDLE | 2.91 | 5.36 | 3.13 | 0.03 | 417488.54 | 20.79 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 4.69 | 2.23 | -0.03 | 197924.45 | 43.79 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 7.4 | 5.88 | -0.06 | 42688.52 | 78.33 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 3.8 | 2.77 | 0.07 | 143666.03 | 11.51 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 9.32 | 2.09 | -0.01 | 171094.92 | 26.63 | skipped_fast |
| CCUSDT | IDLE | 0.48 | 1.17 | 0.17 | -0.07 | 311615.56 | 9.65 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 2.37 | 0.81 | 0.04 | 69041.81 | 8.9 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.99 | 0.86 | -0.04 | 70311.58 | 3.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.48 | 1.21 | 0.01 | 5760.07 | 40.69 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 1.94 | 1.21 | -0.0 | 255348.85 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.8 | 0.61 | 0.04 | 46972.87 | 4.69 | skipped_fast |
| TELUSDT | IDLE | 1.81 | 3.54 | 0.47 | -0.0 | 92614.04 | 89.15 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.04 | 2.0 | -0.06 | 328.66 | 22.0 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 1.01 | 0.54 | -0.03 | 58174.26 | 23.1 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.7 | 0.47 | -0.02 | 35658.88 | 8.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
