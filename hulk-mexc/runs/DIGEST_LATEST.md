# Hulk DIGEST — 2026-10-28T22:44:11Z

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
| ETHUSDT | IDLE | 1.36 | 2.54 | 1.21 | 0.0 | 204662181.87 | 0.42 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 2.56 | 1.22 | 0.0 | 22896212.1 | 2.26 | skipped_fast |
| BTCUSDT | IDLE | 0.85 | 1.62 | 0.57 | 0.01 | 326315100.38 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.06 | 5.96 | 1.04 | 0.01 | 447707.11 | 2.71 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.26 | 2.93 | -0.01 | 397300.82 | 16.62 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 3.76 | 1.0 | 0.02 | 429280.34 | 9.87 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.24 | 5.71 | 5.11 | -0.03 | 39564.72 | 35.66 | skipped_fast |
| QNTUSDT | IDLE | 2.54 | 4.89 | 1.3 | -0.0 | 410680.41 | 2.0 | skipped_fast |
| HBARUSDT | IDLE | 1.73 | 3.13 | 2.18 | -0.01 | 561336.67 | 6.64 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 4.39 | 1.72 | 0.01 | 88774.43 | 8.73 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.52 | 0.51 | 0.0 | 275874.44 | 28.21 | skipped_fast |
| CHIPUSDT | IDLE | 1.02 | 4.78 | 1.18 | -0.08 | 235117.25 | 12.09 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 2.66 | 1.68 | -0.03 | 183074.54 | 24.78 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 3.01 | 1.2 | -0.02 | 62250.22 | 9.45 | skipped_fast |
| IOTAUSDT | IDLE | 2.65 | 4.9 | 2.65 | -0.01 | 78210.05 | 19.11 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.65 | 1.43 | -0.02 | 56138.35 | 15.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.27 | 3.65 | 3.52 | -0.04 | 33958.82 | 7.03 | skipped_fast |
| FLUIDUSDT | IDLE | 0.99 | 3.05 | 1.89 | -0.0 | 9117.65 | 21.43 | skipped_fast |
| RWAUSDT | IDLE | 0.74 | 1.37 | 0.79 | 0.0 | 54265.71 | 15.99 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.51 | 0.36 | 0.01 | 35692.14 | 40.86 | skipped_fast |
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
