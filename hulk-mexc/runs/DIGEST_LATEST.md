# Hulk DIGEST — 2026-08-21T21:14:06Z

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
| PYTHUSDT | IDLE | 1.2 | 4.51 | 1.33 | 0.09 | 5604456.41 | 2.08 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 1.97 | 0.1 | 128143369.9 | 2.17 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.35 | 0.06 | 515340.44 | 3.12 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 8.19 | 5.05 | 0.09 | 482246.68 | 29.04 | skipped_fast |
| CCUSDT | IDLE | 1.16 | 3.14 | 0.67 | 0.1 | 642699.25 | 10.16 | skipped_fast |
| HBARUSDT | IDLE | 1.59 | 3.04 | 0.95 | 0.06 | 809343.3 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.97 | 3.83 | 0.74 | 0.06 | 367071.82 | 15.7 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.2 | 2.67 | 0.01 | 187844.85 | 6.32 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.16 | 0.16 | 153518.34 | 19.64 | skipped_fast |
| EDELUSDT | IDLE | 2.09 | 4.12 | 3.3 | -0.05 | 82446.49 | 11.34 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.41 | 0.02 | 56215.94 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.02 | 10271.93 | 26.85 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 1.96 | 0.11 | 61108.38 | 11.12 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.39 | 1.43 | 0.01 | 179845.34 | 48.27 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.65 | 0.04 | 61161.6 | 1.56 | skipped_fast |
| QAITUSDT | IDLE | 1.75 | 3.21 | 1.91 | -0.02 | 2723.87 | 172.96 | skipped_fast |
| RWAUSDT | IDLE | 0.64 | 1.17 | 0.74 | 0.03 | 53732.17 | 24.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 22.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
