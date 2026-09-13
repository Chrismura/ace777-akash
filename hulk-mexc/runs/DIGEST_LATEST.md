# Hulk DIGEST — 2026-09-13T10:39:43Z

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
| XRPUSDT | IDLE | 1.25 | 2.21 | 1.88 | -0.02 | 14039624.59 | 2.23 | skipped_fast |
| ETHUSDT | IDLE | 1.2 | 2.14 | 1.71 | -0.02 | 211025878.25 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.54 | 0.97 | 0.71 | -0.01 | 300987543.84 | 0.0 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 14.26 | 12.12 | 0.05 | 203811.77 | 24.91 | skipped_fast |
| PYTHUSDT | IDLE | 2.21 | 3.92 | 3.32 | 0.01 | 464080.55 | 1.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 29.39 | 13.64 | 0.15 | 102281.77 | 62.64 | skipped_fast |
| CCUSDT | IDLE | 2.48 | 4.33 | 4.14 | -0.04 | 278190.97 | 3.16 | skipped_fast |
| WUSDT | IDLE | 1.51 | 2.69 | 2.18 | 0.01 | 245449.9 | 13.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.69 | 3.83 | 3.69 | -0.03 | 78623.93 | 12.97 | skipped_fast |
| BIOUSDT | IDLE | 1.39 | 2.54 | 1.66 | -0.01 | 70425.75 | 3.93 | skipped_fast |
| KITEUSDT | IDLE | 1.46 | 2.69 | 1.58 | 0.03 | 62810.89 | 13.75 | skipped_fast |
| REDUSDT | IDLE | 1.4 | 2.52 | 1.8 | 0.02 | 55744.07 | 9.94 | skipped_fast |
| ZBCNUSDT | IDLE | 0.74 | 2.11 | 1.53 | -0.04 | 200537.99 | 20.85 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 4.73 | 2.69 | -0.05 | 85417.17 | 25.08 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.35 | -0.04 | 7816.04 | 5.59 | skipped_fast |
| FLUIDUSDT | IDLE | 1.99 | 3.57 | 2.71 | 0.01 | 1217.06 | 22.19 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.57 | 0.62 | 0.01 | 152720.73 | 1.33 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.31 | 0.87 | -0.01 | 36286.15 | 1.57 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.81 | 1.33 | -0.01 | 55798.49 | 90.02 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.14 | -0.0 | 32966.49 | 30.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
