# Hulk DIGEST — 2026-10-12T13:53:16Z

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
| WUSDT | IDLE | 1.51 | 28.36 | 19.77 | 0.47 | 16076390.34 | 11.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.25 | 10.07 | 5.48 | 0.12 | 2664237.07 | 3.5 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 2.22 | 1.81 | -0.01 | 26864728.91 | 2.16 | skipped_fast |
| BTCUSDT | IDLE | 1.02 | 1.82 | 1.5 | -0.0 | 275691670.97 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.97 | 1.74 | 1.29 | 0.01 | 276666310.41 | 0.04 | skipped_fast |
| QNTUSDT | IDLE | 3.14 | 5.57 | 4.79 | -0.06 | 857941.36 | 0.87 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 21.02 | 16.35 | 0.07 | 190913.21 | 7.53 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 11.51 | 5.71 | 0.04 | 22545.27 | 9.71 | skipped_fast |
| EDELUSDT | IDLE | 2.59 | 5.09 | 4.35 | -0.07 | 210449.58 | 19.31 | skipped_fast |
| CHIPUSDT | IDLE | 2.08 | 6.9 | 5.55 | -0.06 | 179482.42 | 12.89 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.02 | 2.74 | -0.0 | 616483.22 | 4.35 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.59 | 2.07 | -0.0 | 380607.89 | 7.27 | skipped_fast |
| KITEUSDT | IDLE | 2.51 | 4.42 | 3.99 | 0.01 | 66424.88 | 8.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.49 | 2.63 | 2.39 | 0.04 | 284233.95 | 8.02 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 2.69 | 2.32 | -0.02 | 97281.51 | 3.44 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 9.65 | 5.34 | 0.16 | 52550.08 | 79.31 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.18 | 1.29 | 0.03 | 168435.5 | 17.01 | skipped_fast |
| FLUIDUSDT | IDLE | 1.84 | 3.31 | 2.49 | 0.01 | 24201.53 | 14.25 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.54 | 0.38 | 0.01 | 51976.41 | 15.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.07 | 0.0 | 40398.61 | 10.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
