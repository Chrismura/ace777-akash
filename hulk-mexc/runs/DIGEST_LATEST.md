# Hulk DIGEST — 2026-09-08T09:39:31Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 0.67 | 1.34 | 0.04 | -0.0 | 30957495.24 | 2.14 | skipped_fast |
| ETHUSDT | IDLE | 0.61 | 1.22 | 0.0 | 0.0 | 289783801.29 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.5 | 0.94 | 0.35 | -0.01 | 610340968.84 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 1.55 | 2.82 | 1.91 | -0.03 | 434360.11 | 6.65 | skipped_fast |
| HBARUSDT | IDLE | 1.44 | 2.66 | 1.4 | -0.0 | 556596.35 | 1.24 | skipped_fast |
| PYTHUSDT | IDLE | 0.93 | 1.84 | 0.07 | -0.02 | 377266.71 | 1.85 | skipped_fast |
| ZBCNUSDT | IDLE | 1.16 | 3.17 | 1.28 | -0.05 | 224412.89 | 11.83 | skipped_fast |
| WUSDT | IDLE | 1.33 | 2.65 | 0.12 | 0.0 | 194191.12 | 10.53 | skipped_fast |
| REDUSDT | IDLE | 1.79 | 3.39 | 1.25 | 0.02 | 56379.44 | 8.33 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.56 | 0.38 | 0.02 | 80505.39 | 9.59 | skipped_fast |
| RIZEUSDT | IDLE | 1.96 | 5.27 | 4.37 | -0.07 | 48971.64 | 67.48 | skipped_fast |
| RWAINCUSDT | IDLE | 2.09 | 8.35 | 6.57 | -0.11 | 5161.85 | 111.05 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 2.82 | 1.41 | -0.07 | 112787.66 | 15.68 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.59 | 0.15 | 0.0 | 66492.47 | 3.65 | skipped_fast |
| KITEUSDT | IDLE | 0.65 | 1.24 | 0.45 | -0.02 | 63863.88 | 11.77 | skipped_fast |
| TELUSDT | IDLE | 1.77 | 3.4 | 0.98 | -0.01 | 77890.62 | 64.05 | skipped_fast |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
