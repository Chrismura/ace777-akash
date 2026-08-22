# Hulk DIGEST — 2026-08-22T17:12:22Z

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
| PYTHUSDT | IDLE | 1.72 | 8.48 | 0.28 | 0.1 | 49182806.33 | 7.59 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.86 | 0.04 | 213967858.35 | 1.36 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 4.25 | 0.17 | 0.11 | 771712.15 | 1.67 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.05 | -0.01 | 1106504.05 | 5.17 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.06 | -0.1 | 631169.83 | 6.71 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.36 | -0.01 | 534641.23 | 11.59 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.74 | -0.08 | 226246.92 | 3.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 3.45 | 1.0 | -0.01 | 310375.53 | 20.39 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 3.0 | 2.91 | -0.03 | 74832.61 | 34.5 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 3.22 | 0.52 | 0.04 | 87646.07 | 11.49 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.19 | -0.13 | 122259.75 | 21.7 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.44 | 0.05 | 46192.11 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.0 | -0.01 | 181165.34 | 4.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 86.25 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.05 | -0.0 | 136262.23 | 37.5 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.16 | 0.02 | 56110.67 | 8.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
