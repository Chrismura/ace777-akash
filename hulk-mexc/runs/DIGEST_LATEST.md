# Hulk DIGEST — 2026-08-21T20:07:31Z

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
| PYTHUSDT | IDLE | 1.34 | 4.78 | 3.36 | 0.07 | 5467593.85 | 2.12 | skipped_fast |
| XRPUSDT | IDLE | 1.27 | 4.21 | 3.69 | 0.11 | 129029511.22 | 2.19 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 25.8 | 12.96 | 0.17 | 154280.2 | 19.55 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.53 | 10.86 | 7.43 | 0.1 | 478041.98 | 31.12 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 3.91 | 1.71 | 0.07 | 633538.15 | 7.46 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.23 | 2.72 | 0.05 | 794049.81 | 1.31 | skipped_fast |
| CHIPUSDT | IDLE | 1.35 | 4.81 | 3.76 | 0.08 | 513670.92 | 3.1 | skipped_fast |
| WUSDT | IDLE | 2.15 | 3.92 | 2.52 | 0.05 | 366436.04 | 13.87 | skipped_fast |
| BIOUSDT | IDLE | 2.6 | 5.33 | 3.74 | 0.0 | 189859.17 | 3.19 | skipped_fast |
| EDELUSDT | IDLE | 2.42 | 4.29 | 3.68 | -0.05 | 79714.95 | 22.5 | skipped_fast |
| RWAINCUSDT | IDLE | 2.26 | 4.3 | 1.53 | 0.04 | 11069.14 | 16.21 | skipped_fast |
| RIZEUSDT | IDLE | 1.91 | 9.71 | 1.44 | 0.02 | 56215.96 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 3.06 | 0.1 | 61181.02 | 11.24 | skipped_fast |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2857.0 | 63.29 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 3.39 | 2.49 | 0.01 | 183634.6 | 43.41 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 59882.99 | 6.25 | skipped_fast |
| RWAUSDT | IDLE | 0.66 | 1.16 | 1.07 | 0.03 | 54351.23 | 16.6 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
