# Hulk DIGEST — 2026-08-28T12:08:05Z

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
| XRPUSDT | IDLE | 1.13 | 2.15 | 0.77 | -0.0 | 48547581.73 | 2.11 | skipped_fast |
| PYTHUSDT | IDLE | 1.7 | 3.05 | 2.39 | -0.01 | 1250183.74 | 2.07 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 10.77 | 0.0 | 0.18 | 870909.19 | 31.79 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 2.55 | 0.29 | -0.01 | 419464.42 | 9.69 | skipped_fast |
| REDUSDT | IDLE | 2.45 | 4.32 | 3.83 | -0.04 | 80366.53 | 10.41 | skipped_fast |
| KITEUSDT | IDLE | 2.43 | 4.27 | 3.95 | -0.03 | 75688.33 | 8.73 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 4.26 | 1.02 | 0.02 | 250462.96 | 19.71 | skipped_fast |
| WUSDT | IDLE | 0.99 | 1.91 | 0.49 | -0.01 | 185757.3 | 15.84 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 9.19 | 3.42 | -0.2 | 115087.32 | 57.04 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 2.02 | 0.8 | -0.01 | 85148.94 | 3.51 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.54 | 0.7 | -0.01 | 323020.75 | 2.57 | skipped_fast |
| FLUIDUSDT | IDLE | 2.26 | 4.04 | 3.26 | -0.03 | 4504.61 | 23.2 | skipped_fast |
| EDELUSDT | IDLE | 0.5 | 2.26 | 2.13 | -0.03 | 54577.39 | 17.35 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.21 | 1.35 | -0.01 | 133253.02 | 43.81 | skipped_fast |
| RWAINCUSDT | IDLE | 0.9 | 3.17 | 0.0 | 0.01 | 19420.48 | 118.79 | skipped_fast |
| QNTUSDT | IDLE | 1.17 | 2.29 | 0.27 | 0.02 | 40458.48 | 6.33 | skipped_fast |
| QAITUSDT | IDLE | 0.33 | 4.31 | 1.39 | -0.17 | 42954.91 | 162.93 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.66 | 0.58 | 0.01 | 53487.63 | 16.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
