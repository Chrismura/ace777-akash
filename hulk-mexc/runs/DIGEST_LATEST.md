# Hulk DIGEST — 2026-08-17T16:11:50Z

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
| XRPUSDT | IDLE | 0.59 | 1.13 | 0.37 | 0.0 | 12897421.78 | 1.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.76 | 26.76 | 15.44 | 0.2 | 70959.76 | 43.92 | skipped_fast |
| CHIPUSDT | IDLE | 2.08 | 8.94 | 8.17 | 0.0 | 333647.44 | 3.45 | skipped_fast |
| EDELUSDT | IDLE | 2.86 | 5.45 | 3.69 | 0.02 | 65067.41 | 12.78 | skipped_fast |
| CCUSDT | IDLE | 2.01 | 3.57 | 3.02 | -0.04 | 244939.03 | 6.51 | skipped_fast |
| ZBCNUSDT | IDLE | 2.04 | 3.95 | 0.91 | 0.0 | 172532.44 | 13.33 | skipped_fast |
| REDUSDT | IDLE | 2.09 | 3.97 | 1.37 | -0.03 | 56931.16 | 18.9 | skipped_fast |
| TELUSDT | IDLE | 2.77 | 4.86 | 4.5 | -0.03 | 105427.58 | 35.65 | skipped_fast |
| PYTHUSDT | IDLE | 0.63 | 1.16 | 0.61 | -0.01 | 145345.07 | 2.56 | skipped_fast |
| WUSDT | IDLE | 0.67 | 1.21 | 0.89 | -0.03 | 156776.1 | 17.95 | skipped_fast |
| KITEUSDT | IDLE | 0.85 | 1.48 | 1.46 | -0.02 | 59244.05 | 14.08 | skipped_fast |
| BIOUSDT | IDLE | 0.64 | 1.22 | 0.36 | -0.0 | 72896.96 | 4.05 | skipped_fast |
| QNTUSDT | IDLE | 1.98 | 3.77 | 1.26 | -0.01 | 37028.85 | 3.51 | skipped_fast |
| RWAINCUSDT | IDLE | 1.1 | 1.92 | 1.88 | -0.0 | 1860.75 | 81.35 | skipped_fast |
| FLUIDUSDT | IDLE | 1.8 | 3.15 | 3.05 | -0.02 | 859.84 | 21.62 | skipped_fast |
| QAITUSDT | IDLE | 0.78 | 1.39 | 1.18 | -0.01 | 737.18 | 61.3 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.48 | 0.41 | 0.01 | 125588.23 | 1.51 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.96 | 0.17 | 0.01 | 49753.67 | 25.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
