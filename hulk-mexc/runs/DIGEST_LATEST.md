# Hulk DIGEST — 2026-08-30T16:10:31Z

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
| XRPUSDT | IDLE | 0.85 | 1.57 | 0.83 | 0.0 | 18158520.0 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.27 | 0.15 | 0.02 | 167241646.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.13 | 0.21 | 0.01 | 259215337.77 | 0.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.25 | 8.01 | 6.43 | -0.03 | 562353.8 | 12.52 | skipped_fast |
| PYTHUSDT | IDLE | 3.16 | 5.93 | 2.63 | 0.02 | 407253.53 | 2.04 | skipped_fast |
| ZBCNUSDT | IDLE | 2.55 | 4.6 | 3.34 | -0.03 | 163153.92 | 5.24 | skipped_fast |
| EDELUSDT | IDLE | 2.16 | 5.99 | 5.33 | 0.05 | 72078.38 | 34.19 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.63 | 0.34 | 0.04 | 221672.46 | 10.49 | skipped_fast |
| CCUSDT | IDLE | 0.9 | 1.62 | 1.17 | 0.02 | 268381.42 | 5.91 | skipped_fast |
| REDUSDT | IDLE | 1.1 | 2.14 | 0.35 | 0.01 | 60148.41 | 13.53 | skipped_fast |
| BIOUSDT | IDLE | 0.73 | 1.36 | 0.69 | -0.01 | 73871.76 | 3.65 | skipped_fast |
| KITEUSDT | IDLE | 0.65 | 1.21 | 0.64 | -0.04 | 60845.42 | 10.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.7 | 2.45 | 0.98 | -0.05 | 45944.33 | 58.56 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 3.37 | 0.52 | -0.02 | 82047.67 | 40.9 | skipped_fast |
| RWAINCUSDT | IDLE | 1.5 | 3.01 | 0.0 | 0.0 | 1671.88 | 127.74 | skipped_fast |
| HBARUSDT | IDLE | 0.62 | 1.13 | 0.74 | -0.0 | 130173.27 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.52 | 0.96 | 0.5 | 0.0 | 38368.1 | 6.47 | skipped_fast |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.64 | 0.02 | 33063.58 | 42.7 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.82 | 0.16 | 0.01 | 53120.26 | 32.52 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.83 | 0.0 | 0.02 | 2467.03 | 21.67 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
