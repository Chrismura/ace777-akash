# Hulk DIGEST — 2026-10-25T10:37:31Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 1.21 | 2.16 | 1.77 | -0.02 | 127798011.65 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 1.95 | 1.68 | 0.01 | 22671051.28 | 1.55 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.02 | 0.74 | -0.0 | 201836377.24 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.2 | 3.96 | 2.97 | -0.05 | 811713.19 | 16.76 | skipped_fast |
| PYTHUSDT | IDLE | 1.71 | 3.31 | 0.77 | 0.01 | 485954.3 | 1.41 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 3.33 | 3.02 | -0.08 | 535701.22 | 23.68 | skipped_fast |
| REDUSDT | IDLE | 2.45 | 4.39 | 3.37 | -0.07 | 74426.27 | 10.4 | skipped_fast |
| QNTUSDT | IDLE | 2.18 | 4.04 | 2.12 | 0.01 | 407740.82 | 1.1 | skipped_fast |
| BIOUSDT | IDLE | 2.1 | 3.77 | 2.89 | -0.05 | 66331.82 | 4.51 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 2.04 | 1.37 | -0.02 | 197066.88 | 9.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.67 | 3.11 | 1.56 | -0.01 | 55501.53 | 5.48 | skipped_fast |
| CHIPUSDT | IDLE | 1.45 | 4.36 | 1.81 | 0.05 | 92969.99 | 18.04 | skipped_fast |
| KITEUSDT | IDLE | 1.56 | 2.87 | 1.69 | -0.06 | 59181.39 | 11.66 | skipped_fast |
| ZBCNUSDT | IDLE | 0.77 | 1.73 | 1.08 | 0.01 | 224478.9 | 16.26 | skipped_fast |
| WAXLUSDT | IDLE | 2.76 | 5.62 | 4.6 | -0.05 | 54041.29 | 60.87 | skipped_fast |
| LAUSDT | IDLE | 1.36 | 9.18 | 6.82 | -0.19 | 92955.08 | 26.29 | skipped_fast |
| IOTAUSDT | IDLE | 1.84 | 3.29 | 2.55 | -0.03 | 66247.12 | 30.42 | skipped_fast |
| HBARUSDT | IDLE | 1.07 | 1.89 | 1.69 | -0.0 | 198441.89 | 7.82 | skipped_fast |
| FLUIDUSDT | IDLE | 1.81 | 3.43 | 1.27 | -0.03 | 7213.49 | 21.58 | skipped_fast |
| RIZEUSDT | IDLE | 0.33 | 0.86 | 0.76 | -0.04 | 41505.4 | 55.66 | skipped_fast |
| RWAUSDT | IDLE | 0.84 | 1.59 | 0.55 | 0.0 | 51893.25 | 55.31 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.76 | 0.46 | -0.01 | 37645.18 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
