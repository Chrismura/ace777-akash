# Hulk DIGEST — 2026-09-02T20:58:30Z

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
| XRPUSDT | IDLE | 1.18 | 2.31 | 0.29 | -0.0 | 37159420.2 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.33 | 0.45 | -0.01 | 365617627.4 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.06 | 0.16 | 0.0 | 512841127.66 | 0.1 | skipped_fast |
| PYTHUSDT | IDLE | 1.27 | 5.36 | 2.39 | 0.14 | 1334761.85 | 1.73 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 6.3 | 1.36 | -0.07 | 1017306.12 | 2.37 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.31 | 33.7 | 11.8 | 0.12 | 48091.86 | 61.74 | skipped_fast |
| ZBCNUSDT | IDLE | 3.36 | 8.19 | 2.56 | -0.04 | 181736.0 | 21.81 | skipped_fast |
| WUSDT | IDLE | 2.75 | 5.4 | 0.69 | -0.01 | 271096.51 | 14.33 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.52 | 1.5 | -0.03 | 408983.16 | 9.09 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 9.23 | 3.82 | 0.15 | 134060.05 | 17.02 | skipped_fast |
| EDELUSDT | IDLE | 1.11 | 5.76 | 5.04 | 0.06 | 166580.99 | 68.73 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.39 | 1.36 | -0.01 | 67537.53 | 3.95 | skipped_fast |
| RWAINCUSDT | IDLE | 1.57 | 4.48 | 0.96 | 0.08 | 9667.19 | 21.53 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 1.97 | 1.2 | 0.01 | 118050.36 | 11.33 | skipped_fast |
| QNTUSDT | IDLE | 1.91 | 3.44 | 2.49 | 0.01 | 60145.25 | 7.8 | skipped_fast |
| TELUSDT | IDLE | 1.62 | 3.03 | 1.38 | 0.03 | 73920.36 | 23.39 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.5 | 0.13 | -0.01 | 185053.07 | 1.35 | skipped_fast |
| RWAUSDT | IDLE | 1.26 | 2.31 | 1.43 | 0.01 | 52379.18 | 7.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.13 | 0.0 | -0.01 | 2460.23 | 21.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.12 | -0.0 | 26429.32 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
