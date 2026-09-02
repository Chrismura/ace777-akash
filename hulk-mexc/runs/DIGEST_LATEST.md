# Hulk DIGEST — 2026-09-02T00:28:32Z

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
| XRPUSDT | IDLE | 1.09 | 1.97 | 1.35 | -0.03 | 35589777.47 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.08 | 0.45 | -0.02 | 345833490.85 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.9 | 0.39 | -0.02 | 527347564.88 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.8 | 7.41 | 0.8 | 0.06 | 721765.0 | 3.76 | skipped_fast |
| CHIPUSDT | IDLE | 1.95 | 9.45 | 4.7 | 0.12 | 742334.09 | 4.57 | skipped_fast |
| WUSDT | IDLE | 2.51 | 4.39 | 4.14 | 0.02 | 419295.94 | 14.68 | skipped_fast |
| ZBCNUSDT | IDLE | 2.41 | 4.24 | 3.93 | -0.04 | 196637.14 | 8.26 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 5.5 | 3.53 | 0.08 | 120243.35 | 9.64 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.82 | 1.37 | -0.07 | 333107.04 | 7.06 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 4.22 | 1.8 | -0.04 | 40645.26 | 74.83 | skipped_fast |
| EDELUSDT | IDLE | 1.0 | 9.32 | 0.17 | -0.03 | 157936.43 | 78.91 | skipped_fast |
| KITEUSDT | IDLE | 1.09 | 2.11 | 0.47 | 0.04 | 68883.54 | 11.31 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 1.82 | 0.85 | -0.04 | 69075.2 | 3.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 1.95 | 1.91 | -0.02 | 5487.56 | 17.68 | skipped_fast |
| HBARUSDT | IDLE | 0.72 | 1.26 | 1.25 | -0.0 | 249555.16 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.48 | 2.8 | 1.01 | 0.04 | 46465.68 | 4.71 | skipped_fast |
| TELUSDT | IDLE | 1.48 | 2.69 | 1.85 | -0.04 | 93795.92 | 54.6 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 1.01 | 0.15 | -0.03 | 58603.34 | 7.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.48 | 0.96 | 0.0 | -0.04 | 244.85 | 21.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.37 | 0.7 | 0.25 | -0.02 | 34725.86 | 60.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
