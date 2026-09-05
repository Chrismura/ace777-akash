# Hulk DIGEST — 2026-09-05T12:27:06Z

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
| XRPUSDT | IDLE | 0.42 | 0.79 | 0.39 | -0.03 | 35846466.61 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.16 | 0.3 | 0.2 | -0.03 | 344692467.69 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.25 | 0.09 | -0.02 | 478826728.38 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.4 | 25.72 | 13.07 | -0.19 | 152947.95 | 49.88 | skipped_fast |
| PYTHUSDT | IDLE | 1.16 | 2.28 | 0.22 | -0.0 | 417360.23 | 1.83 | skipped_fast |
| ZBCNUSDT | IDLE | 1.39 | 2.66 | 0.77 | -0.05 | 198535.04 | 2.62 | skipped_fast |
| CCUSDT | IDLE | 0.5 | 0.97 | 0.14 | -0.02 | 318141.84 | 10.11 | skipped_fast |
| REDUSDT | IDLE | 1.3 | 2.32 | 1.91 | 0.04 | 65316.39 | 8.73 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.14 | 1.92 | -0.05 | 62840.94 | 10.76 | skipped_fast |
| WUSDT | IDLE | 0.54 | 1.05 | 0.26 | 0.02 | 201582.31 | 12.03 | skipped_fast |
| BIOUSDT | IDLE | 0.8 | 1.5 | 0.65 | -0.0 | 85223.82 | 7.29 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.6 | 0.35 | 0.02 | 284401.62 | 1.24 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 1.9 | 1.22 | -0.03 | 75621.36 | 29.49 | skipped_fast |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
