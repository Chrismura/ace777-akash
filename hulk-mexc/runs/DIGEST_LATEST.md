# Hulk DIGEST — 2026-08-21T21:48:12Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.6 | 0.09 | 5665305.98 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.76 | 0.11 | 129944190.45 | 2.14 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.64 | 0.04 | 527411.1 | 9.28 | skipped_fast |
| HBARUSDT | IDLE | 1.93 | 4.08 | 0.09 | 0.08 | 821283.99 | 2.54 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 3.76 | 0.0 | 0.1 | 647334.86 | 10.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.94 | 8.19 | 3.43 | 0.1 | 492584.69 | 63.1 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.83 | 0.06 | 0.07 | 368824.83 | 10.41 | skipped_fast |
| BIOUSDT | IDLE | 2.39 | 5.2 | 1.44 | 0.03 | 187674.81 | 6.23 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.23 | 0.17 | 154181.22 | 18.02 | skipped_fast |
| EDELUSDT | IDLE | 1.98 | 4.12 | 1.65 | -0.05 | 83634.02 | 33.28 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.01 | 0.04 | 55828.44 | 47.31 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.33 | 0.11 | 61189.84 | 13.81 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 4.81 | 1.04 | 0.02 | 183688.96 | 68.87 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.65 | 0.57 | 0.04 | 62632.17 | 7.73 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.17 | 0.25 | 0.03 | 53902.07 | 24.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
