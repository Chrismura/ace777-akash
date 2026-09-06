# Hulk DIGEST — 2026-09-06T00:30:03Z

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
| XRPUSDT | IDLE | 0.75 | 1.41 | 0.59 | 0.01 | 23239876.21 | 1.41 | skipped_fast |
| ETHUSDT | IDLE | 0.4 | 0.78 | 0.19 | 0.01 | 162609630.71 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.07 | 0.0 | 368665158.73 | 0.0 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.26 | 20.43 | 13.04 | -0.06 | 128486.91 | 61.54 | skipped_fast |
| PYTHUSDT | IDLE | 1.9 | 3.73 | 0.43 | 0.03 | 358475.86 | 1.78 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 3.41 | 1.55 | 0.07 | 421736.62 | 1.69 | skipped_fast |
| RWAINCUSDT | IDLE | 2.87 | 5.2 | 3.59 | 0.0 | 8280.39 | 26.96 | skipped_fast |
| ZBCNUSDT | IDLE | 1.73 | 3.24 | 1.41 | -0.0 | 217321.21 | 26.54 | skipped_fast |
| WUSDT | IDLE | 1.57 | 3.11 | 0.23 | 0.05 | 161370.91 | 10.82 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 1.39 | 1.1 | 0.02 | 271864.26 | 6.43 | skipped_fast |
| BIOUSDT | IDLE | 0.8 | 1.51 | 0.64 | 0.03 | 82352.65 | 7.14 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 1.73 | 0.57 | 0.02 | 60431.43 | 13.4 | skipped_fast |
| HBARUSDT | IDLE | 0.76 | 1.43 | 0.55 | 0.02 | 356449.14 | 1.24 | skipped_fast |
| EDELUSDT | IDLE | 0.23 | 2.85 | 2.77 | -0.02 | 168093.08 | 28.5 | skipped_fast |
| KITEUSDT | IDLE | 0.55 | 1.21 | 0.83 | -0.08 | 64441.32 | 10.32 | skipped_fast |
| TELUSDT | IDLE | 1.94 | 3.58 | 2.01 | -0.0 | 72036.16 | 47.0 | skipped_fast |
| RWAUSDT | IDLE | 1.64 | 2.96 | 2.19 | 0.04 | 52930.21 | 13.99 | skipped_fast |
| QNTUSDT | IDLE | 0.47 | 0.93 | 0.0 | 0.02 | 36599.96 | 4.6 | skipped_fast |
| MNSRYUSDT | IDLE | 0.14 | 0.26 | 0.1 | 0.0 | 38846.41 | 6.82 | skipped_fast |
| FLUIDUSDT | IDLE | 0.4 | 0.79 | 0.1 | 0.01 | 385.8 | 21.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
