# Hulk DIGEST — 2026-08-22T01:10:46Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.65 | 8.74 | 0.0 | 0.14 | 6605110.99 | 5.91 | tvl≈107,253,350 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.21 | 8.4 | 1.22 | 0.15 | 149176554.92 | 2.73 | n/a |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.74 | 0.09 | 956463.88 | 2.5 | empty_tvl |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.82 | 0.11 | 541163.38 | 18.88 | n/a |
| CCUSDT | IDLE | 1.73 | 6.94 | 0.1 | 0.16 | 655585.25 | 10.49 | no_map |
| WUSDT | IDLE | 2.69 | 6.65 | 0.46 | 0.09 | 392473.41 | 10.15 | tvl≈1,638,353,418 |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.94 | 0.01 | 535695.81 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.46 | 5.53 | 0.37 | 0.03 | 186899.34 | 3.05 | n/a |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.02 | 79626.96 | 44.3 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.2 | 0.11 | 60426.3 | 45.81 | no_map |
| REDUSDT | IDLE | 0.93 | 8.27 | 2.19 | 0.22 | 159238.89 | 18.66 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.4 | 5.18 | 0.73 | 0.07 | 170396.72 | 4.51 | n/a |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.77 | 0.05 | 181206.27 | 46.38 | no_map |
| KITEUSDT | IDLE | 1.46 | 4.48 | 0.0 | 0.12 | 60927.85 | 12.61 | no_map |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | no_map |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | no_map |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.03 | 55221.43 | 8.21 | no_map |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4888.85 | 22.32 | tvl≈2,603,605,946 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
