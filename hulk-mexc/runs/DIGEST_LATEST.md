# Hulk DIGEST — 2026-08-21T23:43:26Z

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
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.69 | 0.1 | 6159756.3 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 1.96 | 8.23 | 1.32 | 0.15 | 141312146.1 | 4.12 | skipped_fast |
| HBARUSDT | IDLE | 2.62 | 6.36 | 1.05 | 0.09 | 909819.27 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.8 | 0.13 | 514001.64 | 19.17 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.13 | 0.13 | 645633.03 | 9.79 | skipped_fast |
| WUSDT | IDLE | 2.79 | 6.91 | 2.04 | 0.07 | 379990.47 | 13.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.43 | 0.03 | 547446.99 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.02 | 186494.62 | 3.11 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 4.86 | 0.12 | 58841.31 | 46.13 | skipped_fast |
| EDELUSDT | IDLE | 2.57 | 5.5 | 1.19 | -0.04 | 82634.42 | 66.15 | skipped_fast |
| TELUSDT | IDLE | 2.82 | 6.89 | 0.36 | 0.07 | 190391.72 | 25.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.02 | 10311.15 | 21.39 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.75 | 0.18 | 157735.35 | 12.92 | skipped_fast |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.08 | 145804.42 | 1.49 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.13 | 0.09 | 61477.04 | 12.98 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.08 | 0.04 | 54602.26 | 8.18 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.87 | 0.66 | 0.1 | 4934.79 | 21.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
