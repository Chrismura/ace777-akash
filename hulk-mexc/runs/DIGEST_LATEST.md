# Hulk DIGEST — 2026-09-12T18:32:52Z

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
| ETHUSDT | IDLE | 0.54 | 0.94 | 0.88 | -0.01 | 253833951.16 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.43 | 0.76 | 0.69 | 0.0 | 19780541.82 | 2.2 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.48 | 0.44 | -0.0 | 356110063.85 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 64.93 | 14.01 | 0.53 | 122378.27 | 3.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.59 | 6.2 | 4.36 | -0.03 | 208704.37 | 24.06 | skipped_fast |
| EDELUSDT | IDLE | 2.9 | 5.85 | 0.84 | 0.08 | 173328.33 | 25.35 | skipped_fast |
| PYTHUSDT | IDLE | 1.77 | 4.42 | 0.83 | 0.07 | 349158.71 | 1.82 | skipped_fast |
| CHIPUSDT | IDLE | 2.75 | 6.86 | 4.33 | 0.02 | 73213.36 | 14.33 | skipped_fast |
| RWAINCUSDT | IDLE | 2.69 | 5.05 | 4.23 | -0.02 | 10400.23 | 5.5 | skipped_fast |
| WUSDT | IDLE | 1.62 | 3.23 | 0.07 | 0.03 | 117732.48 | 10.98 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.66 | 1.52 | -0.01 | 243451.56 | 9.24 | skipped_fast |
| REDUSDT | IDLE | 1.21 | 2.4 | 0.09 | 0.03 | 61003.33 | 17.56 | skipped_fast |
| KITEUSDT | IDLE | 0.81 | 1.47 | 1.06 | -0.02 | 58870.98 | 12.23 | skipped_fast |
| BIOUSDT | IDLE | 0.66 | 1.17 | 1.01 | 0.02 | 70823.31 | 3.91 | skipped_fast |
| TELUSDT | IDLE | 1.27 | 2.3 | 1.6 | -0.06 | 101554.58 | 36.14 | skipped_fast |
| RWAUSDT | IDLE | 1.1 | 1.93 | 1.82 | 0.0 | 53066.04 | 7.42 | skipped_fast |
| HBARUSDT | IDLE | 0.47 | 0.83 | 0.73 | 0.0 | 153505.3 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 0.55 | 1.05 | 0.36 | 0.01 | 42437.19 | 4.66 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.54 | 0.0 | 0.02 | 1429.0 | 21.32 | skipped_fast |
| MNSRYUSDT | IDLE | 0.22 | 0.4 | 0.22 | -0.0 | 24266.76 | 27.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
