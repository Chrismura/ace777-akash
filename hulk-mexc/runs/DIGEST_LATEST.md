# Hulk DIGEST — 2026-08-17T06:47:12Z

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
| XRPUSDT | IDLE | 0.65 | 1.3 | 0.01 | 0.0 | 9176350.63 | 1.99 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.66 | 15.34 | 0.13 | 0.14 | 320316.69 | 12.65 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 25.44 | 11.99 | 0.14 | 46385.98 | 238.12 | skipped_fast |
| WUSDT | IDLE | 1.21 | 2.14 | 1.85 | 0.02 | 188493.14 | 11.79 | skipped_fast |
| REDUSDT | IDLE | 1.73 | 3.13 | 2.2 | -0.04 | 58212.11 | 15.34 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.57 | 0.46 | -0.01 | 257061.45 | 6.27 | skipped_fast |
| EDELUSDT | IDLE | 1.64 | 3.17 | 0.77 | 0.04 | 55232.3 | 12.91 | skipped_fast |
| BIOUSDT | IDLE | 1.54 | 3.08 | 0.04 | 0.01 | 62976.92 | 8.08 | skipped_fast |
| PYTHUSDT | IDLE | 0.98 | 1.97 | 0.0 | 0.0 | 162279.29 | 5.09 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 2.54 | 1.61 | 0.0 | 54163.55 | 14.87 | skipped_fast |
| ZBCNUSDT | IDLE | 0.57 | 1.03 | 0.7 | 0.01 | 195513.34 | 18.47 | skipped_fast |
| QAITUSDT | IDLE | 1.08 | 2.41 | 2.0 | -0.03 | 2151.91 | 61.48 | skipped_fast |
| RWAINCUSDT | IDLE | 0.58 | 1.02 | 0.9 | -0.01 | 2286.48 | 79.55 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 1.65 | 1.49 | -0.01 | 87826.58 | 41.15 | skipped_fast |
| QNTUSDT | IDLE | 0.82 | 1.53 | 0.78 | -0.02 | 34037.49 | 5.36 | skipped_fast |
| HBARUSDT | IDLE | 0.44 | 0.88 | 0.02 | 0.0 | 89970.85 | 1.53 | skipped_fast |
| FLUIDUSDT | IDLE | 0.94 | 1.69 | 1.27 | 0.01 | 802.22 | 22.56 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 1.05 | 0.09 | 0.01 | 49579.58 | 17.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
