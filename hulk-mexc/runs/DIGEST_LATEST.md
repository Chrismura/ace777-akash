# Hulk DIGEST — 2026-09-06T05:31:01Z

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
| XRPUSDT | IDLE | 0.81 | 1.49 | 0.86 | 0.02 | 24465334.85 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.41 | 0.34 | 0.02 | 201019902.64 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.39 | 0.32 | 0.0 | 380213995.22 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.85 | 5.29 | 2.75 | 0.04 | 430705.71 | 1.8 | skipped_fast |
| CHIPUSDT | IDLE | 2.54 | 5.64 | 2.82 | 0.0 | 409531.25 | 1.69 | skipped_fast |
| RWAINCUSDT | IDLE | 2.92 | 5.37 | 3.12 | 0.01 | 9214.25 | 5.36 | skipped_fast |
| RIZEUSDT | IDLE | 1.94 | 12.58 | 4.81 | 0.11 | 119189.63 | 59.51 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 2.52 | 1.31 | 0.02 | 295168.8 | 1.82 | skipped_fast |
| KITEUSDT | IDLE | 2.11 | 4.05 | 1.19 | -0.02 | 64841.52 | 8.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 2.68 | 0.2 | 0.0 | 207800.94 | 10.12 | skipped_fast |
| WUSDT | IDLE | 1.4 | 2.52 | 1.81 | 0.03 | 175227.67 | 10.91 | skipped_fast |
| HBARUSDT | IDLE | 1.37 | 2.59 | 0.98 | 0.02 | 426863.37 | 1.23 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.67 | 1.81 | 0.01 | 59026.34 | 8.7 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.65 | 0.96 | 0.03 | 97266.13 | 3.57 | skipped_fast |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.57 | 0.02 | 111966.63 | 18.74 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 3.4 | 0.0 | 0.05 | 37041.6 | 1.49 | skipped_fast |
| MNSRYUSDT | IDLE | 1.38 | 2.64 | 0.77 | 0.02 | 39783.43 | 2.68 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.06 | 1.81 | 0.03 | 53359.82 | 14.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.33 | 0.14 | 0.04 | 380.96 | 21.93 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.59 | 0.81 | 0.0 | 72458.64 | 46.84 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
