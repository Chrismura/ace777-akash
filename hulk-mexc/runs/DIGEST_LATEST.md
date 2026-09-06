# Hulk DIGEST — 2026-09-06T05:45:32Z

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
| ETHUSDT | IDLE | 0.92 | 1.79 | 0.3 | 0.03 | 210104491.34 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.78 | 1.49 | 0.45 | 0.02 | 24731135.82 | 2.1 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.11 | 0.01 | 385806253.34 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.81 | 5.29 | 2.17 | 0.05 | 434460.29 | 1.79 | skipped_fast |
| CHIPUSDT | IDLE | 2.57 | 5.64 | 3.38 | -0.0 | 401382.59 | 3.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.98 | 5.37 | 3.9 | -0.0 | 9262.24 | 10.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.94 | 12.58 | 4.92 | 0.11 | 116158.12 | 35.86 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 2.52 | 1.37 | 0.01 | 304741.16 | 7.28 | skipped_fast |
| KITEUSDT | IDLE | 2.15 | 4.05 | 1.62 | -0.05 | 64507.95 | 9.31 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 2.9 | 0.18 | 0.0 | 208482.14 | 20.19 | skipped_fast |
| WUSDT | IDLE | 1.39 | 2.52 | 1.67 | 0.03 | 173406.46 | 11.89 | skipped_fast |
| HBARUSDT | IDLE | 1.35 | 2.59 | 0.78 | 0.03 | 435397.92 | 1.22 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 2.67 | 1.65 | 0.0 | 58456.22 | 18.93 | skipped_fast |
| BIOUSDT | IDLE | 0.88 | 1.65 | 0.78 | 0.03 | 97479.95 | 7.13 | skipped_fast |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.29 | 0.02 | 112133.41 | 18.71 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 3.64 | 0.54 | 0.05 | 37003.54 | 8.98 | skipped_fast |
| MNSRYUSDT | IDLE | 1.38 | 2.64 | 0.83 | 0.02 | 39886.93 | 2.69 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.06 | 1.81 | 0.03 | 53219.21 | 14.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.33 | 0.14 | 0.04 | 380.96 | 21.12 | skipped_fast |
| TELUSDT | IDLE | 0.83 | 1.59 | 0.46 | 0.01 | 73055.65 | 46.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
