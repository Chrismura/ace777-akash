# Hulk DIGEST — 2026-09-23T18:24:03Z

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
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 6.67 | 5.91 | -0.06 | 120944062.17 | 2.01 | n/a |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.71 | 11.74 | 7.32 | -0.07 | 1374326.64 | 3.21 | tvl≈140,236,528 |
| ETHUSDT | IDLE | 1.83 | 3.32 | 2.32 | -0.03 | 504398707.76 | 0.04 | no_map |
| BTCUSDT | IDLE | 1.59 | 2.87 | 2.07 | -0.03 | 886658496.29 | 0.0 | no_map |
| HBARUSDT | IDLE | 2.12 | 6.6 | 5.1 | -0.07 | 1493445.23 | 1.11 | empty_tvl |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.43 | 8.79 | 7.07 | -0.06 | 396342.05 | 11.5 | miss:timeout |
| CCUSDT | IDLE | 2.92 | 6.58 | 4.97 | -0.05 | 524629.74 | 9.31 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.47 | 10.36 | 8.91 | -0.09 | 219782.73 | 19.07 | no_map |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 9.69 | 6.58 | -0.04 | 97118.88 | 10.62 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.41 | 6.14 | 5.25 | -0.04 | 57978.59 | 7.22 | tvl≈2,847,874 |
| KITEUSDT | IDLE | 2.64 | 4.83 | 3.41 | -0.05 | 172505.84 | 8.3 | no_map |
| ZBCNUSDT | IDLE | 2.02 | 4.91 | 3.98 | -0.02 | 253743.13 | 24.55 | n/a |
| RIZEUSDT | IDLE | 1.21 | 14.94 | 11.97 | 0.31 | 73510.58 | 106.44 | no_map |
| TELUSDT | IDLE | 1.37 | 3.61 | 2.91 | -0.04 | 156652.3 | 82.26 | no_map |
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
