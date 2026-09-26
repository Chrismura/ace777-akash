# Hulk DIGEST — 2026-09-26T04:52:25Z

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
| XRPUSDT | IDLE | 1.07 | 1.91 | 1.57 | 0.01 | 109984754.83 | 1.93 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.54 | 0.22 | 0.0 | 300455972.91 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.41 | 0.17 | -0.0 | 653142315.39 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.26 | 3.33 | 1.41 | 0.08 | 1199749.55 | 1.35 | skipped_fast |
| CCUSDT | IDLE | 1.2 | 5.0 | 2.82 | 0.14 | 913236.66 | 6.84 | skipped_fast |
| HBARUSDT | IDLE | 1.32 | 2.35 | 1.95 | 0.02 | 897004.68 | 1.06 | skipped_fast |
| QNTUSDT | IDLE | 2.28 | 7.46 | 5.54 | 0.02 | 552840.03 | 3.03 | skipped_fast |
| WUSDT | IDLE | 1.45 | 2.68 | 1.84 | 0.05 | 456690.44 | 3.26 | skipped_fast |
| ZBCNUSDT | IDLE | 1.89 | 4.21 | 3.39 | 0.03 | 226336.45 | 17.57 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 4.96 | 3.6 | 0.05 | 148742.27 | 14.3 | skipped_fast |
| KITEUSDT | IDLE | 1.99 | 5.63 | 1.55 | 0.09 | 78621.02 | 7.26 | skipped_fast |
| REDUSDT | IDLE | 1.61 | 3.38 | 2.3 | 0.02 | 85598.19 | 9.33 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 2.93 | 2.25 | 0.06 | 113545.98 | 3.07 | skipped_fast |
| EDELUSDT | IDLE | 0.77 | 1.5 | 0.3 | 0.01 | 168472.61 | 20.26 | skipped_fast |
| RIZEUSDT | IDLE | 0.2 | 2.64 | 0.98 | -0.19 | 77829.18 | 33.7 | skipped_fast |
| RWAINCUSDT | IDLE | 0.25 | 0.71 | 0.71 | -0.1 | 12751.69 | 60.88 | skipped_fast |
| TELUSDT | IDLE | 0.7 | 1.23 | 1.15 | 0.01 | 113104.05 | 24.51 | skipped_fast |
| FLUIDUSDT | IDLE | 1.05 | 1.83 | 1.79 | 0.0 | 3437.87 | 21.74 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.04 | 0.44 | -0.01 | 52961.14 | 7.38 | skipped_fast |
| MNSRYUSDT | IDLE | 0.48 | 0.91 | 0.36 | 0.01 | 41085.7 | 39.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
