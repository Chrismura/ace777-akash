# Hulk DIGEST — 2026-10-18T10:02:54Z

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
| XRPUSDT | IDLE | 0.63 | 1.2 | 0.38 | -0.0 | 19918465.2 | 0.77 | n/a |
| ETHUSDT | IDLE | 0.48 | 0.93 | 0.18 | -0.0 | 94071928.41 | 0.7 | no_map |
| BTCUSDT | IDLE | 0.42 | 0.81 | 0.14 | 0.01 | 190598400.18 | 0.0 | no_map |
| HBARUSDT | IDLE | 2.42 | 4.8 | 1.84 | 0.05 | 385021.65 | 8.01 | empty_tvl |
| ZBCNUSDT | IDLE | 0.81 | 1.57 | 0.31 | -0.03 | 156894.08 | 15.23 | n/a |
| RIZEUSDT | IDLE | 0.8 | 1.56 | 0.27 | 0.0 | 45607.2 | 59.03 | no_map |
| WUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| REDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| PYTHUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| BIOUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
