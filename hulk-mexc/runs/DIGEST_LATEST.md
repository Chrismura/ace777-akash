# Hulk DIGEST — 2026-10-15T09:37:37Z

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
| PYTHUSDT | IDLE | 2.57 | 8.03 | 3.12 | 0.06 | 2810171.89 | 3.48 | skipped_fast |
| WUSDT | IDLE | 2.46 | 7.02 | 6.08 | -0.1 | 2793439.09 | 14.51 | skipped_fast |
| XRPUSDT | IDLE | 1.41 | 2.73 | 0.63 | -0.04 | 60815556.91 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.94 | 1.9 | 0.69 | -0.05 | 353527529.36 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.5 | 0.52 | -0.02 | 541725958.59 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.82 | 5.01 | 0.64 | -0.04 | 1167513.94 | 2.99 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 4.69 | 4.46 | -0.13 | 449481.28 | 5.65 | skipped_fast |
| EDELUSDT | IDLE | 2.41 | 7.65 | 5.97 | -0.11 | 219153.7 | 19.61 | skipped_fast |
| HBARUSDT | IDLE | 1.39 | 2.82 | 1.27 | -0.05 | 563794.43 | 7.35 | skipped_fast |
| RIZEUSDT | IDLE | 1.78 | 11.92 | 7.76 | -0.03 | 65375.83 | 58.86 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 7.22 | 6.48 | -0.21 | 122590.37 | 13.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 3.08 | 0.49 | -0.05 | 219627.9 | 15.76 | skipped_fast |
| BIOUSDT | IDLE | 1.23 | 3.98 | 1.86 | -0.09 | 84576.12 | 8.05 | skipped_fast |
| REDUSDT | IDLE | 1.33 | 2.33 | 2.21 | 0.0 | 69290.26 | 8.99 | skipped_fast |
| KITEUSDT | IDLE | 0.83 | 3.01 | 2.41 | -0.12 | 67987.8 | 10.97 | skipped_fast |
| RWAINCUSDT | IDLE | 1.03 | 2.27 | 1.01 | 0.01 | 26911.29 | 15.29 | skipped_fast |
| FLUIDUSDT | IDLE | 1.99 | 5.96 | 4.11 | -0.02 | 20393.8 | 21.5 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 1.77 | 1.1 | -0.05 | 99996.9 | 46.87 | skipped_fast |
| MNSRYUSDT | IDLE | 0.59 | 1.04 | 1.0 | -0.02 | 31344.03 | 2.86 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.73 | 0.56 | -0.04 | 55384.16 | 16.14 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
