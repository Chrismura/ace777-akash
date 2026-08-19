# Hulk DIGEST — 2026-08-19T19:12:00Z

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
| XRPUSDT | IDLE | 2.96 | 5.83 | 0.54 | 0.07 | 26224455.36 | 0.94 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.01 | 17.68 | 8.85 | 0.01 | 120705.11 | 13.84 | skipped_fast |
| CCUSDT | IDLE | 3.83 | 11.04 | 2.26 | 0.08 | 296238.76 | 7.17 | skipped_fast |
| RIZEUSDT | IDLE | 4.25 | 8.15 | 3.41 | -0.02 | 44789.03 | 11.44 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 19.8 | 7.5 | 0.09 | 167485.58 | 44.6 | skipped_fast |
| PYTHUSDT | IDLE | 2.82 | 5.55 | 0.64 | 0.03 | 252221.1 | 2.48 | skipped_fast |
| BIOUSDT | IDLE | 2.63 | 13.4 | 3.55 | 0.16 | 131336.84 | 7.0 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.79 | 14.65 | 1.64 | 0.13 | 74433.34 | 94.9 | skipped_fast |
| ZBCNUSDT | IDLE | 2.84 | 7.73 | 0.01 | 0.1 | 200348.06 | 10.45 | skipped_fast |
| WUSDT | IDLE | 2.59 | 5.07 | 0.68 | 0.05 | 168922.77 | 14.12 | skipped_fast |
| QAITUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.27 | 9.16 | 1.07 | 0.03 | 11397.81 | 62.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 5.02 | 2.53 | 0.05 | 171830.79 | 3.55 | skipped_fast |
| KITEUSDT | IDLE | 2.32 | 4.5 | 0.87 | 0.04 | 56979.5 | 12.53 | skipped_fast |
| FLUIDUSDT | IDLE | 3.45 | 7.57 | 3.64 | 0.03 | 2835.1 | 20.41 | skipped_fast |
| HBARUSDT | IDLE | 2.15 | 4.08 | 1.45 | 0.05 | 254858.31 | 1.44 | skipped_fast |
| RWAINCUSDT | IDLE | 1.08 | 3.17 | 1.79 | 0.05 | 17149.78 | 22.84 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 3.54 | 1.37 | 0.03 | 38063.62 | 6.94 | skipped_fast |
| RWAUSDT | IDLE | 0.8 | 1.49 | 0.69 | 0.0 | 53969.24 | 17.44 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
