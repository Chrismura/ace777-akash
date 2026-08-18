# Hulk DIGEST — 2026-08-18T16:42:02Z

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
| XRPUSDT | IDLE | 0.55 | 1.05 | 0.38 | -0.0 | 11086119.71 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 3.32 | 8.95 | 4.98 | -0.06 | 243078.77 | 7.32 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 27.25 | 18.47 | -0.19 | 18264.04 | 64.05 | skipped_fast |
| REDUSDT | IDLE | 1.63 | 11.94 | 9.74 | 0.08 | 125831.04 | 23.94 | skipped_fast |
| RIZEUSDT | IDLE | 2.88 | 5.45 | 4.2 | -0.02 | 37498.62 | 45.29 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 2.35 | 0.15 | -0.01 | 191616.66 | 5.16 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.46 | 1.19 | -0.0 | 245843.56 | 8.78 | skipped_fast |
| ZBCNUSDT | IDLE | 1.05 | 1.89 | 1.4 | -0.0 | 197825.67 | 21.64 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 4.34 | 2.08 | -0.04 | 75082.74 | 26.53 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.72 | 0.2 | 0.01 | 74775.5 | 4.02 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 2.17 | 0.25 | -0.0 | 64707.08 | 11.95 | skipped_fast |
| WUSDT | IDLE | 0.51 | 0.93 | 0.62 | -0.03 | 138241.35 | 12.32 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 4.27 | 1.78 | 0.02 | 117027.33 | 48.7 | skipped_fast |
| RWAINCUSDT | IDLE | 0.99 | 2.1 | 0.53 | -0.02 | 5115.69 | 17.74 | skipped_fast |
| HBARUSDT | IDLE | 0.53 | 0.96 | 0.69 | 0.0 | 117168.21 | 1.52 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 1.75 | 0.35 | -0.01 | 35147.76 | 5.33 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.96 | 0.52 | -0.01 | 50579.7 | 17.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.35 | 0.0 | 0.0 | 167.93 | 22.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
