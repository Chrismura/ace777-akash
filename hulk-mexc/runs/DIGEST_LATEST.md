# Hulk DIGEST — 2026-09-05T14:29:00Z

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
| XRPUSDT | IDLE | 0.6 | 1.17 | 0.25 | 0.01 | 25220750.45 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.26 | 0.48 | 0.21 | 0.0 | 198077437.94 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.26 | 0.05 | 0.0 | 390245982.44 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 3.6 | 1.48 | 0.03 | 358508.97 | 1.83 | skipped_fast |
| CHIPUSDT | IDLE | 1.3 | 5.15 | 0.46 | 0.1 | 443731.27 | 1.73 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.7 | 6.21 | 5.27 | -0.06 | 65331.49 | 9.54 | skipped_fast |
| REDUSDT | IDLE | 1.92 | 3.4 | 2.94 | 0.01 | 64707.75 | 10.42 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.73 | 0.76 | 0.01 | 301001.69 | 9.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 11.89 | 3.62 | -0.0 | 155676.72 | 61.77 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.66 | 0.65 | -0.01 | 187842.37 | 14.16 | skipped_fast |
| BIOUSDT | IDLE | 1.45 | 2.86 | 0.32 | 0.03 | 81830.38 | 3.58 | skipped_fast |
| WUSDT | IDLE | 0.56 | 1.03 | 0.54 | 0.06 | 162594.89 | 10.06 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 1.94 | 1.17 | 0.04 | 319093.3 | 1.24 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.22 | 2.01 | -0.01 | 7385.39 | 32.41 | skipped_fast |
| EDELUSDT | IDLE | 0.13 | 2.29 | 1.31 | -0.02 | 193620.3 | 37.74 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.14 | 0.76 | -0.01 | 74505.59 | 29.28 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 1.94 | 0.63 | 0.02 | 52502.14 | 21.28 | skipped_fast |
| QNTUSDT | IDLE | 0.63 | 1.15 | 0.76 | -0.02 | 39666.2 | 6.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.3 | 0.01 | -0.0 | 39111.91 | 2.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 820.75 | 21.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
