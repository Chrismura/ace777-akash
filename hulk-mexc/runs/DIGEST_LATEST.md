# Hulk DIGEST — 2026-09-19T01:55:39Z

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
| XRPUSDT | IDLE | 0.91 | 2.02 | 0.48 | 0.08 | 68661052.86 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.42 | 0.91 | 0.06 | 659741896.98 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.09 | 0.45 | 0.06 | 788539372.76 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.95 | 3.26 | 1.77 | 0.1 | 938859.64 | 8.22 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 19.02 | 15.29 | 0.05 | 90274.43 | 8.36 | skipped_fast |
| PYTHUSDT | IDLE | 1.15 | 2.16 | 0.93 | 0.06 | 781416.7 | 4.97 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.98 | 13.38 | 7.72 | -0.05 | 194557.78 | 36.56 | skipped_fast |
| CCUSDT | IDLE | 1.35 | 2.54 | 1.05 | 0.05 | 677096.32 | 10.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.35 | 8.08 | 2.66 | 0.09 | 163148.64 | 17.62 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 2.02 | 0.64 | 0.06 | 700013.43 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 2.33 | 1.6 | 0.03 | 236110.47 | 17.65 | skipped_fast |
| TELUSDT | IDLE | 2.45 | 11.46 | 6.4 | 0.12 | 126793.61 | 37.64 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.36 | 0.31 | 0.04 | 78295.45 | 9.78 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.85 | 0.65 | 0.07 | 86906.0 | 7.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.56 | 1.04 | 0.57 | 0.04 | 6732.04 | 5.75 | skipped_fast |
| RIZEUSDT | IDLE | 0.16 | 2.77 | 0.0 | -0.07 | 56109.12 | 70.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 4.42 | 2.02 | 0.15 | 3675.86 | 19.42 | skipped_fast |
| QNTUSDT | IDLE | 0.62 | 1.12 | 0.86 | 0.03 | 75495.48 | 9.48 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.04 | 0.74 | 0.01 | 57326.8 | 22.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.7 | 0.16 | 0.06 | 42442.69 | 2.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
