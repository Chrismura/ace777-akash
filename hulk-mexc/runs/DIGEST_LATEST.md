# Hulk DIGEST — 2026-09-17T08:16:05Z

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
| ETHUSDT | IDLE | 0.65 | 1.2 | 0.64 | 0.02 | 379997532.94 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.61 | 1.11 | 0.68 | 0.01 | 55348665.33 | 3.08 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.64 | 0.35 | 0.01 | 486469174.59 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.14 | 3.9 | 2.49 | 0.02 | 523914.59 | 5.58 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 3.46 | 0.02 | 0.1 | 605213.09 | 8.97 | skipped_fast |
| EDELUSDT | IDLE | 2.43 | 10.04 | 4.35 | -0.04 | 213474.86 | 55.64 | skipped_fast |
| ZBCNUSDT | IDLE | 2.32 | 4.35 | 1.9 | 0.03 | 168991.59 | 6.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 4.47 | 0.45 | 0.02 | 102543.72 | 8.01 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.74 | 2.22 | 0.08 | 67120.47 | 12.15 | skipped_fast |
| WUSDT | IDLE | 0.84 | 1.61 | 0.55 | 0.04 | 224346.99 | 13.0 | skipped_fast |
| RIZEUSDT | IDLE | 0.99 | 10.57 | 5.22 | -0.08 | 62291.26 | 66.16 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.89 | 0.75 | 0.0 | 61671.79 | 16.79 | skipped_fast |
| BIOUSDT | IDLE | 0.67 | 1.24 | 0.71 | 0.02 | 71186.48 | 7.92 | skipped_fast |
| HBARUSDT | IDLE | 0.67 | 1.21 | 0.86 | -0.0 | 318948.24 | 1.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.71 | 1.34 | 0.52 | -0.0 | 13942.65 | 23.22 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 1.68 | 1.44 | -0.03 | 113165.84 | 34.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.62 | 1.22 | 0.17 | 0.01 | 36974.1 | 5.61 | skipped_fast |
| QNTUSDT | IDLE | 0.43 | 0.83 | 0.26 | 0.02 | 34381.08 | 3.3 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.83 | 0.22 | 0.02 | 56494.75 | 29.9 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1561.53 | 22.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
