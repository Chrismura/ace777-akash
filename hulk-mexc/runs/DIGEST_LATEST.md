# Hulk DIGEST — 2026-08-21T20:43:16Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.6 | 0.08 | 5545140.68 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.25 | 4.21 | 3.37 | 0.1 | 128928073.24 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.25 | 0.17 | 152961.14 | 12.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.76 | 0.12 | 478632.03 | 28.06 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.39 | 0.1 | 640551.55 | 7.37 | skipped_fast |
| HBARUSDT | IDLE | 1.72 | 3.23 | 1.81 | 0.05 | 809878.52 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 4.81 | 3.1 | 0.08 | 514452.99 | 3.08 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.54 | 0.06 | 367563.03 | 11.62 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.33 | 2.79 | 0.01 | 189183.8 | 3.16 | skipped_fast |
| EDELUSDT | IDLE | 2.77 | 5.01 | 3.9 | -0.05 | 81469.14 | 56.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.55 | 0.02 | 56290.74 | 33.04 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.03 | 10892.53 | 26.77 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.39 | 0.11 | 60938.55 | 13.96 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | 0.01 | 2767.35 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.37 | 0.01 | 181480.43 | 26.83 | skipped_fast |
| QNTUSDT | IDLE | 1.46 | 2.65 | 1.74 | 0.04 | 59883.06 | 4.7 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53938.57 | 8.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 22.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
