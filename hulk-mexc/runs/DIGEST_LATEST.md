# Hulk DIGEST — 2026-09-23T09:17:39Z

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
| XRPUSDT | IDLE | 2.24 | 4.59 | 3.33 | 0.05 | 119418884.09 | 1.25 | skipped_fast |
| PYTHUSDT | IDLE | 0.67 | 3.18 | 1.3 | 0.07 | 1817863.97 | 4.49 | skipped_fast |
| ETHUSDT | IDLE | 1.24 | 2.22 | 1.69 | 0.0 | 403071665.35 | 0.11 | skipped_fast |
| BTCUSDT | IDLE | 1.03 | 1.84 | 1.51 | 0.0 | 853817408.34 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 2.02 | 4.03 | 3.36 | 0.02 | 1685417.0 | 1.03 | skipped_fast |
| CCUSDT | IDLE | 2.49 | 4.52 | 3.04 | -0.04 | 402478.37 | 7.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.75 | 5.08 | 2.86 | -0.03 | 201696.29 | 21.83 | skipped_fast |
| ZBCNUSDT | IDLE | 2.04 | 4.8 | 3.38 | 0.04 | 217069.74 | 22.62 | skipped_fast |
| WUSDT | IDLE | 1.17 | 2.32 | 0.18 | 0.05 | 322004.67 | 10.47 | skipped_fast |
| BIOUSDT | IDLE | 1.76 | 3.2 | 2.15 | 0.04 | 116751.7 | 10.01 | skipped_fast |
| KITEUSDT | IDLE | 1.52 | 2.95 | 2.11 | 0.05 | 133507.84 | 10.37 | skipped_fast |
| EDELUSDT | IDLE | 0.65 | 3.1 | 1.49 | -0.05 | 255114.96 | 3.28 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.76 | 0.07 | 0.04 | 60408.98 | 13.44 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 2.01 | 1.91 | 0.03 | 21566.13 | 16.26 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 12.5 | 2.75 | 0.5 | 63836.06 | 96.59 | skipped_fast |
| QNTUSDT | IDLE | 0.8 | 2.57 | 0.42 | 0.12 | 241875.57 | 1.32 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 5.65 | 3.12 | 0.14 | 124617.73 | 65.57 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 1.95 | 1.91 | 0.0 | 2562.84 | 22.42 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.02 | 0.79 | 0.01 | 53822.24 | 7.24 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.55 | 0.33 | 0.01 | 40267.63 | 15.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
