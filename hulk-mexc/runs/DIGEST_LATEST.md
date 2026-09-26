# Hulk DIGEST — 2026-09-26T02:51:23Z

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
| XRPUSDT | IDLE | 1.1 | 2.08 | 0.85 | 0.03 | 110897163.33 | 2.55 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.69 | 0.11 | 0.0 | 310442616.18 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.31 | 0.6 | 0.09 | -0.0 | 666088720.53 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.41 | 3.66 | 2.03 | 0.07 | 1244857.2 | 1.36 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 7.09 | 1.52 | 0.17 | 913534.68 | 6.75 | skipped_fast |
| HBARUSDT | IDLE | 1.32 | 2.43 | 1.35 | 0.02 | 898323.14 | 1.05 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.49 | 2.02 | 0.05 | 461667.66 | 7.34 | skipped_fast |
| CHIPUSDT | IDLE | 1.84 | 4.72 | 3.82 | 0.06 | 153129.23 | 14.33 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 4.3 | 1.02 | 0.11 | 562352.42 | 9.02 | skipped_fast |
| KITEUSDT | IDLE | 1.96 | 5.13 | 0.35 | 0.09 | 79371.28 | 10.16 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 2.1 | 1.56 | 0.06 | 245190.86 | 19.98 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 3.32 | 1.95 | 0.07 | 113165.52 | 6.13 | skipped_fast |
| REDUSDT | IDLE | 1.31 | 2.76 | 1.88 | 0.05 | 88481.36 | 13.95 | skipped_fast |
| EDELUSDT | IDLE | 0.76 | 1.5 | 0.07 | -0.01 | 184965.86 | 6.74 | skipped_fast |
| RIZEUSDT | IDLE | 0.15 | 2.06 | 0.18 | -0.06 | 88637.79 | 38.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.42 | 1.27 | 0.75 | -0.07 | 13220.64 | 55.82 | skipped_fast |
| TELUSDT | IDLE | 0.69 | 1.23 | 0.97 | 0.02 | 106033.53 | 48.96 | skipped_fast |
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
