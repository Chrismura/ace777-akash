# Hulk DIGEST — 2026-09-05T15:28:52Z

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
| XRPUSDT | IDLE | 0.68 | 1.28 | 0.5 | 0.01 | 22737046.81 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 0.25 | 0.48 | 0.14 | 0.0 | 180556879.61 | 0.12 | skipped_fast |
| BTCUSDT | IDLE | 0.15 | 0.28 | 0.07 | 0.0 | 356493294.84 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 6.25 | 2.69 | 0.11 | 448022.7 | 5.24 | skipped_fast |
| PYTHUSDT | IDLE | 1.82 | 3.39 | 1.73 | 0.02 | 344247.23 | 1.83 | skipped_fast |
| KITEUSDT | IDLE | 2.66 | 6.21 | 4.6 | -0.03 | 61072.85 | 7.89 | skipped_fast |
| RIZEUSDT | IDLE | 1.25 | 11.89 | 5.45 | 0.04 | 153574.16 | 33.7 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 2.59 | 1.68 | -0.01 | 187192.79 | 3.71 | skipped_fast |
| REDUSDT | IDLE | 1.9 | 3.4 | 2.61 | 0.02 | 62294.21 | 10.4 | skipped_fast |
| WUSDT | IDLE | 1.35 | 2.36 | 2.31 | 0.04 | 164504.15 | 13.18 | skipped_fast |
| CCUSDT | IDLE | 0.8 | 1.51 | 0.54 | 0.01 | 293381.05 | 8.23 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.86 | 0.68 | 0.04 | 80443.23 | 3.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.8 | 3.17 | 2.92 | -0.02 | 7361.85 | 16.35 | skipped_fast |
| EDELUSDT | IDLE | 0.27 | 4.89 | 2.15 | -0.03 | 192901.01 | 19.08 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.81 | 1.02 | 0.05 | 308606.37 | 1.24 | skipped_fast |
| RWAUSDT | IDLE | 1.16 | 2.23 | 0.63 | 0.03 | 51742.14 | 21.21 | skipped_fast |
| TELUSDT | IDLE | 1.09 | 2.14 | 0.29 | -0.0 | 70493.9 | 35.07 | skipped_fast |
| QNTUSDT | IDLE | 0.64 | 1.15 | 0.82 | -0.01 | 38487.87 | 4.7 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 0.95 | 0.91 | 0.01 | 800.01 | 21.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.3 | 0.05 | 0.0 | 38344.17 | 4.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
