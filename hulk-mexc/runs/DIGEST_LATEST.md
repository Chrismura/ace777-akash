# Hulk DIGEST — 2026-08-22T02:40:00Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.6 | 10.52 | 1.12 | 0.16 | 7154945.61 | 1.92 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 12.02 | 0.55 | 0.18 | 156623982.97 | 0.65 | skipped_fast |
| HBARUSDT | IDLE | 2.43 | 5.62 | 0.42 | 0.08 | 978798.0 | 1.23 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 9.63 | 1.27 | 0.11 | 541966.9 | 40.18 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 6.79 | 0.09 | 0.15 | 653817.48 | 8.66 | skipped_fast |
| CHIPUSDT | IDLE | 2.28 | 5.26 | 0.0 | -0.01 | 458865.21 | 11.99 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.14 | 8.18 | 1.0 | 0.1 | 193375.77 | 5.92 | skipped_fast |
| WUSDT | IDLE | 1.94 | 5.62 | 0.05 | 0.1 | 411190.21 | 13.96 | skipped_fast |
| EDELUSDT | IDLE | 2.44 | 5.02 | 2.5 | -0.03 | 79742.3 | 33.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.23 | 0.1 | 61551.43 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 5.28 | 0.18 | 157854.0 | 15.22 | skipped_fast |
| QNTUSDT | IDLE | 2.35 | 5.48 | 0.48 | 0.08 | 172679.6 | 7.46 | skipped_fast |
| RWAINCUSDT | IDLE | 1.86 | 3.27 | 2.95 | 0.01 | 9365.53 | 37.95 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.16 | 0.12 | 62496.94 | 9.85 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.18 | 0.06 | 176328.51 | 46.57 | skipped_fast |
| RWAUSDT | IDLE | 1.14 | 2.25 | 0.24 | 0.04 | 55424.65 | 24.48 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 49.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
