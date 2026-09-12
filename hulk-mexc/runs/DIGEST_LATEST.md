# Hulk DIGEST — 2026-09-12T02:21:59Z

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
| ETHUSDT | IDLE | 0.67 | 1.42 | 1.1 | 0.03 | 648478821.9 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.7 | 1.49 | 0.31 | 0.01 | 53144751.35 | 2.2 | n/a |
| BTCUSDT | IDLE | 0.3 | 0.58 | 0.16 | 0.01 | 570582452.66 | 0.0 | no_map |
| ZBCNUSDT | IDLE | 1.86 | 3.4 | 2.13 | -0.01 | 195248.72 | 11.2 | n/a |
| WUSDT | IDLE | 1.41 | 2.99 | 0.0 | 0.03 | 198359.37 | 10.22 | miss:timeout |
| RIZEUSDT | IDLE | 0.14 | 9.28 | 4.42 | 0.38 | 209625.85 | 164.33 | no_map |
| HBARUSDT | IDLE | 0.51 | 1.01 | 0.11 | -0.01 | 260833.59 | 1.34 | empty_tvl |
| REDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| PYTHUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| BIOUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| KITEUSDT | ERR | — | — | — | — | — | — | scan_deadline |
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
