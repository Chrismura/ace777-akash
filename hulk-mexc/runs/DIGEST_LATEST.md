# Hulk DIGEST — 2026-09-13T01:38:06Z

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
| XRPUSDT | IDLE | 0.27 | 0.5 | 0.32 | 0.0 | 14551935.95 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 0.19 | 0.35 | 0.21 | 0.0 | 196310356.83 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.15 | 0.28 | 0.13 | -0.0 | 317164443.68 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.32 | 2.74 | 1.45 | 0.07 | 426393.35 | 3.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.82 | 5.39 | 2.46 | 0.0 | 227261.22 | 10.7 | skipped_fast |
| EDELUSDT | IDLE | 2.05 | 5.27 | 1.86 | 0.08 | 168730.99 | 16.45 | skipped_fast |
| WUSDT | IDLE | 1.7 | 3.39 | 0.04 | 0.05 | 187263.68 | 11.73 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 15.37 | 13.08 | 0.33 | 92216.39 | 68.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.12 | 4.25 | 1.5 | 0.03 | 9655.03 | 21.91 | skipped_fast |
| CCUSDT | IDLE | 1.01 | 1.95 | 0.44 | -0.01 | 209861.1 | 8.16 | skipped_fast |
| REDUSDT | IDLE | 1.17 | 2.32 | 0.12 | 0.01 | 55591.97 | 9.82 | skipped_fast |
| CHIPUSDT | IDLE | 0.91 | 1.72 | 1.67 | -0.01 | 76956.62 | 16.78 | skipped_fast |
| KITEUSDT | IDLE | 0.95 | 1.72 | 1.23 | -0.02 | 62476.97 | 12.18 | skipped_fast |
| BIOUSDT | IDLE | 0.52 | 0.95 | 0.59 | 0.01 | 65642.24 | 15.74 | skipped_fast |
| TELUSDT | IDLE | 0.87 | 1.53 | 1.44 | -0.04 | 88549.06 | 24.42 | skipped_fast |
| HBARUSDT | IDLE | 0.36 | 0.7 | 0.07 | 0.0 | 122891.47 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 0.64 | 1.2 | 0.58 | 0.0 | 35223.65 | 7.81 | skipped_fast |
| FLUIDUSDT | IDLE | 0.74 | 1.34 | 0.91 | -0.0 | 436.08 | 21.14 | skipped_fast |
| RWAUSDT | IDLE | 0.16 | 0.3 | 0.07 | 0.0 | 53358.43 | 14.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.35 | 0.12 | -0.0 | 28313.37 | 15.28 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
