# Hulk DIGEST — 2026-09-14T00:34:31Z

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
| XRPUSDT | IDLE | 1.14 | 2.12 | 1.13 | -0.01 | 18794837.93 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 1.12 | 2.06 | 1.25 | -0.02 | 284938903.75 | 1.13 | skipped_fast |
| BTCUSDT | IDLE | 0.75 | 1.39 | 0.79 | -0.01 | 294550880.52 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.31 | 4.44 | 2.9 | 0.02 | 456918.99 | 5.34 | skipped_fast |
| RWAINCUSDT | IDLE | 3.86 | 7.11 | 4.01 | -0.01 | 9357.03 | 21.94 | skipped_fast |
| WUSDT | IDLE | 2.86 | 5.11 | 4.1 | -0.02 | 220089.22 | 15.29 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 7.47 | 6.0 | -0.14 | 95499.12 | 16.91 | skipped_fast |
| CCUSDT | IDLE | 1.16 | 2.17 | 1.01 | -0.03 | 315652.25 | 9.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.8 | 3.32 | 1.88 | 0.01 | 201484.72 | 31.03 | skipped_fast |
| EDELUSDT | IDLE | 1.66 | 5.84 | 0.59 | 0.11 | 198989.86 | 29.56 | skipped_fast |
| BIOUSDT | IDLE | 2.05 | 3.8 | 1.95 | -0.01 | 70210.5 | 3.97 | skipped_fast |
| HBARUSDT | IDLE | 2.0 | 3.62 | 2.48 | 0.01 | 244443.62 | 2.65 | skipped_fast |
| REDUSDT | IDLE | 1.47 | 2.74 | 1.27 | -0.01 | 64088.02 | 17.64 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.76 | 0.88 | -0.0 | 60327.84 | 14.95 | skipped_fast |
| QNTUSDT | IDLE | 2.56 | 4.52 | 4.05 | -0.03 | 37953.13 | 3.2 | skipped_fast |
| RIZEUSDT | IDLE | 0.49 | 6.89 | 6.05 | -0.09 | 65757.85 | 46.5 | skipped_fast |
| TELUSDT | IDLE | 1.5 | 2.7 | 1.94 | -0.05 | 84152.15 | 44.69 | skipped_fast |
| FLUIDUSDT | IDLE | 1.15 | 2.0 | 1.96 | -0.01 | 1325.28 | 22.11 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.67 | 0.52 | 0.0 | 54766.38 | 14.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.47 | 0.43 | -0.0 | 30192.35 | 15.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
