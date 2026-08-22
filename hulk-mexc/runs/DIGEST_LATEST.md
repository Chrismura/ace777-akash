# Hulk DIGEST — 2026-08-22T02:00:52Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.22 | 0.14 | 6876757.79 | 11.74 | skipped_fast |
| XRPUSDT | IDLE | 2.35 | 10.03 | 2.15 | 0.14 | 154054801.58 | 7.45 | skipped_fast |
| ZBCNUSDT | IDLE | 2.5 | 9.63 | 3.0 | 0.08 | 549127.34 | 15.52 | skipped_fast |
| HBARUSDT | IDLE | 2.36 | 4.9 | 1.14 | 0.07 | 950756.29 | 10.02 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 6.06 | 1.01 | 0.15 | 662421.37 | 7.92 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.46 | 0.01 | 510647.58 | 15.21 | skipped_fast |
| WUSDT | IDLE | 1.7 | 4.31 | 0.21 | 0.08 | 399746.74 | 12.12 | skipped_fast |
| BIOUSDT | IDLE | 2.18 | 4.31 | 0.33 | 0.06 | 184638.15 | 18.28 | skipped_fast |
| EDELUSDT | IDLE | 2.4 | 5.02 | 1.85 | -0.02 | 79546.11 | 33.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.9 | 0.11 | 61028.04 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.43 | 0.16 | 156913.19 | 18.67 | skipped_fast |
| QNTUSDT | IDLE | 2.31 | 4.89 | 1.24 | 0.06 | 171329.74 | 9.08 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.22 | 0.13 | 61260.9 | 11.66 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.05 | 180939.68 | 46.52 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9241.73 | 64.41 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54539.67 | 8.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 47.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
