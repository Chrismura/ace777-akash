# Hulk DIGEST — 2026-10-06T17:38:16Z

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
| QNTUSDT | IDLE | 3.09 | 5.61 | 3.77 | 0.01 | 2699704.14 | 8.18 | skipped_fast |
| XRPUSDT | IDLE | 0.99 | 1.78 | 1.33 | 0.01 | 27485781.87 | 2.0 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.38 | 1.29 | 0.0 | 549316944.16 | 0.05 | skipped_fast |
| ETHUSDT | IDLE | 0.63 | 1.11 | 0.98 | -0.0 | 252359517.84 | 0.67 | skipped_fast |
| PYTHUSDT | IDLE | 2.95 | 5.23 | 4.41 | 0.02 | 611824.0 | 3.89 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.62 | 7.81 | 6.13 | -0.04 | 342564.02 | 23.3 | skipped_fast |
| WUSDT | IDLE | 1.92 | 3.58 | 1.67 | 0.03 | 436487.2 | 8.89 | skipped_fast |
| CCUSDT | IDLE | 1.74 | 3.33 | 1.06 | 0.03 | 436852.36 | 6.22 | skipped_fast |
| RWAINCUSDT | IDLE | 3.74 | 7.03 | 3.06 | -0.01 | 12668.8 | 46.36 | skipped_fast |
| CHIPUSDT | IDLE | 1.4 | 4.62 | 1.13 | 0.07 | 167821.3 | 17.18 | skipped_fast |
| BIOUSDT | IDLE | 1.61 | 3.76 | 0.89 | 0.02 | 103849.1 | 9.3 | skipped_fast |
| ZBCNUSDT | IDLE | 0.76 | 1.43 | 0.63 | 0.01 | 237392.43 | 5.1 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.78 | 0.8 | 0.0 | 474638.6 | 3.97 | skipped_fast |
| FLUIDUSDT | IDLE | 2.16 | 8.72 | 6.74 | -0.09 | 88781.44 | 16.5 | skipped_fast |
| RIZEUSDT | IDLE | 0.86 | 9.78 | 0.35 | 0.23 | 116630.4 | 39.12 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 2.42 | 1.72 | -0.02 | 57364.93 | 9.15 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 4.43 | 4.03 | -0.02 | 123297.76 | 37.28 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 2.4 | 1.38 | 0.02 | 62029.88 | 7.77 | skipped_fast |
| RWAUSDT | IDLE | 0.63 | 1.1 | 1.02 | 0.0 | 51934.42 | 14.66 | skipped_fast |
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
