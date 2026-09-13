# Hulk DIGEST — 2026-09-13T17:40:39Z

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
| ETHUSDT | IDLE | 1.05 | 2.05 | 0.32 | -0.01 | 256164900.64 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.96 | 1.87 | 0.29 | -0.01 | 14958222.12 | 2.22 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 1.07 | 0.15 | 0.0 | 295313115.66 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.56 | 5.02 | 0.69 | 0.02 | 444044.24 | 1.78 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 9.71 | 0.98 | 0.11 | 204318.13 | 38.12 | skipped_fast |
| CHIPUSDT | IDLE | 2.2 | 6.72 | 5.15 | -0.11 | 84948.9 | 13.74 | skipped_fast |
| WUSDT | IDLE | 1.62 | 3.14 | 0.73 | 0.02 | 255002.28 | 11.91 | skipped_fast |
| ZBCNUSDT | IDLE | 1.54 | 2.96 | 0.78 | -0.0 | 201039.17 | 16.2 | skipped_fast |
| CCUSDT | IDLE | 0.89 | 1.75 | 0.25 | -0.02 | 294993.67 | 7.32 | skipped_fast |
| REDUSDT | IDLE | 1.56 | 2.79 | 2.18 | 0.0 | 61079.82 | 16.83 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.5 | 2.3 | 0.01 | 63403.55 | 12.18 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 2.03 | 0.43 | -0.0 | 68390.89 | 7.82 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 10.73 | 1.68 | -0.07 | 78897.92 | 54.25 | skipped_fast |
| RWAINCUSDT | IDLE | 0.93 | 1.65 | 1.45 | -0.03 | 6758.55 | 28.37 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.98 | 0.4 | 0.02 | 198799.3 | 1.31 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.96 | 0.3 | -0.0 | 54709.86 | 14.85 | skipped_fast |
| QNTUSDT | IDLE | 0.84 | 1.66 | 0.11 | 0.01 | 37338.9 | 3.09 | skipped_fast |
| TELUSDT | IDLE | 0.73 | 1.4 | 0.38 | -0.05 | 82632.21 | 44.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.63 | 1.11 | 1.05 | -0.01 | 1479.56 | 21.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.25 | 0.14 | 0.0 | 32116.28 | 13.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
