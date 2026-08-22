# Hulk DIGEST — 2026-08-22T12:32:00Z

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.87 | 0.11 | 215882962.8 | 1.98 | skipped_fast |
| PYTHUSDT | IDLE | 1.63 | 7.83 | 1.65 | 0.06 | 51607964.83 | 1.98 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 4.63 | 2.02 | 0.03 | 1260580.62 | 6.41 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 8.38 | 2.76 | 0.14 | 776390.3 | 8.36 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.47 | 0.02 | 577814.8 | 10.55 | skipped_fast |
| ZBCNUSDT | IDLE | 2.2 | 5.77 | 3.54 | -0.02 | 350662.98 | 11.26 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.25 | -0.09 | 605345.61 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.65 | 6.37 | 0.24 | 0.05 | 83433.16 | 21.12 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.89 | 2.32 | -0.02 | 78154.6 | 33.84 | skipped_fast |
| BIOUSDT | IDLE | 0.77 | 5.65 | 0.88 | -0.01 | 241787.32 | 3.18 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.16 | 2.56 | -0.01 | 2396.75 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.37 | 0.01 | 153352.97 | 21.35 | skipped_fast |
| TELUSDT | IDLE | 2.17 | 5.61 | 3.93 | -0.03 | 163499.83 | 47.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10048.58 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.55 | 0.0 | 188088.83 | 1.55 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.27 | -0.03 | 47955.02 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 0.98 | 1.8 | 1.12 | 0.02 | 57741.83 | 16.26 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 20.71 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
