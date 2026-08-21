# Hulk DIGEST — 2026-08-21T21:06:42Z

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
| PYTHUSDT | IDLE | 1.21 | 4.51 | 1.68 | 0.09 | 5582408.6 | 2.09 | skipped_fast |
| XRPUSDT | IDLE | 1.17 | 3.73 | 2.59 | 0.1 | 128069469.44 | 2.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.03 | 8.19 | 5.96 | 0.08 | 480291.83 | 29.32 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 4.62 | 3.85 | 0.08 | 513848.21 | 3.11 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.14 | 0.25 | 0.1 | 640981.98 | 6.44 | skipped_fast |
| HBARUSDT | IDLE | 1.64 | 3.04 | 1.55 | 0.06 | 806168.84 | 2.6 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.83 | 0.88 | 0.06 | 368045.83 | 11.55 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.2 | 2.76 | 0.01 | 187899.1 | 3.16 | skipped_fast |
| REDUSDT | IDLE | 1.35 | 11.01 | 9.46 | 0.16 | 153376.21 | 10.68 | skipped_fast |
| EDELUSDT | IDLE | 2.1 | 4.12 | 3.52 | -0.06 | 82274.93 | 45.4 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.41 | 0.01 | 56238.21 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.04 | 10891.5 | 48.14 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.0 | 2.33 | 0.11 | 61130.22 | 11.16 | skipped_fast |
| TELUSDT | IDLE | 1.37 | 3.39 | 1.11 | 0.01 | 180430.02 | 32.12 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 60166.85 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.72 | 3.0 | 2.88 | -0.03 | 2646.1 | 178.96 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.17 | 1.07 | 0.03 | 53745.72 | 16.64 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
