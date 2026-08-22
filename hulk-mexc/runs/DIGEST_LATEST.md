# Hulk DIGEST — 2026-08-22T11:06:46Z

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
| PYTHUSDT | IDLE | 2.19 | 9.66 | 7.77 | 0.0 | 51658100.56 | 12.42 | skipped_fast |
| XRPUSDT | IDLE | 2.33 | 14.26 | 8.32 | 0.07 | 218229171.15 | 6.7 | skipped_fast |
| CCUSDT | IDLE | 2.05 | 10.24 | 7.64 | 0.11 | 816760.37 | 6.06 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.35 | 0.0 | 1252033.08 | 3.88 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.56 | 0.01 | 595554.2 | 12.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 5.08 | 4.33 | -0.04 | 425072.95 | 27.82 | skipped_fast |
| CHIPUSDT | IDLE | 0.73 | 4.16 | 1.95 | -0.1 | 646308.59 | 3.37 | skipped_fast |
| EDELUSDT | IDLE | 2.76 | 4.93 | 3.93 | -0.03 | 78818.01 | 34.03 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.64 | 3.18 | -0.05 | 240655.85 | 12.99 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 4.3 | 2.1 | 0.03 | 73611.47 | 11.85 | skipped_fast |
| QAITUSDT | IDLE | 2.29 | 4.16 | 2.83 | -0.0 | 2498.14 | 35.86 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.56 | -0.04 | 169181.44 | 48.19 | skipped_fast |
| REDUSDT | IDLE | 0.48 | 6.02 | 4.25 | 0.03 | 154371.61 | 20.64 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.29 | 2.24 | 0.0 | 11326.93 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.47 | 1.87 | -0.01 | 189142.87 | 12.47 | skipped_fast |
| RIZEUSDT | IDLE | 0.68 | 2.89 | 1.36 | -0.0 | 49216.92 | 46.66 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.31 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57533.61 | 24.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
