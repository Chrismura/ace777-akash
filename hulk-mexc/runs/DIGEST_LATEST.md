# Hulk DIGEST — 2026-08-29T18:11:46Z

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
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.07 | 74.23 | 38.5 | -0.02 | 137033.6 | 18.0 | skipped_fast |
| XRPUSDT | IDLE | 0.8 | 1.48 | 0.77 | 0.01 | 20651467.11 | 2.87 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.93 | 1.7 | -0.04 | 1008169.99 | 4.87 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.73 | 9.65 | 7.58 | 0.04 | 67801.35 | 8.48 | skipped_fast |
| RIZEUSDT | IDLE | 3.77 | 7.59 | 4.68 | -0.02 | 36740.18 | 58.87 | skipped_fast |
| PYTHUSDT | IDLE | 1.68 | 3.12 | 1.62 | 0.02 | 330661.87 | 2.09 | skipped_fast |
| CCUSDT | IDLE | 1.6 | 3.12 | 0.57 | 0.06 | 212201.24 | 4.28 | skipped_fast |
| REDUSDT | IDLE | 2.04 | 4.04 | 3.88 | 0.04 | 76446.36 | 10.22 | skipped_fast |
| ZBCNUSDT | IDLE | 1.55 | 2.74 | 2.39 | -0.04 | 188140.11 | 5.67 | skipped_fast |
| WUSDT | IDLE | 1.25 | 2.3 | 1.39 | 0.0 | 186719.7 | 5.48 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.53 | 1.19 | -0.01 | 64220.95 | 3.64 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.31 | 0.57 | -0.01 | 193929.77 | 1.33 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.15 | 1.65 | -0.03 | 70393.99 | 17.41 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.12 | 1.11 | -0.04 | 3664.71 | 105.76 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 1.28 | 0.99 | 0.0 | 29341.44 | 4.92 | skipped_fast |
| FLUIDUSDT | IDLE | 0.43 | 0.86 | 0.0 | 0.0 | 1985.37 | 2.31 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.58 | 0.16 | 0.01 | 53863.33 | 24.68 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
