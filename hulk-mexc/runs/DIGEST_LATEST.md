# Hulk DIGEST — 2026-08-20T05:21:03Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.8 | 2.58 | 0.99 | 0.1 | 46413304.61 | 1.81 | skipped_fast |
| REDUSDT | IDLE | 2.69 | 21.26 | 4.08 | 0.26 | 126153.27 | 20.79 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.33 | 22.65 | 9.96 | 0.12 | 60917.34 | 163.19 | skipped_fast |
| CCUSDT | IDLE | 1.24 | 4.08 | 1.66 | 0.12 | 384219.48 | 8.96 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 7.2 | 0.03 | 0.17 | 217933.84 | 3.34 | skipped_fast |
| WUSDT | IDLE | 1.38 | 2.93 | 2.58 | 0.07 | 275326.62 | 8.19 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 11.14 | 8.7 | 0.22 | 100352.08 | 22.12 | skipped_fast |
| PYTHUSDT | IDLE | 0.69 | 2.05 | 0.91 | 0.09 | 297643.73 | 2.35 | skipped_fast |
| ZBCNUSDT | IDLE | 0.97 | 3.98 | 1.59 | 0.14 | 226655.26 | 13.4 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 4.97 | 0.93 | 0.16 | 171047.96 | 6.92 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.71 | 0.48 | 0.05 | 364345.2 | 1.41 | skipped_fast |
| QAITUSDT | IDLE | 1.19 | 3.23 | 1.06 | 0.05 | 10308.39 | 30.48 | skipped_fast |
| KITEUSDT | IDLE | 0.7 | 1.35 | 0.84 | 0.06 | 59642.55 | 13.52 | skipped_fast |
| RWAINCUSDT | IDLE | 0.51 | 1.54 | 0.22 | 0.06 | 17213.23 | 28.18 | skipped_fast |
| TELUSDT | IDLE | 0.53 | 2.31 | 2.08 | 0.11 | 188829.51 | 62.31 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.31 | 0.52 | 0.05 | 37261.71 | 3.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.4 | 1.15 | 0.12 | 0.07 | 3500.81 | 23.37 | skipped_fast |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
