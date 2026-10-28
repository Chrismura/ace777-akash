# Hulk DIGEST — 2026-10-28T00:17:31Z

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
| XRPUSDT | IDLE | 0.66 | 1.27 | 0.38 | 0.02 | 19420669.86 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.03 | 0.7 | 0.01 | 237751023.68 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.82 | 0.57 | 0.01 | 325400429.17 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 3.95 | 1.34 | 0.02 | 461485.03 | 24.18 | skipped_fast |
| WUSDT | IDLE | 0.91 | 2.09 | 0.74 | 0.03 | 681348.63 | 14.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.12 | 7.31 | 5.75 | -0.02 | 242061.91 | 31.16 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 11.59 | 9.97 | -0.01 | 7726.08 | 21.32 | skipped_fast |
| QNTUSDT | IDLE | 1.21 | 2.18 | 1.64 | -0.01 | 678224.16 | 1.51 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.03 | 0.99 | -0.02 | 396003.75 | 5.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 3.57 | 2.93 | -0.04 | 58547.53 | 6.7 | skipped_fast |
| CHIPUSDT | IDLE | 1.28 | 3.09 | 1.65 | 0.05 | 131635.68 | 20.29 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 1.5 | 0.34 | -0.01 | 225956.19 | 8.08 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.83 | 1.52 | 0.03 | 58287.32 | 9.34 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 1.98 | 1.61 | 0.04 | 59940.18 | 14.9 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.6 | 0.75 | 0.01 | 58881.89 | 8.84 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.31 | 1.02 | -0.02 | 310080.03 | 7.9 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 1.24 | 0.37 | 0.0 | 33583.16 | 64.68 | skipped_fast |
| LAUSDT | IDLE | 1.21 | 2.33 | 1.95 | 0.01 | 60133.53 | 25.06 | skipped_fast |
| IOTAUSDT | IDLE | 0.97 | 1.89 | 0.31 | -0.01 | 79167.51 | 25.91 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.72 | 0.64 | -0.0 | 57521.24 | 16.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.8 | 0.44 | -0.01 | 37156.34 | 79.41 | skipped_fast |
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
