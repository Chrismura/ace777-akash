# Hulk DIGEST — 2026-09-14T16:42:57Z

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
| XRPUSDT | IDLE | 1.37 | 2.65 | 0.63 | 0.05 | 45305764.24 | 2.13 | skipped_fast |
| BTCUSDT | IDLE | 0.93 | 1.81 | 0.3 | 0.02 | 474157398.54 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.7 | 0.33 | 0.01 | 351558812.9 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.6 | 3.07 | 0.87 | -0.0 | 479867.69 | 1.8 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 8.59 | 6.5 | 0.06 | 180936.4 | 17.34 | skipped_fast |
| EDELUSDT | IDLE | 1.55 | 6.54 | 2.38 | 0.15 | 258328.95 | 20.28 | skipped_fast |
| RIZEUSDT | IDLE | 1.65 | 18.12 | 14.88 | 0.03 | 68323.37 | 98.97 | skipped_fast |
| WUSDT | IDLE | 1.72 | 3.21 | 1.53 | -0.01 | 224099.26 | 9.04 | skipped_fast |
| CHIPUSDT | IDLE | 2.19 | 4.25 | 2.75 | -0.04 | 88348.21 | 14.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 2.8 | 0.73 | 0.0 | 205790.59 | 21.21 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 2.08 | 0.23 | 0.02 | 278213.43 | 10.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.46 | 2.84 | 0.6 | 0.03 | 10357.39 | 5.46 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 2.02 | 0.43 | 0.01 | 83711.19 | 3.9 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 2.17 | 1.23 | -0.01 | 61529.27 | 12.32 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.63 | 0.03 | 0.02 | 293713.32 | 1.29 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.77 | 0.63 | 0.0 | 41402.68 | 4.66 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 2.01 | 1.29 | 0.01 | 90026.21 | 56.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.91 | 1.59 | 1.57 | 0.0 | 623.71 | 21.83 | skipped_fast |
| MNSRYUSDT | IDLE | 0.52 | 1.01 | 0.25 | 0.0 | 29045.49 | 31.91 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.22 | 0.0 | 54641.47 | 29.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
