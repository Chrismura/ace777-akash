# Hulk DIGEST — 2026-08-20T17:26:04Z

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
| XRPUSDT | IDLE | 1.96 | 12.41 | 0.37 | 0.25 | 85277099.35 | 1.52 | skipped_fast |
| PYTHUSDT | IDLE | 1.01 | 3.22 | 0.36 | 0.11 | 1196836.3 | 2.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.63 | 12.78 | 1.77 | 0.12 | 262658.64 | 36.1 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 3.17 | 2.54 | 0.07 | 503393.18 | 4.89 | skipped_fast |
| CHIPUSDT | IDLE | 1.77 | 5.17 | 2.86 | 0.08 | 301863.64 | 3.3 | skipped_fast |
| WUSDT | IDLE | 1.85 | 3.68 | 0.11 | 0.06 | 314555.62 | 15.58 | skipped_fast |
| TELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.73 | 17.01 | 0.52 | 0.24 | 171722.25 | 25.91 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 4.88 | 3.67 | 0.09 | 239585.73 | 3.28 | skipped_fast |
| HBARUSDT | IDLE | 1.49 | 2.85 | 0.86 | 0.06 | 456195.07 | 4.06 | skipped_fast |
| KITEUSDT | IDLE | 1.95 | 3.89 | 0.04 | 0.05 | 59100.49 | 13.03 | skipped_fast |
| REDUSDT | IDLE | 0.75 | 5.14 | 3.84 | 0.02 | 190603.89 | 14.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 6.9 | 3.25 | 0.06 | 57055.51 | 24.91 | skipped_fast |
| EDELUSDT | IDLE | 0.99 | 4.87 | 0.22 | 0.12 | 96782.21 | 21.65 | skipped_fast |
| RWAINCUSDT | IDLE | 1.48 | 2.95 | 0.0 | 0.04 | 6556.66 | 22.22 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | 0.0 | 5270.43 | 62.35 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 4.25 | 2.69 | 0.08 | 64454.51 | 3.22 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.55 | 0.0 | 0.08 | 2310.91 | 21.02 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.12 | 0.34 | 0.01 | 51747.19 | 8.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
