# Hulk DIGEST — 2026-09-16T18:03:04Z

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
| XRPUSDT | IDLE | 1.48 | 2.67 | 2.0 | -0.11 | 81298357.02 | 5.56 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.6 | 0.93 | -0.02 | 408545200.56 | 2.43 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.89 | 0.55 | -0.02 | 528601867.59 | 0.0 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 15.0 | 10.05 | -0.04 | 65765.77 | 77.61 | skipped_fast |
| RIZEUSDT | IDLE | 2.23 | 36.05 | 20.62 | 0.33 | 60189.98 | 92.97 | skipped_fast |
| CCUSDT | IDLE | 1.85 | 3.55 | 1.01 | -0.02 | 474647.73 | 17.57 | skipped_fast |
| PYTHUSDT | IDLE | 2.08 | 3.79 | 2.49 | -0.05 | 406293.26 | 21.24 | skipped_fast |
| CHIPUSDT | IDLE | 3.18 | 6.39 | 4.41 | -0.06 | 89592.54 | 19.42 | skipped_fast |
| EDELUSDT | IDLE | 0.72 | 5.84 | 4.23 | 0.08 | 377310.99 | 19.23 | skipped_fast |
| WUSDT | IDLE | 1.77 | 3.22 | 2.16 | -0.08 | 204643.55 | 22.84 | skipped_fast |
| REDUSDT | IDLE | 2.17 | 4.2 | 3.23 | -0.06 | 67331.52 | 21.41 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 4.05 | 3.29 | -0.05 | 81126.39 | 53.91 | skipped_fast |
| HBARUSDT | IDLE | 1.69 | 2.99 | 2.66 | -0.08 | 360185.31 | 16.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 2.37 | 0.83 | -0.05 | 216375.79 | 77.95 | skipped_fast |
| RWAINCUSDT | IDLE | 1.06 | 1.84 | 1.81 | -0.04 | 12269.86 | 11.93 | skipped_fast |
| TELUSDT | IDLE | 1.85 | 4.45 | 3.16 | -0.1 | 120738.93 | 42.64 | skipped_fast |
| QNTUSDT | IDLE | 1.19 | 2.12 | 1.73 | -0.06 | 39736.42 | 16.87 | skipped_fast |
| RWAUSDT | IDLE | 0.81 | 1.61 | 0.08 | -0.0 | 52848.37 | 7.53 | skipped_fast |
| FLUIDUSDT | IDLE | 1.09 | 2.05 | 0.9 | -0.06 | 2543.25 | 47.13 | skipped_fast |
| MNSRYUSDT | IDLE | 0.34 | 0.62 | 0.45 | -0.02 | 33413.16 | 9.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
