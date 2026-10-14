# Hulk DIGEST — 2026-10-14T01:10:44Z

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
| WUSDT | IDLE | 0.97 | 6.17 | 4.42 | -0.12 | 4208337.91 | 6.49 | skipped_fast |
| PYTHUSDT | IDLE | 1.13 | 3.72 | 1.44 | 0.0 | 2005327.88 | 3.78 | skipped_fast |
| QNTUSDT | IDLE | 1.71 | 5.77 | 4.73 | -0.06 | 1700741.91 | 1.43 | skipped_fast |
| XRPUSDT | IDLE | 0.59 | 1.08 | 0.73 | 0.03 | 30926834.36 | 2.19 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.9 | 0.63 | 0.03 | 178685337.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.67 | 0.45 | 0.02 | 357514048.73 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 3.41 | 2.74 | 0.06 | 593968.89 | 5.6 | skipped_fast |
| RWAINCUSDT | IDLE | 3.39 | 6.07 | 4.71 | -0.01 | 32655.97 | 20.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.77 | 3.19 | 2.39 | 0.0 | 97413.95 | 5.26 | skipped_fast |
| EDELUSDT | IDLE | 1.15 | 2.05 | 1.64 | 0.04 | 217868.34 | 11.7 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.59 | 1.79 | 0.04 | 124127.78 | 9.64 | skipped_fast |
| ZBCNUSDT | IDLE | 0.98 | 1.88 | 0.56 | 0.0 | 216417.94 | 27.29 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 2.89 | 0.64 | 0.08 | 57356.26 | 9.94 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.63 | 1.18 | 0.04 | 71535.31 | 7.23 | skipped_fast |
| FLUIDUSDT | IDLE | 2.45 | 4.9 | 0.0 | 0.09 | 19930.11 | 21.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.03 | 3.25 | 2.59 | -0.01 | 50417.88 | 59.57 | skipped_fast |
| TELUSDT | IDLE | 1.94 | 3.88 | 0.05 | 0.06 | 118145.91 | 43.98 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.43 | 0.68 | 0.02 | 249499.2 | 4.57 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.42 | 0.14 | -0.0 | 37360.27 | 5.58 | skipped_fast |
| RWAUSDT | IDLE | 0.16 | 0.31 | 0.08 | 0.01 | 51970.85 | 15.47 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
