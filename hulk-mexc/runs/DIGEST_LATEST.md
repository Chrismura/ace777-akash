# Hulk DIGEST — 2026-09-06T09:30:12Z

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
| ETHUSDT | IDLE | 0.87 | 1.61 | 0.85 | 0.02 | 228412209.68 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.74 | 1.41 | 0.48 | 0.01 | 25369218.59 | 1.41 | skipped_fast |
| BTCUSDT | IDLE | 0.34 | 0.65 | 0.14 | 0.0 | 394111699.17 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.67 | 4.86 | 3.15 | 0.03 | 424784.25 | 3.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.5 | 2.9 | 0.62 | 0.02 | 229575.05 | 14.67 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.93 | 0.0 | 0.02 | 302676.85 | 9.9 | skipped_fast |
| RIZEUSDT | IDLE | 1.41 | 7.67 | 6.82 | 0.05 | 91728.14 | 48.74 | skipped_fast |
| BIOUSDT | IDLE | 1.51 | 2.76 | 1.7 | 0.01 | 93633.56 | 3.6 | skipped_fast |
| WUSDT | IDLE | 1.16 | 2.13 | 1.25 | 0.01 | 174629.38 | 13.91 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 2.02 | 0.89 | 0.01 | 439090.86 | 1.23 | skipped_fast |
| REDUSDT | IDLE | 1.39 | 2.75 | 0.26 | 0.02 | 62502.36 | 10.16 | skipped_fast |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
