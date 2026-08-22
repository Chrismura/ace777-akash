# Hulk DIGEST — 2026-08-22T02:14:45Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 8.42 | 0.91 | 0.14 | 6921837.71 | 1.95 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 10.08 | 0.43 | 0.17 | 154132522.49 | 1.99 | n/a |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.88 | 0.09 | 545650.23 | 15.05 | n/a |
| HBARUSDT | IDLE | 2.29 | 4.9 | 0.12 | 0.08 | 955377.66 | 1.24 | empty_tvl |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.1 | 0.15 | 653201.87 | 7.84 | no_map |
| CHIPUSDT | IDLE | 1.95 | 4.5 | 0.0 | -0.01 | 512532.25 | 3.01 | no_map |
| BIOUSDT | IDLE | 2.98 | 6.88 | 0.27 | 0.09 | 192508.44 | 2.98 | n/a |
| WUSDT | IDLE | 1.71 | 4.41 | 0.03 | 0.09 | 400329.07 | 8.06 | tvl≈1,638,353,418 |
| EDELUSDT | IDLE | 2.37 | 5.02 | 1.41 | -0.01 | 79546.3 | 21.98 | no_map |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.93 | 0.11 | 61200.53 | 45.71 | no_map |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.03 | 0.18 | 156876.08 | 10.51 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.28 | 4.89 | 0.84 | 0.07 | 171238.93 | 7.52 | n/a |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.41 | 0.12 | 61467.26 | 8.98 | no_map |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.01 | 9604.71 | 43.38 | no_map |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | no_map |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.43 | 0.04 | 179367.89 | 62.24 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.15 | tvl≈2,603,605,946 |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54876.49 | 32.73 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
