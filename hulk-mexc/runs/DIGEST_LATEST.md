# Hulk DIGEST — 2026-10-23T11:46:49Z

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
| XRPUSDT | IDLE | 0.64 | 1.16 | 0.77 | -0.01 | 25914088.01 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.89 | 0.48 | -0.0 | 226640557.59 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.28 | 0.5 | 0.34 | -0.0 | 328370173.46 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.84 | 6.32 | 4.05 | -0.06 | 1043324.03 | 1.09 | skipped_fast |
| WUSDT | IDLE | 2.92 | 5.22 | 4.08 | -0.01 | 620802.28 | 12.72 | skipped_fast |
| PYTHUSDT | IDLE | 1.89 | 3.42 | 2.45 | -0.04 | 678116.08 | 1.39 | skipped_fast |
| ZBCNUSDT | IDLE | 3.02 | 6.78 | 1.69 | -0.04 | 170376.43 | 13.8 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 3.48 | 2.19 | -0.04 | 403375.35 | 15.76 | skipped_fast |
| CHIPUSDT | IDLE | 2.48 | 4.76 | 3.3 | 0.02 | 124872.15 | 20.07 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 2.91 | 2.07 | -0.02 | 327160.8 | 11.33 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.7 | 0.15 | 0.01 | 194575.68 | 8.67 | skipped_fast |
| REDUSDT | IDLE | 1.05 | 1.89 | 1.38 | -0.01 | 81730.7 | 9.28 | skipped_fast |
| RWAINCUSDT | IDLE | 1.06 | 2.07 | 0.38 | 0.03 | 52521.89 | 5.51 | skipped_fast |
| KITEUSDT | IDLE | 0.92 | 1.71 | 0.84 | 0.01 | 57485.81 | 10.77 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.35 | 0.12 | 0.0 | 59300.23 | 8.3 | skipped_fast |
| LAUSDT | IDLE | 1.99 | 3.89 | 0.55 | 0.02 | 54576.9 | 22.99 | skipped_fast |
| RIZEUSDT | IDLE | 0.55 | 2.53 | 0.69 | -0.09 | 45345.87 | 64.47 | skipped_fast |
| WAXLUSDT | IDLE | 1.72 | 3.15 | 1.89 | -0.03 | 56932.05 | 54.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.84 | 3.21 | 3.11 | -0.05 | 9534.99 | 50.3 | skipped_fast |
| IOTAUSDT | IDLE | 0.71 | 1.3 | 0.86 | -0.01 | 66475.8 | 22.3 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.95 | 0.55 | 0.0 | 52167.02 | 7.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.6 | 1.13 | 0.45 | -0.0 | 37327.12 | 74.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
