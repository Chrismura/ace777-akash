# Hulk DIGEST — 2026-09-22T06:08:44Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.94 | 2.21 | 0.92 | 0.06 | 120190146.02 | 1.98 | skipped_fast |
| ETHUSDT | IDLE | 0.83 | 1.49 | 1.07 | 0.02 | 717574262.85 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.56 | 1.01 | 0.76 | 0.05 | 1140992947.72 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.9 | 4.44 | 2.84 | 0.06 | 1233099.92 | 1.08 | skipped_fast |
| PYTHUSDT | IDLE | 1.91 | 4.22 | 2.08 | 0.04 | 827110.9 | 3.15 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 2.08 | 1.52 | 0.04 | 660191.77 | 9.4 | skipped_fast |
| WUSDT | IDLE | 1.53 | 2.97 | 0.57 | 0.01 | 478420.55 | 0.84 | skipped_fast |
| RIZEUSDT | IDLE | 2.49 | 24.45 | 9.82 | -0.17 | 53177.43 | 102.97 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 9.16 | 3.35 | 0.13 | 231557.56 | 15.89 | skipped_fast |
| ZBCNUSDT | IDLE | 1.66 | 3.57 | 1.27 | 0.02 | 273203.37 | 46.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 5.12 | 2.98 | 0.07 | 174039.95 | 14.88 | skipped_fast |
| KITEUSDT | IDLE | 2.06 | 4.04 | 0.56 | 0.06 | 83197.82 | 12.23 | skipped_fast |
| BIOUSDT | IDLE | 1.41 | 2.6 | 1.5 | 0.03 | 127834.01 | 3.47 | skipped_fast |
| REDUSDT | IDLE | 1.42 | 2.69 | 1.01 | 0.04 | 98172.82 | 9.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.03 | 2.52 | 1.53 | 0.07 | 22898.6 | 55.46 | skipped_fast |
| QNTUSDT | IDLE | 1.28 | 2.56 | 0.0 | 0.03 | 121896.72 | 28.12 | skipped_fast |
| TELUSDT | IDLE | 0.75 | 2.18 | 1.34 | 0.06 | 120784.47 | 43.22 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.8 | 0.0 | 57506.2 | 21.86 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.76 | 0.65 | 0.02 | 41580.56 | 11.62 | skipped_fast |
| FLUIDUSDT | IDLE | 0.42 | 0.85 | 0.0 | 0.07 | 13180.8 | 21.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
