# Hulk DIGEST — 2026-08-22T11:47:02Z

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
| PYTHUSDT | IDLE | 2.15 | 9.66 | 6.53 | 0.01 | 51615152.8 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.53 | 0.08 | 216642360.86 | 3.36 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.46 | 0.14 | 787394.76 | 9.41 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.27 | 0.02 | 1256049.8 | 5.16 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.53 | 0.02 | 582744.36 | 14.79 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 5.93 | 4.19 | -0.03 | 387990.41 | 19.04 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.62 | -0.1 | 622768.91 | 6.7 | skipped_fast |
| KITEUSDT | IDLE | 2.51 | 6.08 | 0.0 | 0.05 | 80599.59 | 10.57 | skipped_fast |
| EDELUSDT | IDLE | 2.76 | 4.93 | 3.93 | -0.03 | 79168.86 | 45.56 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 6.64 | 1.89 | -0.03 | 242764.05 | 3.21 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.61 | -0.03 | 167304.68 | 42.85 | skipped_fast |
| QAITUSDT | IDLE | 2.16 | 4.16 | 1.12 | 0.01 | 2456.68 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.27 | 0.04 | 154534.2 | 14.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 76.09 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.76 | 0.0 | 188335.91 | 7.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.77 | -0.03 | 48671.08 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 21.53 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57698.12 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
