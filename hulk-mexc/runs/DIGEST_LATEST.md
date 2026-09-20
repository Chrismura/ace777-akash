# Hulk DIGEST — 2026-09-20T09:01:34Z

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
| XRPUSDT | IDLE | 0.46 | 0.84 | 0.58 | -0.03 | 53173820.69 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 0.4 | 0.72 | 0.51 | -0.03 | 247233917.74 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.31 | 0.56 | 0.45 | -0.01 | 500553634.88 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.26 | 5.83 | 4.63 | -0.0 | 490578.19 | 6.44 | skipped_fast |
| PYTHUSDT | IDLE | 1.24 | 2.18 | 1.95 | -0.04 | 677848.37 | 6.9 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.0 | 1.81 | 0.02 | 776837.04 | 1.23 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 2.65 | 2.39 | -0.06 | 343718.64 | 9.67 | skipped_fast |
| REDUSDT | IDLE | 1.97 | 3.68 | 1.75 | 0.0 | 79864.21 | 14.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.27 | 3.11 | 2.07 | -0.08 | 102162.1 | 16.81 | skipped_fast |
| EDELUSDT | IDLE | 1.3 | 4.04 | 1.82 | -0.04 | 70025.99 | 10.21 | skipped_fast |
| BIOUSDT | IDLE | 1.17 | 2.12 | 1.5 | -0.01 | 88028.76 | 3.71 | skipped_fast |
| ZBCNUSDT | IDLE | 0.86 | 2.85 | 2.69 | 0.03 | 225883.3 | 61.82 | skipped_fast |
| KITEUSDT | IDLE | 0.85 | 1.55 | 1.06 | -0.03 | 73896.08 | 13.22 | skipped_fast |
| RWAINCUSDT | IDLE | 0.81 | 1.85 | 0.94 | -0.04 | 10046.68 | 17.83 | skipped_fast |
| RIZEUSDT | IDLE | 0.73 | 2.62 | 2.16 | -0.07 | 35466.64 | 97.77 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 2.0 | 1.01 | -0.07 | 100183.18 | 34.12 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.65 | 1.36 | -0.0 | 57443.27 | 6.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 1.32 | 1.07 | -0.02 | 5954.73 | 21.88 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.75 | 0.59 | -0.01 | 33134.83 | 6.65 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.67 | 0.3 | -0.01 | 52102.03 | 29.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
