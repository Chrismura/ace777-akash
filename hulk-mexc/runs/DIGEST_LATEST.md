# Hulk DIGEST — 2026-08-22T01:39:17Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 10.86 | 0.75 | 0.16 | 6795184.07 | 13.63 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.27 | 9.41 | 0.09 | 0.16 | 151408017.94 | 2.68 | skipped_fast |
| HBARUSDT | IDLE | 2.96 | 6.36 | 0.05 | 0.09 | 960578.33 | 4.96 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.8 | 0.09 | 550887.63 | 17.91 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.17 | 0.17 | 662283.95 | 6.11 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.54 | 0.09 | 392931.24 | 12.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.97 | 0.01 | 513120.4 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.57 | 0.94 | 0.04 | 186367.81 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79541.18 | 11.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.21 | 0.11 | 60822.37 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.99 | 0.17 | 158622.55 | 8.01 | skipped_fast |
| TELUSDT | IDLE | 2.6 | 6.19 | 1.33 | 0.05 | 182004.52 | 20.73 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.17 | 0.0 | 0.13 | 61662.14 | 8.95 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 1.03 | 0.07 | 170737.65 | 9.03 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.73 | 3.27 | 1.32 | 0.03 | 9649.22 | 53.33 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.92 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54764.58 | 24.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
