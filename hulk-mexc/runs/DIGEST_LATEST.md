# Hulk DIGEST — 2026-10-06T23:40:04Z

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
| QNTUSDT | IDLE | 2.92 | 5.6 | 1.62 | 0.02 | 2292538.46 | 5.67 | skipped_fast |
| XRPUSDT | IDLE | 0.61 | 1.06 | 1.01 | -0.01 | 26614205.38 | 1.34 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.03 | 0.52 | -0.01 | 316111514.47 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.29 | 0.52 | 0.36 | -0.0 | 549831901.44 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.76 | 3.08 | 2.9 | -0.04 | 838826.87 | 2.64 | skipped_fast |
| CHIPUSDT | IDLE | 2.93 | 6.77 | 1.2 | 0.04 | 200025.52 | 12.89 | skipped_fast |
| EDELUSDT | IDLE | 1.99 | 6.25 | 4.18 | -0.09 | 386171.05 | 50.93 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 2.94 | 1.89 | 0.01 | 428832.57 | 9.42 | skipped_fast |
| WUSDT | IDLE | 1.67 | 3.21 | 0.9 | 0.01 | 413523.44 | 7.49 | skipped_fast |
| RIZEUSDT | IDLE | 1.36 | 14.14 | 9.98 | -0.01 | 100122.56 | 54.6 | skipped_fast |
| ZBCNUSDT | IDLE | 1.38 | 2.43 | 2.2 | -0.01 | 239792.69 | 11.77 | skipped_fast |
| TELUSDT | IDLE | 2.88 | 5.61 | 1.01 | 0.02 | 125701.02 | 20.45 | skipped_fast |
| RWAINCUSDT | IDLE | 2.43 | 4.37 | 3.26 | -0.04 | 26176.84 | 86.69 | skipped_fast |
| BIOUSDT | IDLE | 1.52 | 2.86 | 1.2 | -0.01 | 80796.71 | 3.13 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.72 | 1.69 | -0.02 | 444200.78 | 7.04 | skipped_fast |
| KITEUSDT | IDLE | 0.93 | 1.8 | 0.34 | 0.01 | 57819.37 | 9.88 | skipped_fast |
| REDUSDT | IDLE | 0.57 | 1.02 | 0.86 | -0.06 | 60337.33 | 8.65 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 3.38 | 0.71 | -0.08 | 79696.74 | 12.93 | skipped_fast |
| MNSRYUSDT | IDLE | 0.8 | 1.45 | 0.97 | -0.0 | 38015.41 | 20.61 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.66 | 0.59 | -0.0 | 51821.22 | 7.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
