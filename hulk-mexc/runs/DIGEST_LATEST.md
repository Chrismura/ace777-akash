# Hulk DIGEST — 2026-08-21T22:50:37Z

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
| PYTHUSDT | IDLE | 1.35 | 5.17 | 0.1 | 0.11 | 5888739.34 | 4.09 | skipped_fast |
| XRPUSDT | IDLE | 1.66 | 6.41 | 0.39 | 0.15 | 136009474.98 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.44 | 0.35 | 0.14 | 659944.9 | 8.83 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 4.73 | 0.33 | 0.08 | 875710.29 | 2.52 | skipped_fast |
| ZBCNUSDT | IDLE | 1.93 | 8.3 | 0.01 | 0.14 | 508458.66 | 6.76 | skipped_fast |
| WUSDT | IDLE | 2.62 | 6.46 | 0.08 | 0.09 | 371542.39 | 9.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.11 | 0.05 | 534795.44 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.26 | 0.03 | 188132.76 | 3.12 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.53 | 0.17 | 157189.09 | 13.0 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.03 | 82543.54 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10244.46 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 6.45 | 0.67 | 0.06 | 186888.04 | 31.04 | skipped_fast |
| QAITUSDT | IDLE | 2.34 | 4.38 | 1.94 | -0.02 | 3835.98 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.16 | 0.11 | 61331.21 | 12.0 | skipped_fast |
| QNTUSDT | IDLE | 2.16 | 4.32 | 0.02 | 0.06 | 87305.27 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 2.05 | 0.06 | 56403.66 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.92 | 1.83 | 0.08 | 0.04 | 54124.34 | 8.19 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
