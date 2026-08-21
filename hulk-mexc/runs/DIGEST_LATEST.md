# Hulk DIGEST — 2026-08-21T21:16:50Z

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
| PYTHUSDT | IDLE | 1.19 | 4.51 | 1.11 | 0.09 | 5611901.99 | 4.15 | skipped_fast |
| XRPUSDT | IDLE | 1.14 | 3.73 | 1.89 | 0.11 | 128221136.67 | 0.72 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.35 | 0.06 | 515476.52 | 3.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 8.19 | 5.0 | 0.08 | 483048.43 | 21.9 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.14 | 0.56 | 0.1 | 642354.45 | 5.53 | skipped_fast |
| HBARUSDT | IDLE | 1.59 | 3.04 | 0.96 | 0.06 | 810485.12 | 2.58 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.83 | 0.63 | 0.06 | 366916.35 | 14.67 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.2 | 2.58 | 0.01 | 187178.26 | 3.15 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.16 | 0.16 | 153493.62 | 21.26 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.03 | 10271.93 | 21.48 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.12 | 3.19 | -0.06 | 82446.49 | 45.45 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.46 | 0.01 | 56207.43 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.04 | 0.11 | 60975.98 | 12.98 | skipped_fast |
| QAITUSDT | IDLE | 2.5 | 4.38 | 4.2 | -0.04 | 3753.25 | 151.45 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 179157.8 | 21.51 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.68 | 0.03 | 61219.3 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.17 | 1.07 | 0.03 | 53765.79 | 41.55 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 22.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
