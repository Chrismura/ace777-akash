# Hulk DIGEST — 2026-08-17T04:10:27Z

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
| XRPUSDT | IDLE | 0.82 | 1.62 | 0.17 | 0.0 | 8176526.21 | 1.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.49 | 26.44 | 17.11 | 0.07 | 44113.16 | 13.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 7.11 | 1.67 | 0.06 | 292025.91 | 3.46 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.6 | 0.97 | -0.02 | 287431.51 | 10.47 | skipped_fast |
| WUSDT | IDLE | 0.93 | 1.66 | 1.39 | 0.02 | 188748.23 | 11.73 | skipped_fast |
| EDELUSDT | IDLE | 1.85 | 3.58 | 0.77 | 0.03 | 55281.39 | 51.68 | skipped_fast |
| PYTHUSDT | IDLE | 1.0 | 1.99 | 0.03 | -0.01 | 152012.57 | 2.57 | skipped_fast |
| KITEUSDT | IDLE | 1.42 | 2.62 | 1.48 | -0.01 | 54552.56 | 14.87 | skipped_fast |
| REDUSDT | IDLE | 1.37 | 2.4 | 2.3 | -0.06 | 59554.3 | 16.48 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 1.48 | 0.78 | -0.0 | 195461.83 | 15.31 | skipped_fast |
| BIOUSDT | IDLE | 0.74 | 1.46 | 0.16 | -0.01 | 64191.59 | 4.11 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 3.35 | 0.61 | 0.0 | 90585.82 | 40.82 | skipped_fast |
| QNTUSDT | IDLE | 1.28 | 2.28 | 1.93 | -0.03 | 32557.61 | 3.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.65 | 1.25 | 0.34 | 0.01 | 3226.81 | 67.64 | skipped_fast |
| HBARUSDT | IDLE | 0.59 | 1.15 | 0.18 | -0.0 | 88280.4 | 1.54 | skipped_fast |
| QAITUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 2142.08 | 61.3 | skipped_fast |
| RWAUSDT | IDLE | 0.45 | 0.88 | 0.09 | 0.01 | 50480.76 | 26.08 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.14 | 0.15 | 0.01 | 411.11 | 22.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
