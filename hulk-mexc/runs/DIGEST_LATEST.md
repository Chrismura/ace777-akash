# Hulk DIGEST — 2026-08-18T16:09:38Z

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
| XRPUSDT | IDLE | 0.56 | 1.05 | 0.4 | -0.0 | 11133774.08 | 1.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.4 | 8.95 | 6.61 | -0.08 | 238751.71 | 3.73 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 27.25 | 18.21 | -0.19 | 18256.13 | 67.85 | skipped_fast |
| REDUSDT | IDLE | 1.55 | 11.28 | 9.47 | 0.09 | 124986.36 | 10.83 | skipped_fast |
| RIZEUSDT | IDLE | 2.93 | 5.45 | 4.82 | -0.09 | 51665.12 | 47.45 | skipped_fast |
| PYTHUSDT | IDLE | 1.04 | 2.03 | 0.34 | -0.01 | 190790.75 | 2.59 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.46 | 1.14 | -0.01 | 248846.59 | 9.86 | skipped_fast |
| ZBCNUSDT | IDLE | 1.07 | 1.89 | 1.68 | -0.01 | 200790.54 | 22.96 | skipped_fast |
| EDELUSDT | IDLE | 1.47 | 4.34 | 2.73 | -0.04 | 75101.4 | 26.67 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.68 | 0.04 | 0.01 | 74563.67 | 4.01 | skipped_fast |
| KITEUSDT | IDLE | 1.13 | 2.17 | 0.55 | -0.0 | 65067.77 | 16.33 | skipped_fast |
| TELUSDT | IDLE | 2.11 | 4.27 | 1.23 | 0.03 | 116487.71 | 27.7 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 2.1 | 0.47 | -0.02 | 5071.71 | 5.91 | skipped_fast |
| WUSDT | IDLE | 0.48 | 0.93 | 0.17 | -0.03 | 139261.25 | 14.72 | skipped_fast |
| HBARUSDT | IDLE | 0.51 | 0.96 | 0.44 | -0.0 | 117941.2 | 1.51 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 1.73 | 0.39 | -0.01 | 34969.63 | 3.56 | skipped_fast |
| RWAUSDT | IDLE | 0.51 | 0.96 | 0.35 | -0.01 | 50703.6 | 17.36 | skipped_fast |
| FLUIDUSDT | IDLE | 0.68 | 1.35 | 0.0 | -0.0 | 172.68 | 21.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
