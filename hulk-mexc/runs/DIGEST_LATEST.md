# Hulk DIGEST — 2026-08-21T21:13:25Z

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
| PYTHUSDT | IDLE | 1.2 | 4.51 | 1.4 | 0.09 | 5601127.11 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 2.04 | 0.11 | 128180062.88 | 4.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.38 | 0.07 | 515340.09 | 3.12 | skipped_fast |
| ZBCNUSDT | IDLE | 1.99 | 8.19 | 4.93 | 0.09 | 482189.06 | 31.05 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 3.14 | 0.42 | 0.1 | 642215.06 | 10.14 | skipped_fast |
| HBARUSDT | IDLE | 1.6 | 3.04 | 1.07 | 0.06 | 809129.76 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.97 | 3.83 | 0.74 | 0.07 | 367785.83 | 13.62 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.2 | 2.49 | 0.01 | 187930.08 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.2 | 0.16 | 153529.99 | 26.97 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.02 | 10271.93 | 10.72 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.12 | 3.19 | -0.06 | 82446.46 | 34.03 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.42 | 0.01 | 56220.62 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 1.96 | 0.11 | 61154.64 | 12.04 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.32 | 0.01 | 180150.11 | 48.27 | skipped_fast |
| QAITUSDT | IDLE | 1.75 | 3.21 | 1.87 | -0.02 | 2705.72 | 157.29 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.68 | 0.04 | 61001.05 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.17 | 0.74 | 0.03 | 53723.23 | 16.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 20.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
