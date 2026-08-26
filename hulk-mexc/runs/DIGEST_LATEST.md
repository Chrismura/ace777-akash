# Hulk DIGEST — 2026-08-26T06:09:54Z

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
| PYTHUSDT | IDLE | 2.34 | 4.98 | 0.32 | 0.02 | 2784860.36 | 5.67 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 73.61 | 39.08 | 0.09 | 62549.31 | 52.67 | skipped_fast |
| XRPUSDT | IDLE | 0.9 | 1.75 | 0.33 | -0.05 | 59744355.24 | 2.08 | skipped_fast |
| CCUSDT | IDLE | 1.04 | 2.08 | 1.3 | -0.05 | 505511.23 | 7.57 | skipped_fast |
| BIOUSDT | IDLE | 1.97 | 3.51 | 2.89 | -0.04 | 94962.49 | 6.99 | skipped_fast |
| WUSDT | IDLE | 1.09 | 2.16 | 0.13 | -0.02 | 283626.14 | 13.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 2.78 | 0.73 | -0.02 | 158153.76 | 16.26 | skipped_fast |
| KITEUSDT | IDLE | 1.79 | 3.41 | 1.17 | -0.01 | 60474.52 | 12.16 | skipped_fast |
| REDUSDT | IDLE | 1.57 | 3.9 | 2.61 | 0.0 | 75795.38 | 9.54 | skipped_fast |
| HBARUSDT | IDLE | 0.57 | 1.08 | 0.43 | -0.05 | 544669.39 | 1.28 | skipped_fast |
| QAITUSDT | IDLE | 1.61 | 3.03 | 1.32 | 0.04 | 10683.36 | 63.14 | skipped_fast |
| TELUSDT | IDLE | 1.2 | 2.33 | 0.43 | -0.02 | 93455.15 | 38.14 | skipped_fast |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
