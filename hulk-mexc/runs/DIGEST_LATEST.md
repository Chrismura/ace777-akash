# Hulk DIGEST — 2026-10-12T08:08:47Z

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
| WUSDT | IDLE | 1.82 | 35.96 | 2.56 | 0.72 | 11800019.01 | 7.95 | skipped_fast |
| ETHUSDT | IDLE | 0.8 | 1.51 | 0.57 | 0.02 | 235764612.21 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.35 | 0.59 | 0.01 | 22160527.55 | 2.12 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.98 | 0.4 | 0.01 | 191602977.25 | 0.02 | skipped_fast |
| PYTHUSDT | IDLE | 2.84 | 6.39 | 1.65 | 0.05 | 1097293.84 | 4.89 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.61 | 7.86 | 5.29 | -0.01 | 222933.49 | 14.11 | skipped_fast |
| ZBCNUSDT | IDLE | 2.65 | 5.36 | 1.69 | 0.06 | 279671.37 | 12.1 | skipped_fast |
| REDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.45 | 8.57 | 0.09 | 0.08 | 56015.14 | 15.41 | skipped_fast |
| CCUSDT | IDLE | 1.24 | 2.28 | 1.31 | 0.05 | 427263.76 | 5.58 | skipped_fast |
| RIZEUSDT | IDLE | 2.49 | 16.43 | 4.83 | 0.14 | 46773.05 | 74.76 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 1.96 | 1.27 | 0.02 | 456860.95 | 6.36 | skipped_fast |
| KITEUSDT | IDLE | 1.17 | 2.14 | 1.3 | 0.02 | 62338.05 | 12.47 | skipped_fast |
| BIOUSDT | IDLE | 0.94 | 1.69 | 1.23 | -0.01 | 99380.08 | 6.72 | skipped_fast |
| TELUSDT | IDLE | 1.47 | 2.75 | 1.31 | -0.03 | 175023.63 | 11.55 | skipped_fast |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
