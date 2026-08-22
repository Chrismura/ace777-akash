# Hulk DIGEST — 2026-08-22T17:09:25Z

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
| PYTHUSDT | IDLE | 1.73 | 8.45 | 0.62 | 0.1 | 49188636.44 | 7.61 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.69 | 0.05 | 214046947.71 | 2.04 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.04 | -0.01 | 1116460.42 | 5.16 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 4.25 | 0.3 | 0.1 | 769511.33 | 0.83 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.1 | -0.1 | 631092.02 | 6.72 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.44 | -0.01 | 535493.76 | 13.74 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.27 | -0.01 | 310465.01 | 13.8 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.61 | -0.08 | 226496.01 | 3.35 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 3.0 | 2.91 | -0.02 | 74911.87 | 45.92 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 3.22 | 0.57 | 0.04 | 87536.01 | 13.22 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.68 | -0.14 | 122443.03 | 13.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.63 | 0.34 | 0.05 | 46171.22 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.04 | -0.02 | 181178.23 | 3.15 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 86.25 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.94 | -0.0 | 136219.17 | 42.9 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 56145.96 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
