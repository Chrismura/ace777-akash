# Hulk DIGEST — 2026-10-26T06:15:57Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 1.05 | 1.96 | 0.88 | -0.01 | 16838242.51 | 1.55 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.75 | 0.61 | -0.01 | 106859226.12 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.59 | 1.14 | 0.23 | -0.01 | 201595911.83 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 3.15 | 2.79 | 0.05 | 761257.13 | 2.72 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.08 | 10.37 | 1.4 | 0.05 | 101294.21 | 12.91 | skipped_fast |
| WUSDT | IDLE | 1.28 | 2.31 | 1.61 | -0.03 | 584923.73 | 15.37 | skipped_fast |
| QNTUSDT | IDLE | 1.15 | 3.44 | 0.53 | 0.06 | 739066.43 | 5.66 | skipped_fast |
| RWAINCUSDT | IDLE | 2.24 | 4.22 | 3.43 | -0.07 | 66733.34 | 11.62 | skipped_fast |
| REDUSDT | IDLE | 2.02 | 3.84 | 1.4 | -0.02 | 61185.97 | 8.94 | skipped_fast |
| ZBCNUSDT | IDLE | 1.59 | 2.92 | 2.05 | 0.01 | 184203.18 | 33.88 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 3.01 | 1.11 | 0.0 | 53550.57 | 12.42 | skipped_fast |
| BIOUSDT | IDLE | 1.34 | 2.52 | 1.07 | -0.02 | 61579.34 | 9.04 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.58 | 0.91 | 0.0 | 163458.92 | 9.91 | skipped_fast |
| EDELUSDT | IDLE | 0.89 | 2.13 | 1.65 | 0.05 | 170470.38 | 25.28 | skipped_fast |
| HBARUSDT | IDLE | 1.02 | 1.85 | 1.33 | -0.01 | 181151.84 | 6.52 | skipped_fast |
| RIZEUSDT | IDLE | 0.54 | 1.0 | 0.53 | 0.0 | 33112.47 | 25.36 | skipped_fast |
| FLUIDUSDT | IDLE | 0.55 | 2.7 | 1.17 | -0.02 | 19116.06 | 19.47 | skipped_fast |
| RWAUSDT | IDLE | 0.18 | 0.32 | 0.24 | -0.01 | 52684.93 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.57 | 0.07 | -0.01 | 37802.73 | 60.17 | skipped_fast |
| IOTAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| LAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| WAXLUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
