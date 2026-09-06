# Hulk DIGEST — 2026-09-06T07:30:41Z

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
| XRPUSDT | IDLE | 0.92 | 1.65 | 1.22 | 0.01 | 25773870.42 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.89 | 1.61 | 1.13 | 0.02 | 226938742.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.36 | 0.0 | 387057721.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.96 | 5.29 | 4.16 | 0.02 | 417145.11 | 3.65 | skipped_fast |
| CHIPUSDT | IDLE | 2.31 | 4.92 | 4.04 | -0.02 | 407074.31 | 3.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 3.0 | 0.25 | -0.0 | 225919.59 | 2.13 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 1.91 | 1.34 | 0.01 | 303719.14 | 9.11 | skipped_fast |
| RIZEUSDT | IDLE | 1.38 | 7.54 | 6.67 | 0.01 | 98348.38 | 28.41 | skipped_fast |
| WUSDT | IDLE | 1.41 | 2.57 | 1.66 | 0.01 | 172065.35 | 16.88 | skipped_fast |
| RWAINCUSDT | IDLE | 2.33 | 4.51 | 0.99 | 0.03 | 9383.1 | 47.36 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 2.76 | 2.05 | 0.01 | 97018.37 | 7.23 | skipped_fast |
| HBARUSDT | IDLE | 1.18 | 2.1 | 1.71 | 0.01 | 439795.48 | 1.24 | skipped_fast |
| KITEUSDT | IDLE | 1.51 | 2.72 | 1.95 | -0.03 | 64355.46 | 10.92 | skipped_fast |
| EDELUSDT | IDLE | 1.33 | 2.46 | 1.29 | 0.01 | 73647.27 | 28.02 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 1.85 | 0.71 | 0.01 | 62485.49 | 10.27 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 3.09 | 2.0 | 0.03 | 39021.18 | 10.61 | skipped_fast |
| MNSRYUSDT | IDLE | 1.37 | 2.57 | 1.16 | 0.01 | 41319.18 | 24.28 | skipped_fast |
| TELUSDT | IDLE | 0.71 | 1.29 | 0.93 | 0.0 | 72465.99 | 40.95 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.07 | 1.06 | 0.02 | 52454.85 | 28.51 | skipped_fast |
| FLUIDUSDT | IDLE | 0.47 | 0.91 | 0.14 | 0.03 | 358.09 | 21.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
