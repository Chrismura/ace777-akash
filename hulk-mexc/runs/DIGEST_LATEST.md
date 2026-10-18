# Hulk DIGEST — 2026-10-18T03:05:00Z

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
| ETHUSDT | IDLE | 0.86 | 1.69 | 0.18 | -0.0 | 94303592.16 | 0.08 | skipped_fast |
| PYTHUSDT | IDLE | 2.83 | 7.25 | 4.79 | -0.08 | 1152269.57 | 1.28 | skipped_fast |
| XRPUSDT | IDLE | 0.71 | 1.37 | 0.39 | -0.01 | 17869949.52 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.91 | 0.12 | 0.0 | 183133414.59 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.81 | 2.4 | 1.39 | -0.03 | 1079596.15 | 16.74 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.76 | 8.69 | 6.51 | -0.1 | 165862.99 | 11.34 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.51 | 1.46 | -0.02 | 583777.28 | 0.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 3.48 | 3.05 | -0.04 | 178554.19 | 28.63 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.22 | 2.08 | -0.01 | 247546.48 | 9.76 | skipped_fast |
| HBARUSDT | IDLE | 1.93 | 3.7 | 1.06 | 0.03 | 267903.85 | 5.81 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.13 | 1.15 | -0.03 | 71798.2 | 8.27 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 3.48 | 2.02 | 0.06 | 20384.18 | 5.27 | skipped_fast |
| CHIPUSDT | IDLE | 0.98 | 2.63 | 1.9 | -0.07 | 81021.52 | 14.02 | skipped_fast |
| REDUSDT | IDLE | 1.12 | 2.01 | 1.47 | -0.03 | 60944.65 | 15.88 | skipped_fast |
| KITEUSDT | IDLE | 0.77 | 1.99 | 0.79 | -0.04 | 70647.64 | 11.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.23 | 2.2 | 1.67 | -0.01 | 45958.16 | 59.57 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 1.93 | 1.77 | -0.06 | 103132.44 | 24.86 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.72 | 0.08 | -0.0 | 52258.88 | 15.94 | skipped_fast |
| FLUIDUSDT | IDLE | 0.61 | 1.23 | 0.0 | -0.01 | 1680.94 | 21.33 | skipped_fast |
| MNSRYUSDT | IDLE | 0.53 | 0.97 | 0.56 | -0.01 | 29981.26 | 41.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
