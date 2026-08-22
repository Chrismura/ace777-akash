# Hulk DIGEST — 2026-08-22T17:14:42Z

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
| PYTHUSDT | IDLE | 1.74 | 8.48 | 0.93 | 0.1 | 49179090.63 | 13.37 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.82 | 0.05 | 214019145.01 | 1.36 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.24 | -0.0 | 1106052.49 | 3.88 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 4.25 | 0.72 | 0.11 | 772256.16 | 8.39 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.1 | -0.1 | 631221.27 | 3.36 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.54 | -0.01 | 535570.73 | 12.67 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.92 | -0.08 | 226309.99 | 3.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.21 | -0.01 | 310002.78 | 27.57 | skipped_fast |
| EDELUSDT | IDLE | 1.75 | 3.11 | 2.57 | -0.02 | 74762.57 | 34.5 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 3.22 | 0.85 | 0.04 | 87713.39 | 13.27 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.3 | -0.13 | 122348.38 | 9.96 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.44 | 0.05 | 46119.52 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.0 | -0.01 | 181174.79 | 3.15 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.05 | -0.0 | 136298.84 | 37.52 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 113.06 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.16 | 0.02 | 56098.75 | 8.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
