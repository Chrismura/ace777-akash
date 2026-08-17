# Hulk DIGEST — 2026-08-17T12:10:36Z

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
| XRPUSDT | IDLE | 0.55 | 1.0 | 0.64 | -0.0 | 10787520.57 | 1.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.59 | 11.83 | 5.49 | 0.05 | 362605.32 | 12.89 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.63 | 27.31 | 7.47 | 0.31 | 72372.85 | 50.98 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 1.96 | 1.91 | -0.03 | 255392.36 | 1.06 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 4.18 | 0.25 | 0.05 | 58382.31 | 25.13 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 2.31 | 1.53 | 0.01 | 156652.82 | 10.12 | skipped_fast |
| PYTHUSDT | IDLE | 0.93 | 1.64 | 1.42 | -0.01 | 157447.78 | 2.57 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.69 | 1.85 | -0.05 | 55089.75 | 16.86 | skipped_fast |
| WUSDT | IDLE | 0.72 | 1.34 | 0.7 | -0.03 | 181197.86 | 11.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.47 | 2.79 | 1.02 | -0.02 | 2236.21 | 11.43 | skipped_fast |
| KITEUSDT | IDLE | 1.15 | 2.17 | 0.91 | -0.01 | 52938.42 | 10.72 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 1.67 | 1.32 | -0.0 | 69830.5 | 4.06 | skipped_fast |
| QAITUSDT | IDLE | 1.44 | 2.63 | 1.68 | -0.01 | 1719.21 | 61.12 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 3.6 | 0.68 | 0.01 | 97923.11 | 54.83 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.92 | 0.66 | 0.01 | 119699.31 | 1.52 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.9 | 0.75 | -0.03 | 32417.88 | 1.79 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.05 | 1.04 | -0.01 | 772.36 | 19.57 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.26 | 0.01 | 49352.86 | 34.69 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
