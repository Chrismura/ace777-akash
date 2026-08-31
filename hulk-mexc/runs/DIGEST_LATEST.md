# Hulk DIGEST — 2026-08-31T02:08:20Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 2.85 | 5.09 | 4.03 | -0.03 | 33616187.16 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 2.38 | 4.32 | 2.97 | -0.02 | 376265590.81 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 1.27 | 2.34 | 1.32 | -0.0 | 378164273.59 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.97 | 5.84 | 4.7 | -0.02 | 489687.72 | 2.14 | skipped_fast |
| CHIPUSDT | IDLE | 2.08 | 6.38 | 3.87 | -0.04 | 524505.98 | 2.61 | skipped_fast |
| WUSDT | IDLE | 3.39 | 6.33 | 3.86 | -0.0 | 238807.92 | 12.11 | skipped_fast |
| BIOUSDT | IDLE | 3.4 | 6.22 | 4.14 | -0.05 | 88754.61 | 3.82 | skipped_fast |
| CCUSDT | IDLE | 2.33 | 4.26 | 2.68 | -0.02 | 229720.09 | 7.76 | skipped_fast |
| KITEUSDT | IDLE | 2.67 | 7.34 | 4.31 | -0.07 | 91228.04 | 11.71 | skipped_fast |
| EDELUSDT | IDLE | 2.9 | 6.32 | 4.34 | 0.06 | 82181.03 | 41.93 | skipped_fast |
| ZBCNUSDT | IDLE | 1.94 | 4.62 | 3.88 | -0.06 | 218523.01 | 21.2 | skipped_fast |
| REDUSDT | IDLE | 2.41 | 4.49 | 2.22 | -0.01 | 62869.37 | 22.18 | skipped_fast |
| RIZEUSDT | IDLE | 2.6 | 4.92 | 1.85 | -0.03 | 40349.33 | 50.64 | skipped_fast |
| FLUIDUSDT | IDLE | 3.47 | 6.19 | 4.98 | -0.02 | 3849.88 | 18.7 | skipped_fast |
| TELUSDT | IDLE | 2.75 | 4.91 | 3.99 | -0.0 | 83009.88 | 41.56 | skipped_fast |
| HBARUSDT | IDLE | 1.79 | 3.19 | 2.6 | -0.03 | 214752.18 | 1.36 | skipped_fast |
| RWAINCUSDT | IDLE | 1.46 | 2.55 | 2.49 | 0.0 | 2191.44 | 90.34 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 2.79 | 1.86 | -0.03 | 37767.74 | 3.33 | skipped_fast |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
