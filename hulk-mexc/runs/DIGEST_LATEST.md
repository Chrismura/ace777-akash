# Hulk DIGEST — 2026-10-17T07:15:00Z

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
| PYTHUSDT | IDLE | 1.32 | 3.95 | 3.44 | -0.12 | 1677221.46 | 1.19 | skipped_fast |
| WUSDT | IDLE | 3.11 | 6.76 | 0.93 | -0.03 | 1281235.91 | 6.05 | skipped_fast |
| XRPUSDT | IDLE | 0.37 | 0.71 | 0.22 | -0.02 | 24289821.38 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 0.33 | 0.65 | 0.06 | -0.01 | 191357640.17 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.15 | 0.3 | 0.0 | -0.01 | 300340229.61 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.57 | 2.96 | 1.23 | -0.02 | 716832.04 | 1.48 | skipped_fast |
| KITEUSDT | IDLE | 2.47 | 4.82 | 0.79 | 0.02 | 56028.14 | 12.75 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 1.97 | 0.7 | -0.04 | 351039.57 | 10.56 | skipped_fast |
| EDELUSDT | IDLE | 1.49 | 2.66 | 2.15 | -0.02 | 181454.64 | 17.18 | skipped_fast |
| ZBCNUSDT | IDLE | 1.15 | 2.04 | 1.74 | -0.03 | 204412.13 | 13.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 3.14 | 2.06 | -0.05 | 51025.68 | 29.83 | skipped_fast |
| CHIPUSDT | IDLE | 0.91 | 2.47 | 2.26 | -0.09 | 112363.13 | 10.9 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 1.75 | 1.51 | -0.05 | 73863.44 | 16.15 | skipped_fast |
| BIOUSDT | IDLE | 0.6 | 1.04 | 1.03 | -0.04 | 65137.97 | 4.01 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 1.0 | 0.66 | -0.03 | 315023.96 | 3.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.5 | 2.57 | 0.0 | -0.09 | 24435.36 | 21.74 | skipped_fast |
| TELUSDT | IDLE | 0.87 | 1.53 | 1.45 | -0.05 | 84869.79 | 23.47 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.88 | 0.4 | -0.01 | 51879.5 | 23.95 | skipped_fast |
| FLUIDUSDT | IDLE | 0.6 | 1.21 | 0.0 | 0.0 | 4714.54 | 21.26 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.08 | -0.0 | 30473.05 | 7.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
