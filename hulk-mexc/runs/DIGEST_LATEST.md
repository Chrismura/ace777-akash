# Hulk DIGEST — 2026-08-16T14:04:33Z

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
| XRPUSDT | IDLE | 0.29 | 0.54 | 0.22 | -0.0 | 4870410.47 | 2.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.44 | 15.73 | 7.13 | 0.19 | 230154.41 | 10.21 | skipped_fast |
| QAITUSDT | IDLE | 3.28 | 10.06 | 3.82 | -0.05 | 2615.08 | 62.04 | skipped_fast |
| EDELUSDT | IDLE | 2.74 | 5.22 | 1.7 | -0.01 | 66384.22 | 39.76 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.93 | 0.81 | 0.03 | 139507.18 | 12.78 | skipped_fast |
| CCUSDT | IDLE | 1.0 | 2.0 | 0.58 | 0.0 | 313189.4 | 6.23 | skipped_fast |
| RIZEUSDT | IDLE | 2.15 | 4.27 | 1.73 | -0.04 | 48892.78 | 28.05 | skipped_fast |
| ZBCNUSDT | IDLE | 0.44 | 0.81 | 0.46 | -0.02 | 209102.09 | 18.62 | skipped_fast |
| PYTHUSDT | IDLE | 0.51 | 0.92 | 0.71 | -0.02 | 99904.43 | 2.55 | skipped_fast |
| BIOUSDT | IDLE | 0.6 | 1.1 | 0.6 | -0.01 | 65755.19 | 4.04 | skipped_fast |
| KITEUSDT | IDLE | 0.52 | 0.9 | 0.87 | -0.03 | 58162.47 | 14.87 | skipped_fast |
| REDUSDT | IDLE | 0.16 | 1.34 | 0.92 | -0.01 | 89352.93 | 25.15 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 2.59 | 1.23 | -0.02 | 97061.6 | 48.46 | skipped_fast |
| RWAINCUSDT | IDLE | 0.21 | 0.56 | 0.39 | 0.1 | 8826.23 | 44.54 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.74 | 0.0 | 0.02 | 102.3 | 22.47 | skipped_fast |
| HBARUSDT | IDLE | 0.11 | 0.22 | 0.06 | -0.01 | 79572.74 | 1.54 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.53 | 0.17 | -0.01 | 51812.21 | 17.48 | skipped_fast |
| QNTUSDT | IDLE | 0.22 | 0.4 | 0.24 | -0.01 | 32596.27 | 3.48 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
