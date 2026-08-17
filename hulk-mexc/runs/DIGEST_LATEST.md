# Hulk DIGEST — 2026-08-17T09:11:06Z

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
| XRPUSDT | IDLE | 0.55 | 0.98 | 0.82 | -0.0 | 10289336.71 | 2.0 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 15.04 | 8.5 | 0.07 | 349839.07 | 3.33 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 23.98 | 8.68 | 0.2 | 56630.47 | 89.75 | skipped_fast |
| WUSDT | IDLE | 1.13 | 2.03 | 1.51 | 0.01 | 187446.03 | 5.95 | skipped_fast |
| CCUSDT | IDLE | 0.7 | 1.34 | 0.34 | -0.01 | 257201.49 | 8.37 | skipped_fast |
| BIOUSDT | IDLE | 1.42 | 2.72 | 0.76 | 0.0 | 69276.54 | 4.04 | skipped_fast |
| PYTHUSDT | IDLE | 0.94 | 1.75 | 0.83 | -0.0 | 166603.57 | 5.1 | skipped_fast |
| REDUSDT | IDLE | 1.46 | 2.58 | 2.26 | -0.05 | 56371.2 | 19.15 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 2.39 | 2.04 | -0.03 | 53224.54 | 14.08 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 2.89 | 0.26 | 0.05 | 55609.16 | 25.58 | skipped_fast |
| ZBCNUSDT | IDLE | 0.69 | 1.32 | 0.35 | 0.01 | 169759.65 | 13.29 | skipped_fast |
| QAITUSDT | IDLE | 1.04 | 2.41 | 0.0 | -0.01 | 2368.59 | 61.12 | skipped_fast |
| TELUSDT | IDLE | 1.06 | 1.87 | 1.7 | -0.0 | 88123.27 | 20.71 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 1.49 | 0.73 | 0.0 | 108570.03 | 1.53 | skipped_fast |
| RWAINCUSDT | IDLE | 0.3 | 0.57 | 0.23 | -0.02 | 2234.64 | 62.55 | skipped_fast |
| QNTUSDT | IDLE | 0.62 | 1.17 | 0.44 | -0.03 | 31852.98 | 3.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.76 | 1.33 | 1.28 | 0.01 | 813.45 | 21.86 | skipped_fast |
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
