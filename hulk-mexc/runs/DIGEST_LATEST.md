# Hulk DIGEST — 2026-08-22T16:52:53Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 10.19 | 0.72 | 0.08 | 49881883.48 | 11.45 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 7.64 | 3.03 | 0.07 | 214844481.02 | 2.02 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.36 | 0.08 | 761395.58 | 4.27 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.89 | -0.01 | 1130907.57 | 6.45 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.53 | -0.1 | 629348.24 | 6.69 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.65 | -0.01 | 544799.59 | 6.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.26 | -0.02 | 313350.6 | 19.93 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.58 | -0.08 | 226125.56 | 6.68 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 4.35 | 0.78 | 0.03 | 86587.82 | 9.72 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.02 | 74694.07 | 22.75 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.77 | -0.14 | 128073.69 | 10.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 3.47 | 0.52 | 0.05 | 46599.51 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.87 | -0.01 | 181208.45 | 3.14 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.1 | -0.0 | 136508.11 | 53.59 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7704.25 | 113.06 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.53 | skipped_fast |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
