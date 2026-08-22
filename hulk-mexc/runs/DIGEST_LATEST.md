# Hulk DIGEST — 2026-08-22T12:45:51Z

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
| XRPUSDT | IDLE | 2.48 | 14.26 | 6.93 | 0.09 | 216185134.96 | 1.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.62 | 7.83 | 1.15 | 0.05 | 51599495.08 | 3.93 | skipped_fast |
| HBARUSDT | IDLE | 1.25 | 4.63 | 2.16 | 0.01 | 1253651.54 | 1.28 | skipped_fast |
| CCUSDT | IDLE | 1.61 | 8.38 | 3.85 | 0.13 | 778164.75 | 8.45 | skipped_fast |
| WUSDT | IDLE | 1.55 | 6.27 | 3.69 | -0.0 | 575525.34 | 12.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.19 | 5.77 | 3.39 | -0.0 | 335529.66 | 18.39 | skipped_fast |
| CHIPUSDT | IDLE | 0.72 | 4.16 | 1.72 | -0.1 | 603152.09 | 3.36 | skipped_fast |
| KITEUSDT | IDLE | 2.67 | 6.37 | 0.69 | 0.03 | 84997.64 | 10.59 | skipped_fast |
| EDELUSDT | IDLE | 2.13 | 3.89 | 2.43 | -0.02 | 78229.7 | 22.57 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 5.65 | 2.64 | -0.05 | 238397.38 | 3.23 | skipped_fast |
| QAITUSDT | IDLE | 2.22 | 4.16 | 1.9 | -0.01 | 2395.57 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.44 | 0.01 | 152878.88 | 14.25 | skipped_fast |
| TELUSDT | IDLE | 2.15 | 5.61 | 3.68 | -0.02 | 163152.57 | 37.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.01 | 10007.28 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.06 | 3.47 | 1.45 | -0.01 | 187689.65 | 4.66 | skipped_fast |
| RIZEUSDT | IDLE | 0.48 | 2.03 | 0.0 | 0.0 | 46787.11 | 46.02 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.04 | 5072.55 | 22.22 | skipped_fast |
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
