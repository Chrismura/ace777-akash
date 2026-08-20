# Hulk DIGEST — 2026-08-20T01:13:01Z

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
| XRPUSDT | IDLE | 1.96 | 6.45 | 2.4 | 0.11 | 43511957.34 | 0.9 | skipped_fast |
| PYTHUSDT | IDLE | 1.49 | 4.44 | 1.7 | 0.1 | 314637.87 | 2.37 | skipped_fast |
| CCUSDT | IDLE | 1.21 | 4.08 | 1.63 | 0.1 | 361152.29 | 7.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.75 | 7.77 | 2.27 | 0.14 | 216623.48 | 23.92 | skipped_fast |
| WUSDT | IDLE | 1.64 | 3.85 | 1.38 | 0.07 | 259722.69 | 11.57 | skipped_fast |
| RIZEUSDT | IDLE | 2.29 | 6.87 | 0.57 | 0.05 | 49701.06 | 46.43 | skipped_fast |
| EDELUSDT | IDLE | 1.51 | 8.62 | 0.77 | 0.21 | 83297.5 | 11.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.13 | 3.54 | 1.82 | 0.05 | 193576.13 | 3.56 | skipped_fast |
| HBARUSDT | IDLE | 1.77 | 3.35 | 1.27 | 0.05 | 344677.36 | 1.41 | skipped_fast |
| REDUSDT | IDLE | 1.36 | 6.19 | 1.58 | 0.08 | 98731.27 | 13.25 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 4.57 | 0.98 | 0.15 | 156026.87 | 7.05 | skipped_fast |
| KITEUSDT | IDLE | 1.14 | 2.23 | 1.08 | 0.05 | 58295.04 | 13.49 | skipped_fast |
| FLUIDUSDT | IDLE | 2.23 | 6.0 | 3.65 | 0.06 | 3459.89 | 18.37 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 2.88 | 0.22 | 0.06 | 16954.71 | 56.34 | skipped_fast |
| TELUSDT | IDLE | 1.28 | 6.05 | 2.0 | 0.11 | 187782.19 | 61.84 | skipped_fast |
| QAITUSDT | IDLE | 0.74 | 2.03 | 0.5 | 0.03 | 10647.2 | 61.42 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 2.01 | 0.64 | 0.06 | 38892.34 | 6.78 | skipped_fast |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.26 | 0.01 | 53895.69 | 17.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
