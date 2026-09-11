# Hulk DIGEST — 2026-09-11T19:20:59Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 6.41 | 5.71 | -0.0 | 53807786.8 | 2.96 | skipped_fast |
| ETHUSDT | IDLE | 2.56 | 5.39 | 4.68 | 0.03 | 635535109.86 | 0.2 | skipped_fast |
| BTCUSDT | IDLE | 2.14 | 3.79 | 3.31 | 0.0 | 558047820.38 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 93.24 | 10.6 | 0.97 | 187642.62 | 78.52 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.63 | 6.68 | 5.76 | -0.0 | 408901.58 | 1.96 | skipped_fast |
| CCUSDT | IDLE | 2.66 | 4.74 | 3.83 | -0.01 | 418192.55 | 9.2 | skipped_fast |
| RWAINCUSDT | IDLE | 4.07 | 8.33 | 3.84 | 0.04 | 11883.82 | 26.98 | skipped_fast |
| EDELUSDT | IDLE | 3.37 | 7.37 | 0.35 | 0.01 | 155715.98 | 26.44 | skipped_fast |
| WUSDT | IDLE | 2.57 | 4.84 | 4.02 | 0.01 | 196182.15 | 13.48 | skipped_fast |
| BIOUSDT | IDLE | 2.64 | 4.68 | 3.97 | -0.01 | 82318.47 | 8.04 | skipped_fast |
| CHIPUSDT | IDLE | 2.16 | 6.38 | 4.66 | -0.01 | 149889.47 | 14.72 | skipped_fast |
| ZBCNUSDT | IDLE | 2.12 | 3.73 | 3.36 | 0.0 | 189972.82 | 7.62 | skipped_fast |
| HBARUSDT | IDLE | 2.41 | 4.25 | 3.74 | -0.01 | 236867.81 | 1.35 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.05 | 2.41 | -0.02 | 59385.47 | 13.86 | skipped_fast |
| TELUSDT | IDLE | 3.03 | 5.94 | 4.9 | -0.01 | 93229.64 | 56.75 | skipped_fast |
| REDUSDT | IDLE | 1.66 | 3.16 | 1.04 | 0.05 | 61298.78 | 17.37 | skipped_fast |
| QNTUSDT | IDLE | 1.79 | 3.13 | 3.02 | -0.03 | 40838.29 | 1.56 | skipped_fast |
| FLUIDUSDT | IDLE | 1.53 | 2.66 | 2.6 | -0.0 | 1306.32 | 21.78 | skipped_fast |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
