# Hulk DIGEST — 2026-09-02T08:36:07Z

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
| XRPUSDT | IDLE | 0.93 | 1.63 | 1.59 | -0.02 | 37479592.54 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 0.58 | 1.01 | 0.99 | -0.02 | 359172827.92 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.91 | 0.89 | -0.01 | 503499821.4 | 0.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 7.58 | 0.13 | 0.16 | 952600.65 | 2.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 7.01 | 2.65 | 0.12 | 817427.56 | 3.65 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.91 | 16.28 | 5.77 | 0.05 | 173549.02 | 32.55 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.84 | 2.11 | 0.02 | 406977.99 | 11.42 | skipped_fast |
| CCUSDT | IDLE | 2.25 | 4.27 | 3.66 | -0.07 | 338790.18 | 10.71 | skipped_fast |
| RWAINCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.41 | 10.57 | 1.64 | 0.1 | 10357.02 | 21.45 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 9.77 | 0.73 | 0.16 | 75019.15 | 16.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 2.67 | 1.98 | -0.01 | 216365.56 | 11.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.9 | 6.4 | 5.85 | -0.12 | 39451.28 | 78.72 | skipped_fast |
| QNTUSDT | IDLE | 2.54 | 6.12 | 2.96 | 0.06 | 63148.75 | 7.67 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.94 | 1.22 | 0.0 | 154473.85 | 11.7 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 1.34 | 1.32 | -0.03 | 74350.45 | 3.93 | skipped_fast |
| HBARUSDT | IDLE | 0.53 | 0.96 | 0.62 | -0.0 | 229173.27 | 1.35 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 1.73 | 1.64 | -0.02 | 87210.69 | 65.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.73 | 1.47 | 0.0 | -0.03 | 323.84 | 0.78 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.62 | 0.38 | -0.01 | 50539.92 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.66 | 0.29 | -0.02 | 36095.25 | 63.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
