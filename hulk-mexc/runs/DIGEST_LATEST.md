# Hulk DIGEST — 2026-08-21T00:28:43Z

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
| XRPUSDT | IDLE | 0.77 | 4.5 | 0.4 | 0.15 | 103545724.4 | 1.57 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 2.16 | 0.25 | 0.04 | 1413514.06 | 2.25 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.38 | 8.34 | 1.26 | 0.11 | 301261.0 | 3.21 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.3 | 1.55 | -0.01 | 470441.72 | 11.09 | skipped_fast |
| ZBCNUSDT | IDLE | 1.74 | 5.51 | 0.44 | 0.04 | 274960.98 | 16.09 | skipped_fast |
| HBARUSDT | IDLE | 1.67 | 3.33 | 0.07 | 0.04 | 443438.63 | 1.35 | skipped_fast |
| WUSDT | IDLE | 1.23 | 2.45 | 0.12 | 0.04 | 255204.06 | 7.69 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 5.22 | 2.85 | 0.03 | 91238.94 | 32.56 | skipped_fast |
| QAITUSDT | IDLE | 2.55 | 6.4 | 1.93 | -0.03 | 6213.4 | 62.92 | skipped_fast |
| RIZEUSDT | IDLE | 1.66 | 9.79 | 6.16 | 0.0 | 48989.69 | 51.01 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.08 | 3.32 | 0.02 | 7832.49 | 78.52 | skipped_fast |
| BIOUSDT | IDLE | 0.56 | 2.75 | 0.32 | 0.12 | 230776.73 | 12.67 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 2.69 | 0.34 | 0.02 | 62584.08 | 13.11 | skipped_fast |
| REDUSDT | IDLE | 0.42 | 2.31 | 2.07 | 0.05 | 183956.37 | 11.59 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 4.98 | 3.32 | 0.14 | 186356.68 | 32.72 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.99 | 0.25 | 0.01 | 54168.45 | 16.99 | skipped_fast |
| QNTUSDT | IDLE | 0.83 | 1.81 | 0.34 | 0.06 | 64272.05 | 6.42 | skipped_fast |
| FLUIDUSDT | IDLE | 0.54 | 1.25 | 0.0 | 0.08 | 1512.87 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
