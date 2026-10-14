# Hulk DIGEST — 2026-10-14T14:21:12Z

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
| PYTHUSDT | IDLE | 2.61 | 6.19 | 3.46 | 0.01 | 2102033.66 | 8.48 | tvl≈189,914,482 |
| WUSDT | IDLE | 1.85 | 7.99 | 6.8 | -0.16 | 3383802.5 | 5.23 | tvl≈1,634,527,541 |
| ETHUSDT | IDLE | 2.03 | 3.56 | 3.34 | -0.03 | 161015920.12 | 0.04 | no_map |
| XRPUSDT | IDLE | 2.02 | 3.56 | 3.22 | -0.03 | 36269719.22 | 2.24 | n/a |
| BTCUSDT | IDLE | 1.32 | 2.31 | 2.23 | -0.02 | 381427948.2 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.92 | 4.44 | 4.12 | -0.03 | 1552893.33 | 4.92 | n/a |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 18.92 | 15.6 | -0.01 | 50448.82 | 60.06 | no_map |
| CCUSDT | IDLE | 1.96 | 4.89 | 4.44 | -0.09 | 470238.23 | 7.67 | no_map |
| ZBCNUSDT | IDLE | 2.84 | 4.98 | 4.64 | -0.03 | 190117.74 | 4.95 | n/a |
| CHIPUSDT | IDLE | 2.84 | 5.51 | 4.39 | -0.07 | 77318.32 | 12.78 | no_map |
| BIOUSDT | IDLE | 2.29 | 4.04 | 3.56 | -0.04 | 68982.01 | 7.54 | n/a |
| EDELUSDT | IDLE | 2.05 | 3.65 | 3.06 | -0.04 | 144757.72 | 17.86 | no_map |
| KITEUSDT | IDLE | 2.0 | 5.55 | 4.52 | 0.03 | 83697.64 | 9.91 | no_map |
| HBARUSDT | IDLE | 2.25 | 3.94 | 3.79 | -0.05 | 302826.26 | 8.35 | empty_tvl |
| REDUSDT | IDLE | 1.94 | 3.43 | 3.0 | -0.01 | 59625.89 | 6.6 | tvl≈3,792,735 |
| RWAINCUSDT | IDLE | 1.77 | 5.62 | 3.63 | -0.07 | 32669.94 | 79.34 | no_map |
| TELUSDT | IDLE | 1.71 | 3.02 | 2.71 | 0.0 | 106047.21 | 39.85 | no_map |
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
