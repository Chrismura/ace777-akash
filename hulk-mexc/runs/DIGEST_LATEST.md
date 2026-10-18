# Hulk DIGEST — 2026-10-18T00:03:25Z

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
| ETHUSDT | IDLE | 1.47 | 2.79 | 1.05 | -0.01 | 88585186.9 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.44 | 2.74 | 0.99 | -0.01 | 17083928.52 | 1.55 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 9.68 | 5.48 | -0.09 | 1063985.48 | 2.51 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.06 | 0.34 | -0.0 | 173802387.1 | 0.15 | skipped_fast |
| WUSDT | IDLE | 1.87 | 5.68 | 2.45 | -0.03 | 987942.67 | 15.83 | skipped_fast |
| QNTUSDT | IDLE | 2.82 | 5.23 | 2.7 | -0.03 | 600219.78 | 2.56 | skipped_fast |
| BIOUSDT | IDLE | 2.31 | 4.41 | 1.46 | -0.04 | 71413.61 | 4.12 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 2.74 | 1.67 | -0.0 | 256622.4 | 6.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.07 | 5.85 | 2.44 | -0.07 | 84159.63 | 13.87 | skipped_fast |
| ZBCNUSDT | IDLE | 1.47 | 2.79 | 0.97 | -0.01 | 188398.88 | 18.07 | skipped_fast |
| REDUSDT | IDLE | 1.87 | 3.41 | 2.2 | -0.05 | 61784.33 | 9.4 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 2.64 | 2.26 | -0.05 | 149336.37 | 17.78 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 3.83 | 1.84 | -0.05 | 69377.08 | 2.58 | skipped_fast |
| HBARUSDT | IDLE | 1.92 | 3.74 | 0.63 | 0.02 | 243166.5 | 5.87 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 3.53 | 2.48 | 0.06 | 21575.14 | 5.3 | skipped_fast |
| TELUSDT | IDLE | 2.02 | 3.59 | 2.99 | -0.06 | 103415.27 | 12.32 | skipped_fast |
| RIZEUSDT | IDLE | 1.21 | 2.28 | 0.89 | -0.02 | 50304.16 | 58.86 | skipped_fast |
| RWAUSDT | IDLE | 1.34 | 2.52 | 1.03 | -0.01 | 51589.33 | 16.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.42 | 2.69 | 0.97 | -0.01 | 1814.21 | 21.43 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.58 | 0.55 | -0.0 | 30872.82 | 9.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
