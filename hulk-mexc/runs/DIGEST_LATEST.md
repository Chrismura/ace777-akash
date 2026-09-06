# Hulk DIGEST — 2026-09-06T19:31:50Z

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
| ETHUSDT | IDLE | 0.76 | 1.48 | 0.32 | 0.0 | 249216404.47 | 1.28 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.35 | 0.42 | -0.01 | 24347939.37 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.96 | 0.15 | -0.0 | 352546617.21 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.53 | 7.14 | 3.4 | 0.05 | 372433.9 | 10.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.64 | 3.07 | 1.41 | -0.01 | 538621.06 | 1.83 | skipped_fast |
| CHIPUSDT | IDLE | 1.9 | 3.93 | 2.47 | -0.03 | 417606.59 | 1.75 | skipped_fast |
| RIZEUSDT | IDLE | 1.93 | 13.16 | 7.6 | -0.21 | 68760.44 | 32.84 | skipped_fast |
| RWAINCUSDT | IDLE | 2.33 | 4.88 | 4.0 | 0.05 | 6294.85 | 10.43 | skipped_fast |
| BIOUSDT | IDLE | 1.95 | 3.71 | 1.29 | -0.01 | 91149.23 | 7.24 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.63 | 0.63 | -0.0 | 314254.23 | 5.47 | skipped_fast |
| EDELUSDT | IDLE | 1.87 | 3.5 | 1.59 | -0.01 | 57659.22 | 38.1 | skipped_fast |
| ZBCNUSDT | IDLE | 0.95 | 1.66 | 1.57 | 0.01 | 168662.44 | 12.42 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.38 | 1.02 | -0.01 | 413084.9 | 1.24 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 2.07 | 0.35 | 0.01 | 66449.4 | 11.73 | skipped_fast |
| KITEUSDT | IDLE | 0.8 | 1.43 | 1.1 | 0.0 | 59546.14 | 12.67 | skipped_fast |
| TELUSDT | IDLE | 1.16 | 2.3 | 0.17 | 0.0 | 67038.22 | 51.95 | skipped_fast |
| QNTUSDT | IDLE | 0.91 | 1.76 | 0.35 | 0.01 | 33996.17 | 7.59 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.08 | 0.57 | -0.02 | 53846.02 | 14.37 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.2 | 0.02 | 41552.12 | 4.03 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.63 | 0.63 | 0.02 | 194.56 | 22.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
