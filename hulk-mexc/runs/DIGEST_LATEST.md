# Hulk DIGEST — 2026-08-22T16:15:23Z

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
| PYTHUSDT | IDLE | 1.51 | 7.24 | 1.67 | 0.05 | 51450297.87 | 1.98 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 7.64 | 5.48 | 0.04 | 215382229.54 | 2.07 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.08 | -0.01 | 1140861.32 | 3.91 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 4.14 | 2.72 | 0.08 | 765944.52 | 3.43 | skipped_fast |
| CHIPUSDT | IDLE | 0.58 | 3.36 | 1.36 | -0.1 | 623837.52 | 3.37 | skipped_fast |
| WUSDT | IDLE | 0.65 | 2.58 | 1.92 | -0.02 | 546058.98 | 9.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 3.49 | 2.65 | -0.06 | 317991.38 | 11.92 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.26 | -0.07 | 219722.95 | 6.65 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 4.35 | 1.18 | 0.04 | 85449.6 | 12.43 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 2.52 | 2.46 | -0.03 | 74816.2 | 22.88 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.47 | -0.12 | 133924.6 | 22.02 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.05 | 0.03 | 56536.69 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.36 | -0.02 | 183818.6 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 48.3 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.52 | -0.0 | 137334.78 | 31.95 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.06 | 0.4 | 0.02 | 56311.49 | 8.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 22.45 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
