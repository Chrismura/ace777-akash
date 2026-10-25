# Hulk DIGEST — 2026-10-25T22:10:41Z

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
| ETHUSDT | IDLE | 0.82 | 1.52 | 0.8 | 0.0 | 81053092.38 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.83 | 1.53 | 0.83 | 0.0 | 14267940.15 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.92 | 0.48 | 0.0 | 141482219.54 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.28 | 5.27 | 0.34 | 0.08 | 607473.97 | 3.96 | skipped_fast |
| WUSDT | IDLE | 2.04 | 3.7 | 2.47 | -0.02 | 593468.91 | 16.77 | skipped_fast |
| RIZEUSDT | IDLE | 3.33 | 6.05 | 4.08 | 0.01 | 34481.61 | 62.78 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 3.82 | 2.06 | 0.05 | 187890.3 | 49.03 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.56 | 0.99 | 0.01 | 197660.31 | 7.85 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 1.97 | 0.89 | -0.03 | 58450.37 | 15.1 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.82 | 1.06 | -0.0 | 155198.07 | 9.05 | skipped_fast |
| BIOUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
