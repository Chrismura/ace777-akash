# Hulk DIGEST — 2026-09-14T05:41:45Z

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
| XRPUSDT | IDLE | 1.7 | 3.39 | 0.09 | 0.01 | 24780953.8 | 2.17 | skipped_fast |
| ETHUSDT | IDLE | 1.11 | 2.2 | 0.18 | -0.0 | 312963838.93 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.0 | 1.94 | 0.35 | 0.0 | 382717163.31 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.51 | 49.46 | 19.2 | 0.28 | 74855.71 | 11.63 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 9.85 | 6.51 | -0.0 | 114217.0 | 16.68 | skipped_fast |
| PYTHUSDT | IDLE | 2.06 | 4.78 | 1.04 | 0.05 | 521015.36 | 3.45 | skipped_fast |
| WUSDT | IDLE | 2.68 | 5.31 | 0.36 | 0.01 | 189425.17 | 10.78 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.01 | 8.94 | 0.14 | 0.14 | 228076.58 | 21.22 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.69 | 0.93 | -0.02 | 324619.28 | 7.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.85 | 3.47 | 1.56 | -0.01 | 208253.42 | 21.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 7.62 | 2.02 | -0.09 | 103529.58 | 16.21 | skipped_fast |
| BIOUSDT | IDLE | 1.75 | 3.41 | 0.62 | -0.0 | 67615.41 | 3.9 | skipped_fast |
| KITEUSDT | IDLE | 1.71 | 3.2 | 1.47 | -0.01 | 59362.18 | 12.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 2.07 | 1.09 | -0.01 | 9552.11 | 5.54 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 2.0 | 0.01 | 0.01 | 269791.65 | 1.31 | skipped_fast |
| QNTUSDT | IDLE | 1.2 | 2.39 | 0.09 | -0.0 | 36301.18 | 6.27 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.75 | 0.85 | -0.01 | 1263.3 | 21.85 | skipped_fast |
| TELUSDT | IDLE | 1.15 | 2.25 | 0.38 | -0.03 | 85097.47 | 44.15 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.74 | 0.3 | 0.0 | 52554.04 | 22.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.21 | 0.18 | -0.0 | 30037.12 | 4.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
