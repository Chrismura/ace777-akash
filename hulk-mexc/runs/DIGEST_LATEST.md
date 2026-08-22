# Hulk DIGEST — 2026-08-22T01:11:30Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.73 | 9.41 | 0.25 | 0.14 | 6610589.12 | 15.71 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.2 | 8.4 | 1.02 | 0.15 | 149230296.96 | 2.73 | skipped_fast |
| HBARUSDT | IDLE | 3.0 | 6.36 | 0.64 | 0.08 | 956451.89 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.8 | 0.1 | 540930.53 | 16.94 | skipped_fast |
| CCUSDT | IDLE | 1.75 | 7.09 | 0.18 | 0.16 | 656127.58 | 8.75 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.4 | 0.09 | 392354.68 | 12.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.97 | 0.01 | 535695.81 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.45 | 5.53 | 0.18 | 0.03 | 186899.34 | 3.05 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.03 | 79651.96 | 22.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.2 | 0.11 | 60434.1 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 8.27 | 2.19 | 0.22 | 159254.44 | 17.17 | skipped_fast |
| QNTUSDT | IDLE | 2.4 | 5.18 | 0.73 | 0.07 | 170405.77 | 7.52 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.72 | 0.05 | 181223.4 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 4.48 | 0.0 | 0.12 | 60985.26 | 10.82 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 55180.98 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4888.85 | 22.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
