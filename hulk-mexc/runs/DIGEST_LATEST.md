# Hulk DIGEST — 2026-09-02T23:02:37Z

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
| XRPUSDT | IDLE | 0.78 | 1.42 | 0.92 | -0.0 | 35704495.62 | 1.49 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.88 | 0.85 | -0.01 | 348869704.75 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.64 | 0.62 | -0.0 | 502018687.98 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.84 | 2.73 | 2.48 | 0.1 | 1338770.26 | 1.76 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 27.69 | 11.98 | 0.14 | 53117.14 | 61.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.81 | 6.79 | 0.4 | -0.01 | 176901.17 | 18.85 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 2.1 | 0.96 | -0.03 | 425956.25 | 8.18 | skipped_fast |
| WUSDT | IDLE | 1.84 | 3.39 | 1.9 | 0.01 | 239457.73 | 13.42 | skipped_fast |
| KITEUSDT | IDLE | 1.62 | 7.31 | 3.1 | 0.15 | 140673.97 | 9.2 | skipped_fast |
| BIOUSDT | IDLE | 1.93 | 3.59 | 1.81 | 0.0 | 69182.63 | 3.91 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.85 | 1.05 | 0.0 | 112097.28 | 7.84 | skipped_fast |
| HBARUSDT | IDLE | 0.31 | 0.58 | 0.26 | 0.0 | 183090.05 | 1.35 | skipped_fast |
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
