# Hulk DIGEST — 2026-08-17T23:16:53Z

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
| XRPUSDT | IDLE | 0.3 | 0.56 | 0.32 | 0.01 | 12215483.42 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 6.26 | 4.16 | -0.01 | 335601.23 | 7.23 | skipped_fast |
| CCUSDT | IDLE | 1.2 | 2.14 | 1.69 | -0.06 | 252865.05 | 7.77 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 3.69 | 2.92 | -0.0 | 66354.05 | 39.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 2.07 | 1.59 | 0.01 | 221172.17 | 16.48 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.49 | 2.07 | 0.02 | 79802.79 | 4.06 | skipped_fast |
| TELUSDT | IDLE | 2.65 | 5.93 | 2.66 | -0.04 | 136321.17 | 43.04 | skipped_fast |
| QAITUSDT | IDLE | 1.97 | 3.68 | 1.79 | -0.05 | 1323.31 | 56.53 | skipped_fast |
| PYTHUSDT | IDLE | 0.87 | 1.56 | 1.2 | -0.0 | 144821.32 | 2.59 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 7.23 | 5.05 | 0.07 | 88622.59 | 48.1 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.11 | 1.12 | 0.0 | 57619.48 | 13.86 | skipped_fast |
| WUSDT | IDLE | 0.53 | 0.97 | 0.58 | -0.03 | 133855.71 | 10.86 | skipped_fast |
| KITEUSDT | IDLE | 0.57 | 1.03 | 0.79 | -0.01 | 61113.53 | 14.08 | skipped_fast |
| RWAINCUSDT | IDLE | 0.41 | 0.76 | 0.41 | -0.03 | 1106.04 | 58.58 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.64 | 1.51 | -0.0 | 35285.15 | 3.52 | skipped_fast |
| HBARUSDT | IDLE | 0.28 | 0.55 | 0.11 | 0.02 | 112479.91 | 1.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.62 | 1.24 | 0.0 | -0.01 | 771.14 | 22.49 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.17 | 0.01 | 49736.89 | 17.26 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
