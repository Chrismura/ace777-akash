# Hulk DIGEST — 2026-09-27T12:08:19Z

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
| WUSDT | IDLE | 1.76 | 10.35 | 8.84 | 0.13 | 3286249.85 | 17.23 | skipped_fast |
| PYTHUSDT | IDLE | 1.5 | 6.09 | 1.23 | 0.12 | 2097733.62 | 6.85 | skipped_fast |
| QNTUSDT | IDLE | 0.76 | 15.05 | 10.91 | 0.56 | 5593279.57 | 12.96 | skipped_fast |
| XRPUSDT | IDLE | 1.01 | 2.0 | 0.13 | -0.0 | 41049726.6 | 1.3 | skipped_fast |
| ETHUSDT | IDLE | 0.43 | 0.79 | 0.48 | 0.01 | 163388530.05 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.68 | 0.17 | 0.01 | 431450858.83 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 3.74 | 0.3 | 0.03 | 640920.29 | 7.96 | skipped_fast |
| REDUSDT | IDLE | 2.51 | 4.43 | 3.95 | 0.01 | 64443.27 | 9.35 | skipped_fast |
| EDELUSDT | IDLE | 2.38 | 5.84 | 3.65 | -0.05 | 146186.95 | 48.46 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.79 | 0.67 | 0.01 | 626420.04 | 1.05 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 5.5 | 3.04 | 0.1 | 172111.0 | 9.3 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.53 | 1.44 | -0.01 | 228189.24 | 16.57 | skipped_fast |
| CHIPUSDT | IDLE | 1.12 | 2.7 | 1.28 | 0.01 | 121060.46 | 16.26 | skipped_fast |
| RWAINCUSDT | IDLE | 1.04 | 4.59 | 0.0 | 0.08 | 6918.7 | 9.13 | skipped_fast |
| BIOUSDT | IDLE | 0.72 | 1.32 | 0.74 | -0.02 | 93291.31 | 12.49 | skipped_fast |
| TELUSDT | IDLE | 1.17 | 4.1 | 0.83 | 0.13 | 139574.81 | 16.76 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.8 | 0.59 | -0.03 | 46206.97 | 54.16 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.71 | 0.7 | 0.04 | 55939.65 | 7.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.98 | 1.92 | 0.21 | 0.01 | 39521.92 | 7.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.99 | 1.9 | 0.6 | 0.02 | 1010.88 | 18.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
