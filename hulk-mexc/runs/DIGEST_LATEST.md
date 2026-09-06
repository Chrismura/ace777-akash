# Hulk DIGEST — 2026-09-06T22:32:47Z

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
| XRPUSDT | IDLE | 0.75 | 1.41 | 0.62 | 0.0 | 24311318.46 | 2.82 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.36 | 0.59 | 0.01 | 262579134.73 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.28 | 0.52 | 0.2 | -0.0 | 347101497.39 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.82 | 5.32 | 3.06 | 0.04 | 417333.18 | 13.41 | skipped_fast |
| PYTHUSDT | IDLE | 2.02 | 3.88 | 1.07 | 0.01 | 567300.56 | 1.81 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 4.0 | 1.7 | 0.0 | 417764.48 | 1.71 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 2.89 | 2.36 | 0.0 | 332469.38 | 4.58 | skipped_fast |
| TELUSDT | IDLE | 3.3 | 6.74 | 1.7 | 0.04 | 85085.63 | 44.69 | skipped_fast |
| HBARUSDT | IDLE | 1.08 | 2.02 | 0.95 | 0.01 | 438425.49 | 1.23 | skipped_fast |
| REDUSDT | IDLE | 1.37 | 2.52 | 1.53 | 0.01 | 67138.64 | 12.48 | skipped_fast |
| ZBCNUSDT | IDLE | 0.89 | 1.62 | 1.0 | 0.0 | 155691.18 | 13.44 | skipped_fast |
| RIZEUSDT | IDLE | 2.42 | 20.29 | 12.82 | -0.17 | 75608.54 | 336.13 | skipped_fast |
| BIOUSDT | IDLE | 0.87 | 1.57 | 1.11 | -0.01 | 91932.3 | 3.62 | skipped_fast |
| KITEUSDT | IDLE | 1.07 | 2.02 | 0.76 | -0.0 | 59042.35 | 11.1 | skipped_fast |
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
