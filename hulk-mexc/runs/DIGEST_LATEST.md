# Hulk DIGEST — 2026-08-28T05:05:01Z

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
| PYTHUSDT | IDLE | 1.56 | 3.65 | 3.0 | 0.02 | 20160721.83 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 2.13 | 3.73 | 3.5 | 0.01 | 57212593.06 | 2.81 | skipped_fast |
| CHIPUSDT | IDLE | 2.02 | 9.97 | 4.78 | 0.03 | 764301.49 | 7.69 | skipped_fast |
| CCUSDT | IDLE | 2.14 | 3.96 | 2.07 | -0.02 | 471261.34 | 9.76 | skipped_fast |
| WUSDT | IDLE | 2.56 | 4.51 | 4.02 | -0.0 | 200962.23 | 4.24 | skipped_fast |
| BIOUSDT | IDLE | 2.92 | 5.18 | 4.45 | -0.0 | 94971.12 | 3.51 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 4.42 | 3.25 | 0.05 | 245790.75 | 7.18 | skipped_fast |
| REDUSDT | IDLE | 1.9 | 3.56 | 1.59 | 0.02 | 82422.2 | 11.76 | skipped_fast |
| KITEUSDT | IDLE | 1.76 | 3.15 | 2.49 | 0.01 | 78404.74 | 11.73 | skipped_fast |
| HBARUSDT | IDLE | 1.84 | 3.24 | 2.97 | 0.0 | 332450.78 | 1.29 | skipped_fast |
| QAITUSDT | IDLE | 0.38 | 18.58 | 13.16 | -0.21 | 61337.7 | 65.05 | skipped_fast |
| RIZEUSDT | IDLE | 0.94 | 11.77 | 2.6 | -0.18 | 119012.81 | 53.43 | skipped_fast |
| TELUSDT | IDLE | 2.01 | 3.73 | 3.44 | 0.01 | 127228.23 | 37.79 | skipped_fast |
| RWAINCUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.05 | 20742.22 | 32.03 | skipped_fast |
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
