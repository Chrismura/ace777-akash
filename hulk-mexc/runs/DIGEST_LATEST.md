# Hulk DIGEST — 2026-08-21T20:06:48Z

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
| PYTHUSDT | IDLE | 1.35 | 4.78 | 3.44 | 0.07 | 5465392.02 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.58 | 0.11 | 128890669.88 | 1.46 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 25.8 | 13.34 | 0.17 | 154274.94 | 17.99 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.53 | 10.86 | 7.46 | 0.1 | 478004.58 | 26.53 | skipped_fast |
| CCUSDT | IDLE | 1.48 | 3.91 | 1.64 | 0.07 | 633538.15 | 5.6 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.23 | 2.64 | 0.05 | 794084.22 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.85 | 0.08 | 513740.08 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.16 | 3.92 | 2.62 | 0.05 | 366436.04 | 10.68 | skipped_fast |
| BIOUSDT | IDLE | 2.58 | 5.33 | 3.56 | 0.0 | 189842.04 | 3.19 | skipped_fast |
| EDELUSDT | IDLE | 2.42 | 4.29 | 3.68 | -0.04 | 79739.95 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.44 | 0.02 | 56226.23 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.26 | 4.3 | 1.53 | 0.04 | 11069.14 | 32.4 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 3.03 | 0.1 | 61181.02 | 11.24 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2867.01 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.49 | 0.01 | 183629.91 | 48.82 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.61 | 0.04 | 59952.48 | 6.26 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.16 | 0.82 | 0.04 | 54382.24 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 23.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
