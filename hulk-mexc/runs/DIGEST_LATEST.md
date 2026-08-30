# Hulk DIGEST — 2026-08-30T17:46:43Z

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
| ETHUSDT | IDLE | 1.6 | 3.05 | 1.01 | 0.02 | 218168937.44 | 0.32 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 2.44 | 0.51 | 0.02 | 20783629.99 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.58 | 0.41 | 0.01 | 278891745.96 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.92 | 7.33 | 6.24 | -0.03 | 515170.08 | 2.51 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 9.26 | 5.68 | -0.06 | 198430.43 | 9.67 | skipped_fast |
| PYTHUSDT | IDLE | 3.05 | 5.66 | 2.91 | 0.02 | 389946.96 | 4.1 | skipped_fast |
| WUSDT | IDLE | 1.61 | 3.02 | 1.3 | 0.04 | 222774.48 | 10.54 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 5.99 | 3.55 | 0.07 | 72790.42 | 25.09 | skipped_fast |
| KITEUSDT | IDLE | 1.77 | 3.1 | 2.98 | -0.03 | 61253.22 | 3.98 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 1.74 | 1.47 | 0.01 | 254989.98 | 7.63 | skipped_fast |
| REDUSDT | IDLE | 1.2 | 2.09 | 2.02 | 0.01 | 63096.73 | 14.62 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.65 | 0.61 | -0.0 | 80543.98 | 3.63 | skipped_fast |
| RIZEUSDT | IDLE | 1.26 | 4.02 | 3.39 | -0.07 | 37306.59 | 62.12 | skipped_fast |
| TELUSDT | IDLE | 2.21 | 4.37 | 0.29 | 0.0 | 83450.69 | 23.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.81 | 3.63 | 0.0 | 0.02 | 1921.2 | 120.81 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.21 | 0.15 | 0.01 | 142535.77 | 1.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.56 | 0.01 | 32220.52 | 5.33 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.22 | 0.16 | 0.02 | 52893.08 | 8.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.73 | 0.04 | 0.03 | 3186.73 | 21.53 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.97 | 0.35 | 0.01 | 38251.82 | 4.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
