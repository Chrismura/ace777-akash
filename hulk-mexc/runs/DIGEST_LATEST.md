# Hulk DIGEST — 2026-08-22T04:42:42Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.91 | 14.68 | 0.04 | 0.21 | 11689746.7 | 3.61 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.35 | 16.04 | 0.2 | 0.26 | 174436429.63 | 5.46 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 8.85 | 0.08 | 0.14 | 1066269.06 | 1.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.05 | 0.2 | 736517.2 | 4.09 | skipped_fast |
| CHIPUSDT | IDLE | 2.79 | 5.36 | 1.44 | 0.02 | 451140.43 | 2.98 | skipped_fast |
| WUSDT | IDLE | 2.0 | 7.62 | 0.05 | 0.15 | 435289.75 | 7.7 | skipped_fast |
| BIOUSDT | IDLE | 2.95 | 7.36 | 1.26 | 0.07 | 200769.35 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 4.29 | 1.01 | 0.13 | 537787.33 | 27.02 | skipped_fast |
| EDELUSDT | IDLE | 2.03 | 4.07 | 2.82 | -0.03 | 80261.64 | 11.17 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 8.56 | 4.26 | 0.1 | 181840.77 | 2.95 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.83 | 0.09 | 58588.51 | 46.13 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.65 | 0.2 | 158216.86 | 17.53 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.3 | 0.13 | 67993.04 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.48 | 0.01 | 9348.0 | 21.77 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 1.73 | 4.48 | 0.05 | 0.1 | 177846.11 | 44.92 | skipped_fast |
| RWAUSDT | IDLE | 1.52 | 3.05 | 0.0 | 0.06 | 56639.14 | 24.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
