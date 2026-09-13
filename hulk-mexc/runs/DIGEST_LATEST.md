# Hulk DIGEST — 2026-09-13T09:39:23Z

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
| XRPUSDT | IDLE | 1.24 | 2.21 | 1.78 | -0.02 | 13837265.52 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 1.2 | 2.14 | 1.67 | -0.02 | 209784958.32 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.97 | 0.77 | -0.01 | 299825513.7 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.84 | 13.41 | 11.53 | 0.08 | 204128.86 | 16.45 | skipped_fast |
| PYTHUSDT | IDLE | 2.2 | 3.92 | 3.26 | 0.02 | 455989.63 | 1.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.89 | 30.17 | 11.2 | 0.18 | 101154.3 | 52.42 | skipped_fast |
| CCUSDT | IDLE | 2.38 | 4.21 | 3.69 | -0.04 | 281398.8 | 6.3 | skipped_fast |
| WUSDT | IDLE | 1.47 | 2.7 | 1.56 | 0.02 | 243607.33 | 20.12 | skipped_fast |
| REDUSDT | IDLE | 1.98 | 3.52 | 3.0 | 0.02 | 55266.83 | 12.28 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.67 | 2.27 | -0.02 | 77694.59 | 14.93 | skipped_fast |
| KITEUSDT | IDLE | 1.66 | 3.01 | 2.08 | 0.02 | 61951.31 | 11.98 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.54 | 1.78 | -0.0 | 70756.7 | 7.89 | skipped_fast |
| TELUSDT | IDLE | 2.65 | 4.86 | 2.99 | -0.06 | 88301.81 | 18.85 | skipped_fast |
| ZBCNUSDT | IDLE | 0.74 | 2.11 | 1.56 | -0.03 | 213799.09 | 28.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.35 | -0.03 | 9194.63 | 5.59 | skipped_fast |
| FLUIDUSDT | IDLE | 1.99 | 3.57 | 2.71 | 0.01 | 1217.06 | 21.41 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.57 | 0.94 | 0.01 | 153066.35 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.73 | 1.31 | 0.95 | -0.01 | 36928.48 | 9.42 | skipped_fast |
| RWAUSDT | IDLE | 0.92 | 1.66 | 1.26 | -0.01 | 55910.68 | 52.53 | skipped_fast |
| MNSRYUSDT | IDLE | 0.2 | 0.36 | 0.33 | -0.0 | 33415.26 | 26.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
