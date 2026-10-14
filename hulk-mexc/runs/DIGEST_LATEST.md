# Hulk DIGEST — 2026-10-14T17:22:52Z

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
| PYTHUSDT | IDLE | 3.81 | 8.84 | 4.85 | 0.02 | 2102745.91 | 3.69 | skipped_fast |
| WUSDT | IDLE | 1.65 | 7.15 | 3.83 | -0.07 | 3029482.62 | 11.7 | skipped_fast |
| XRPUSDT | IDLE | 2.42 | 4.34 | 3.34 | -0.02 | 42713982.65 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 2.33 | 4.22 | 2.94 | -0.02 | 191072353.24 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.58 | 2.82 | 2.32 | -0.01 | 423233272.05 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.07 | 4.8 | 2.4 | 0.02 | 1445523.97 | 7.25 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 22.88 | 17.62 | 0.02 | 49683.02 | 61.51 | skipped_fast |
| ZBCNUSDT | IDLE | 3.92 | 7.17 | 4.52 | -0.03 | 187125.87 | 19.32 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 9.7 | 7.04 | -0.07 | 109894.7 | 9.41 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 3.9 | 1.79 | -0.07 | 451234.54 | 4.19 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 7.14 | 5.01 | 0.02 | 87215.5 | 3.86 | skipped_fast |
| HBARUSDT | IDLE | 2.26 | 4.11 | 2.72 | -0.03 | 489320.83 | 5.9 | skipped_fast |
| BIOUSDT | IDLE | 2.57 | 4.67 | 3.12 | -0.03 | 69501.74 | 3.75 | skipped_fast |
| REDUSDT | IDLE | 2.53 | 4.95 | 0.69 | 0.02 | 62390.92 | 8.29 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 3.55 | 2.26 | -0.01 | 170658.86 | 5.94 | skipped_fast |
| RWAINCUSDT | IDLE | 1.63 | 5.27 | 4.08 | -0.11 | 31486.24 | 5.39 | skipped_fast |
| TELUSDT | IDLE | 2.22 | 4.39 | 0.28 | 0.03 | 114203.33 | 11.1 | skipped_fast |
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
