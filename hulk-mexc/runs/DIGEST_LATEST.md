# Hulk DIGEST — 2026-09-25T11:25:50Z

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
| XRPUSDT | IDLE | 2.21 | 4.53 | 0.49 | 0.07 | 75152443.92 | 3.16 | skipped_fast |
| ETHUSDT | IDLE | 1.47 | 2.83 | 0.69 | 0.03 | 362707969.46 | 0.55 | skipped_fast |
| BTCUSDT | IDLE | 0.93 | 1.79 | 0.44 | 0.02 | 707613838.5 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.79 | 6.31 | 0.71 | 0.12 | 1093889.57 | 5.6 | skipped_fast |
| CCUSDT | IDLE | 1.72 | 5.95 | 0.37 | 0.13 | 648947.57 | 7.4 | skipped_fast |
| HBARUSDT | IDLE | 2.0 | 3.93 | 0.4 | 0.05 | 895958.28 | 1.05 | skipped_fast |
| ZBCNUSDT | IDLE | 3.32 | 9.65 | 2.67 | 0.06 | 219098.29 | 16.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.25 | 29.69 | 12.94 | 0.76 | 122294.42 | 43.4 | skipped_fast |
| WUSDT | IDLE | 2.22 | 4.33 | 0.68 | 0.05 | 326724.98 | 8.34 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 9.34 | 6.43 | 0.35 | 620705.05 | 9.18 | skipped_fast |
| KITEUSDT | IDLE | 2.7 | 5.37 | 0.14 | 0.0 | 73244.29 | 9.88 | skipped_fast |
| CHIPUSDT | IDLE | 1.85 | 9.9 | 2.32 | 0.17 | 106767.13 | 16.38 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 4.87 | 0.18 | 0.09 | 135434.2 | 14.76 | skipped_fast |
| RWAINCUSDT | IDLE | 1.95 | 8.91 | 7.06 | 0.07 | 23284.17 | 75.55 | skipped_fast |
| BIOUSDT | IDLE | 1.47 | 4.04 | 0.54 | 0.08 | 92637.48 | 9.51 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 5.06 | 0.59 | -0.01 | 112236.45 | 47.79 | skipped_fast |
| EDELUSDT | IDLE | 0.39 | 4.31 | 1.98 | 0.11 | 197826.66 | 33.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.5 | 3.44 | 0.47 | 0.08 | 442.27 | 22.01 | skipped_fast |
| MNSRYUSDT | IDLE | 1.27 | 2.42 | 0.82 | 0.03 | 44268.27 | 40.76 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.66 | 0.22 | 0.02 | 58965.38 | 36.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
