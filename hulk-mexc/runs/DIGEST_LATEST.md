# Hulk DIGEST — 2026-08-17T08:15:36Z

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
| XRPUSDT | IDLE | 0.37 | 0.65 | 0.59 | -0.0 | 9692208.57 | 1.0 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.1 | 15.04 | 1.8 | 0.16 | 336302.32 | 15.37 | skipped_fast |
| WUSDT | IDLE | 1.1 | 1.94 | 1.77 | 0.01 | 186788.41 | 11.9 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 2.97 | 0.56 | 0.01 | 64095.01 | 4.03 | skipped_fast |
| CCUSDT | IDLE | 0.71 | 1.34 | 0.49 | -0.01 | 251999.62 | 6.28 | skipped_fast |
| PYTHUSDT | IDLE | 1.02 | 1.96 | 0.51 | 0.0 | 166179.1 | 2.54 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 2.75 | 2.27 | -0.04 | 58135.11 | 18.99 | skipped_fast |
| KITEUSDT | IDLE | 1.44 | 2.54 | 2.3 | -0.01 | 53644.11 | 15.0 | skipped_fast |
| ZBCNUSDT | IDLE | 0.58 | 1.1 | 0.34 | 0.01 | 175973.45 | 12.06 | skipped_fast |
| EDELUSDT | IDLE | 1.28 | 2.49 | 0.51 | 0.05 | 55303.36 | 38.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.36 | 11.25 | 0.57 | 0.14 | 48411.15 | 173.79 | skipped_fast |
| QAITUSDT | IDLE | 0.96 | 2.41 | 0.0 | -0.01 | 2368.59 | 61.12 | skipped_fast |
| RWAINCUSDT | IDLE | 0.55 | 1.02 | 0.56 | -0.02 | 2234.64 | 51.21 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.57 | 0.64 | 0.01 | 108652.48 | 1.53 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.65 | 1.42 | -0.0 | 87439.14 | 13.73 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.28 | 0.68 | -0.03 | 31496.97 | 3.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.66 | 1.28 | 0.01 | 823.44 | 21.89 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.17 | 0.01 | 48725.01 | 17.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
