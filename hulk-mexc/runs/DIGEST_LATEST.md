# Hulk DIGEST — 2026-08-19T08:54:10Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.59 | 1.16 | 0.11 | 0.01 | 10206747.4 | 1.98 | n/a |
| PYTHUSDT | IDLE | 1.61 | 3.01 | 1.4 | 0.02 | 164805.74 | 2.57 | tvl≈87,687,219 |
| BIOUSDT | IDLE | 1.56 | 3.0 | 0.83 | 0.03 | 63435.0 | 3.97 | n/a |
| REDUSDT | IDLE | 0.96 | 4.43 | 1.54 | -0.09 | 145422.16 | 15.72 | tvl≈1,584,928 |
| ZBCNUSDT | IDLE | 1.13 | 2.21 | 0.28 | 0.01 | 155774.11 | 17.09 | n/a |
| CCUSDT | IDLE | 0.63 | 1.24 | 0.17 | -0.02 | 211547.55 | 6.64 | no_map |
| RIZEUSDT | IDLE | 1.5 | 4.17 | 2.75 | -0.05 | 27415.05 | 50.0 | no_map |
| KITEUSDT | IDLE | 1.18 | 2.19 | 1.12 | -0.0 | 65075.52 | 14.33 | no_map |
| WUSDT | IDLE | 0.91 | 1.73 | 0.59 | -0.01 | 106595.32 | 6.19 | tvl≈1,355,243,290 |
| QAITUSDT | IDLE | 0.9 | 5.53 | 4.01 | -0.17 | 10287.81 | 68.26 | no_map |
| HBARUSDT | IDLE | 0.62 | 1.15 | 0.57 | 0.03 | 122250.97 | 1.48 | empty_tvl |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
