# Hulk DIGEST — 2026-08-22T02:13:50Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 8.42 | 1.02 | 0.14 | 6916727.72 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 10.08 | 0.57 | 0.17 | 154390438.1 | 0.67 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.88 | 0.09 | 545731.25 | 13.56 | skipped_fast |
| HBARUSDT | IDLE | 2.3 | 4.9 | 0.25 | 0.08 | 955183.53 | 1.24 | skipped_fast |
| CCUSDT | IDLE | 1.68 | 6.1 | 0.4 | 0.14 | 654124.09 | 10.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.85 | 4.28 | 0.0 | 0.0 | 513330.0 | 3.02 | skipped_fast |
| BIOUSDT | IDLE | 2.98 | 6.88 | 0.21 | 0.09 | 191646.03 | 2.97 | skipped_fast |
| WUSDT | IDLE | 1.72 | 4.41 | 0.22 | 0.08 | 400110.17 | 11.11 | skipped_fast |
| EDELUSDT | IDLE | 2.34 | 5.02 | 0.98 | -0.01 | 79541.33 | 32.95 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.77 | 0.11 | 61189.3 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.95 | 0.18 | 156858.59 | 16.98 | skipped_fast |
| QNTUSDT | IDLE | 2.29 | 4.89 | 0.93 | 0.07 | 171258.33 | 4.52 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.51 | 0.12 | 61416.68 | 11.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.01 | 9604.71 | 59.6 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.11 | 1.53 | 0.04 | 179144.64 | 62.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 22.57 | skipped_fast |
| QAITUSDT | IDLE | 1.93 | 3.57 | 1.92 | -0.01 | 3904.51 | 222.58 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54840.93 | 24.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
