# Hulk DIGEST — 2026-09-06T02:45:14Z

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
| XRPUSDT | IDLE | 0.73 | 1.41 | 0.4 | 0.01 | 23864305.41 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.33 | 0.31 | 0.02 | 196318614.93 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.23 | 0.43 | 0.22 | 0.0 | 372278616.22 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.14 | 3.75 | 3.58 | 0.01 | 410119.91 | 3.67 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 4.43 | 2.03 | 0.07 | 423021.47 | 3.36 | skipped_fast |
| RWAINCUSDT | IDLE | 2.84 | 5.2 | 3.23 | 0.0 | 8482.49 | 26.96 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.59 | 1.6 | 0.04 | 171479.77 | 13.85 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 2.52 | 0.41 | 0.03 | 291830.12 | 9.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.37 | 2.5 | 1.57 | -0.01 | 223628.94 | 15.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.4 | 9.29 | 2.32 | -0.05 | 123880.47 | 60.42 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 2.67 | 2.42 | 0.0 | 58888.13 | 8.75 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 2.56 | 0.0 | -0.05 | 64630.68 | 9.31 | skipped_fast |
| HBARUSDT | IDLE | 1.03 | 1.98 | 0.55 | 0.03 | 374283.81 | 9.85 | skipped_fast |
| RWAUSDT | IDLE | 2.22 | 3.91 | 3.56 | 0.03 | 53652.42 | 21.27 | skipped_fast |
| BIOUSDT | IDLE | 0.63 | 1.22 | 0.28 | 0.03 | 95905.53 | 3.57 | skipped_fast |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.85 | 0.02 | 115870.8 | 28.26 | skipped_fast |
| TELUSDT | IDLE | 1.74 | 3.28 | 1.27 | 0.0 | 72928.54 | 23.36 | skipped_fast |
| QNTUSDT | IDLE | 1.37 | 2.62 | 0.74 | 0.03 | 36808.04 | 7.59 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 2.11 | 0.0 | 0.03 | 390.92 | 22.05 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.97 | 0.11 | 0.01 | 38762.79 | 39.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
