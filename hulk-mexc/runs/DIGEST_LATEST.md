# Hulk DIGEST — 2026-10-12T22:50:52Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 2.11 | 8.11 | 5.62 | 0.05 | 3406989.5 | 3.62 | skipped_fast |
| WUSDT | IDLE | 1.06 | 15.92 | 12.9 | -0.13 | 15335543.14 | 6.8 | skipped_fast |
| XRPUSDT | IDLE | 1.13 | 2.08 | 1.21 | -0.04 | 30068995.81 | 2.21 | skipped_fast |
| ETHUSDT | IDLE | 1.06 | 1.87 | 1.73 | -0.02 | 221457426.82 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.55 | 0.99 | 0.67 | -0.01 | 298432151.28 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.71 | 3.36 | 1.37 | -0.04 | 823010.87 | 2.62 | skipped_fast |
| EDELUSDT | IDLE | 1.55 | 6.93 | 2.14 | -0.1 | 289363.86 | 8.86 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 14.0 | 8.02 | -0.05 | 73055.1 | 73.97 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.65 | 1.92 | -0.06 | 600219.8 | 3.39 | skipped_fast |
| CCUSDT | IDLE | 0.85 | 1.5 | 1.32 | -0.04 | 394666.29 | 7.44 | skipped_fast |
| KITEUSDT | IDLE | 2.22 | 4.06 | 2.55 | -0.02 | 65538.43 | 8.73 | skipped_fast |
| REDUSDT | IDLE | 0.67 | 4.24 | 2.86 | 0.02 | 266622.39 | 8.39 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 3.0 | 2.35 | -0.07 | 75273.35 | 3.59 | skipped_fast |
| ZBCNUSDT | IDLE | 0.9 | 1.65 | 0.99 | 0.01 | 266423.7 | 22.47 | skipped_fast |
| CHIPUSDT | IDLE | 0.77 | 3.53 | 2.72 | -0.15 | 160815.85 | 12.01 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 2.2 | 0.15 | 0.01 | 32262.5 | 4.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.95 | 3.58 | 2.17 | -0.01 | 15558.91 | 21.15 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 2.79 | 1.47 | 0.02 | 120115.98 | 22.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.51 | 0.92 | 0.71 | -0.01 | 41252.65 | 27.53 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.15 | 0.0 | 52331.15 | 15.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
