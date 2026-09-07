# Hulk DIGEST — 2026-09-07T12:35:34Z

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
| XRPUSDT | IDLE | 0.87 | 1.65 | 0.57 | -0.01 | 33294267.76 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.55 | 1.04 | 0.34 | -0.0 | 325118529.68 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.87 | 0.24 | -0.01 | 409095201.37 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.97 | 3.86 | 0.48 | 0.01 | 585949.17 | 1.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.42 | 6.53 | 4.3 | -0.08 | 345591.79 | 12.87 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 3.66 | 2.13 | -0.02 | 426516.51 | 7.41 | skipped_fast |
| WUSDT | IDLE | 1.59 | 2.96 | 1.52 | 0.0 | 440511.99 | 14.56 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 7.34 | 5.62 | -0.06 | 76109.31 | 19.9 | skipped_fast |
| KITEUSDT | IDLE | 2.5 | 4.52 | 3.15 | -0.03 | 57941.97 | 10.66 | skipped_fast |
| REDUSDT | IDLE | 2.4 | 4.69 | 0.75 | 0.03 | 65781.54 | 12.17 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 2.93 | 1.62 | -0.01 | 191965.03 | 10.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 9.0 | 3.55 | -0.12 | 73312.3 | 67.96 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 2.13 | 0.11 | -0.02 | 70289.75 | 3.66 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.91 | 0.0 | 0.0 | 333574.34 | 1.23 | skipped_fast |
| TELUSDT | IDLE | 1.77 | 3.11 | 2.84 | -0.01 | 107966.54 | 29.28 | skipped_fast |
| RWAINCUSDT | IDLE | 0.62 | 2.13 | 0.0 | 0.07 | 6059.04 | 38.65 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 2.01 | 0.77 | 0.0 | 41748.76 | 7.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.81 | 1.58 | 0.25 | -0.01 | 1152.45 | 21.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.16 | -0.0 | 37589.41 | 2.69 | skipped_fast |
| RWAUSDT | IDLE | 0.27 | 0.51 | 0.22 | -0.01 | 53434.71 | 28.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
