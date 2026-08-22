# Hulk DIGEST — 2026-08-22T08:16:31Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.2 | 0.03 | 26707932.71 | 7.8 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 23.87 | 8.62 | 0.15 | 224251241.33 | 2.58 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.23 | 0.04 | 1357561.97 | 6.34 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.28 | 24.54 | 11.44 | -0.09 | 684759.47 | 6.64 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.26 | 17.58 | 7.35 | 0.05 | 610729.01 | 15.42 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 29.98 | 8.31 | -0.02 | 247586.53 | 3.15 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 42.01 | 11.05 | 0.07 | 154460.09 | 12.22 | tvl≈2,081,438 |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 11.25 | 1.94 | 0.2 | 822428.45 | 8.16 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 8.47 | 5.91 | 0.03 | 537527.62 | 20.95 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 13.91 | 8.21 | 0.04 | 194211.74 | 9.21 | n/a |
| KITEUSDT | IDLE | 3.78 | 9.68 | 3.58 | 0.07 | 72914.54 | 11.76 | no_map |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 19.48 | tvl≈2,556,699,557 |
| EDELUSDT | IDLE | 2.24 | 4.52 | 2.81 | -0.02 | 87017.0 | 33.43 | no_map |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11216.08 | 112.81 | no_map |
| TELUSDT | IDLE | 1.85 | 4.7 | 3.85 | -0.01 | 173723.24 | 30.79 | no_map |
| RIZEUSDT | IDLE | 0.84 | 3.73 | 0.78 | 0.0 | 52291.88 | 44.42 | no_map |
| RWAUSDT | IDLE | 1.72 | 3.29 | 0.96 | 0.05 | 58207.77 | 16.1 | no_map |
| QAITUSDT | IDLE | 1.42 | 2.71 | 0.86 | 0.02 | 3187.61 | 152.61 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
