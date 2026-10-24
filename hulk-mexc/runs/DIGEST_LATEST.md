# Hulk DIGEST — 2026-10-24T01:25:15Z

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
| XRPUSDT | IDLE | 1.25 | 2.28 | 1.53 | -0.01 | 28114318.51 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 1.16 | 2.17 | 1.06 | -0.0 | 157542924.47 | 0.13 | skipped_fast |
| BTCUSDT | IDLE | 0.66 | 1.21 | 0.78 | -0.01 | 287841904.16 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.78 | 5.19 | 2.41 | -0.03 | 858661.3 | 1.43 | skipped_fast |
| WUSDT | IDLE | 1.99 | 4.94 | 3.24 | -0.04 | 914680.84 | 17.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 6.53 | 4.57 | -0.03 | 218445.69 | 17.76 | skipped_fast |
| EDELUSDT | IDLE | 1.62 | 3.01 | 1.48 | -0.0 | 570878.9 | 46.82 | skipped_fast |
| REDUSDT | IDLE | 3.51 | 6.98 | 0.22 | 0.04 | 58041.73 | 15.1 | skipped_fast |
| BIOUSDT | IDLE | 2.72 | 5.17 | 1.76 | -0.01 | 78018.77 | 4.27 | skipped_fast |
| CHIPUSDT | IDLE | 2.26 | 5.65 | 1.89 | -0.02 | 75974.44 | 20.68 | skipped_fast |
| KITEUSDT | IDLE | 2.36 | 4.5 | 1.51 | 0.0 | 57020.07 | 11.77 | skipped_fast |
| CCUSDT | IDLE | 1.59 | 3.15 | 0.25 | 0.0 | 194433.93 | 6.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.89 | 3.65 | 0.91 | 0.04 | 53061.14 | 26.89 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 3.47 | 0.99 | -0.03 | 259292.98 | 11.58 | skipped_fast |
| RIZEUSDT | IDLE | 0.91 | 3.67 | 2.11 | -0.02 | 69972.17 | 48.07 | skipped_fast |
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
