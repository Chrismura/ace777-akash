# Hulk DIGEST — 2026-10-17T14:19:12Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 11.6 | 6.77 | -0.04 | 1334229.29 | 14.79 | skipped_fast |
| XRPUSDT | IDLE | 0.73 | 1.33 | 0.81 | -0.03 | 20219592.04 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.48 | 0.85 | 0.77 | -0.02 | 118388333.45 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.18 | 0.32 | 0.3 | -0.01 | 227849007.53 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.83 | 1.58 | 0.53 | -0.04 | 1161811.37 | 9.43 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 12.81 | 8.85 | -0.03 | 23982.02 | 26.95 | skipped_fast |
| ZBCNUSDT | IDLE | 2.3 | 4.76 | 1.09 | -0.05 | 224610.86 | 3.26 | skipped_fast |
| KITEUSDT | IDLE | 2.59 | 4.58 | 4.06 | -0.02 | 61326.69 | 9.25 | skipped_fast |
| CHIPUSDT | IDLE | 2.51 | 4.46 | 3.78 | -0.07 | 89420.39 | 13.46 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 1.93 | 1.54 | -0.02 | 589030.69 | 2.97 | skipped_fast |
| CCUSDT | IDLE | 0.73 | 1.43 | 0.15 | -0.01 | 278665.71 | 10.56 | skipped_fast |
| EDELUSDT | IDLE | 1.05 | 1.85 | 1.71 | -0.06 | 160483.08 | 10.45 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.42 | 1.76 | -0.04 | 70218.69 | 8.15 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.53 | 1.02 | -0.07 | 69210.09 | 10.63 | skipped_fast |
| FLUIDUSDT | IDLE | 2.54 | 4.47 | 4.27 | 0.01 | 3566.02 | 21.28 | skipped_fast |
| HBARUSDT | IDLE | 0.91 | 1.66 | 1.07 | -0.04 | 163072.81 | 3.61 | skipped_fast |
| RIZEUSDT | IDLE | 0.54 | 1.04 | 0.4 | -0.04 | 42991.95 | 54.99 | skipped_fast |
| RWAUSDT | IDLE | 1.21 | 2.35 | 0.4 | -0.01 | 52061.87 | 7.96 | skipped_fast |
| TELUSDT | IDLE | 0.64 | 1.19 | 0.59 | -0.06 | 85594.21 | 17.74 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.26 | 0.06 | -0.0 | 27383.66 | 14.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
