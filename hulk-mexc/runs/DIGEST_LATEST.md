# Hulk DIGEST — 2026-09-23T10:18:06Z

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
| XRPUSDT | IDLE | 1.75 | 3.44 | 3.15 | 0.04 | 120141828.62 | 1.26 | skipped_fast |
| PYTHUSDT | IDLE | 0.77 | 3.7 | 1.09 | 0.08 | 1857550.9 | 2.97 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 1.91 | 1.71 | -0.01 | 401092793.36 | 0.48 | skipped_fast |
| BTCUSDT | IDLE | 0.96 | 1.7 | 1.51 | -0.0 | 848147942.48 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.81 | 3.57 | 3.3 | 0.03 | 1680814.77 | 1.03 | skipped_fast |
| CCUSDT | IDLE | 2.52 | 4.52 | 3.51 | -0.05 | 420653.11 | 7.99 | skipped_fast |
| CHIPUSDT | IDLE | 2.75 | 5.08 | 2.78 | -0.01 | 195216.53 | 17.44 | skipped_fast |
| WUSDT | IDLE | 1.61 | 2.97 | 1.65 | 0.04 | 397355.35 | 11.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.78 | 4.1 | 3.5 | 0.04 | 214778.33 | 20.44 | skipped_fast |
| BIOUSDT | IDLE | 1.74 | 3.2 | 1.93 | 0.05 | 117535.49 | 13.33 | skipped_fast |
| KITEUSDT | IDLE | 1.53 | 2.95 | 1.47 | 0.04 | 131292.1 | 11.04 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.76 | 1.32 | 0.04 | 59695.22 | 15.45 | skipped_fast |
| EDELUSDT | IDLE | 0.56 | 2.64 | 1.56 | -0.06 | 243794.12 | 52.91 | skipped_fast |
| RWAINCUSDT | IDLE | 0.96 | 2.23 | 1.44 | 0.02 | 21476.13 | 16.16 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 12.5 | 2.79 | 0.5 | 63661.19 | 93.38 | skipped_fast |
| TELUSDT | IDLE | 1.43 | 5.65 | 2.96 | 0.12 | 130847.06 | 16.36 | skipped_fast |
| QNTUSDT | IDLE | 1.02 | 2.57 | 1.23 | 0.1 | 240838.54 | 6.67 | skipped_fast |
| FLUIDUSDT | IDLE | 0.93 | 1.64 | 1.42 | 0.01 | 4904.63 | 21.68 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.87 | 0.5 | 0.01 | 53996.24 | 14.46 | skipped_fast |
| MNSRYUSDT | IDLE | 0.3 | 0.55 | 0.32 | 0.01 | 40389.66 | 8.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
