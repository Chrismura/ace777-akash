# Hulk DIGEST — 2026-10-25T23:10:29Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.72 | 1.29 | 0.95 | -0.0 | 81136890.8 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.6 | 1.11 | 0.56 | 0.0 | 14368476.44 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.75 | 0.53 | -0.0 | 146366776.96 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.7 | 3.08 | -0.03 | 602542.8 | 18.55 | skipped_fast |
| PYTHUSDT | IDLE | 1.42 | 3.19 | 0.99 | 0.07 | 630016.56 | 17.29 | skipped_fast |
| QNTUSDT | IDLE | 2.15 | 5.96 | 4.16 | 0.08 | 636893.91 | 1.04 | skipped_fast |
| CHIPUSDT | IDLE | 2.96 | 5.26 | 4.44 | -0.02 | 92307.67 | 18.1 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 5.03 | 1.03 | 0.06 | 318939.39 | 25.1 | skipped_fast |
| RIZEUSDT | IDLE | 3.31 | 6.05 | 3.83 | 0.0 | 33503.42 | 67.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.57 | 2.84 | 2.27 | 0.03 | 180785.74 | 21.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.88 | 3.3 | 3.08 | -0.04 | 63365.18 | 5.65 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.5 | 1.47 | 0.0 | 200318.94 | 8.88 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 2.03 | 1.37 | -0.02 | 59865.2 | 4.49 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 1.81 | 1.38 | -0.04 | 58529.28 | 15.16 | skipped_fast |
| KITEUSDT | IDLE | 0.71 | 1.3 | 0.82 | -0.02 | 53258.2 | 9.78 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.82 | 0.47 | 0.0 | 155188.73 | 6.43 | skipped_fast |
| FLUIDUSDT | IDLE | 0.86 | 3.96 | 3.81 | 0.0 | 19077.39 | 21.19 | skipped_fast |
| RWAUSDT | IDLE | 0.29 | 0.56 | 0.16 | 0.0 | 51725.73 | 7.96 | skipped_fast |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
