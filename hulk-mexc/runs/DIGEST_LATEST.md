# Hulk DIGEST — 2026-09-13T06:33:31Z

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
| XRPUSDT | IDLE | 0.29 | 0.54 | 0.31 | 0.0 | 13725652.99 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 0.19 | 0.34 | 0.25 | 0.0 | 190212853.08 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.1 | 0.19 | 0.05 | 0.0 | 278561658.37 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.1 | 34.95 | 19.52 | 0.1 | 94474.3 | 155.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.35 | 2.49 | 1.42 | 0.05 | 424754.32 | 1.82 | skipped_fast |
| WUSDT | IDLE | 1.81 | 3.25 | 2.44 | 0.02 | 223641.25 | 11.93 | skipped_fast |
| RWAINCUSDT | IDLE | 2.49 | 4.36 | 4.17 | 0.0 | 9553.68 | 16.52 | skipped_fast |
| QNTUSDT | IDLE | 3.02 | 5.3 | 4.93 | 0.0 | 40860.65 | 4.68 | skipped_fast |
| KITEUSDT | IDLE | 1.83 | 3.65 | 0.09 | 0.03 | 63965.41 | 14.57 | skipped_fast |
| CCUSDT | IDLE | 0.9 | 1.68 | 0.85 | -0.01 | 237403.19 | 6.11 | skipped_fast |
| REDUSDT | IDLE | 1.67 | 3.11 | 1.56 | 0.04 | 55698.78 | 11.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.39 | 2.77 | 1.97 | -0.0 | 78048.49 | 12.68 | skipped_fast |
| ZBCNUSDT | IDLE | 0.64 | 2.02 | 0.06 | -0.0 | 228116.07 | 5.57 | skipped_fast |
| EDELUSDT | IDLE | 1.0 | 2.81 | 0.24 | 0.09 | 174395.8 | 24.16 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 1.73 | 0.39 | 0.01 | 72371.66 | 3.88 | skipped_fast |
| TELUSDT | IDLE | 1.66 | 2.93 | 2.61 | -0.05 | 90701.53 | 74.53 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.22 | 0.12 | 0.02 | 123334.54 | 1.32 | skipped_fast |
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
