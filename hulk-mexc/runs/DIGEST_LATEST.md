# Hulk DIGEST — 2026-08-19T07:10:56Z

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
| XRPUSDT | IDLE | 0.4 | 0.77 | 0.18 | 0.01 | 10029177.41 | 1.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.01 | 1.9 | 0.02 | 166419.61 | 2.59 | skipped_fast |
| CHIPUSDT | IDLE | 1.27 | 4.52 | 3.42 | -0.09 | 179606.78 | 3.9 | skipped_fast |
| CCUSDT | IDLE | 0.83 | 1.53 | 0.9 | -0.01 | 216011.91 | 8.9 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 4.43 | 1.99 | -0.12 | 153987.97 | 18.05 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 2.58 | 2.25 | -0.04 | 59169.76 | 40.57 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.19 | 1.54 | -0.02 | 65764.06 | 17.71 | skipped_fast |
| ZBCNUSDT | IDLE | 0.73 | 1.45 | 0.03 | 0.0 | 156599.15 | 6.98 | skipped_fast |
| WUSDT | IDLE | 0.9 | 1.73 | 0.53 | -0.01 | 114212.38 | 12.37 | skipped_fast |
| BIOUSDT | IDLE | 1.01 | 1.91 | 0.72 | 0.02 | 61657.96 | 4.01 | skipped_fast |
| RIZEUSDT | IDLE | 1.56 | 4.17 | 3.96 | -0.06 | 27426.26 | 152.58 | skipped_fast |
| QAITUSDT | IDLE | 0.56 | 3.72 | 0.62 | -0.14 | 9569.99 | 50.53 | skipped_fast |
| RWAINCUSDT | IDLE | 0.68 | 1.49 | 0.06 | 0.01 | 10735.68 | 71.22 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.15 | 0.66 | 0.03 | 119929.3 | 1.48 | skipped_fast |
| QNTUSDT | IDLE | 1.01 | 1.97 | 0.33 | 0.02 | 37580.91 | 8.8 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.5 | 1.04 | -0.01 | 51623.63 | 17.59 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 1.68 | 0.58 | -0.01 | 187.92 | 21.33 | skipped_fast |
| TELUSDT | IDLE | 0.67 | 1.25 | 0.62 | 0.04 | 87202.01 | 48.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
