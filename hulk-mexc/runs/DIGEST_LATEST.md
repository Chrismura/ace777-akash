# Hulk DIGEST — 2026-08-29T14:11:05Z

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
| XRPUSDT | IDLE | 0.39 | 0.75 | 0.14 | -0.01 | 34905486.91 | 2.88 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 6.99 | 3.55 | -0.09 | 1092701.76 | 2.45 | skipped_fast |
| EDELUSDT | IDLE | 2.82 | 10.29 | 4.57 | -0.08 | 102630.22 | 74.91 | skipped_fast |
| PYTHUSDT | IDLE | 1.33 | 2.57 | 0.54 | 0.01 | 390129.67 | 4.2 | skipped_fast |
| CCUSDT | IDLE | 1.43 | 2.79 | 0.44 | 0.03 | 212288.65 | 10.45 | skipped_fast |
| REDUSDT | IDLE | 1.85 | 5.15 | 4.21 | 0.02 | 76578.79 | 21.92 | skipped_fast |
| KITEUSDT | IDLE | 2.02 | 4.07 | 0.0 | 0.05 | 63249.52 | 19.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.12 | 2.71 | 2.04 | -0.08 | 187586.98 | 15.98 | skipped_fast |
| WUSDT | IDLE | 0.83 | 1.63 | 0.19 | -0.02 | 211335.02 | 9.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.68 | 3.66 | 0.19 | -0.01 | 26971.43 | 31.74 | skipped_fast |
| BIOUSDT | IDLE | 0.41 | 0.8 | 0.18 | -0.02 | 82513.75 | 3.63 | skipped_fast |
| HBARUSDT | IDLE | 0.34 | 0.68 | 0.01 | -0.03 | 365134.83 | 1.33 | skipped_fast |
| RWAINCUSDT | IDLE | 0.53 | 1.0 | 0.39 | -0.03 | 4402.82 | 111.3 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 1.5 | 1.14 | -0.04 | 77306.82 | 40.36 | skipped_fast |
| QNTUSDT | IDLE | 0.53 | 0.97 | 0.64 | -0.01 | 33575.85 | 3.28 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.5 | 0.33 | 0.01 | 56236.66 | 8.24 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.06 | 0.09 | -0.01 | 1904.51 | 21.45 | skipped_fast |
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
