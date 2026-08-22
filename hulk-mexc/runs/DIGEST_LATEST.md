# Hulk DIGEST — 2026-08-22T02:43:17Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.58 | 10.52 | 0.51 | 0.16 | 7193951.24 | 1.91 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 12.02 | 0.21 | 0.19 | 156904946.98 | 1.96 | skipped_fast |
| HBARUSDT | IDLE | 2.44 | 5.79 | 0.17 | 0.09 | 979460.5 | 2.46 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 9.63 | 2.2 | 0.1 | 541139.22 | 26.42 | skipped_fast |
| CCUSDT | IDLE | 1.87 | 7.61 | 0.04 | 0.15 | 657091.54 | 14.59 | skipped_fast |
| CHIPUSDT | IDLE | 2.29 | 5.26 | 0.27 | -0.02 | 459442.65 | 3.0 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.19 | 8.18 | 1.91 | 0.1 | 192856.04 | 17.94 | skipped_fast |
| WUSDT | IDLE | 1.98 | 5.8 | 0.18 | 0.11 | 412867.39 | 7.97 | skipped_fast |
| EDELUSDT | IDLE | 2.51 | 5.02 | 3.58 | -0.04 | 79912.99 | 33.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.23 | 0.1 | 61304.91 | 28.82 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 5.07 | 0.19 | 158145.03 | 10.39 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9400.35 | 16.28 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.33 | 0.08 | 172678.28 | 11.91 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.28 | 0.12 | 62472.4 | 11.66 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.06 | 174228.86 | 51.76 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 22.43 | skipped_fast |
| RWAUSDT | IDLE | 1.14 | 2.25 | 0.24 | 0.04 | 55557.44 | 16.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
