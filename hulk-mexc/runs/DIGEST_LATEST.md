# Hulk DIGEST — 2026-10-11T17:56:00Z

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
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.58 | 15.58 | 0.0 | 0.13 | 1173497.17 | 13.04 | skipped_fast |
| XRPUSDT | IDLE | 1.23 | 2.38 | 0.53 | 0.01 | 13840052.14 | 2.11 | skipped_fast |
| ETHUSDT | IDLE | 1.1 | 2.14 | 0.41 | 0.01 | 212067102.01 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.71 | 1.38 | 0.29 | 0.01 | 151114794.53 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.27 | 2.51 | 0.23 | -0.02 | 786644.86 | 1.29 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 11.9 | 6.02 | 0.02 | 27805.35 | 33.71 | skipped_fast |
| CCUSDT | IDLE | 2.74 | 5.57 | 0.26 | 0.07 | 319873.39 | 5.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.71 | 9.0 | 4.84 | 0.13 | 395251.64 | 13.31 | skipped_fast |
| ZBCNUSDT | IDLE | 2.86 | 5.47 | 1.67 | 0.02 | 188516.28 | 2.55 | skipped_fast |
| EDELUSDT | IDLE | 1.77 | 3.17 | 2.49 | -0.01 | 404104.74 | 18.23 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 2.06 | 0.31 | 0.01 | 839964.86 | 3.26 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.97 | 7.16 | 5.25 | -0.04 | 155263.97 | 17.49 | skipped_fast |
| RIZEUSDT | IDLE | 2.69 | 7.45 | 0.84 | -0.01 | 32031.47 | 58.33 | skipped_fast |
| REDUSDT | IDLE | 1.88 | 3.69 | 0.42 | 0.02 | 57745.06 | 14.39 | skipped_fast |
| BIOUSDT | IDLE | 1.64 | 3.24 | 0.3 | 0.04 | 86169.49 | 6.63 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.09 | 0.4 | -0.02 | 72641.73 | 10.18 | skipped_fast |
| HBARUSDT | IDLE | 1.43 | 2.79 | 0.5 | 0.01 | 241819.3 | 3.21 | skipped_fast |
| RWAUSDT | IDLE | 1.3 | 2.54 | 0.39 | 0.01 | 51066.33 | 23.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 5.76 | 0.69 | 0.08 | 55730.95 | 21.2 | skipped_fast |
| MNSRYUSDT | IDLE | 0.85 | 1.66 | 0.26 | -0.01 | 30751.01 | 46.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
