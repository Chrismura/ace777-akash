# Hulk DIGEST — 2026-08-29T17:07:10Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.11 | 75.24 | 38.23 | -0.01 | 138515.67 | 17.94 | skipped_fast |
| XRPUSDT | IDLE | 0.86 | 1.62 | 0.71 | 0.0 | 22330913.62 | 1.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.93 | 0.96 | -0.04 | 1035662.94 | 2.41 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 9.82 | 6.54 | 0.04 | 66754.96 | 9.91 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 3.53 | 1.75 | 0.02 | 319782.76 | 4.18 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 3.84 | 0.33 | 0.06 | 212276.52 | 6.84 | skipped_fast |
| RIZEUSDT | IDLE | 2.61 | 5.39 | 2.41 | 0.01 | 33349.41 | 36.18 | skipped_fast |
| REDUSDT | IDLE | 1.94 | 4.67 | 3.81 | 0.04 | 76346.05 | 10.14 | skipped_fast |
| WUSDT | IDLE | 1.48 | 2.81 | 0.94 | 0.0 | 189823.47 | 10.91 | skipped_fast |
| ZBCNUSDT | IDLE | 1.47 | 2.94 | 0.01 | -0.03 | 189070.36 | 8.56 | skipped_fast |
| BIOUSDT | IDLE | 0.83 | 1.57 | 0.65 | -0.01 | 64491.91 | 3.62 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.41 | 0.37 | -0.0 | 215348.64 | 1.32 | skipped_fast |
| RWAINCUSDT | IDLE | 0.64 | 1.12 | 1.11 | -0.04 | 3664.71 | 105.76 | skipped_fast |
| TELUSDT | IDLE | 0.89 | 1.62 | 1.03 | -0.02 | 70361.41 | 46.11 | skipped_fast |
| QNTUSDT | IDLE | 0.74 | 1.4 | 0.47 | 0.0 | 30428.28 | 6.52 | skipped_fast |
| RWAUSDT | IDLE | 0.3 | 0.58 | 0.08 | 0.01 | 53792.12 | 8.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.2 | 0.0 | 0.02 | 2001.2 | 22.21 | skipped_fast |
| QAITUSDT | ERR | — | — | — | — | — | — | HTTP Error 400: Bad Request |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
