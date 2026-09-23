# Hulk DIGEST — 2026-09-23T08:07:44Z

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
| XRPUSDT | IDLE | 2.17 | 4.47 | 3.05 | 0.06 | 118708967.57 | 1.87 | skipped_fast |
| HBARUSDT | IDLE | 2.18 | 4.3 | 3.97 | 0.02 | 1786245.01 | 3.08 | skipped_fast |
| PYTHUSDT | IDLE | 0.72 | 3.18 | 2.78 | 0.04 | 1795434.29 | 4.56 | skipped_fast |
| ETHUSDT | IDLE | 1.1 | 1.93 | 1.76 | 0.0 | 415834694.25 | 0.18 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.46 | 1.35 | 0.01 | 871603171.76 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.29 | 4.03 | 3.73 | -0.06 | 402731.83 | 9.79 | skipped_fast |
| CHIPUSDT | IDLE | 3.04 | 5.37 | 4.67 | -0.07 | 208383.15 | 13.27 | skipped_fast |
| ZBCNUSDT | IDLE | 2.35 | 5.53 | 3.81 | 0.04 | 220772.57 | 20.34 | skipped_fast |
| WUSDT | IDLE | 1.47 | 2.62 | 2.11 | 0.03 | 314984.31 | 6.55 | skipped_fast |
| KITEUSDT | IDLE | 1.93 | 4.78 | 3.86 | 0.07 | 146344.36 | 11.11 | skipped_fast |
| BIOUSDT | IDLE | 1.67 | 2.92 | 2.84 | 0.03 | 112361.14 | 10.04 | skipped_fast |
| EDELUSDT | IDLE | 0.67 | 3.1 | 2.14 | -0.04 | 261171.11 | 23.09 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 2.07 | 0.92 | 0.01 | 59679.32 | 13.02 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 12.5 | 3.07 | 0.49 | 63718.12 | 93.81 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 2.57 | 1.69 | 0.11 | 240860.3 | 5.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.7 | 1.68 | 1.44 | 0.03 | 20978.56 | 123.82 | skipped_fast |
| FLUIDUSDT | IDLE | 1.02 | 1.78 | 1.75 | 0.01 | 2938.19 | 20.5 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 4.39 | 4.21 | 0.12 | 117961.35 | 133.19 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.87 | 0.65 | 0.01 | 53400.93 | 14.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.54 | 0.46 | 0.01 | 39721.61 | 29.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
