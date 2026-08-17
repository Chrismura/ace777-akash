# Hulk DIGEST — 2026-08-17T07:07:22Z

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
| XRPUSDT | IDLE | 0.5 | 0.96 | 0.22 | 0.0 | 9482713.71 | 1.0 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.32 | 14.28 | 1.03 | 0.16 | 326524.21 | 18.79 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 11.66 | 2.28 | 0.13 | 47093.68 | 44.36 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 3.28 | 0.08 | 0.01 | 63482.79 | 4.02 | skipped_fast |
| REDUSDT | IDLE | 1.53 | 2.71 | 2.37 | -0.05 | 58369.81 | 15.41 | skipped_fast |
| CCUSDT | IDLE | 0.68 | 1.34 | 0.11 | -0.01 | 250355.01 | 6.26 | skipped_fast |
| PYTHUSDT | IDLE | 0.98 | 1.89 | 0.48 | -0.0 | 162618.23 | 2.56 | skipped_fast |
| WUSDT | IDLE | 0.82 | 1.43 | 1.39 | 0.02 | 188677.27 | 13.01 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 2.38 | 1.87 | -0.0 | 53681.93 | 17.05 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 2.76 | 1.79 | 0.03 | 55256.14 | 39.04 | skipped_fast |
| ZBCNUSDT | IDLE | 0.5 | 0.97 | 0.21 | 0.01 | 191867.94 | 15.85 | skipped_fast |
| QAITUSDT | IDLE | 1.08 | 2.41 | 2.0 | -0.03 | 2151.91 | 61.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.58 | 1.02 | 0.9 | -0.01 | 2282.92 | 79.55 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 1.65 | 1.22 | -0.01 | 87922.45 | 34.23 | skipped_fast |
| QNTUSDT | IDLE | 0.81 | 1.53 | 0.62 | -0.02 | 31930.67 | 7.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.94 | 1.69 | 1.27 | 0.01 | 802.22 | 20.88 | skipped_fast |
| HBARUSDT | IDLE | 0.33 | 0.66 | 0.03 | 0.0 | 91255.22 | 1.53 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.87 | 0.0 | 0.01 | 49509.54 | 26.01 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
