# Hulk DIGEST — 2026-08-28T21:08:43Z

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
| XRPUSDT | IDLE | 1.95 | 3.57 | 2.26 | -0.05 | 52678266.64 | 0.72 | n/a |
| QAITUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 34.24 | 22.11 | -0.18 | 83246.07 | 70.46 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.97 | 7.41 | 6.51 | -0.09 | 193175.57 | 13.35 | n/a |
| HBARUSDT | IDLE | 1.97 | 3.94 | 0.0 | -0.03 | 442499.62 | 1.3 | empty_tvl |
| WUSDT | IDLE | 1.36 | 3.03 | 1.45 | -0.06 | 206138.86 | 9.88 | tvl≈1,520,907,618 |
| RIZEUSDT | IDLE | 1.95 | 5.61 | 0.84 | -0.01 | 40104.25 | 56.09 | no_map |
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

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
