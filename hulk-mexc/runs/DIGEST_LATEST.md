# Hulk DIGEST — 2026-09-06T23:32:58Z

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
| XRPUSDT | IDLE | 0.66 | 1.25 | 0.46 | 0.0 | 24837682.3 | 2.11 | skipped_fast |
| ETHUSDT | IDLE | 0.54 | 1.07 | 0.1 | 0.01 | 271937443.2 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.85 | 0.24 | 0.0 | 351509489.58 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.52 | 5.04 | 0.0 | 0.03 | 589972.41 | 5.28 | skipped_fast |
| WUSDT | IDLE | 2.48 | 4.56 | 2.7 | 0.04 | 419979.3 | 7.7 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 2.74 | 1.66 | 0.01 | 362986.5 | 5.45 | skipped_fast |
| RIZEUSDT | IDLE | 2.46 | 20.29 | 14.67 | -0.16 | 74737.11 | 184.86 | skipped_fast |
| ZBCNUSDT | IDLE | 1.83 | 3.35 | 2.12 | 0.0 | 153842.45 | 29.11 | skipped_fast |
| REDUSDT | IDLE | 1.4 | 2.52 | 1.93 | 0.01 | 67238.2 | 8.62 | skipped_fast |
| HBARUSDT | IDLE | 1.01 | 1.93 | 0.61 | 0.01 | 415030.93 | 1.23 | skipped_fast |
| KITEUSDT | IDLE | 1.05 | 2.02 | 0.51 | 0.0 | 57850.59 | 8.7 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 1.57 | 0.36 | -0.0 | 92103.0 | 3.6 | skipped_fast |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
