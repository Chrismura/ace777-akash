# Hulk DIGEST — 2026-09-18T01:17:56Z

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
| XRPUSDT | IDLE | 0.62 | 1.2 | 0.23 | 0.01 | 36170705.93 | 1.54 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.91 | 0.37 | 0.01 | 289617439.07 | 0.33 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.62 | 0.28 | 0.0 | 420981023.54 | 0.0 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 29.67 | 1.46 | -0.12 | 270745.54 | 34.86 | skipped_fast |
| CCUSDT | IDLE | 2.42 | 4.84 | 0.02 | 0.05 | 477829.22 | 7.71 | skipped_fast |
| PYTHUSDT | IDLE | 1.43 | 2.92 | 0.56 | 0.07 | 559914.76 | 3.53 | skipped_fast |
| CHIPUSDT | IDLE | 2.87 | 7.95 | 0.87 | 0.09 | 181688.61 | 15.08 | skipped_fast |
| WUSDT | IDLE | 1.18 | 3.13 | 1.54 | 0.09 | 337907.22 | 14.07 | skipped_fast |
| REDUSDT | IDLE | 2.37 | 4.74 | 0.0 | 0.04 | 67407.59 | 27.35 | skipped_fast |
| HBARUSDT | IDLE | 1.27 | 2.39 | 1.0 | 0.02 | 530236.35 | 1.33 | skipped_fast |
| ZBCNUSDT | IDLE | 0.82 | 1.52 | 0.86 | 0.01 | 203254.25 | 32.52 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 2.21 | 0.31 | 0.0 | 68795.56 | 11.82 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.82 | 0.24 | -0.01 | 60825.46 | 12.2 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 3.85 | 2.96 | -0.02 | 73330.37 | 42.49 | skipped_fast |
| RWAINCUSDT | IDLE | 0.31 | 0.54 | 0.47 | -0.02 | 13899.94 | 23.74 | skipped_fast |
| RIZEUSDT | IDLE | 0.54 | 2.95 | 1.62 | -0.04 | 42704.98 | 148.87 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 1.4 | 0.11 | 0.01 | 40488.16 | 8.13 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.6 | 0.37 | 0.0 | 56761.93 | 14.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.51 | 0.24 | 0.01 | 43093.08 | 18.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.22 | 0.39 | 0.39 | 0.02 | 148.34 | 21.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
