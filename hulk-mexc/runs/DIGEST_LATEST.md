# Hulk DIGEST — 2026-08-18T08:23:23Z

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
| XRPUSDT | IDLE | 0.62 | 1.15 | 0.55 | -0.01 | 12226035.39 | 1.0 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 28.93 | 14.04 | 0.17 | 78999.69 | 25.54 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.45 | 11.21 | 8.4 | -0.02 | 82002.81 | 13.1 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 8.07 | 1.83 | -0.1 | 298013.96 | 6.91 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 3.06 | 1.1 | -0.04 | 301149.7 | 4.35 | skipped_fast |
| KITEUSDT | IDLE | 2.62 | 4.61 | 4.26 | -0.02 | 61240.0 | 16.48 | skipped_fast |
| QAITUSDT | IDLE | 1.64 | 10.79 | 8.08 | -0.05 | 11406.21 | 56.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.15 | 3.76 | 3.62 | -0.07 | 1845.52 | 42.28 | skipped_fast |
| ZBCNUSDT | IDLE | 0.73 | 1.32 | 0.94 | -0.01 | 214716.73 | 9.61 | skipped_fast |
| PYTHUSDT | IDLE | 0.81 | 1.54 | 0.55 | -0.03 | 178877.72 | 2.63 | skipped_fast |
| WUSDT | IDLE | 0.82 | 1.51 | 0.83 | -0.03 | 149103.08 | 14.75 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.33 | 0.25 | -0.02 | 81026.9 | 4.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.39 | 2.72 | 1.23 | -0.06 | 74902.84 | 47.45 | skipped_fast |
| HBARUSDT | IDLE | 0.65 | 1.2 | 0.68 | 0.0 | 127215.85 | 1.53 | skipped_fast |
| TELUSDT | IDLE | 0.77 | 1.67 | 0.14 | -0.04 | 134594.52 | 42.89 | skipped_fast |
| QNTUSDT | IDLE | 0.51 | 0.9 | 0.75 | -0.0 | 37203.59 | 7.16 | skipped_fast |
| RWAUSDT | IDLE | 0.39 | 0.7 | 0.52 | -0.0 | 50257.74 | 8.69 | skipped_fast |
| FLUIDUSDT | IDLE | 0.3 | 0.54 | 0.38 | -0.04 | 201.93 | 21.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
