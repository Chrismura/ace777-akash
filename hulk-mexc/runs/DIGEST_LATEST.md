# Hulk DIGEST — 2026-08-16T09:19:03Z

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
| XRPUSDT | IDLE | 0.17 | 0.33 | 0.05 | 0.0 | 4555634.01 | 1.0 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.63 | 2.36 | 0.0 | 308740.16 | 2.09 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 7.86 | 1.92 | 0.17 | 173568.05 | 17.77 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.7 | 2.25 | -0.02 | 67584.58 | 67.52 | skipped_fast |
| ZBCNUSDT | IDLE | 0.85 | 1.55 | 0.98 | -0.01 | 212525.34 | 3.2 | skipped_fast |
| WUSDT | IDLE | 0.92 | 1.73 | 0.78 | -0.01 | 117477.09 | 14.36 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.68 | 0.56 | -0.0 | 67041.34 | 4.05 | skipped_fast |
| PYTHUSDT | IDLE | 0.52 | 0.97 | 0.41 | -0.02 | 86606.23 | 2.54 | skipped_fast |
| KITEUSDT | IDLE | 0.68 | 1.29 | 0.53 | -0.02 | 58814.24 | 11.65 | skipped_fast |
| REDUSDT | IDLE | 0.38 | 3.27 | 2.42 | 0.02 | 91271.93 | 27.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 2.06 | 1.17 | -0.03 | 39032.61 | 64.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 3.31 | 0.88 | 0.1 | 8475.94 | 83.68 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.65 | 1.36 | -0.03 | 94036.68 | 27.47 | skipped_fast |
| QAITUSDT | IDLE | 0.3 | 0.53 | 0.53 | -0.03 | 922.1 | 59.31 | skipped_fast |
| QNTUSDT | IDLE | 0.75 | 1.4 | 0.62 | -0.01 | 33025.89 | 1.74 | skipped_fast |
| HBARUSDT | IDLE | 0.25 | 0.45 | 0.38 | -0.01 | 77234.37 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.53 | 0.09 | -0.0 | 52974.54 | 17.48 | skipped_fast |
| FLUIDUSDT | IDLE | 0.2 | 0.41 | 0.0 | 0.05 | 168.03 | 21.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
