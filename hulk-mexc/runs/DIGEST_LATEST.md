# Hulk DIGEST — 2026-08-22T04:01:36Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.76 | 11.77 | 0.26 | 0.18 | 9357396.06 | 12.99 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 12.22 | 1.78 | 0.2 | 166325114.47 | 3.82 | skipped_fast |
| CCUSDT | IDLE | 1.98 | 10.1 | 0.11 | 0.21 | 710019.18 | 7.39 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 6.03 | 0.59 | 0.1 | 1013488.76 | 1.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.83 | 5.36 | 1.94 | -0.03 | 458839.99 | 6.0 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.32 | 0.07 | 199248.47 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.97 | 7.18 | 0.64 | 0.14 | 428041.82 | 4.86 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.63 | 0.13 | 537524.04 | 9.05 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80627.46 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.7 | 0.11 | 59266.11 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.78 | 0.23 | 157748.25 | 19.59 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.29 | 0.13 | 67548.41 | 20.32 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.56 | 0.09 | 178519.31 | 11.87 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.16 | 0.06 | 56374.73 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.4 | 0.41 | 0.07 | 174222.0 | 35.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 48.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
