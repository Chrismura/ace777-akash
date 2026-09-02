# Hulk DIGEST — 2026-09-02T20:56:39Z

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
| XRPUSDT | IDLE | 1.18 | 2.31 | 0.32 | -0.0 | 37184413.86 | 0.74 | skipped_fast |
| ETHUSDT | IDLE | 0.7 | 1.33 | 0.48 | -0.01 | 365732323.04 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 1.06 | 0.18 | -0.0 | 512676452.21 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 5.36 | 2.29 | 0.14 | 1334783.48 | 3.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 6.3 | 1.45 | -0.07 | 1016982.85 | 2.38 | skipped_fast |
| ZBCNUSDT | IDLE | 3.38 | 8.19 | 2.82 | -0.04 | 181753.2 | 27.47 | skipped_fast |
| WUSDT | IDLE | 2.74 | 5.4 | 0.55 | -0.02 | 274116.92 | 11.24 | skipped_fast |
| CCUSDT | IDLE | 1.36 | 2.52 | 1.32 | -0.03 | 407432.36 | 8.16 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 9.23 | 3.88 | 0.14 | 134015.58 | 10.63 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 33.7 | 11.2 | 0.13 | 48031.75 | 598.51 | skipped_fast |
| EDELUSDT | IDLE | 1.09 | 5.67 | 4.96 | 0.06 | 166824.95 | 68.61 | skipped_fast |
| BIOUSDT | IDLE | 1.31 | 2.39 | 1.56 | -0.01 | 67509.16 | 7.9 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 1.97 | 1.34 | 0.01 | 118082.31 | 13.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.57 | 4.48 | 0.96 | 0.08 | 9693.17 | 43.13 | skipped_fast |
| QNTUSDT | IDLE | 1.92 | 3.44 | 2.72 | 0.01 | 59857.47 | 6.25 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 3.03 | 1.56 | 0.03 | 73882.39 | 29.25 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.5 | 0.18 | -0.0 | 185035.48 | 1.35 | skipped_fast |
| RWAUSDT | IDLE | 1.26 | 2.31 | 1.43 | 0.01 | 52292.72 | 7.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.13 | 0.0 | -0.01 | 2460.23 | 21.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.12 | -0.0 | 26451.8 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
