# Hulk DIGEST — 2026-10-10T16:53:42Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.78 | 12.38 | 5.48 | 0.01 | 1235695.25 | 8.38 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.89 | 0.41 | 0.0 | 86409589.79 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.7 | 0.46 | 0.01 | 15477550.55 | 2.13 | skipped_fast |
| QNTUSDT | IDLE | 3.66 | 6.57 | 4.94 | -0.01 | 1177018.04 | 0.41 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.36 | 0.04 | 0.0 | 183249463.58 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.34 | 0.31 | -0.06 | 949939.14 | 5.05 | skipped_fast |
| EDELUSDT | IDLE | 2.81 | 5.64 | 4.56 | -0.04 | 219673.94 | 13.05 | skipped_fast |
| CHIPUSDT | IDLE | 2.59 | 8.93 | 2.87 | 0.1 | 99102.46 | 9.17 | skipped_fast |
| KITEUSDT | IDLE | 2.17 | 5.87 | 2.47 | 0.06 | 72247.48 | 7.76 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.69 | 1.4 | -0.02 | 358923.31 | 7.54 | skipped_fast |
| TELUSDT | IDLE | 2.85 | 5.22 | 3.24 | -0.04 | 122812.43 | 33.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.05 | 1.96 | 0.99 | -0.01 | 202155.61 | 9.17 | skipped_fast |
| BIOUSDT | IDLE | 1.25 | 2.45 | 0.31 | 0.04 | 85513.62 | 3.43 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.87 | 0.71 | 0.02 | 54513.49 | 9.96 | skipped_fast |
| HBARUSDT | IDLE | 0.9 | 1.69 | 0.7 | 0.02 | 354453.01 | 4.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.89 | 1.73 | 0.29 | -0.04 | 8638.04 | 38.99 | skipped_fast |
| RIZEUSDT | IDLE | 0.55 | 1.26 | 0.69 | -0.0 | 43432.84 | 55.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 1.94 | 1.28 | 0.0 | 15311.85 | 21.61 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.71 | 0.55 | -0.01 | 54525.31 | 15.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.23 | 0.43 | 0.26 | 0.0 | 38794.89 | 21.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
