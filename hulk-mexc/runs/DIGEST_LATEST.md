# Hulk DIGEST — 2026-08-22T16:11:24Z

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
| PYTHUSDT | IDLE | 1.52 | 7.24 | 2.02 | 0.04 | 51457329.88 | 3.97 | skipped_fast |
| XRPUSDT | IDLE | 1.38 | 7.64 | 5.67 | 0.03 | 215439604.38 | 0.69 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.2 | -0.01 | 1141820.62 | 5.23 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 4.14 | 2.75 | 0.09 | 766322.74 | 5.14 | skipped_fast |
| CHIPUSDT | IDLE | 0.59 | 3.36 | 1.59 | -0.09 | 627732.45 | 3.38 | skipped_fast |
| WUSDT | IDLE | 0.66 | 2.58 | 2.09 | -0.02 | 547148.88 | 12.85 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 3.49 | 2.08 | -0.05 | 318113.88 | 23.73 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 6.58 | 5.52 | -0.08 | 219105.21 | 10.01 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 4.35 | 1.25 | 0.04 | 85445.42 | 12.43 | skipped_fast |
| EDELUSDT | IDLE | 1.35 | 2.41 | 1.9 | -0.03 | 74667.49 | 11.4 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 4.76 | -0.13 | 135667.64 | 14.67 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.24 | 0.03 | 56542.98 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.24 | -0.02 | 183544.48 | 9.47 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.52 | -0.0 | 137275.87 | 48.04 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.06 | 0.49 | 0.02 | 56346.26 | 16.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 20.99 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
