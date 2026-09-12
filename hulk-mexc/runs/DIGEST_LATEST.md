# Hulk DIGEST — 2026-09-12T10:23:03Z

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
| ETHUSDT | IDLE | 0.49 | 1.12 | 0.18 | 0.03 | 609469554.97 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.33 | 0.73 | 0.02 | 0.02 | 50161900.93 | 2.19 | n/a |
| BTCUSDT | IDLE | 0.15 | 0.29 | 0.02 | 0.0 | 545743665.03 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.09 | 2.21 | 0.36 | 0.04 | 410156.67 | 1.89 | tvl≈118,603,894 |
| ZBCNUSDT | IDLE | 1.41 | 2.77 | 0.34 | 0.01 | 224854.29 | 12.59 | n/a |
| CCUSDT | IDLE | 0.62 | 1.2 | 0.3 | 0.02 | 386089.15 | 9.08 | no_map |
| WUSDT | IDLE | 0.68 | 1.31 | 0.86 | 0.02 | 200546.94 | 12.27 | tvl≈1,482,189,388 |
| RIZEUSDT | IDLE | 0.14 | 9.79 | 2.37 | 1.06 | 188165.86 | 46.79 | no_map |
| REDUSDT | IDLE | 0.65 | 1.76 | 0.34 | 0.06 | 64851.64 | 20.27 | tvl≈2,302,047 |
| HBARUSDT | IDLE | 0.42 | 0.78 | 0.37 | 0.01 | 242692.1 | 1.34 | empty_tvl |
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
