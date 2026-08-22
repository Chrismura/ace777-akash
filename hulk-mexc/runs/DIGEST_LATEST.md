# Hulk DIGEST — 2026-08-22T15:17:35Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.58 | 0.04 | 51470923.5 | 3.95 | skipped_fast |
| XRPUSDT | IDLE | 1.36 | 7.49 | 5.88 | 0.02 | 214963055.33 | 2.78 | skipped_fast |
| CCUSDT | IDLE | 1.32 | 5.65 | 2.8 | 0.11 | 800654.13 | 5.15 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 2.85 | 2.66 | -0.02 | 1172374.29 | 5.25 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.82 | -0.1 | 613326.44 | 6.83 | skipped_fast |
| KITEUSDT | IDLE | 2.82 | 6.37 | 3.06 | 0.02 | 85136.49 | 7.24 | skipped_fast |
| WUSDT | IDLE | 0.8 | 3.17 | 2.15 | -0.03 | 555980.28 | 18.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.33 | 3.49 | 2.09 | -0.07 | 325313.4 | 12.37 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.23 | -0.07 | 223060.53 | 3.32 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.62 | 5.14 | -0.05 | 150722.34 | 12.0 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 2.52 | 2.35 | -0.05 | 79097.42 | 34.27 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.45 | 0.03 | 46063.39 | 43.92 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9931.39 | 32.17 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.27 | -0.01 | 188402.73 | 7.91 | skipped_fast |
| TELUSDT | IDLE | 1.12 | 2.75 | 1.73 | -0.01 | 140209.14 | 42.62 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 22.5 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.23 | 0.57 | 0.02 | 57192.21 | 8.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
