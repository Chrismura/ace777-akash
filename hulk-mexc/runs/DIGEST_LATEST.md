# Hulk DIGEST — 2026-09-06T11:31:49Z

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
| ETHUSDT | IDLE | 0.65 | 1.21 | 0.54 | 0.02 | 230884541.18 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.63 | 1.19 | 0.48 | 0.01 | 25202915.85 | 2.11 | skipped_fast |
| BTCUSDT | IDLE | 0.28 | 0.54 | 0.16 | 0.0 | 403933003.51 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.82 | 7.32 | 3.82 | 0.05 | 412127.59 | 3.38 | skipped_fast |
| RWAINCUSDT | IDLE | 3.52 | 7.89 | 2.1 | 0.04 | 7867.88 | 46.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 2.16 | 0.31 | 0.03 | 440600.46 | 5.4 | skipped_fast |
| WUSDT | IDLE | 2.1 | 4.15 | 0.39 | 0.04 | 191966.71 | 10.63 | skipped_fast |
| RIZEUSDT | IDLE | 2.04 | 11.34 | 8.52 | 0.02 | 91423.55 | 64.75 | skipped_fast |
| REDUSDT | IDLE | 2.4 | 4.59 | 1.36 | 0.02 | 61113.5 | 11.62 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 2.07 | 1.16 | 0.01 | 317984.78 | 9.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 2.76 | 1.37 | 0.0 | 205498.31 | 22.71 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.63 | 1.56 | 0.0 | 69460.42 | 18.62 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.75 | 0.64 | 0.02 | 93681.08 | 3.6 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 1.84 | 1.32 | -0.03 | 64948.47 | 10.18 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.37 | 0.2 | 0.02 | 422540.29 | 1.23 | skipped_fast |
| QNTUSDT | IDLE | 1.43 | 2.56 | 2.03 | 0.03 | 40168.44 | 3.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.61 | 1.15 | 0.45 | 0.02 | 42511.17 | 2.68 | skipped_fast |
| TELUSDT | IDLE | 0.89 | 1.65 | 0.87 | 0.01 | 71733.71 | 52.49 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.0 | 0.85 | 0.0 | 53058.66 | 14.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 21.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
