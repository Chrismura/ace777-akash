# Hulk DIGEST — 2026-08-22T03:00:21Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 9.55 | 1.3 | 0.14 | 7403513.36 | 1.91 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.54 | 13.33 | 0.41 | 0.2 | 159603581.5 | 3.23 | skipped_fast |
| HBARUSDT | IDLE | 2.58 | 6.77 | 0.05 | 0.1 | 992010.46 | 3.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 9.63 | 2.17 | 0.11 | 541052.63 | 22.12 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 8.48 | 0.0 | 0.19 | 665451.95 | 10.91 | skipped_fast |
| BIOUSDT | IDLE | 3.0 | 7.36 | 2.05 | 0.08 | 194361.77 | 5.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 4.28 | 0.0 | 0.0 | 451597.75 | 2.97 | skipped_fast |
| WUSDT | IDLE | 1.67 | 5.04 | 0.04 | 0.12 | 416246.91 | 12.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.41 | 0.1 | 61382.22 | 44.22 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 3.83 | 2.39 | -0.03 | 79943.62 | 22.25 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.47 | 0.2 | 158034.64 | 11.92 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 48.79 | skipped_fast |
| KITEUSDT | IDLE | 1.3 | 4.03 | 0.14 | 0.12 | 62462.38 | 11.66 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 3.97 | 0.18 | 0.09 | 172676.47 | 1.49 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.31 | 0.16 | 0.05 | 56169.6 | 8.09 | skipped_fast |
| TELUSDT | IDLE | 0.82 | 1.88 | 0.87 | 0.06 | 173328.92 | 51.65 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 16.83 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
