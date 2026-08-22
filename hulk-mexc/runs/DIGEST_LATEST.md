# Hulk DIGEST — 2026-08-22T00:11:12Z

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
| PYTHUSDT | IDLE | 1.78 | 6.39 | 1.88 | 0.1 | 6289832.23 | 4.11 | skipped_fast |
| XRPUSDT | IDLE | 2.07 | 8.23 | 2.95 | 0.13 | 143232749.13 | 3.49 | skipped_fast |
| HBARUSDT | IDLE | 2.82 | 6.36 | 2.02 | 0.07 | 912600.3 | 1.26 | skipped_fast |
| ZBCNUSDT | IDLE | 2.9 | 11.25 | 3.14 | 0.11 | 515621.84 | 25.25 | skipped_fast |
| CCUSDT | IDLE | 1.95 | 7.42 | 1.35 | 0.12 | 644929.84 | 8.93 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.1 | 0.08 | 380861.06 | 12.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.06 | 0.04 | 545127.96 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.32 | 5.04 | 1.51 | 0.02 | 187167.03 | 3.12 | skipped_fast |
| EDELUSDT | IDLE | 2.58 | 5.5 | 1.41 | 0.0 | 79886.01 | 11.02 | skipped_fast |
| RIZEUSDT | IDLE | 2.25 | 9.82 | 3.53 | 0.13 | 59052.45 | 45.5 | skipped_fast |
| TELUSDT | IDLE | 2.87 | 6.89 | 1.18 | 0.05 | 190390.62 | 36.22 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.27 | 0.06 | 166738.55 | 16.66 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.58 | 4.91 | 2.91 | 0.19 | 157631.9 | 8.09 | skipped_fast |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.98 | 0.09 | 61453.88 | 11.1 | skipped_fast |
| RWAINCUSDT | IDLE | 1.6 | 2.99 | 1.43 | 0.02 | 10317.62 | 91.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.98 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54672.98 | 41.03 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
