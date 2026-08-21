# Hulk DIGEST — 2026-08-21T22:59:15Z

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
| PYTHUSDT | IDLE | 1.51 | 5.77 | 0.2 | 0.12 | 5929079.44 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.68 | 6.54 | 0.32 | 0.15 | 137173180.16 | 3.45 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.47 | 0.24 | 0.14 | 661747.45 | 7.94 | skipped_fast |
| HBARUSDT | IDLE | 2.24 | 5.03 | 0.33 | 0.09 | 878358.35 | 2.51 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 9.96 | 0.51 | 0.15 | 508853.38 | 29.18 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.91 | 0.32 | 0.09 | 372964.17 | 11.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.14 | 0.05 | 543023.37 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 0.98 | 0.03 | 187819.87 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.89 | 0.19 | 157214.38 | 18.57 | skipped_fast |
| EDELUSDT | IDLE | 2.29 | 5.04 | 0.11 | -0.03 | 82578.54 | 21.83 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10217.99 | 16.16 | skipped_fast |
| QAITUSDT | IDLE | 2.36 | 4.38 | 2.29 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.05 | 186721.77 | 10.36 | skipped_fast |
| QNTUSDT | IDLE | 2.46 | 4.91 | 0.0 | 0.07 | 88649.05 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.19 | 0.1 | 61366.42 | 20.32 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.94 | 0.06 | 56400.01 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 2.0 | 0.08 | 0.04 | 54191.45 | 24.58 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.79 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
