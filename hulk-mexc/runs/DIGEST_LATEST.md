# Hulk DIGEST — 2026-10-10T14:52:08Z

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
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.68 | 8.77 | 0.24 | 0.03 | 1053176.62 | 14.29 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.95 | 0.35 | 0.01 | 88117334.57 | 0.24 | skipped_fast |
| XRPUSDT | IDLE | 0.38 | 0.73 | 0.24 | 0.02 | 16772931.35 | 1.42 | skipped_fast |
| BTCUSDT | IDLE | 0.19 | 0.36 | 0.12 | -0.0 | 194470901.23 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.91 | 3.49 | 2.24 | -0.02 | 1130855.59 | 0.4 | skipped_fast |
| PYTHUSDT | IDLE | 0.97 | 2.47 | 1.96 | -0.09 | 1023064.14 | 1.28 | skipped_fast |
| EDELUSDT | IDLE | 3.22 | 6.53 | 4.76 | 0.0 | 227484.17 | 15.69 | skipped_fast |
| KITEUSDT | IDLE | 2.3 | 6.2 | 0.45 | 0.07 | 72437.64 | 9.94 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.8 | 0.86 | -0.02 | 386089.93 | 5.81 | skipped_fast |
| ZBCNUSDT | IDLE | 0.6 | 1.16 | 0.29 | -0.01 | 210813.46 | 8.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.0 | 2.75 | 2.67 | 0.07 | 86919.11 | 15.47 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 1.93 | 0.24 | 0.03 | 78944.45 | 6.92 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 2.16 | 0.19 | 0.04 | 55232.43 | 16.51 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 1.69 | 0.25 | 0.03 | 327486.59 | 2.14 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 3.06 | 2.53 | -0.02 | 109457.78 | 44.27 | skipped_fast |
| RWAINCUSDT | IDLE | 0.91 | 1.78 | 0.29 | -0.02 | 9630.91 | 48.73 | skipped_fast |
| RIZEUSDT | IDLE | 0.6 | 1.56 | 0.79 | 0.01 | 45292.14 | 55.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.67 | 1.94 | 1.47 | -0.01 | 15362.48 | 21.47 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.71 | 0.47 | -0.01 | 53802.75 | 7.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.67 | 0.27 | 0.0 | 39326.95 | 12.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
