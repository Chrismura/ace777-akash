# Hulk DIGEST — 2026-10-11T16:19:57Z

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
| XRPUSDT | IDLE | 1.38 | 2.67 | 0.65 | 0.01 | 12575707.35 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.78 | 1.53 | 0.25 | 0.01 | 190175811.99 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.61 | 1.18 | 0.27 | 0.01 | 136698369.7 | 0.3 | skipped_fast |
| WUSDT | IDLE | 1.89 | 3.67 | 0.7 | 0.01 | 863070.48 | 6.19 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 31.62 | 15.37 | 0.07 | 53364.44 | 21.37 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.35 | 11.9 | 7.11 | -0.0 | 29262.35 | 4.88 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.51 | 0.42 | -0.01 | 731026.22 | 3.86 | skipped_fast |
| CCUSDT | IDLE | 2.85 | 5.7 | 0.0 | 0.05 | 319767.61 | 4.74 | skipped_fast |
| QNTUSDT | IDLE | 1.11 | 2.06 | 1.09 | -0.0 | 955898.84 | 1.64 | skipped_fast |
| CHIPUSDT | IDLE | 1.11 | 9.0 | 2.24 | 0.31 | 418794.59 | 14.47 | skipped_fast |
| TELUSDT | IDLE | 3.78 | 7.16 | 2.65 | -0.01 | 140567.49 | 28.35 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.64 | 1.53 | 0.01 | 404505.17 | 41.43 | skipped_fast |
| BIOUSDT | IDLE | 1.96 | 3.88 | 0.23 | 0.04 | 74013.89 | 6.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.63 | 3.23 | 0.22 | 0.01 | 162773.28 | 21.16 | skipped_fast |
| REDUSDT | IDLE | 1.97 | 3.91 | 0.17 | 0.02 | 58170.19 | 9.13 | skipped_fast |
| HBARUSDT | IDLE | 1.66 | 3.23 | 0.62 | 0.01 | 246999.72 | 6.42 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 2.11 | 0.05 | -0.01 | 70177.42 | 6.25 | skipped_fast |
| RIZEUSDT | IDLE | 1.6 | 4.42 | 0.65 | -0.06 | 29664.85 | 61.33 | skipped_fast |
| RWAUSDT | IDLE | 1.34 | 2.62 | 0.46 | 0.01 | 51364.77 | 7.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.73 | 0.16 | -0.01 | 30148.99 | 27.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
