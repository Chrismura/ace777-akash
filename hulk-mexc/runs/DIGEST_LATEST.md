# Hulk DIGEST — 2026-09-14T07:42:27Z

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
| XRPUSDT | IDLE | 1.52 | 3.02 | 0.14 | 0.02 | 28064877.1 | 1.44 | skipped_fast |
| ETHUSDT | IDLE | 0.73 | 1.44 | 0.16 | 0.0 | 331701778.44 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.1 | 0.12 | 0.01 | 384455380.16 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.98 | 49.46 | 13.64 | 0.3 | 79214.55 | 90.93 | skipped_fast |
| REDUSDT | IDLE | 3.66 | 8.4 | 4.97 | 0.02 | 113523.31 | 16.4 | skipped_fast |
| PYTHUSDT | IDLE | 1.57 | 3.32 | 3.03 | 0.04 | 520850.98 | 5.29 | skipped_fast |
| EDELUSDT | IDLE | 1.96 | 9.61 | 4.0 | 0.12 | 241245.17 | 14.41 | skipped_fast |
| ZBCNUSDT | IDLE | 1.88 | 3.47 | 1.97 | -0.01 | 192889.2 | 16.98 | skipped_fast |
| WUSDT | IDLE | 1.52 | 2.9 | 0.88 | 0.01 | 224728.97 | 10.82 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.8 | 1.68 | -0.03 | 274310.7 | 9.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.46 | 4.85 | 4.2 | -0.1 | 103408.11 | 14.2 | skipped_fast |
| KITEUSDT | IDLE | 1.56 | 2.84 | 1.83 | -0.02 | 61548.73 | 12.09 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.9 | 1.05 | -0.01 | 72562.5 | 3.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.04 | 2.07 | 0.11 | 0.01 | 9685.84 | 21.87 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.44 | 0.27 | 0.01 | 272327.59 | 1.3 | skipped_fast |
| QNTUSDT | IDLE | 1.18 | 2.26 | 0.61 | -0.01 | 37633.58 | 7.84 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 2.75 | 0.85 | -0.0 | 736.22 | 22.45 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 1.85 | 1.0 | -0.02 | 87942.64 | 63.33 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.59 | 0.3 | 0.0 | 52693.49 | 22.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.32 | 0.56 | 0.47 | -0.01 | 30126.0 | 37.7 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
