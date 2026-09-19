# Hulk DIGEST — 2026-09-19T03:57:00Z

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
| XRPUSDT | IDLE | 1.2 | 2.51 | 0.55 | 0.07 | 69480721.02 | 2.11 | skipped_fast |
| ETHUSDT | IDLE | 0.64 | 1.21 | 0.52 | 0.06 | 637309412.94 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.09 | 0.67 | 0.05 | 756601623.31 | 0.0 | skipped_fast |
| WUSDT | IDLE | 0.96 | 3.14 | 2.39 | 0.08 | 950740.27 | 5.51 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 19.02 | 14.03 | 0.07 | 101107.47 | 15.1 | skipped_fast |
| PYTHUSDT | IDLE | 1.85 | 3.6 | 0.65 | 0.04 | 739692.58 | 6.51 | skipped_fast |
| CCUSDT | IDLE | 1.55 | 2.99 | 0.71 | 0.04 | 590064.32 | 5.31 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 11.9 | 3.93 | -0.01 | 168193.41 | 70.89 | skipped_fast |
| CHIPUSDT | IDLE | 2.17 | 7.81 | 0.97 | 0.09 | 156167.51 | 10.6 | skipped_fast |
| HBARUSDT | IDLE | 0.94 | 1.82 | 0.46 | 0.02 | 679963.45 | 1.26 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.54 | 11.02 | 7.17 | 0.1 | 126850.48 | 25.3 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 3.29 | 0.0 | 0.07 | 80991.66 | 11.37 | skipped_fast |
| ZBCNUSDT | IDLE | 0.71 | 1.33 | 0.61 | 0.01 | 214729.22 | 14.89 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 1.85 | 0.84 | 0.04 | 85052.97 | 10.97 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 1.21 | 1.19 | 0.05 | 6779.13 | 34.36 | skipped_fast |
| RIZEUSDT | IDLE | 0.54 | 4.29 | 1.3 | -0.1 | 37958.81 | 100.54 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.11 | 0.34 | 0.02 | 74380.73 | 4.72 | skipped_fast |
| FLUIDUSDT | IDLE | 0.8 | 3.39 | 1.93 | 0.16 | 5216.25 | 21.43 | skipped_fast |
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
