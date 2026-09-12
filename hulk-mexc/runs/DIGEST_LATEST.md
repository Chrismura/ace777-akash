# Hulk DIGEST — 2026-09-12T00:21:21Z

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
| RIZEUSDT | IDLE | 1.51 | 102.76 | 44.15 | 0.63 | 215729.74 | 148.38 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.71 | 1.24 | 0.03 | 656920141.74 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.79 | 1.63 | 0.77 | 0.01 | 54286546.25 | 2.21 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.68 | 0.28 | 0.01 | 593037648.44 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 2.47 | 0.95 | -0.01 | 412902.53 | 1.96 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 5.32 | 5.06 | 0.01 | 14801.21 | 5.55 | skipped_fast |
| CCUSDT | IDLE | 1.24 | 2.28 | 1.34 | -0.01 | 418157.87 | 6.16 | skipped_fast |
| EDELUSDT | IDLE | 2.09 | 5.98 | 1.71 | 0.07 | 166605.57 | 17.38 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.25 | 1.85 | 0.01 | 194583.82 | 11.09 | skipped_fast |
| WUSDT | IDLE | 1.21 | 2.45 | 0.76 | 0.01 | 200586.36 | 14.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 3.82 | 1.09 | -0.0 | 121800.87 | 16.93 | skipped_fast |
| BIOUSDT | IDLE | 1.18 | 2.34 | 0.08 | 0.02 | 82232.94 | 7.9 | skipped_fast |
| REDUSDT | IDLE | 1.14 | 2.27 | 0.38 | 0.06 | 64367.46 | 8.62 | skipped_fast |
| KITEUSDT | IDLE | 0.73 | 1.35 | 0.74 | 0.0 | 59154.02 | 13.86 | skipped_fast |
| TELUSDT | IDLE | 1.93 | 3.74 | 3.32 | -0.03 | 103644.48 | 46.59 | skipped_fast |
| HBARUSDT | IDLE | 0.63 | 1.18 | 0.48 | -0.01 | 248725.63 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 2.26 | 0.87 | -0.01 | 46376.79 | 7.85 | skipped_fast |
| FLUIDUSDT | IDLE | 0.36 | 0.73 | 0.0 | 0.03 | 807.07 | 20.71 | skipped_fast |
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
