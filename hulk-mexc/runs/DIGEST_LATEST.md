# Hulk DIGEST — 2026-08-21T20:40:03Z

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
| PYTHUSDT | IDLE | 1.32 | 4.78 | 2.7 | 0.08 | 5542294.26 | 2.1 | skipped_fast |
| XRPUSDT | IDLE | 1.26 | 4.21 | 3.47 | 0.1 | 128970117.5 | 2.92 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.0 | 25.8 | 12.33 | 0.18 | 153953.46 | 12.92 | skipped_fast |
| ZBCNUSDT | IDLE | 2.48 | 10.86 | 5.73 | 0.11 | 478616.81 | 52.6 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 3.91 | 0.39 | 0.09 | 639161.05 | 9.2 | skipped_fast |
| HBARUSDT | IDLE | 1.74 | 3.23 | 2.08 | 0.05 | 808385.08 | 1.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.33 | 4.81 | 3.25 | 0.09 | 514174.22 | 3.08 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.92 | 1.6 | 0.06 | 367721.98 | 14.79 | skipped_fast |
| BIOUSDT | IDLE | 2.55 | 5.33 | 3.1 | 0.01 | 189383.12 | 3.16 | skipped_fast |
| EDELUSDT | IDLE | 2.8 | 5.01 | 4.33 | -0.05 | 81394.04 | 33.99 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.8 | 0.02 | 10892.53 | 26.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.71 | 0.62 | 0.02 | 56286.69 | 47.09 | skipped_fast |
| KITEUSDT | IDLE | 1.25 | 4.0 | 2.61 | 0.1 | 60922.14 | 12.11 | skipped_fast |
| QAITUSDT | IDLE | 1.53 | 3.0 | 0.35 | -0.01 | 2793.19 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.48 | 0.01 | 181957.81 | 26.83 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.69 | 0.03 | 59916.22 | 3.13 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.25 | 1.07 | 0.03 | 53963.61 | 8.32 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.07 | 4286.4 | 21.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
