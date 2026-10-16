# Hulk DIGEST — 2026-10-16T17:02:30Z

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
| PYTHUSDT | IDLE | 2.43 | 6.94 | 6.49 | -0.1 | 2261466.42 | 4.67 | skipped_fast |
| WUSDT | IDLE | 2.68 | 4.81 | 4.27 | -0.02 | 1638893.93 | 17.37 | skipped_fast |
| XRPUSDT | IDLE | 1.88 | 3.3 | 3.1 | -0.02 | 23752373.06 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 1.27 | 2.23 | 2.05 | -0.0 | 204829344.58 | 0.78 | skipped_fast |
| BTCUSDT | IDLE | 0.98 | 1.73 | 1.55 | -0.01 | 345404753.78 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.86 | 5.16 | 3.67 | -0.03 | 870719.02 | 0.98 | skipped_fast |
| CCUSDT | IDLE | 2.38 | 4.21 | 3.66 | -0.06 | 386252.96 | 8.77 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 10.33 | 7.58 | -0.1 | 25016.82 | 5.36 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 7.8 | 7.22 | -0.01 | 152287.15 | 13.08 | skipped_fast |
| REDUSDT | IDLE | 2.7 | 4.92 | 4.58 | -0.07 | 96472.93 | 7.49 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 3.49 | 3.37 | -0.02 | 206439.08 | 8.67 | skipped_fast |
| HBARUSDT | IDLE | 2.72 | 4.76 | 4.54 | -0.0 | 308902.5 | 4.81 | skipped_fast |
| BIOUSDT | IDLE | 2.31 | 4.07 | 3.72 | -0.03 | 61582.69 | 7.96 | skipped_fast |
| KITEUSDT | IDLE | 2.3 | 4.2 | 2.67 | -0.02 | 57032.37 | 8.25 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 2.91 | 1.59 | -0.05 | 215172.31 | 23.08 | skipped_fast |
| RIZEUSDT | IDLE | 2.36 | 5.54 | 0.73 | 0.05 | 34482.6 | 30.48 | skipped_fast |
| TELUSDT | IDLE | 1.23 | 2.2 | 1.71 | 0.01 | 91677.79 | 28.11 | skipped_fast |
| RWAUSDT | IDLE | 0.76 | 1.35 | 1.09 | 0.01 | 52594.6 | 7.9 | skipped_fast |
| FLUIDUSDT | IDLE | 0.85 | 1.61 | 0.63 | -0.02 | 6085.48 | 21.33 | skipped_fast |
| MNSRYUSDT | IDLE | 0.23 | 0.41 | 0.38 | -0.01 | 36184.72 | 26.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
