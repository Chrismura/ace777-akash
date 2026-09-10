# Hulk DIGEST — 2026-09-10T21:16:18Z

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
| ETHUSDT | IDLE | 0.9 | 1.71 | 0.55 | -0.0 | 443644346.42 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.88 | 1.66 | 0.67 | -0.03 | 44145522.26 | 0.74 | n/a |
| BTCUSDT | IDLE | 0.49 | 0.93 | 0.35 | -0.01 | 541400589.47 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.71 | 3.36 | 0.44 | -0.04 | 689559.91 | 1.92 | tvl≈117,068,218 |
| CCUSDT | IDLE | 1.46 | 2.7 | 1.49 | -0.05 | 512371.86 | 2.02 | no_map |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.13 | 8.58 | 1.31 | -0.09 | 90229.38 | 22.12 | no_map |
| ZBCNUSDT | IDLE | 1.93 | 3.52 | 2.28 | -0.0 | 200781.1 | 8.73 | n/a |
| WUSDT | IDLE | 1.61 | 3.07 | 0.96 | -0.04 | 189319.76 | 13.46 | tvl≈1,495,286,163 |
| RIZEUSDT | IDLE | 0.5 | 28.21 | 4.28 | -0.49 | 126196.03 | 91.98 | no_map |
| EDELUSDT | IDLE | 0.8 | 4.65 | 2.04 | 0.09 | 262929.67 | 18.13 | no_map |
| BIOUSDT | IDLE | 1.5 | 2.7 | 1.96 | -0.06 | 79688.7 | 4.0 | n/a |
| KITEUSDT | IDLE | 1.39 | 2.54 | 1.63 | -0.04 | 57359.5 | 10.03 | no_map |
| REDUSDT | IDLE | 0.66 | 1.48 | 0.35 | -0.06 | 67549.5 | 18.93 | tvl≈2,183,923 |
| HBARUSDT | IDLE | 0.87 | 1.73 | 0.13 | -0.02 | 243924.53 | 1.32 | empty_tvl |
| RWAINCUSDT | IDLE | 1.24 | 2.38 | 0.67 | -0.01 | 4986.91 | 101.01 | no_map |
| QNTUSDT | IDLE | 1.15 | 2.03 | 1.78 | -0.02 | 36783.82 | 7.66 | n/a |
| TELUSDT | IDLE | 1.01 | 1.92 | 0.67 | -0.02 | 83582.67 | 39.16 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 1.84 | 1.81 | -0.06 | 1786.37 | 21.34 | tvl≈2,650,870,886 |
| RWAUSDT | IDLE | 0.41 | 0.76 | 0.45 | -0.03 | 51521.25 | 15.17 | no_map |
| MNSRYUSDT | IDLE | 0.31 | 0.62 | 0.03 | -0.02 | 32321.22 | 5.57 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
