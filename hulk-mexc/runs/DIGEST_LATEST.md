# Hulk DIGEST — 2026-09-02T23:36:00Z

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
| XRPUSDT | IDLE | 0.76 | 1.42 | 0.72 | -0.0 | 35732503.62 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.91 | 0.63 | -0.01 | 349659382.57 | 0.84 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.65 | 0.46 | -0.0 | 502001236.3 | 0.2 | skipped_fast |
| PYTHUSDT | IDLE | 0.85 | 2.76 | 2.62 | 0.09 | 1348657.68 | 3.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.38 | 5.3 | 2.1 | -0.05 | 917409.38 | 2.38 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.72 | 27.69 | 9.86 | 0.16 | 54029.54 | 77.84 | skipped_fast |
| ZBCNUSDT | IDLE | 2.88 | 6.9 | 0.85 | -0.01 | 176911.43 | 15.01 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 2.1 | 1.04 | -0.03 | 429645.02 | 5.46 | skipped_fast |
| WUSDT | IDLE | 1.83 | 3.39 | 1.78 | 0.01 | 236354.69 | 13.41 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 7.31 | 2.64 | 0.16 | 141106.15 | 10.54 | skipped_fast |
| BIOUSDT | IDLE | 1.97 | 3.59 | 2.38 | -0.0 | 69887.65 | 3.94 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 1.85 | 1.68 | 0.0 | 112587.21 | 14.0 | skipped_fast |
| HBARUSDT | IDLE | 0.48 | 0.96 | 0.05 | 0.01 | 193402.41 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 1.17 | 2.19 | 1.04 | 0.03 | 74937.26 | 35.09 | skipped_fast |
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
