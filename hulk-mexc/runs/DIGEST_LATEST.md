# Hulk DIGEST — 2026-08-22T04:14:19Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 13.13 | 0.18 | 0.2 | 10325981.29 | 23.8 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 12.22 | 1.03 | 0.21 | 167012184.98 | 3.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 11.56 | 0.11 | 0.22 | 723131.64 | 10.53 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 6.2 | 0.11 | 0.11 | 1005223.74 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.87 | 5.36 | 2.47 | 0.0 | 449504.55 | 3.01 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.49 | 0.06 | 199815.12 | 3.01 | skipped_fast |
| WUSDT | IDLE | 1.97 | 7.18 | 0.69 | 0.14 | 429244.57 | 11.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.39 | 0.11 | 535256.43 | 15.22 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.58 | -0.05 | 80357.13 | 22.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.01 | 0.1 | 59149.64 | 32.55 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.82 | 0.21 | 158559.2 | 14.22 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.35 | 0.13 | 67557.81 | 12.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.6 | 3.22 | 0.01 | 9433.64 | 70.21 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.44 | 0.09 | 178541.08 | 8.88 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.32 | 0.06 | 56319.19 | 24.05 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.51 | 0.07 | 173859.98 | 35.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.62 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
