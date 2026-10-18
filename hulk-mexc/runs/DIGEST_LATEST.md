# Hulk DIGEST — 2026-10-18T04:27:30Z

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
| ETHUSDT | IDLE | 0.81 | 1.57 | 0.3 | -0.0 | 91615089.06 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.8 | 1.54 | 0.42 | -0.01 | 18262287.95 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 1.02 | 0.18 | 0.0 | 185545923.5 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.44 | 3.56 | 3.27 | -0.09 | 1286188.34 | 14.25 | skipped_fast |
| WUSDT | IDLE | 0.79 | 2.4 | 0.93 | -0.03 | 1114743.9 | 15.94 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 8.42 | 4.08 | -0.08 | 183451.71 | 22.21 | skipped_fast |
| ZBCNUSDT | IDLE | 2.11 | 3.69 | 3.49 | -0.04 | 177999.23 | 22.05 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.49 | 1.57 | -0.03 | 571587.4 | 2.04 | skipped_fast |
| CCUSDT | IDLE | 0.88 | 1.58 | 1.24 | -0.01 | 251455.14 | 7.79 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.16 | 0.61 | 0.03 | 273078.95 | 9.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.07 | 3.15 | 0.18 | -0.05 | 75455.94 | 13.73 | skipped_fast |
| REDUSDT | IDLE | 1.11 | 1.97 | 1.65 | -0.04 | 60560.14 | 15.93 | skipped_fast |
| RIZEUSDT | IDLE | 1.21 | 2.2 | 1.46 | -0.0 | 45798.82 | 27.62 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.58 | 0.94 | -0.03 | 71229.7 | 4.13 | skipped_fast |
| KITEUSDT | IDLE | 0.64 | 1.56 | 1.21 | -0.05 | 71223.42 | 12.13 | skipped_fast |
| RWAINCUSDT | IDLE | 0.56 | 1.82 | 0.26 | 0.06 | 19567.27 | 5.26 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 2.31 | 1.95 | -0.06 | 101013.93 | 24.92 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.72 | 0.16 | -0.0 | 51203.32 | 15.95 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.88 | 0.57 | -0.0 | 29864.04 | 51.15 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 1661.58 | 21.2 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
