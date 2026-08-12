# Hulk DIGEST — 2026-08-12T22:28:43Z

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
| XRPUSDT | IDLE | 0.52 | 0.96 | 0.48 | -0.01 | 14510901.86 | 1.98 | skipped_fast |
| CHIPUSDT | IDLE | 2.88 | 6.56 | 3.51 | 0.05 | 103626.86 | 8.56 | skipped_fast |
| PYTHUSDT | IDLE | 1.56 | 2.84 | 1.81 | -0.04 | 328227.31 | 2.49 | skipped_fast |
| EDELUSDT | IDLE | 2.32 | 8.52 | 4.4 | 0.09 | 71987.21 | 32.89 | skipped_fast |
| BIOUSDT | IDLE | 2.23 | 3.98 | 3.18 | -0.05 | 62247.4 | 4.21 | skipped_fast |
| REDUSDT | IDLE | 2.27 | 4.0 | 3.56 | -0.02 | 60772.81 | 11.9 | skipped_fast |
| WUSDT | IDLE | 1.75 | 3.2 | 2.05 | -0.04 | 186876.46 | 16.2 | skipped_fast |
| ZBCNUSDT | IDLE | 1.65 | 3.06 | 1.64 | -0.04 | 189297.1 | 18.37 | skipped_fast |
| QNTUSDT | IDLE | 3.16 | 5.57 | 4.97 | 0.01 | 60339.38 | 5.17 | skipped_fast |
| RWAINCUSDT | IDLE | 2.12 | 4.03 | 1.36 | -0.01 | 1626.25 | 58.15 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.85 | 0.47 | -0.03 | 60413.01 | 12.73 | skipped_fast |
| CCUSDT | IDLE | 0.67 | 1.2 | 0.94 | -0.02 | 214438.26 | 9.13 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 7.29 | 1.06 | 0.13 | 48437.0 | 32.54 | skipped_fast |
| QAITUSDT | IDLE | 0.68 | 2.51 | 1.67 | -0.05 | 4222.39 | 60.51 | skipped_fast |
| TELUSDT | IDLE | 0.86 | 1.67 | 0.38 | 0.02 | 96418.13 | 38.07 | skipped_fast |
| HBARUSDT | IDLE | 0.41 | 0.75 | 0.44 | -0.01 | 84368.17 | 1.52 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.0 | 0.66 | 0.01 | 51649.36 | 16.63 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 0.64 | 0.23 | -0.02 | 557.16 | 24.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
