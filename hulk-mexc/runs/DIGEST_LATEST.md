# Hulk DIGEST — 2026-09-19T14:58:58Z

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
| XRPUSDT | IDLE | 1.64 | 3.14 | 0.96 | 0.03 | 64825459.7 | 0.69 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.18 | 0.79 | 0.02 | 442253470.74 | 0.15 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.53 | 0.12 | 0.01 | 546623093.84 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.15 | 5.55 | 3.33 | 0.07 | 1073598.47 | 8.15 | skipped_fast |
| PYTHUSDT | IDLE | 1.22 | 2.26 | 1.21 | -0.0 | 658460.68 | 3.31 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.53 | 9.89 | 8.6 | -0.05 | 5427.88 | 111.32 | skipped_fast |
| BIOUSDT | IDLE | 3.28 | 6.31 | 1.67 | 0.04 | 84847.09 | 3.53 | skipped_fast |
| CHIPUSDT | IDLE | 2.13 | 5.21 | 3.68 | 0.01 | 143389.49 | 15.97 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.15 | 0.92 | 0.03 | 532661.44 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.78 | 3.55 | 0.1 | 0.02 | 196311.21 | 14.86 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.87 | 0.28 | 0.03 | 360025.36 | 8.97 | skipped_fast |
| EDELUSDT | IDLE | 1.3 | 7.9 | 1.44 | -0.12 | 189382.28 | 42.32 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 2.57 | 1.14 | 0.05 | 72402.37 | 11.17 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 2.44 | 1.88 | 0.04 | 134231.71 | 17.48 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 5.39 | 2.21 | -0.01 | 126319.76 | 38.76 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.27 | 0.85 | 0.03 | 69162.29 | 6.12 | skipped_fast |
| RIZEUSDT | IDLE | 0.67 | 5.41 | 3.9 | 0.11 | 35734.82 | 101.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.21 | 4.33 | 0.24 | 0.14 | 10875.61 | 21.46 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.11 | 0.0 | -0.0 | 54788.46 | 21.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.83 | 1.52 | 0.97 | 0.01 | 36951.57 | 50.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
