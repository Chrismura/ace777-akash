# Hulk DIGEST — 2026-08-18T22:45:01Z

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
| XRPUSDT | IDLE | 0.23 | 0.43 | 0.25 | 0.0 | 10822139.85 | 1.0 | skipped_fast |
| RWAINCUSDT | IDLE | 3.51 | 7.03 | 4.83 | -0.01 | 10175.65 | 29.61 | skipped_fast |
| CHIPUSDT | IDLE | 2.25 | 6.74 | 5.74 | -0.06 | 201895.94 | 3.83 | skipped_fast |
| PYTHUSDT | IDLE | 1.5 | 2.69 | 2.13 | 0.0 | 172568.4 | 2.6 | skipped_fast |
| RIZEUSDT | IDLE | 2.41 | 4.65 | 3.29 | -0.08 | 32288.64 | 50.25 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.44 | 1.4 | -0.0 | 245602.07 | 6.67 | skipped_fast |
| REDUSDT | IDLE | 0.73 | 5.38 | 3.44 | 0.07 | 153110.06 | 12.85 | skipped_fast |
| ZBCNUSDT | IDLE | 0.5 | 0.96 | 0.29 | -0.0 | 161093.54 | 14.69 | skipped_fast |
| WUSDT | IDLE | 0.55 | 0.96 | 0.91 | -0.03 | 133457.42 | 13.67 | skipped_fast |
| EDELUSDT | IDLE | 0.86 | 2.57 | 1.32 | -0.03 | 74422.23 | 40.13 | skipped_fast |
| BIOUSDT | IDLE | 0.54 | 0.94 | 0.93 | -0.01 | 64529.91 | 4.08 | skipped_fast |
| KITEUSDT | IDLE | 0.22 | 0.4 | 0.26 | -0.01 | 63491.43 | 15.26 | skipped_fast |
| FLUIDUSDT | IDLE | 1.72 | 3.05 | 2.58 | -0.02 | 212.15 | 22.01 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 2.02 | 0.01 | 0.02 | 117021.55 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 0.22 | 3.0 | 1.73 | -0.18 | 18652.2 | 51.93 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 1.89 | 0.48 | 0.04 | 91046.2 | 27.59 | skipped_fast |
| QNTUSDT | IDLE | 0.54 | 0.95 | 0.83 | -0.02 | 34438.95 | 3.58 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.26 | -0.01 | 51149.02 | 17.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
