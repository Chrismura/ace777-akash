# Hulk DIGEST — 2026-08-22T12:07:51Z

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
| PYTHUSDT | IDLE | 1.74 | 7.83 | 5.13 | 0.01 | 51609813.7 | 2.05 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 14.26 | 7.65 | 0.11 | 215233178.33 | 3.33 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 4.63 | 2.61 | 0.02 | 1252990.41 | 6.45 | skipped_fast |
| CCUSDT | IDLE | 1.64 | 8.38 | 5.0 | 0.13 | 776371.23 | 5.99 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.68 | 0.02 | 579568.03 | 20.09 | skipped_fast |
| ZBCNUSDT | IDLE | 2.27 | 5.77 | 4.92 | -0.04 | 380827.16 | 27.5 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.72 | -0.1 | 611320.66 | 3.35 | skipped_fast |
| KITEUSDT | IDLE | 2.6 | 6.24 | 0.27 | 0.04 | 82662.5 | 21.12 | skipped_fast |
| EDELUSDT | IDLE | 2.19 | 3.89 | 3.2 | -0.03 | 78059.5 | 22.75 | skipped_fast |
| BIOUSDT | IDLE | 0.79 | 5.65 | 1.73 | -0.03 | 240663.71 | 3.2 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2385.65 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 2.19 | 5.61 | 4.29 | -0.03 | 165121.04 | 37.36 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.21 | 0.03 | 153598.58 | 11.55 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.48 | 0.01 | 188299.33 | 6.22 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 1.91 | 0.44 | -0.06 | 47944.36 | 20.52 | skipped_fast |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
