# Hulk DIGEST — 2026-08-19T10:22:52Z

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
| XRPUSDT | IDLE | 0.55 | 1.01 | 0.54 | 0.01 | 10428108.78 | 1.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 1.93 | 1.8 | 0.01 | 180115.97 | 7.84 | skipped_fast |
| REDUSDT | IDLE | 0.85 | 3.42 | 2.53 | -0.14 | 145525.35 | 12.59 | skipped_fast |
| BIOUSDT | IDLE | 1.29 | 2.42 | 1.06 | 0.04 | 65008.09 | 7.96 | skipped_fast |
| CHIPUSDT | IDLE | 0.7 | 2.04 | 1.62 | -0.11 | 164660.23 | 3.92 | skipped_fast |
| KITEUSDT | IDLE | 1.19 | 2.19 | 1.33 | -0.0 | 64941.5 | 14.36 | skipped_fast |
| CCUSDT | IDLE | 0.49 | 0.91 | 0.41 | -0.01 | 215288.25 | 8.88 | skipped_fast |
| ZBCNUSDT | IDLE | 0.76 | 1.52 | 0.06 | 0.01 | 154560.75 | 13.83 | skipped_fast |
| WUSDT | IDLE | 0.88 | 1.66 | 0.68 | -0.01 | 102266.49 | 11.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.86 | 1.46 | -0.04 | 28901.3 | 51.27 | skipped_fast |
| EDELUSDT | IDLE | 1.24 | 2.31 | 1.19 | -0.03 | 59276.79 | 53.55 | skipped_fast |
| QAITUSDT | IDLE | 0.79 | 5.33 | 0.35 | -0.14 | 12213.35 | 65.65 | skipped_fast |
| RWAINCUSDT | IDLE | 0.78 | 1.49 | 0.53 | -0.01 | 10173.09 | 65.3 | skipped_fast |
| HBARUSDT | IDLE | 0.5 | 0.91 | 0.66 | 0.03 | 131976.84 | 1.48 | skipped_fast |
| TELUSDT | IDLE | 0.66 | 1.25 | 0.41 | 0.03 | 86978.63 | 13.76 | skipped_fast |
| QNTUSDT | IDLE | 0.78 | 1.42 | 1.0 | 0.01 | 38348.92 | 7.09 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.26 | -0.01 | 52512.79 | 17.51 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 1.66 | 0.0 | -0.01 | 1163.31 | 52.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
