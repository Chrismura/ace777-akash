# Hulk DIGEST — 2026-08-22T01:13:02Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.75 | 9.41 | 0.69 | 0.14 | 6628084.99 | 1.97 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.4 | 0.74 | 0.15 | 149317017.77 | 3.4 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.69 | 0.09 | 956576.85 | 2.49 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.82 | 0.1 | 540518.39 | 16.95 | skipped_fast |
| CCUSDT | IDLE | 1.75 | 7.1 | 0.02 | 0.16 | 657594.42 | 8.73 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.53 | 0.09 | 392433.67 | 10.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.37 | 0.01 | 535077.13 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.57 | 0.06 | 0.04 | 186923.61 | 3.05 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.74 | -0.03 | 79651.96 | 33.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.15 | 0.11 | 60471.19 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 8.27 | 2.81 | 0.22 | 159048.31 | 14.1 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.84 | 0.07 | 170426.9 | 3.01 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.72 | 0.05 | 181138.78 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 4.48 | 0.2 | 0.11 | 61028.02 | 9.02 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.04 | 55238.93 | 24.62 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4888.85 | 41.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
