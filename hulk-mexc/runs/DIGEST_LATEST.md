# Hulk DIGEST — 2026-08-28T13:07:47Z

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
| XRPUSDT | IDLE | 1.13 | 2.15 | 0.71 | -0.0 | 48894019.76 | 2.11 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 2.86 | 2.51 | -0.02 | 1235615.16 | 2.09 | skipped_fast |
| CHIPUSDT | IDLE | 2.65 | 13.26 | 2.67 | 0.2 | 908195.91 | 20.59 | skipped_fast |
| ZBCNUSDT | IDLE | 2.02 | 4.26 | 2.32 | 0.01 | 257378.42 | 5.71 | skipped_fast |
| CCUSDT | IDLE | 1.25 | 2.37 | 0.9 | -0.03 | 406174.81 | 6.22 | skipped_fast |
| REDUSDT | IDLE | 1.78 | 3.25 | 2.01 | -0.04 | 73078.73 | 12.2 | skipped_fast |
| WUSDT | IDLE | 1.15 | 2.13 | 1.07 | -0.02 | 187196.22 | 12.72 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 9.19 | 2.83 | -0.18 | 115488.45 | 54.62 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.24 | 1.1 | -0.01 | 74837.18 | 8.64 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 2.02 | 0.73 | -0.01 | 83007.5 | 3.5 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.43 | 0.8 | -0.01 | 308930.97 | 2.57 | skipped_fast |
| EDELUSDT | IDLE | 0.49 | 2.26 | 1.11 | -0.13 | 54801.72 | 42.94 | skipped_fast |
| RWAINCUSDT | IDLE | 1.2 | 4.22 | 0.0 | 0.02 | 19255.41 | 112.51 | skipped_fast |
| QNTUSDT | IDLE | 1.28 | 2.29 | 1.86 | -0.0 | 46445.01 | 1.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.63 | 2.93 | 2.22 | -0.03 | 4504.61 | 22.34 | skipped_fast |
| RWAUSDT | IDLE | 1.19 | 2.11 | 1.82 | -0.0 | 53241.51 | 16.82 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.11 | 1.47 | -0.01 | 133857.76 | 44.08 | skipped_fast |
| QAITUSDT | IDLE | 0.4 | 5.19 | 2.84 | -0.18 | 43793.71 | 211.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
