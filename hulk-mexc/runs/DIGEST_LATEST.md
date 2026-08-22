# Hulk DIGEST — 2026-08-22T16:39:56Z

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
| PYTHUSDT | IDLE | 1.91 | 9.43 | 0.06 | 0.09 | 51421096.8 | 3.82 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.76 | 0.05 | 214776944.68 | 0.68 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.95 | -0.0 | 1124769.86 | 5.16 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.27 | 0.08 | 760384.69 | 7.68 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.6 | -0.11 | 626880.45 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.75 | -0.01 | 543527.68 | 6.35 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 3.49 | 1.53 | -0.04 | 315071.58 | 18.95 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.58 | 3.88 | -0.06 | 219697.61 | 3.28 | skipped_fast |
| KITEUSDT | IDLE | 1.92 | 4.35 | 1.96 | 0.02 | 85089.1 | 8.05 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.9 | -0.14 | 129648.36 | 26.4 | skipped_fast |
| RIZEUSDT | IDLE | 1.34 | 3.23 | 0.44 | 0.09 | 47769.57 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 7676.54 | 80.62 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 2.0 | -0.0 | 136877.77 | 48.24 | skipped_fast |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
