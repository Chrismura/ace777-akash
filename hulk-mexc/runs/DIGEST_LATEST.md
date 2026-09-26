# Hulk DIGEST — 2026-09-26T11:59:10Z

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
| XRPUSDT | IDLE | 0.69 | 1.3 | 0.58 | -0.03 | 92521432.02 | 1.94 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.66 | 0.3 | -0.01 | 226957051.83 | 0.33 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.51 | 0.17 | -0.01 | 501592843.23 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.3 | 6.73 | 0.2 | 0.09 | 1152449.16 | 3.84 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 5.09 | 3.33 | 0.09 | 988344.41 | 8.91 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 10.52 | 4.72 | 0.07 | 773355.53 | 4.78 | skipped_fast |
| WUSDT | IDLE | 2.16 | 5.85 | 0.58 | 0.08 | 487440.73 | 10.08 | skipped_fast |
| EDELUSDT | IDLE | 2.66 | 5.11 | 1.39 | 0.02 | 178180.15 | 9.86 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.5 | 0.68 | -0.01 | 718953.81 | 3.19 | skipped_fast |
| RWAINCUSDT | IDLE | 2.59 | 4.93 | 3.75 | 0.03 | 5741.99 | 19.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 2.89 | 1.76 | 0.0 | 138056.58 | 14.4 | skipped_fast |
| BIOUSDT | IDLE | 1.44 | 3.25 | 1.89 | 0.04 | 125637.65 | 3.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 2.52 | 0.27 | -0.03 | 227375.48 | 32.31 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 9.26 | 3.96 | -0.17 | 49554.8 | 52.22 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 1.92 | 1.8 | -0.01 | 58916.64 | 14.19 | skipped_fast |
| RWAUSDT | IDLE | 2.35 | 4.31 | 2.64 | -0.0 | 55661.06 | 14.64 | skipped_fast |
| KITEUSDT | IDLE | 0.99 | 2.24 | 0.94 | 0.04 | 74374.96 | 16.21 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 2.64 | 2.51 | -0.05 | 120424.64 | 18.84 | skipped_fast |
| FLUIDUSDT | IDLE | 1.53 | 3.07 | 0.0 | 0.0 | 3424.92 | 22.0 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.05 | 0.0 | 38837.4 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
