# Hulk DIGEST — 2026-08-21T21:06:03Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.68 | 0.09 | 5581736.08 | 4.18 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 3.73 | 2.6 | 0.1 | 128061246.2 | 1.45 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 8.19 | 6.07 | 0.08 | 480167.43 | 34.52 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.62 | 3.85 | 0.08 | 513905.76 | 6.21 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.14 | 0.25 | 0.1 | 641019.2 | 7.36 | skipped_fast |
| HBARUSDT | IDLE | 1.63 | 3.04 | 1.53 | 0.06 | 806158.89 | 1.3 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.83 | 0.92 | 0.06 | 367995.92 | 11.55 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.2 | 2.76 | 0.01 | 187899.1 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.49 | 0.16 | 153340.51 | 11.5 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 4.12 | 3.08 | -0.06 | 82274.95 | 45.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.42 | 0.01 | 56233.0 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.04 | 10893.0 | 32.12 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.0 | 2.33 | 0.11 | 61144.2 | 11.16 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.53 | 0.01 | 180414.41 | 21.4 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.68 | 0.04 | 60171.35 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 178.96 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.17 | 1.07 | 0.03 | 53762.26 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4286.4 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
