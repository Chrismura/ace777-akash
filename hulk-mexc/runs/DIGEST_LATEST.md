# Hulk DIGEST — 2026-09-16T12:02:24Z

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
| ETHUSDT | IDLE | 1.03 | 2.0 | 0.34 | -0.02 | 492401644.35 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.63 | 1.24 | 0.12 | -0.01 | 592872430.58 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.52 | 1.91 | 0.55 | -0.08 | 94743357.84 | 0.77 | skipped_fast |
| PYTHUSDT | IDLE | 1.51 | 2.72 | 2.01 | -0.03 | 673517.05 | 1.9 | skipped_fast |
| CHIPUSDT | IDLE | 2.33 | 5.63 | 1.2 | -0.06 | 104273.77 | 15.74 | skipped_fast |
| EDELUSDT | IDLE | 0.48 | 7.61 | 0.39 | 0.53 | 437974.94 | 17.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 20.93 | 1.35 | 0.44 | 48767.97 | 51.69 | skipped_fast |
| REDUSDT | IDLE | 1.92 | 3.6 | 1.63 | -0.05 | 68080.1 | 9.9 | skipped_fast |
| CCUSDT | IDLE | 0.35 | 0.69 | 0.13 | -0.04 | 385393.1 | 3.29 | skipped_fast |
| WUSDT | IDLE | 0.89 | 2.06 | 0.88 | -0.07 | 208907.45 | 5.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 3.04 | 0.29 | -0.06 | 202714.64 | 37.59 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.96 | 0.32 | -0.01 | 80838.56 | 8.03 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.22 | 0.53 | -0.03 | 436921.69 | 1.34 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.81 | 1.03 | -0.06 | 60814.66 | 10.99 | skipped_fast |
| RWAINCUSDT | IDLE | 1.2 | 2.1 | 2.06 | -0.04 | 14398.51 | 23.34 | skipped_fast |
| TELUSDT | IDLE | 1.58 | 3.25 | 2.34 | -0.06 | 113854.7 | 68.59 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.67 | 0.33 | -0.05 | 45077.25 | 8.33 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.62 | 1.59 | -0.06 | 1519.5 | 22.05 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.45 | -0.01 | 52325.76 | 22.82 | skipped_fast |
| MNSRYUSDT | IDLE | 0.23 | 0.44 | 0.1 | -0.02 | 33288.24 | 4.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
