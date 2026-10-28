# Hulk DIGEST — 2026-10-28T05:31:14Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.79 | 1.4 | 1.16 | 0.02 | 19435740.12 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.21 | 0.53 | 0.02 | 247443358.02 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.39 | 0.74 | 0.33 | 0.01 | 310386995.56 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.88 | 1.86 | 0.5 | 0.05 | 647145.21 | 16.34 | skipped_fast |
| EDELUSDT | IDLE | 1.82 | 3.34 | 2.0 | 0.02 | 375737.78 | 15.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 4.8 | 2.91 | -0.04 | 202743.12 | 23.55 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.69 | 5.68 | 5.05 | -0.06 | 58064.15 | 27.23 | skipped_fast |
| PYTHUSDT | IDLE | 1.0 | 1.75 | 1.66 | -0.0 | 364768.92 | 1.38 | skipped_fast |
| QNTUSDT | IDLE | 0.98 | 1.89 | 0.51 | 0.01 | 657183.82 | 1.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 3.29 | 2.63 | 0.04 | 125642.94 | 16.63 | skipped_fast |
| CCUSDT | IDLE | 0.71 | 1.35 | 0.52 | 0.02 | 224443.27 | 9.04 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.83 | 1.31 | 0.05 | 59643.05 | 11.02 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 2.07 | 1.09 | 0.0 | 329387.79 | 9.15 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 1.82 | 0.96 | 0.03 | 58392.69 | 8.8 | skipped_fast |
| REDUSDT | IDLE | 0.64 | 1.37 | 0.43 | 0.06 | 58685.54 | 15.55 | skipped_fast |
| RIZEUSDT | IDLE | 0.41 | 0.79 | 0.16 | 0.02 | 34860.57 | 52.98 | skipped_fast |
| FLUIDUSDT | IDLE | 0.46 | 1.38 | 0.72 | 0.01 | 7457.67 | 21.23 | skipped_fast |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
