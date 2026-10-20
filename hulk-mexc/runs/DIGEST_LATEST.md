# Hulk DIGEST — 2026-10-20T16:20:29Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 2.2 | 4.09 | 2.13 | 0.01 | 22998513.24 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 2.15 | 4.03 | 1.78 | 0.01 | 146755529.7 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.37 | 2.55 | 1.23 | 0.0 | 326650187.48 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.93 | 8.81 | 3.82 | 0.01 | 993785.1 | 6.62 | skipped_fast |
| WUSDT | IDLE | 3.35 | 6.16 | 3.57 | -0.02 | 709005.87 | 14.57 | skipped_fast |
| QNTUSDT | IDLE | 3.33 | 6.0 | 4.35 | -0.01 | 684381.54 | 3.6 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.26 | 10.21 | 0.02 | 69331.48 | 63.42 | skipped_fast |
| ZBCNUSDT | IDLE | 4.1 | 7.65 | 3.64 | 0.01 | 191985.52 | 29.14 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.55 | 9.6 | 8.71 | -0.04 | 76547.81 | 74.47 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 10.03 | 5.32 | 0.08 | 114007.63 | 13.37 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 15.05 | 1.76 | 0.33 | 320882.4 | 19.61 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 3.41 | 1.09 | 0.02 | 415744.53 | 7.56 | skipped_fast |
| BIOUSDT | IDLE | 3.08 | 5.87 | 1.93 | 0.03 | 63597.67 | 8.19 | skipped_fast |
| HBARUSDT | IDLE | 2.55 | 4.66 | 2.99 | 0.01 | 370514.29 | 7.22 | skipped_fast |
| REDUSDT | IDLE | 2.65 | 5.05 | 1.7 | 0.01 | 58809.9 | 17.24 | skipped_fast |
| KITEUSDT | IDLE | 2.32 | 4.35 | 1.99 | -0.02 | 84966.37 | 12.31 | skipped_fast |
| IOTAUSDT | IDLE | 3.32 | 6.63 | 3.41 | 0.04 | 91255.24 | 28.0 | skipped_fast |
| LAUSDT | IDLE | 3.11 | 6.0 | 1.5 | 0.02 | 55896.31 | 26.05 | skipped_fast |
| WAXLUSDT | IDLE | 2.94 | 5.42 | 3.01 | -0.05 | 55175.27 | 60.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.38 | 2.67 | 0.66 | 0.04 | 4058.72 | 21.57 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.5 | 1.17 | 0.0 | 51557.37 | 15.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.8 | 1.52 | 0.57 | 0.0 | 39939.79 | 15.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
