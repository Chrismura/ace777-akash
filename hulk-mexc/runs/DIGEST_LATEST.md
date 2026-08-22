# Hulk DIGEST — 2026-08-22T16:50:32Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.09 | 10.19 | 1.16 | 0.08 | 49951348.35 | 1.92 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 7.64 | 2.9 | 0.07 | 214900650.4 | 4.04 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.81 | -0.01 | 1130878.2 | 5.15 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.18 | 0.09 | 760636.45 | 5.97 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.86 | -0.1 | 629290.06 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.55 | -0.01 | 544871.38 | 12.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.52 | -0.03 | 314535.34 | 22.0 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.36 | -0.08 | 225890.45 | 20.09 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 4.35 | 0.77 | 0.03 | 86581.32 | 13.27 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.52 | 1.57 | -0.01 | 74668.98 | 11.37 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.6 | -0.14 | 128076.47 | 10.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 3.47 | 0.23 | 0.05 | 46606.34 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.76 | -0.01 | 181189.58 | 3.14 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7704.25 | 113.06 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.89 | -0.0 | 136464.1 | 69.61 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.23 | 0.08 | 0.02 | 56479.12 | 24.28 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.32 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
